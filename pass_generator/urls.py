from django.urls import path
from pass_generator import views


app_name = 'pass_generator'
urlpatterns = [
    path('', views.generator_main, name='main'),
    path('generate/', views.generate, name='generate'),
]
