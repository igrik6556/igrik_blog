# -*- coding: utf-8 -*-
from django import forms
from .models import Article
from pagedown.widgets import PagedownWidget


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ("article_title", "article_text", "category", "article_image", "is_private")
        widgets = {"article_title": forms.TextInput(attrs={"size": 91, "class": "form-control inp_form"}),
                   "article_text": PagedownWidget(attrs={"rows": 15, "class": "form-control inp_form_text"}),
                   "category": forms.Select(attrs={"class": "form-control inp_form"}),
                   "article_image": forms.ClearableFileInput(attrs={"class": "img_inp"})}
        help_texts = {"article_image": "Картинка размера 200х200"}
