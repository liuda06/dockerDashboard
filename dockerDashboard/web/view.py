# -*- coding: UTF-8 -*-
import time
import copy

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

from dockerDashboard.http import http_client
from dockerDashboard.constant import docker_api
from dockerDashboard.utils import convertor

DEFAULT_HOST = '192.168.137.147'
DEFAULT_PORT = 2375


def __bind_images_id(containes):
    bind_images = []
    for con in containes:
        bind_images.append(con.get('ImageID'))

    return bind_images


def __get_container_all():
    """
    200 – no error
    400 – bad parameter
    500 – server error
    :return:
    """
    status, data = http_client.get_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT, url=docker_api.CONTAINER_ALL)
    if status == 200:
        return convertor.transfer(data)
    return []


def __get_images():
    status, data = http_client.get_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT, url=docker_api.IMAGES_LIST)
    if status == 200:
        return convertor.transfer(data)
    return []


def images(request):
    data = __get_images()
    bind_images = __bind_images_id(__get_container_all())
    image_list = []
    for obj in data:
        index = 0
        if obj.get('Id') in bind_images:
            obj['used'] = True
        else:
            obj['used'] = False
        obj['Id'] = obj.get('Id')[obj.get('Id').index(':') + 1:]
        obj['Created'] = convertor.time_to_str(obj.get('Created'))
        obj['Size'] = convertor.size_format(obj.get('Size'))

        for tag in obj.get('RepoTags'):
            temp = copy.copy(obj)
            temp['tag'] = tag
            if index > 0: temp['used'] = False
            image_list.append(temp)
            index += 1

    return render_to_response('images.html', {'data': image_list})


def image_delete(request, image):
    print image
    http_client.delete_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.IMAGES_DELETE % (image))
    time.sleep(1)
    return HttpResponseRedirect('/images')


def containers(request):
    data = __get_container_all()
    for d in data:
        d['Created'] = convertor.time_to_str(d.get('Created'))
        d['Size'] = convertor.size_format(d.get('Size'))
        d['Ports'] = convertor.port_str(d.get('Ports'))

    return render_to_response('containers.html', {'data': data})


def container_start(request, container):
    http_client.post_req(
        headers={}, body=None, host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_START % (container))
    time.sleep(1)
    return HttpResponseRedirect('/containers')


def container_stop(request, container):
    http_client.post_req(
        headers={}, body=None, host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_STOP % (container))

    return HttpResponseRedirect('/containers')


def container_create(request, image):
    http_client.post_req(
        headers={'Content-type': 'application/json'},
        body=convertor.container_config(image), host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_CREATE)

    return HttpResponseRedirect('/containers')


def container_create_custom(request):
    http_client.post_req(
        headers={'Content-type': 'application/json'},
        body=convertor.container_config_custom(request), host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_CREATE)
    from django.http import JsonResponse
    return JsonResponse({'status':200,'msg':'创建成功！'})

def container_delete(request, container):
    http_client.delete_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_DELETE % (container))
    time.sleep(1)
    return HttpResponseRedirect('/containers')




