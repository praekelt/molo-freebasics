import os

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls
from django.views.generic import TemplateView


from .views import (HomeView, FreeBasicsRegistrationView,
                    FreeBasicsProfilePasswordChangeView)

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
    url(r'^robots\.txt$', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain')),
    url(r'^sitemap\.xml$', 'wagtail.contrib.wagtailsitemaps.views.sitemap'),
    url(
        r'^profiles/register/$',
        FreeBasicsRegistrationView.as_view(),
        name='user_register'),
    url(
        r'^profiles/password-reset/$',
        login_required(FreeBasicsProfilePasswordChangeView.as_view()),
        name="profile_password_change"),
    url(r'^profiles/',
        include('molo.profiles.urls',
                namespace='molo.profiles',
                app_name='molo.profiles')),

    url(r'^commenting/', include('molo.commenting.urls',
        namespace='molo.commenting',
        app_name='molo.commenting')),

    url(r'', include('django_comments.urls')),

    url(r'^yourwords/',
        include('molo.yourwords.urls',
                namespace='molo.yourwords',
                app_name='molo.yourwords')),

    url(r'^polls/',
        include('molo.polls.urls',
                namespace='molo.polls',
                app_name='molo.polls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^403/$', TemplateView.as_view(template_name='403.html')),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
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
