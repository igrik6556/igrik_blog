# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.utils.functional import curry
from django.views.defaults import page_not_found
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', views.flatpage, {'url': '/about/'}, name="about"),
    url(r'^', include('my_blog.urls', namespace="blog")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = curry(page_not_found, template_name='errors/404.html')
