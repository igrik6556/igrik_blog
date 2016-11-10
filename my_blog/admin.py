# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Article, Categories
from django.db import models
from pagedown.widgets import AdminPagedownWidget


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'category', 'article_datetime', 'slug', 'is_private')
    list_filter = ('category', 'is_private', )
    date_hierarchy = 'article_datetime'
    search_fields = ['article_title', ]
    fieldsets = (
        (None, {
            'fields': ('article_title', 'category', 'article_text', 'article_datetime', 'article_image', 'is_private', )
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    fieldsets = (
        (None, {
            'fields': ('name', )
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categories, CategoriesAdmin)
