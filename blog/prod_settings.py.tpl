# -*- coding: utf-8 -*-

from settings import *

SECRET_KEY = 'your_secret_key'

DEBUG = True

ALLOWED_HOSTS = ['your_hosts']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<your_mysql_db_name>',
        'USER': '<your_username>',
        'PASSWORD': '<your_mysql_password>',
        'HOST': '<your_mysql_hostname>',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        }
    }
}
