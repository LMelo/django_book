#!/usr/bin/python
# -*- encoding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns(
    'books.views',
    url(r'search/$', 'search', name="book_search"),
)
