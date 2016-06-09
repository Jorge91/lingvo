from django.contrib.auth.models import User
from django.db import models


class Language(models.Model):
    code = models.CharField(unique=True, max_length=10)
    name = models.CharField(max_length=30, null=True, blank=True)
    flag = models.ImageField(upload_to='flags', blank=True, null=True)

    def __unicode__(self):
        return unicode(self.code)


class User_speaks_language(models.Model):
    user = models.ForeignKey(User, related_name='speaks_user')
    language = models.ForeignKey(Language, related_name='speaks_language')

    class Meta:
        unique_together = ('user', 'language')

    def __unicode__(self):
        return unicode(self.user.username) + ' - ' + unicode(self.language.code)


class User_practices_language(models.Model):
    user = models.ForeignKey(User, related_name='practices_user')
    language = models.ForeignKey(Language, related_name='practices_language')

    class Meta:
        unique_together = ('user', 'language')

    def __unicode__(self):
        return unicode(self.user.username) + ' - ' + unicode(self.language.code)
