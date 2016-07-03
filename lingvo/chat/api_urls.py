# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from chat.api import ChatsViewSet

router = SimpleRouter()
router.register(r'chats', ChatsViewSet, base_name='chats')

urlpatterns = router.urls