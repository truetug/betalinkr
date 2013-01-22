# encoding: utf-8
from datetime import datetime

from django import template

register = template.Library()


@register.simple_tag
def copyright(begin_year):
    """
    {% copyright 2007 %} and now 2009 show - 2007–2009 if now is 2007 shows 2007
    """
    end_year = datetime.now().year
    if end_year > begin_year: result = u'%s-%s' % (begin_year, end_year)
    else: result = u'%s' % begin_year

    return result
