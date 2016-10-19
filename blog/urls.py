# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.utils.functional import curry
from django.views.defaults import page_not_found
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^', include('my_blog.urls', namespace="blog")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = curry(page_not_found, template_name='errors/404.html')
