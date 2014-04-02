#!/usr/bin/python
# -*- encoding: utf-8 -*-

from datetime import datetime, timedelta
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.shortcuts import render
from django.template.loader import get_template


def hello(request):
    return HttpResponse("Hello World")


def current_datetime(request):
    now = datetime.now()
    # Cap 4. (1º)
    #t = get_template('current_datetime.html')
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)

    # Cap 4. (2º)
    return render(request, 'current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.now() + timedelta(hours=offset)
    # Cap 4. (1º)
    # html = "<html><body>In %s hour(s), it will be %s</body></html>" % (offset, dt)
    # return HttpResponse(html)

    # Cap 4. (2º)
    return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})