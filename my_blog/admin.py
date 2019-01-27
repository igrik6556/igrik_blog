# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models

from my_blog.models import Article, Categories, Tag
from pagedown.widgets import AdminPagedownWidget

from django.utils.translation import ugettext as _


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('article_title', 'category', 'article_datetime', 'slug', 'get_tags', 'is_private')
    list_filter = ('is_private', 'category', 'tag')
    date_hierarchy = 'article_datetime'
    search_fields = ['article_title', ]
    fieldsets = (
        (None, {
            'fields': ('article_title', 'category', 'tag', 'article_text', 'article_datetime', 'article_image', 'is_private', )
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    def get_tags(self, obj):
        return ", ".join([t.name for t in obj.tag.all()])
    get_tags.short_description = _('Tags')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    fieldsets = (
        (None, {
            'fields': ('name', )
        }),
    )


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', )
    fieldsets = (
        (None, {
            'fields': ('name', )
        }),
    )


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Tag, TagAdmin)
