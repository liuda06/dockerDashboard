import json
from dockerDashboard.http import http_client
from dockerDashboard.api import docker_api

DEFAULT_HOST = '192.168.137.147'
DEFAULT_PORT = 2375

param = {'Image': '7a',
         'OpenStdin': True,  # Keep STDIN open even if not attached -i
         'Tty': True,  # Allocate a pseudo-TTY -t
         'StdinOnce': False,  # StdinOnce':False== -d=true

         'PublishAllPorts': True,
         'HostConfig': {
             'Binds': [
                 '/opt:/opt/app',
                 '/vol:/vol/app:ro'
             ],
         },
         'PortBindings': {
             '80/tcp': [{'HostIp': '', 'HostPort': '8085'}]
         },
         'NetworkSettings': {
             'NetworkMode': 'bridge',
         },

}
param = json.dumps(param)
print param


def create_container(param):
    print http_client.post_req(
        headers={'Content-type': 'application/json'},
        body=param, host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_CREATE)


def delete_container():
    print http_client.delete_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.CONTAINER_DELETE % ('2cf96cca93bb'))


def delete_image():
    '''
    must use name , id is not unique
    :return:
    '''
    print http_client.delete_req(
        host=DEFAULT_HOST, port=DEFAULT_PORT,
        url=docker_api.IMAGES_DELETE % ('fdbfd7bf9'))


# create_container(param)