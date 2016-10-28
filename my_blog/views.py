# -*- coding: utf-8 -*-
from .forms import ArticleForm
from .models import Article, Categories
from pure_pagination.mixins import PaginationMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView
from django.core.urlresolvers import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.utils.translation import ugettext as _


class ArticleMain(PaginationMixin, ListView):
    """
    Implements pagination of articles from the database.
    """
    template_name = "my_blog/article_main.html"
    model = Article
    paginate_by = 10
    page_kwarg = "num_page"

    def get_queryset(self):
        qs = super(ArticleMain, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(is_private=False)
        return qs


class ArticleDetail(DetailView):
    """
    Show full article.
    """
    model = Article

    def get_queryset(self):
        qs = super(ArticleDetail, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(is_private=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data(**kwargs)
        context["previous_article"] = Article.get_previous_article(self, self.request.user)
        context["next_article"] = Article.get_next_article(self, self.request.user)
        return context


class CategoryList(DetailView):
    """
    Displays all the articles belonging to the category.
    """
    template_name = "my_blog/category_list.html"
    slug_url_kwarg = "cat_slug"
    model = Categories


class ArticleCreate(SuccessMessageMixin, CreateView):
    form_class = ArticleForm
    template_name = "my_blog/article_form.html"
    success_message = _("Article <%(article_title)s> successfully added!")

    def get_success_url(self):
        self.success_url = reverse("blog:article_detail",
                                   kwargs={
                                       "cat_slug": self.object.category.slug,
                                       "slug": self.object.slug
                                   })
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(ArticleCreate, self).get_context_data(**kwargs)
        context["title"] = _("Article creation") + " &#187; IGRIK"
        return context


class ArticleUpdate(SuccessMessageMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = "my_blog/article_form.html"
    success_message = _("Article <%(article_title)s> successfully updated after editing!")

    def get_success_url(self):
        self.success_url = reverse("blog:article_detail",
                                   kwargs={
                                       "cat_slug": self.object.category.slug,
                                       "slug": self.object.slug
                                   })
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(ArticleUpdate, self).get_context_data(**kwargs)
        context["title"] = (_("Edit") + " - %s &#187; IGRIK") % self.object.article_title
        return context


class ArticleDelete(DeleteView):
    form_class = ArticleForm
    model = Article
    template_name = "my_blog/article_delete.html"

    def post(self, request, *args, **kwargs):
        self.success_url = reverse("blog:articles_main")
        messages.success(request,
                         _("Article <%s> deleted successfully!") % Article.objects.get(slug=self.kwargs["slug"])
                         )
        return super(ArticleDelete, self).post(request, *args, **kwargs)


class ArticleArchive(ArchiveIndexView):
    model = Article
    date_field = "article_datetime"
    context_object_name = "articles_archive"
    allow_empty = True
    allow_future = True
    make_object_list = True
    template_name = "my_blog/article_archive.html"

    def get_queryset(self):
        qs = super(ArticleArchive, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(is_private=False)
        return qs


class ArticleMonth(MonthArchiveView):
    model = Article
    date_field = "article_datetime"
    month_format = "%m"
    context_object_name = "archive_month"
    allow_empty = True
    allow_future = True
    make_object_list = True
    template_name = "my_blog/article_month.html"

    def get_queryset(self):
        qs = super(ArticleMonth, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(is_private=False)
        return qs
