# -*- coding: utf-8 -*-
from django.conf.urls import url
from my_blog import views
from my_blog.decorators import superuser_check


urlpatterns = [
    url(r'^page/(?P<num_page>\d+)/$', views.ArticleMain.as_view(), name='articles_main'),
    url(r'^$', views.ArticleMain.as_view(), name='articles_main'),
    url(r'^create_art/$',
        superuser_check((views.ArticleCreate.as_view())), name='article_create'),
    url(r'^update_art/(?P<slug>([-\w]+))/$',
        superuser_check((views.ArticleUpdate.as_view())), name='article_update'),
    url(r'^delete_art/(?P<slug>([-\w]+))/$',
        superuser_check((views.ArticleDelete.as_view())), name='article_delete'),
    url(r'archive/$', views.ArticleArchive.as_view(), name='article_archive'),
    url(r'archive/(?P<year>\d{4})/(?P<month>\d+)/$', views.ArticleMonth.as_view(), name='article_month'),
    url(r'^(?P<cat_slug>([-\w]+))/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^tag/(?P<tag_slug>([-\w]+))/$', views.TagList.as_view(), name='tag_list'),
    url(r'^(?P<cat_slug>([-\w]+))/(?P<slug>([-\w]+))/$', views.ArticleDetail.as_view(), name='article_detail'),
]
