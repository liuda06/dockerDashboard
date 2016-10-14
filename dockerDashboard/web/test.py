# a='[{"RepoDigests": null,"Created":1466711701,"Size":5042677,"VirtualSize":5042677,"Labels":null}]'
# import json
# a=json.loads(a)
#
# print a
#
# b=eval(a)
# print b
#
# c={}
# exec('c='+a)
# print c
dis = [{u'Created': 1476152294, u'Labels': {}, u'VirtualSize': 751178521,
        u'ParentId': u'sha256:76132c07635cdf0fbaea9b7c9ed2486601d36343a4a9d2670e9c83d603d570be',
        u'RepoTags': [u'iaasos/compute:latest'], u'RepoDigests': None,
        u'Id': u'sha256:2c3f26f496891d9af7cc45c3abc06331b434b4a3e784b384b52522dacc016786', u'Size': 751178521},
       {u'Created': 1475999806, u'Labels': {}, u'VirtualSize': 751178524,
        u'ParentId': u'sha256:d36021dd293648a317dcd40ff9c391a1fefb28c7b88e959744371a224f0af5c5',
        u'RepoTags': [u'<none>:<none>'], u'RepoDigests': [u'<none>@<none>'],
        u'Id': u'sha256:5f6a69a93326fead5087c8ee8d6eb3cc8143217e3164881cfcf41e2e9a78f515', u'Size': 751178524},
       {u'Created': 1475914469, u'Labels': {}, u'VirtualSize': 751178287,
        u'ParentId': u'sha256:3c8b78ca54eb229926e04e4ec85d04e58033e506e537d02d51c675b227d70c01',
        u'RepoTags': [u'<none>:<none>'], u'RepoDigests': [u'<none>@<none>'],
        u'Id': u'sha256:734664e9a82f3015c44885d0220b566baf37645cbc5f89255fbaf990c7c952a9', u'Size': 751178287},
       {u'Created': 1475125941,
        u'Labels': {u'build-date': u'20160729', u'vendor': u'CentOS', u'name': u'CentOS Base Image',
                    u'license': u'GPLv2'}, u'VirtualSize': 196742175,
        u'ParentId': u'sha256:252236e4404c7b363654c293afb7d715e7e4cca17f67fee3d7c55ed7ff63f073',
        u'RepoTags': [u'kingaric/centos:ctl'], u'RepoDigests': None,
        u'Id': u'sha256:f4bd3269b6fad0dd5912aed3bd650eebe7d9a4d0ef079132f6cbc07c7b310e5d', u'Size': 196742175},
       {u'Created': 1475120969,
        u'Labels': {u'build-date': u'20160729', u'vendor': u'CentOS', u'name': u'CentOS Base Image',
                    u'license': u'GPLv2'}, u'VirtualSize': 211047617, u'ParentId': u'',
        u'RepoTags': [u'kingaric/redis:latest'], u'RepoDigests': None,
        u'Id': u'sha256:f2a440ec5dde1a03b344f94db270bd81ad1532abcc6b68bb820fac8954e92a54', u'Size': 211047617},
       {u'Created': 1474925169, u'Labels': {}, u'VirtualSize': 187945997, u'ParentId': u'',
        u'RepoTags': [u'ubuntu:14.04'], u'RepoDigests': None,
        u'Id': u'sha256:f2d8ce9fa988ed844dda693fe260b9afd393b9a65b647aa02f62d6eecdb7b635', u'Size': 187945997},
       {u'Created': 1474428531,
        u'Labels': {u'build-date': u'20160729', u'vendor': u'CentOS', u'name': u'CentOS Base Image',
                    u'license': u'GPLv2'}, u'VirtualSize': 560779734,
        u'ParentId': u'sha256:f8e7849ffc4e98feddc2c66014f40431c7bf9731664ce60e128c3d779378793f',
        u'RepoTags': [u'kingaric/wssh:latest'], u'RepoDigests': None,
        u'Id': u'sha256:266aafd24f963b1ea95ff471637b310ff88d9dc0063c5e350d16ad842ad598d7', u'Size': 560779734},
       {u'Created': 1473196220,
        u'Labels': {u'build-date': u'20160906', u'vendor': u'CentOS', u'name': u'CentOS Base Image',
                    u'license': u'GPLv2'}, u'VirtualSize': 196751668, u'ParentId': u'', u'RepoTags': [u'centos:7'],
        u'RepoDigests': None, u'Id': u'sha256:980e0e4c79ec933406e467a296ce3b86685e6b42eed2f873745e6a91d718e37a',
        u'Size': 196751668}, {u'Created': 1469825950, u'Labels': {u'build-date': u'20160729', u'vendor': u'CentOS',
                                                                  u'name': u'CentOS Base Image', u'license': u'GPLv2'},
                              u'VirtualSize': 196742175, u'ParentId': u'',
                              u'RepoTags': [u'centos:latest', u'kingaric/centos:7'], u'RepoDigests': None,
                              u'Id': u'sha256:97063303644439d9cea259b0e5f4b468633c90d88bf526acc67e5ae0a6e9427c',
                              u'Size': 196742175},
       {u'Created': 1469200742, u'Labels': {}, u'VirtualSize': 187957795, u'ParentId': u'',
        u'RepoTags': [u'ubuntu:latest'], u'RepoDigests': None,
        u'Id': u'sha256:0ccb13bf19544abff3bd1f5e69e17c2ad99439408a5a0bac15cf00443bdeb2c7', u'Size': 187957795},
       {u'Created': 1466711701, u'Labels': None, u'VirtualSize': 5042677, u'ParentId': u'',
        u'RepoTags': [u'kingaric/alpine:latest'], u'RepoDigests': None,
        u'Id': u'sha256:39cb6206bacb754ce1467012347b010a47f849bd55a858d3ce6410e8b67bb85c', u'Size': 5042677}]
#
# print len(dis)
# for d in dis:
#     print d.get('Id'),d.get('RepoTags')

id=u'sha256:39cb6206bacb754ce1467012347b010a47f849bd55a858d3ce6410e8b67bb85c'
print id.index(':')
print id[id.index(':')+1:]


import time
x=time.localtime(1466711701)
print time.strftime('%Y-%m-%d %H:%M:%S',x)


port=[{u'IP': u'0.0.0.0', u'Type': u'tcp', u'PublicPort': 6379, u'PrivatePort': 6379},{u'IP': u'0.0.0.0', u'Type': u'tcp', u'PublicPort': 6379, u'PrivatePort': 6379}]
res=[]
for i in port:
    res.append('%s:%d->%d/%s'%(i.get('IP'),i.get('PublicPort'),i.get('PrivatePort'),i.get('Type')))

print ' '.join(res)