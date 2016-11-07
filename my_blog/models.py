# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from uuslug import slugify

from django.utils.translation import ugettext as _


class ArticleManager(models.Manager):
    def public_articles(self):
        return self.get_queryset().filter(is_private=False)


class Categories(models.Model):
    class Meta:
        db_table = "Categories"
        ordering = ['name']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    name = models.CharField(_("Category"), max_length=50)
    slug = models.SlugField(_("Slug"))

    def __str__(self):
        return self.name

    def save(self):
        self.slug = slugify(self.name)
        super(Categories, self).save()

    def get_absolute_url(self):
        return reverse('blog:category_list', kwargs={'cat_slug': self.slug})


class Article(models.Model):
    class Meta:
        db_table = "Articles"
        ordering = ["-article_datetime"]
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    article_title = models.CharField(
        _("Article title"),
        max_length=200,
        unique=True
    )
    article_text = models.TextField(_("Article text"))
    article_datetime = models.DateTimeField(
        _("Date/time publishing"),
        default=timezone.now
    )
    article_image = models.ImageField(
        _("Image article"),
        upload_to="art_image",
        blank=True,
        null=True,
        default=""
    )
    category = models.ForeignKey(
        Categories,
        verbose_name=_("Category"),
        related_name="category"
    )
    is_private = models.BooleanField(
        _("Private article"),
        default=True
    )
    slug = models.SlugField(_("Slug"))

    objects = ArticleManager()

    def __str__(self):
        return self.article_title

    def get_previous_article(self, user):
        self.prev_article = Article.objects.filter(category_id=self.object.category_id) \
        .filter(article_datetime__lt=self.object.article_datetime)
        if user.is_superuser:
            return self.prev_article.first()
        return self.prev_article.filter(is_private=False).first()

    def get_next_article(self, user):
        self.next_article = Article.objects.filter(category_id=self.object.category_id) \
        .filter(article_datetime__gt=self.object.article_datetime).reverse()
        if user.is_superuser:
            return self.next_article.first()
        return self.next_article.filter(is_private=False).first()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.article_title)
        try:
            curr_article = Article.objects.get(id=self.id)
            if curr_article.article_image != self.article_image:
                curr_article.article_image.delete(save=False)
        except ObjectDoesNotExist:
            pass
        super(Article, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.article_image.delete(save=False)
        super(Article, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'cat_slug': self.category.slug, 'slug': self.slug})
