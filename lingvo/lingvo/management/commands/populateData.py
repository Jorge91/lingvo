# -*- coding: utf-8 -*-
from random import randint

from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import BaseCommand

from django.utils.translation import ugettext as _

from language.models import Language, User_speaks_language, User_practices_language

USERS_TO_CREATE = 100

class Command(BaseCommand):
    help = _(u'Syncs all contracts data')

    def populate(self):
        #call_command('loaddata', 'fixture.json')
        len_languages = Language.objects.all().count()

        for x in range(0, USERS_TO_CREATE):
            print str(x) + '/' + str(USERS_TO_CREATE)
            user = User.objects.create(username='username' + str(x), password='password')
            for y in range(0, 50):
                pos = randint(0, len_languages - 1)
                lang = Language.objects.all()[pos]
                try:
                    if y%2==0:
                        User_speaks_language.objects.create(language=lang, user=user)
                    else:
                        User_practices_language.objects.create(language=lang, user=user)
                except Exception as e:
                    print e



    def handle(self, *args, **options):
        print 'Populating data...'
        self.populate()

