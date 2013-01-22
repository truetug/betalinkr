# encoding: utf-8
from django.conf.urls import patterns, url

from .views import Frontpage

urlpatterns = patterns('',
    url(r'^$', Frontpage.as_view(), name='frontpage')
)
