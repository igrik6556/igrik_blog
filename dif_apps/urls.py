from django.urls import path
from django.views.generic.edit import FormView

from dif_apps.forms import GeneratorForm
from dif_apps import views


app_name = 'dif_apps'
urlpatterns = [
    path('password-generator/', FormView.as_view(template_name="dif_apps/main_gen.html",
                                                 form_class=GeneratorForm), name='password-generator'),
    path('generate-password/', views.generate_password, name='generate-password'),
]
