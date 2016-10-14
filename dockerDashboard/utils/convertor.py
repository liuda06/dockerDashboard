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
        res.append('%s:%d->%d/%s' %
                   (i.get('IP'),
                    i.get('PublicPort'),
                    i.get('PrivatePort'),
                    i.get('Type')))
    return ' '.join(res)
