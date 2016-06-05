from django.conf.urls import url, include
from django.contrib import admin
from profile import api_urls as profile_api_urls
from language import api_urls as language_api_urls
from meeting import api_urls as meeting_api_urls
from related import api_urls as related_api_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # API 1.0
    url(r'^api/1.0/', include(profile_api_urls)),
    url(r'^api/1.0/', include(language_api_urls)),
    url(r'^api/1.0/', include(meeting_api_urls)),
    url(r'^api/1.0/', include(related_api_urls)),
]

