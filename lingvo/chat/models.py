from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    label = models.SlugField(unique=True, null=True)
    user_from = models.ForeignKey(User, related_name='from_chat_user')
    user_to = models.ForeignKey(User, related_name='to_chat_user')
    # channel

    def __unicode__(self):
        return unicode(self.user_from.username) + ' - ' + unicode(self.user_to.username)


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(User, related_name='user_message', null=True)

    def __unicode__(self):
        return unicode(self.chat) + ' - ' + unicode(self.message)