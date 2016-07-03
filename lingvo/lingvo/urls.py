from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from lingvo.settings import MEDIA_ROOT
from lingvo.views import IndexView, LoginView, LogoutView
from profile import api_urls as profile_api_urls
from language import api_urls as language_api_urls
from meeting import api_urls as meeting_api_urls
from related import api_urls as related_api_urls
from chat import api_urls as chat_api_urls


urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': MEDIA_ROOT,
    }),

    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),# login required
    url(r'^login/?$', LoginView.as_view(), name='login'),
    url(r'^logout/?$', LogoutView.as_view(), name='logout'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),

    # API 1.0
    url(r'^api/1.0/', include(profile_api_urls)),
    url(r'^api/1.0/', include(language_api_urls)),
    url(r'^api/1.0/', include(meeting_api_urls)),
    url(r'^api/1.0/', include(related_api_urls)),
    url(r'^api/1.0/', include(chat_api_urls)),
]

