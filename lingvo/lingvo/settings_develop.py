# -*- coding: utf-8 -*-
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'lingvo',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'port': '5432'
    }
}