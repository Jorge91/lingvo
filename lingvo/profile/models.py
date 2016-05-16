from django.contrib.auth.models import User
from django.db import models

from profile.settings import GENRES


class Profile(models.Model):
    user = models.ForeignKey(User, name='user')
    description = models.TextField()
    genre = models.CharField(max_length=3, choices=GENRES)
    picture = models.ImageField(upload_to='/profiles')
    born_date = models.DateField()
    # meeting_distance

    def __unicode__(self):
        return unicode(self.user.username)

