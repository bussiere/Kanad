from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
        # Example:
        # (r'^galago/', include('galago.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'pages.views.Index'),
    (r'^page/$', 'pages.views.Pages'),
    (r'^films/', 'pages.views.Films'),
    (r'^actors/', 'pages.views.Actors'),
    (r'^pack/', 'pages.views.Packs'),
    (r'^imagese/', 'pages.views.ImageSe'),
    (r'^test/', 'pages.films.TestPanier'),
    (r'^login/','memberLogin.views.Login'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
