from django.contrib.auth.models import User
from django.db import models


class Language(models.Model):
    code = models.CharField(unique=True, max_length=10)
    flag = models.ImageField(upload_to='/flags')

    def __unicode__(self):
        return unicode(self.code)


class User_speaks_language(models.Model):
    user = models.ForeignKey(User, related_name='speaks_user')
    language = models.ForeignKey(Language, related_name='speaks_language')

    def __unicode__(self):
        return unicode(self.user.username) + ' - ' + unicode(self.language.code)


class User_practices_language(models.Model):
    user = models.ForeignKey(User, related_name='practices_user')
    language = models.ForeignKey(Language, related_name='practices_language')

    def __unicode__(self):
        return unicode(self.user.username) + ' - ' + unicode(self.language.code)
