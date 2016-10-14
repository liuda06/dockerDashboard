from django.conf.urls import patterns, url
from dockerDashboard.web import view

urlpatterns = patterns('',
                       url(r'^images/$',view.images),
                       url(r'^containers/$',view.containers),
url(r'^containers/start/([0-9a-z]*)$',view.container_start),
url(r'^containers/stop/([0-9a-z]*)$',view.container_stop),
                       )