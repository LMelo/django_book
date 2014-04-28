#!/usr/bin/python
# -*- encoding: utf-8 -*-

import re
from django import template
from datetime import datetime


register = template.Library()


# NOME DO FILTRO NO TEMPLATE
@register.filter(name='cut')
# FUNCAO A SER EXECUTADA
def cut(value, arg):
    return value.replace(arg, '')


class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.now()
        return now.strftime(self.format_string)


class CurrentTimeNode2(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.now()
        context['current_time'] = now.strftime(self.format_string)
        return ''

    # {% current_time2 "%Y-%M-%d %I:%M %p" %}
    # <p>The time is {{ current_time }}.</p>


class CurrentTimeNode3(template.Node):
    def __init__(self, format_string, var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''


# NOME DA TAG NO TEMPLATE
@register.tag(name='current_time')
# FUNCAO A SER EXECUTADA
def do_current_time(parser, token):
    try:
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)

    return CurrentTimeNode(format_string[1:-1])

# PARA O CURRENTTIMENODE3
# def do_current_time(parser, token):
#     # This version uses a regular expression to parse tag contents.
#     try:
#         # Splitting by None == splitting by spaces.
#         tag_name, arg = token.contents.split(None, 1)
#     except ValueError:
#         msg = '%r tag requires arguments' % token.contents[0]
#         raise template.TemplateSyntaxError(msg)
#
#     m = re.search(r'(.*?) as (\w+)', arg)
#     if m:
#         fmt, var_name = m.groups()
#     else:
#         msg = '%r tag had invalid arguments' % tag_name
#         raise template.TemplateSyntaxError(msg)
#
#     if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
#         msg = "%r tag's argument should be in quotes" % tag_name
#         raise template.TemplateSyntaxError(msg)
#
#     return CurrentTimeNode3(fmt[1:-1], var_name)