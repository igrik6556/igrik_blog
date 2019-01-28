import json
import string
from random import choice
from django.http import Http404, HttpResponse

from dif_apps.forms import GeneratorForm


def generate_password(request):
    if request.method == "POST":
        form = GeneratorForm(request.POST)
        if form.is_valid():
            symbols = ""
            passwords = []
            password_count = int(request.POST.get('password_count'))
            password_length = int(request.POST.get('password_length'))

            if request.POST.get('uppercase_let'):
                symbols += string.ascii_uppercase
            if request.POST.get('lowercase_let'):
                symbols += string.ascii_lowercase
            if request.POST.get('digits'):
                symbols += string.digits
            if request.POST.get('special_symbols'):
                symbols += "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
            if request.POST.get('user_symbols'):
                symbols += request.POST.get('user_symbols')
            try:
                for i in range(password_count):
                    passwords.append(''.join([choice(symbols) for j in range(password_length)]))
            except IndexError:
                pass

            return HttpResponse(json.dumps(dict(passwords=passwords)),
                                content_type='application/json')
    else:
        raise Http404
