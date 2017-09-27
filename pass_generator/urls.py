from django.conf.urls import url
from pass_generator import views


urlpatterns = [
    url(r'^$', views.generator, name='generator'),
]
