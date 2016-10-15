import json
import time

'''
utils
'''


def transfer(s):
    return json.loads(s)


def time_to_str(t):
    t = time.localtime(t)
    return time.strftime('%Y-%m-%d %H:%M:%S', t)


def size_format(b, temp=1000.0):
    if b == 0 or b is '' or b is u'' or b is None:
        return 0
    elif b < temp:
        return '%i' % b + 'B'
    elif temp <= b < temp ** 2:
        return '%.1f' % float(b / temp) + 'KB'
    elif temp ** 2 <= b < temp ** 3:
        return '%.1f' % float(b / temp ** 2) + 'MB'
    elif temp ** 3 <= b < temp ** 4:
        return '%.1f' % float(b / temp ** 3) + 'GB'
    elif temp ** 4 <= b:
        return '%.1f' % float(b / temp ** 4) + 'TB'


def port_str(s):
    """
    [{u'IP': u'0.0.0.0', u'Type': u'tcp', u'PublicPort': 6379, u'PrivatePort': 6379}]
    :param s:
    :return:
    """
    res = []
    for i in s:
        if i.get('PublicPort'):
            res.append('%s:%d->%d/%s' %
                       (i.get('IP'), i.get('PublicPort'), i.get('PrivatePort'), i.get('Type')))
        else:
            res.append('%d/%s' % (i.get('PrivatePort'), i.get('Type')))
    return ' '.join(res)


def container_config(image):
    param = {'Image': image,
             'OpenStdin': True,  # Keep STDIN open even if not attached ==> -i
             'Tty': True,  # Allocate a pseudo-TTY ==> -t
             'StdinOnce': False,  # StdinOnce':False==> -d=true
             'PublishAllPorts': True,
             }
    return json.dumps(param)

def container_config_custom(request):
    image=request.GET.get('image')
    start_rule = request.GET.get('start_rule') #0 1 2 d it dit
    host_path = request.GET.get('host_path')
    container_path = request.GET.get('container_path')
    host_port = request.GET.get('host_port')
    container_port = request.GET.get('container_port')
    cpu = request.GET.get('cpu')
    memery = request.GET.get('memery')
    cmd = request.GET.get('cmd')
    if start_rule==0:
        param = {'Image': image,
                 'OpenStdin': False,
                 'Tty': False,
                 'StdinOnce': False,
                 'PublishAllPorts': True,
                 }
    elif start_rule==1:
        param = {'Image': image,
                 'OpenStdin': True,
                 'Tty': True,
                 'StdinOnce': True,
                 'PublishAllPorts': True,
                 }
    else:
        param = {'Image': image,
                 'OpenStdin': True,
                 'Tty': True,
                 'StdinOnce': False,
                 'PublishAllPorts': True,
                 }

    if host_port and container_port:
        param['PortBindings'] = {
            '%s/tcp'%(container_port): [{'HostIp': '', 'HostPort': '%s'%(host_port)}]
        }
    if host_path and container_path:
        param['Mounts'] = [
            {
                'Source': '%s'%(host_path),
                'Destination': '%s'%(container_path),
                'Mode': '',
                'RW': True,
                'Propagation': 'rslave'
            }
        ]

    if memery:
        param['Memory']=memery
    if cpu:
       #  Cpu ==> http://www.open-open.com/news/view/1780c43
       pass

    if cmd:
        param['Cmd']=[cmd]

    return json.dumps(param)