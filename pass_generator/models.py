import string
from random import choice
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.utils.translation import ugettext as _


class Generator(models.Model):
    class Meta:
        verbose_name = _("String generator")
        verbose_name_plural = _("String generators")

    up_letters = models.BooleanField(_("Uppercase letters"), help_text="A-Z", default=True)
    low_letters = models.BooleanField(_("Lowercase letters"), help_text="a-z", default=True)
    digits = models.BooleanField(_("Digital symbols"), help_text="0-9", default=False)
    spec_symbols = models.BooleanField(_("Special symbols"), help_text="!#$%&()*+,-./:;<=>?@[\]^_`{|}~", default=False)
    user_symbols = models.CharField(_("User input symbols"), max_length=100,
                                    help_text=_("100 symbols max"), default="", blank=True, null=True)
    length = models.PositiveIntegerField(_("Password length"), help_text=_("The length must be from 1 to 100"), default=8,
                                         validators=[
                                             MaxValueValidator(100),
                                             MinValueValidator(1),
                                         ])
    number = models.PositiveIntegerField(_("Number of passwords"), help_text=_("The length must be from 1 to 100"), default=10,
                                         validators=[
                                             MaxValueValidator(100),
                                             MinValueValidator(1),
                                         ])

    def str_for_choice(self):
        symbols = ""
        passwords = []
        if self.up_letters:
            symbols += string.ascii_uppercase
        if self.low_letters:
            symbols += string.ascii_lowercase
        if self.digits:
            symbols += string.digits
        if self.spec_symbols:
            symbols += "!#$%&()*+,-./:;<=>?@[\]^_`{|}~"
        if self.user_symbols:
            symbols += self.user_symbols
        try:
            for i in range(self.number):
                passwords.append(''.join([choice(symbols) for j in range(self.length)]))
        except IndexError:
            pass
        return passwords
