from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Meeting(models.Model):
    title = models.CharField(max_length=100)
    position = models.PointField(null=True, blank=True)
    time = models.DateTimeField(null=False)

    objects = models.GeoManager()

    def __unicode__(self):
        return unicode(self.title)

    """

    getAdressCoord = Point.objects.get(placename = str(adress))
    po = POINT(getAdressCoord.x getAdressCoord.y)
    pnt = fromstr(str(po), srid=4326)
    qs = Point.objects.filter(point__distance_lte=(pnt, D(km=5)))

    """


class User_attends_meeting(models.Model):
    user = models.ForeignKey(User, related_name='meeting_user')
    meeting = models.ForeignKey(Meeting, related_name='meeting')

    def __unicode__(self):
        return unicode(self.user.username) + ' - ' + unicode(self.meeting.title)
