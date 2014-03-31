#!/usr/bin/python
# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta
from django.http import HttpResponse, Http404


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.now()
    html = "<html><body>It is now %s</body></html>" % now
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s</body></html>" % (offset, dt)
    return HttpResponse(html)