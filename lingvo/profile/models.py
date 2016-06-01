from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from profile.settings import GENRES


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user')
    description = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=3, choices=GENRES, null=True, blank=True)
    picture = models.ImageField(upload_to='profiles', null=True, blank=True)
    born_date = models.DateField(null=True, blank=True)
    # meeting_distance

    def __unicode__(self):
        return unicode(self.user.username)


@receiver(post_save, sender=User)
def on_user_create(sender, **kwargs):
    user = kwargs['instance']
    try:
        Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Create the CustomUser
        custom = Profile()
        custom.user = user
        custom.save()
    return