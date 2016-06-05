# -*- coding: utf-8 -*-
from api import MeetingViewSet, AttendMeetingViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'meetings', MeetingViewSet, base_name='meetings')
router.register(r'attendances', AttendMeetingViewSet, base_name='meetings')


urlpatterns = router.urls