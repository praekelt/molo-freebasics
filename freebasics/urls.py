import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from .views import search, HomeView

# implement CAS URLs in a production setting
if settings.ENABLE_SSO:
    urlpatterns = patterns(
        '',
        url(r'^admin/login/', 'django_cas_ng.views.login'),
        url(r'^admin/logout/', 'django_cas_ng.views.logout'),
        url(r'^admin/callback/', 'django_cas_ng.views.callback'),
    )
else:
    urlpatterns = patterns('', )

urlpatterns += patterns(
    '',
    url(r'^django-admin/', include(admin.site.urls)),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'search/$', search, name='search'),

    url(r'^profiles/',
        include('molo.profiles.urls',
                namespace='molo.profiles',
                app_name='molo.profiles')),

    url(r'^comments/',
        include('django_comments.urls',
                namespace='django_comments',
                app_name='django_comments')),

    url(r'^commenting/',
        include('molo.commenting.urls',
                namespace='molo.commenting',
                app_name='molo.commenting')),

    url(r'^yourwords/',
        include('molo.yourwords.urls',
                namespace='molo.yourwords',
                app_name='molo.yourwords')),

    url(r'^polls/',
        include('molo.polls.urls',
                namespace='molo.polls',
                app_name='molo.polls')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'', include('molo.core.urls')),
    url(r'', include(wagtail_urls)),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL + 'images/',
        document_root=os.path.join(settings.MEDIA_ROOT, 'images'))
