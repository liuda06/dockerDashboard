# -*- coding: UTF-8 -*-
import time
import copy
import commands

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from dockerDashboard.http import http_client
from dockerDashboard.api import docker_api
from dockerDashboard.utils import convertor
from dockerDashboard.web.models import DockerHost

DEFAULT_SERVER = None


def docker_hosts(request=None):
    global DEFAULT_SERVER
    data = DockerHost.objects.all()
    if len(data) <= 0:
        return []
    if request:
        server = request.COOKIES.get('docker_server')
        if server:
            for d in data:
                if d.id == int(server):
                    DEFAULT_SERVER = d
                    d.selected = "selected"
                    return data
    DEFAULT_SERVER = data[0]
    return data


def __default_server(request):
    server = request.COOKIES.get('docker_server')
    global DEFAULT_SERVER
    if DEFAULT_SERVER and server and DEFAULT_SERVER.id == int(server):
        return DEFAULT_SERVER
    docker_hosts(request)
    return DEFAULT_SERVER


def host_list(reqest):
    return render_to_response('dockerHost.html', {'data': docker_hosts()})


def host_delete(request, host_id):
    global DEFAULT_SERVER
    if host_id:
        obj = DockerHost.objects.get(id=int(host_id))
        if obj == __default_server(request): DEFAULT_SERVER = None
        obj.delete()
    return HttpResponseRedirect('/host/list')


@csrf_exempt
def host_test(request):
    addr = request.POST.get('ip_addr')
    if not convertor.validate_ip(addr):
        return JsonResponse({'status': 200, 'msg': '请输入正确的ip:port！'})

    status, output = commands.getstatusoutput('curl http://%s/info' % (addr))
    if status == 0:
        return JsonResponse({'status': 200, 'msg': '连接成功！'})
    else:
        return JsonResponse({'status': 200, 'msg': '连接失败！'})


@csrf_exempt
def host_add(request):
    addr = request.POST.get('ip_addr')
    if convertor.validate_ip(addr):
        index = addr.index(':')
        if DockerHost.objects.filter(ip=addr[:index], port=int(addr[index + 1:])).all():
            return JsonResponse({'status': 200, 'msg': '禁止添加重复地址！'})
        DockerHost(ip=addr[:index], port=int(addr[index + 1:])).save()
        return JsonResponse({'status': 200, 'msg': '添加成功！', 'request': '/host/list'})
    return JsonResponse({'status': 200, 'msg': '请输入正确的ip:port！'})


def __bind_images_id(containers):
    bind_images = []
    for con in containers:
        bind_images.append(con.get('ImageID'))

    return bind_images


def __get_container_all(request):
    """
    200 – no error
    400 – bad parameter
    500 – server error
    :return:
    """
    server = __default_server(request)
    if server:
        status, data = http_client.get_req(
            host=server.ip, port=server.port, url=docker_api.CONTAINER_ALL)
        if status == 200:
            return convertor.transfer(data)
    return []


def __get_images(request):
    server = __default_server(request)
    if server:
        status, data = http_client.get_req(
            host=server.ip, port=server.port, url=docker_api.IMAGES_LIST)
        if status == 200:
            return convertor.transfer(data)
    return []


def images(request):
    data = __get_images(request)
    bind_images = __bind_images_id(__get_container_all(request))
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

    return render_to_response('images.html',
                              {'data': image_list, 'docker_hosts': docker_hosts(request)})


def image_delete(request, image):
    server = __default_server(request)
    http_client.delete_req(
        host=server.ip, port=server.port,
        url=docker_api.IMAGES_DELETE % (image))
    time.sleep(1)
    return HttpResponseRedirect('/images')


def containers(request):
    data = __get_container_all(request)
    for d in data:
        d['Created'] = convertor.time_to_str(d.get('Created'))
        d['Size'] = convertor.size_format(d.get('Size'))
        d['Ports'] = convertor.port_str(d.get('Ports'))

    return render_to_response('containers.html',
                              {'data': data, 'docker_hosts': docker_hosts(request)})


def container_start(request, container):
    server = __default_server(request)
    http_client.post_req(
        headers={}, body=None, host=server.ip, port=server.port,
        url=docker_api.CONTAINER_START % (container))
    time.sleep(1)
    return HttpResponseRedirect('/containers')


def container_stop(request, container):
    server = __default_server(request)
    http_client.post_req(
        headers={}, body=None, host=server.ip, port=server.port,
        url=docker_api.CONTAINER_STOP % (container))

    return HttpResponseRedirect('/containers')


def container_create(request, image):
    server = __default_server(request)
    http_client.post_req(
        headers={'Content-type': 'application/json'},
        body=convertor.container_config(image), host=server.ip, port=server.port,
        url=docker_api.CONTAINER_CREATE)

    return HttpResponseRedirect('/containers')


# todo bug: the vlume and ports is not together used
def container_create_custom(request):
    """
    Status Codes:   201 – no error
    :param request:
    :return:
    """
    server = __default_server(request)
    status, data = http_client.post_req(
        headers={'Content-type': 'application/json'},
        body=convertor.container_config_custom(request), host=server.ip, port=server.port,
        url=docker_api.CONTAINER_CREATE)
    if status == 201:
        return JsonResponse({'status': 200, 'msg': '创建成功！', 'request': '/containers'})
    else:
        return JsonResponse({'status': -1, 'msg': data})


def container_delete(request, container):
    server = __default_server(request)
    http_client.delete_req(
        host=server.ip, port=server.port,
        url=docker_api.CONTAINER_DELETE % (container))
    time.sleep(1)
    return HttpResponseRedirect('/containers')


def container_restart(request, container):
    server = __default_server(request)
    http_client.post_req(
        host=server.ip, port=server.port,
        headers={'Content-type': 'application/json'},
        body=None,
        url=docker_api.CONTAINER_RESTART % (container))
    time.sleep(1)
    return HttpResponseRedirect('/containers')
