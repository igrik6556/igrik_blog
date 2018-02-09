from django.conf.urls import url
from pass_generator import views


urlpatterns = [
    url(r'^$', views.generator_main, name='main'),
    url(r'^generate/$', views.generate, name='generate'),
]
