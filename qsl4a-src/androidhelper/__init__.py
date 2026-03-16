from . import sl4a

class Android(sl4a.Android):
    _o=sl4a.os
    _l=_o.listdir
    _o=_o.path.isdir
    _g=__file__[:-11]

    def _addMethod(_file):
        exec(open(__file__[:-11]+_file+'.py').read())
        for _i in tuple(locals()):
            if _i[0]=='_':
                continue
            exec(f"sl4a.Android.{_i}={_i}")
        locals().clear()

    _f=_g+'fun/'
    for _i in _l(_f):
        _t=open(_f+_i).read()
        exec(_t)

    _f=[_g+'doc/']
    while len(_f)>0:
        _p=_f.pop(-1)
        for _i in _l(_p):
            _t=_p+_i
            if _o(_t):
                _f.append(_t+'/')
            else:
                try:
                    _t=open(_t).read()
                    exec(_i[:-4]+".__doc__=_t")
                except:pass

    _f=_g+'const/'
    for _i in _l(_f):
        try:
            _t=open(_f+_i).read().splitlines()
            _i=_i[:-4]
            _o=[eval(_i+".__doc__"),'']
            if _o[0]==None:
                _o[0]=''
            for _t in _t:
                _p=_i+"."+_t
                exec(_p)
                _o.append(_p)
            _o='\n'.join(_o)
            exec(_i+".__doc__=_o")
        except:pass
    
    def _addMethod(_self,_file):
        if '_'+_file in _self.__dict__:
            return
        exec(open(__file__[:-11]+_file+'.py').read())
        exec(f'_self._{_file}=None')
        from types import MethodType as _m
        for _i in tuple(locals()):
            if _i[0]=='_':
                continue
            exec(f'_self.{_i}=_m({_i},_self)')
        locals().clear()
    
    def _addClass(_self,_file):
        if '_'+_file in _self.__dict__:
            return
        exec(f'_self._{_file}=None')
        exec(f'from .{_file} import {_file}\n{_file}(_self)')
        del _self,_file

    del _f,_i,_t,_l,_g,_o,_p