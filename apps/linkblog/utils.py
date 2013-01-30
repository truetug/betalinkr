#coding: utf-8
from urlparse import urlparse
from base64 import encodestring

from bs4 import BeautifulSoup
import requests
from requests import RequestException

def get_link_info(url):
    ret = {}
    try:
        req = requests.get(url)
    except RequestException:
        return ret
    else:
        soup = BeautifulSoup(req.content)

    ret['title'] = soup.title.text if soup.title else None
    favicon = soup.find('link', {'rel': 'icon'})
    favicon_href = favicon.get('href') if favicon else None
    if not favicon_href:
        link = urlparse(url)
        favicon_href = '%s://%s/favicon.ico' % (link.scheme, link.hostname)

    try:
        req = requests.get(favicon_href)
    except RequestException:
        ret['favicon'] = None
        ret['favicon_type'] = None
    else:
        ret['favicon'] = encodestring(req.content)
        ret['favicon_type'] = req.headers.get('content-type')

    #http://code.google.com/p/arc90labs-readability/

    return ret
