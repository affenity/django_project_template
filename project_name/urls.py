from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #uncomment next line to redirect base site url to /home/
    #url(r'^$', RedirectView.as_view(url='/home/')),

    url(r'^admin/', include(admin.site.urls)),
)

#serving static media files,js,css for development server. DO NOT USE THIS FOR DEPLOYMENT. 

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('', (r'^%s(?P<path>.*)$'%_media_url, serve, {'document_root': settings.MEDIA_ROOT}),
    )
    del(_media_url, serve)