# encoding: utf-8
""" Module for registering centralized signals """

__all__ = [
    'fileman_signals',
    'localsite_signals',
    'nodes_signals',
]

# Импортируем sse-сигналы, только при наличии sse
from django.conf import settings
if 'tornado_sse' in settings.INSTALLED_APPS:
    __all__.append('sse_signals')

from signals import *