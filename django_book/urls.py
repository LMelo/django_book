from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from views import hello, display_meta, current_datetime, hours_ahead


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_book.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^another-time-page/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^display_meta/$', display_meta),
    url(r'^books/', include('books.urls', namespace="books"))
)
