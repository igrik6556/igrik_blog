# -*- coding: utf-8 -*-
from django import template
from django.db.models import Count
from my_blog.models import Article, Categories

register = template.Library()


@register.inclusion_tag("my_blog/_last_articles.html")
def last_articles(user):
    if user.is_superuser:
        last = Article.objects.all()
    else:
        last = Article.objects.public_articles()
    return {'last_articles': last[:7]}


@register.inclusion_tag("my_blog/_list_categories.html")
def list_categories(user):
    if user.is_superuser:
        cats = Categories.objects.annotate(count_post=Count('category'))
    else:
        cats = Categories.objects.filter(category__is_private=False).annotate(count_post=Count('category'))
    return {"list_cats": cats}


@register.inclusion_tag("my_blog/_filter_dates.html")
def filter_dates(user):
    if user.is_superuser:
        years = Article.objects.datetimes("article_datetime", "year")
        month = Article.objects.datetimes("article_datetime", "month")
    else:
        years = Article.objects.public_articles().datetimes("article_datetime", "year")
        month = Article.objects.public_articles().datetimes("article_datetime", "month")
    return {"years": years, "month": month}
