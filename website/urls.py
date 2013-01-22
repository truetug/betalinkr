# encoding: utf-8
from django.conf.urls import patterns, url, include
from django.http import HttpResponse
from django.conf import settings
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    (r'', include('apps.linkblog.urls', 'linkblog')),
    (r'', include('apps.localsite.urls', 'localsite')),
    (r'^admin/', include(admin.site.urls)),
)

from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
