# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.dates import ArchiveIndexView, MonthArchiveView
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from my_blog.forms import ArticleForm
from my_blog.models import Article, Categories, Tag
from pure_pagination.mixins import PaginationMixin

from django.utils.translation import ugettext as _


class QuerysetSuperuserFilterMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(is_private=False)
        return qs


class ArticleMain(PaginationMixin, QuerysetSuperuserFilterMixin, ListView):
    """
    Implements pagination of articles from the database.
    """
    template_name = "my_blog/article_main.html"
    model = Article
    paginate_by = 10
    page_kwarg = "num_page"


class ArticleDetail(QuerysetSuperuserFilterMixin, DetailView):
    """
    Show full article.
    """
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class TagList(DetailView):
    """
    Displays all the articles belonging to the tag.
    """
    template_name = "my_blog/tag_list.html"
    slug_url_kwarg = "tag_slug"
    model = Tag


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
        context = super().get_context_data(**kwargs)
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
        context = super().get_context_data(**kwargs)
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
        return super().post(request, *args, **kwargs)


class ArticleArchive(QuerysetSuperuserFilterMixin, ArchiveIndexView):
    model = Article
    date_field = "article_datetime"
    context_object_name = "articles_archive"
    allow_empty = True
    allow_future = True
    make_object_list = True
    template_name = "my_blog/article_archive.html"


class ArticleMonth(QuerysetSuperuserFilterMixin, MonthArchiveView):
    model = Article
    date_field = "article_datetime"
    month_format = "%m"
    context_object_name = "archive_month"
    allow_empty = True
    allow_future = True
    make_object_list = True
    template_name = "my_blog/article_month.html"
