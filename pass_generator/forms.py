from django import forms
from pass_generator.models import Generator

from django.utils.translation import ugettext as _


class GeneratorForm(forms.ModelForm):
    class Meta:
        model = Generator
        fields = '__all__'
