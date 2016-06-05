# -*- coding: utf-8 -*-
from rest_framework.routers import SimpleRouter

from related.api import RelatedViewSet

router = SimpleRouter()
router.register(r'related', RelatedViewSet, base_name='related')


urlpatterns = router.urls