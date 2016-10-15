# -*- coding: UTF-8 -*-
"""
Status Codes:
204 – no error
404 – no such container
500 – server error

"""

# IMAGES
IMAGES_LIST = '/images/json'            #get
IMAGES_BUILD = ''
IMAGES_DELETE = '/images/%s'     #/images/( name ) delete

# CONTAINER
CONTAINER_LIST = '/containers/json'      #get
CONTAINER_ALL='/containers/json?all=1'   #get
CONTAINER_CREATE = '/containers/create'     #post
CONTAINER_START = '/containers/%s/start' #/containers/(id)/start post
CONTAINER_STOP = '/containers/%s/stop'   #/containers/(id)/stop?t=5  post
CONTAINER_RESTART = ''
CONTAINER_DELETE = '/containers/%s'    #/containers/(id)?v=1 delete
CONTAINER_INFO = ''
