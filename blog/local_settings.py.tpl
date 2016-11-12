# -*- coding: utf-8 -*-

from settings import *

SECRET_KEY = 'your_secret_key'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'my_db.sqlite3'),
    }
}
