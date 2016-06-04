# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from language.api import LanguagesViewSet, UserSpeaksLanguageViewSet, UserPracticesLanguageViewSet

router = SimpleRouter()
router.register(r'languages', LanguagesViewSet, base_name='profiles')
router.register(r'languages/speak', UserSpeaksLanguageViewSet, base_name='speak')
router.register(r'languages/practice', UserPracticesLanguageViewSet, base_name='practice')

urlpatterns = router.urls