from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    user_from = models.ForeignKey(User, related_name='from_chat_user')
    user_to = models.ForeignKey(User, related_name='to_chat_user')
    # channel

    def __unicode__(self):
        return unicode(self.user_from.username) + ' - ' + unicode(self.user_to.username)

