# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.utils.functional import curry
from django.views.defaults import page_not_found
from django.conf.urls.static import static
from django.contrib.flatpages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.flatpage, {'url': '/about/'}, name="about"),
    path('apps/', include('dif_apps.urls')),
    path('', include('my_blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = curry(page_not_found, template_name='errors/404.html')
