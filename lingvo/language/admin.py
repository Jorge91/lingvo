from django.contrib import admin

from language.models import Language, User_practices_language
from language.models import User_speaks_language


admin.site.register(Language)
admin.site.register(User_speaks_language)
admin.site.register(User_practices_language)


