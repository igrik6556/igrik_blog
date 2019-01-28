from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.translation import ugettext as _


class GeneratorForm(forms.Form):
    uppercase_let = forms.BooleanField(label=_("Uppercase letters"), help_text="A-Z", initial=True, required=False)
    lowercase_let = forms.BooleanField(label=_("Lowercase letters"), help_text="a-z", initial=True, required=False)
    digits = forms.BooleanField(label=_("Digital symbols"), help_text="0-9", initial=True, required=False)
    special_symbols = forms.BooleanField(label=_("Special symbols"), help_text="!#$%&()*+,-./:;<=>?@[]^_`{|}~",
                                         required=False)
    user_symbols = forms.CharField(label=_("User input symbols"), max_length=100, required=False,
                                   help_text=_("100 symbols max"))
    password_length = forms.IntegerField(label=_("Password length"), help_text=_("The length must be from 1 to 100"),
                                         initial=8, required=False,
                                         validators=[
                                             MaxValueValidator(100),
                                             MinValueValidator(1),
                                         ])
    password_count = forms.IntegerField(label=_("Number of passwords"), help_text=_("The length must be from 1 to 100"),
                                        initial=10, required=False,
                                        validators=[
                                            MaxValueValidator(100),
                                            MinValueValidator(1),
                                        ])
