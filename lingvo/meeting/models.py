from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    position = models.PointField(null=False, blank=False)
    time = models.DateTimeField(null=False, blank=False)
    creator = models.ForeignKey(User, related_name='creator', null=True)

    objects = models.GeoManager()

    def __unicode__(self):
        return unicode(self.title)


class User_attends_meeting(models.Model):
    user = models.ForeignKey(User, related_name='meeting_user')
    meeting = models.ForeignKey(Meeting, related_name='meeting')

    class Meta:
        unique_together = ('user', 'meeting')

    def __unicode__(self):
        return unicode(self.user.username) + ' - ' + unicode(self.meeting.title)
