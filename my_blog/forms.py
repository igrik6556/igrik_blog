# -*- coding: utf-8 -*-
from django import forms
from .models import Article
from pagedown.widgets import PagedownWidget

from django.utils.translation import ugettext as _


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("article_title", "article_text", "category", "tag", "article_image", "is_private")
        widgets = {"article_title": forms.TextInput(attrs={"size": 118, "class": "form-control inp_form"}),
                   "article_text": PagedownWidget(attrs={"rows": 15, "class": "form-control inp_form_text"}),
                   "category": forms.Select(attrs={"class": "form-control inp_form"}),
                   "tag": forms.SelectMultiple(attrs={"size": 5, "class": "form-control inp_form"}),
                   "article_image": forms.ClearableFileInput(attrs={"class": "img_inp"})}
        help_texts = {"article_image": _("Picture size 200х200")}
