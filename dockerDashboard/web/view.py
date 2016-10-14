# -*- coding: UTF-8 -*-
import time

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from dockerDashboard.http import http_client
from dockerDashboard.constant import docker_api
from dockerDashboard.utils import convertor

DEFAULT_HOST = '0.0.0.0'
DEFAULT_PORT = 2375


def images(request):
    status, data = http_client.get_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT, url=docker_api.IMAGES_LIST)
    data = convertor.transfer(data)
    for d in data:
        d['Id'] = d.get('Id')[d.get('Id').index(':') + 1:]
        d['Created'] = convertor.time_to_str(d.get('Created'))
        d['Size'] = convertor.size_format(d.get('Size'))
        print d['Size']
    return render_to_response('images.html', {'data': data})


def containers(request):
    status, data = http_client.get_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT, url=docker_api.CONTAINER_ALL)
    data = convertor.transfer(data)
    for d in data:
        d['Created'] = convertor.time_to_str(d.get('Created'))
        d['Size'] = convertor.size_format(d.get('Size'))
        d['Ports'] = convertor.port_str(d.get('Ports'))
        print d['Size']
    return render_to_response('containers.html', {'data': data})


def container_start(request, container):
    status, data = http_client.post_req(
        headers={}, body=None, host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_START % (container))
    time.sleep(1)
    return HttpResponseRedirect('/containers')


def container_stop(request, container):
    status, data = http_client.post_req(
        headers={}, body=None, host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_STOP % (container))

    return HttpResponseRedirect('/containers')
