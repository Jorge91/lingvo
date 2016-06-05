from django.contrib import admin

from meeting.models import Meeting, User_attends_meeting

admin.site.register(Meeting)
admin.site.register(User_attends_meeting)
