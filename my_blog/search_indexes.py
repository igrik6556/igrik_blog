# -*- coding: utf-8 -*-
from haystack import indexes
from .models import Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    a_title = indexes.CharField(model_attr='article_title')
    a_text = indexes.CharField(model_attr='article_text')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
