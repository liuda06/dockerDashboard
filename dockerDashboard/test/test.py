a={'a':123}
c=a
c['uu']=''
print a


import copy
a={'a':123}
d=copy.copy(a)
d['uu']=''
print a

##################
port = [{u'IP': u'0.0.0.0', u'Type': u'tcp', u'PublicPort': 6379, u'PrivatePort': 6379},
        {u'IP': u'0.0.0.0', u'Type': u'tcp', u'PublicPort': 6379, u'PrivatePort': 6379}]
res = []
for i in port:
    if i.get('PublicPort'):
        res.append('%s:%d->%d/%s' % (i.get('IP'), i.get('PublicPort'), i.get('PrivatePort'), i.get('Type')))
    else:
        res.append('%d/%s' % (i.get('PrivatePort'), i.get('Type')))
print ' '.join(res)

##################
import json

aa={'ImageID': 'bb11232a492cee4fddc718ea0ae37e5f814499154685204da1aaf3e2d5cdc320'}
print json.dumps(aa)


##################
import json
a='[{"RepoDigests": null,"Created":1466711701,"Size":5042677,"VirtualSize":5042677,"Labels":null}]'
a=json.loads(a)
print a

b=eval(a)
print b

c={}
exec('c='+a)
print c