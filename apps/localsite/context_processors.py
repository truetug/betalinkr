# encoding: utf-8
from django.conf import settings
from django.utils.functional import lazy
from django.contrib.sites.models import get_current_site


def version(request):
    def _get_val():
        result = 'NOTPROVIDED'

        if hasattr(settings, 'VERSION'):
            result = '.'.join(settings.VERSION)

        return result

    _get_val = lazy(_get_val, str)

    return {'version': _get_val()}


def sitename(request):
    def _get_val():
        result = 'NOTPROVIDED'

        current_site = get_current_site(request)

        return current_site.name

    _get_val = lazy(_get_val, str)

    return {'sitename': _get_val()}
