# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from api import UserInfo
from rest_framework.routers import SimpleRouter

from profile.api import ProfileViewSet

router = SimpleRouter()
router.register(r'profiles', ProfileViewSet, base_name='profiles')

urlpatterns = patterns('',
    url(r'^users/me/$', UserInfo.as_view(), name='users_api_me'),
)

urlpatterns += router.urls