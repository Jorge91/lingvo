# -*- coding: utf-8 -*-
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lingvo',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'port': '5432'
    }
}