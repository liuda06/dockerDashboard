from django.conf.urls import patterns, url
from dockerDashboard.web import view

urlpatterns = patterns('',
                       url(r'^$', view.images),  # default url
                       url(r'^images/$', view.images),
                       url(r'^host/list/$', view.host_list),
                       url(r'^host/test/$', view.host_test),
                       url(r'^host/add/$', view.host_add),
                       url(r'^host/delete/([0-9]*)$', view.host_delete),
                       url(r'^images/delete/([0-9a-z_:/.-]*)$', view.image_delete),
                       url(r'^containers/$', view.containers),
                       url(r'^containers/start/([0-9a-z]*)$', view.container_start),
                       url(r'^containers/stop/([0-9a-z]*)$', view.container_stop),
                       url(r'^containers/create/$', view.container_create_custom),
                       url(r'^containers/create/([0-9a-z]*)$', view.container_create),
                       url(r'^containers/shell/$', view.container_create_shell),
                       url(r'^containers/delete/([0-9a-z]*)$', view.container_delete),
                       url(r'^containers/restart/([0-9a-z]*)$', view.container_restart),
                       )
