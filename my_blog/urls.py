# -*- coding: utf-8 -*-
from django.urls import path

from my_blog import views
from my_blog.decorators import superuser_check


app_name = 'blog'
urlpatterns = [
    path('page/<int:num_page>/', views.ArticleMain.as_view(), name='articles_main'),
    path('', views.ArticleMain.as_view(), name='articles_main'),
    path('create_art/', superuser_check((views.ArticleCreate.as_view())), name='article_create'),
    path('update_art/<str:slug>/', superuser_check((views.ArticleUpdate.as_view())), name='article_update'),
    path('delete_art/<str:slug>/', superuser_check((views.ArticleDelete.as_view())), name='article_delete'),
    path('archive/', views.ArticleArchive.as_view(), name='article_archive'),
    path('archive/<int:year>/<int:month>/', views.ArticleMonth.as_view(), name='article_month'),
    path('<str:cat_slug>/', views.CategoryList.as_view(), name='category_list'),
    path('tag/<str:tag_slug>/', views.TagList.as_view(), name='tag_list'),
    path('<str:cat_slug>/<str:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
]
