#简易 SL4A 服务 : 快速 但 单实例 功能限制
#by 乘着船 2021-2024

import os,socket as s

k=os.environ.get
c=s.create_connection((k('AP_HOST'),k('AP_PORT'))).makefile("rw")

import collections
from json import dumps,loads
i=0
w,s,c=c.write,c.flush,c.readline

def jsla(method,*params):
    global i
    w(dumps({'id':i,
    'method':method,'params':params})+'\n')
    s()
    i+=1
    return c()

jsla('_authenticate',k('AP_HANDSHAKE'))
k=collections.namedtuple('Result','id,result,error')

def rsla(*a):
    return loads(jsla(*a))['result']
    
def esla(*a):
    r=loads(jsla(*a))
    if r['error']:
        raise Exception(r['error'])
    else:
        return r['result']

def nsla(*a):
    return k(**loads(jsla(*a)))

class Android:
    def __getattr__(self,method):
        def f(*params):
            return nsla(method,*params)
        setattr(self,method,f)
        return f
droid=Android()

__all__=('droid','esla','rsla','jsla','os')