_k='floatView'
_c=__file__[:__file__.rfind('/')+1]+_k+'/'
_f=open(_c+'Code.py').read().replace('@',_k)
exec(_f.replace('@',_k))
_e=open(_c+'Example.txt').read()
for _i in tuple(locals()):
    if _i[:9]==_k:
        _f=_c+'@'+_i[9:]
        try:
            _g=open(_f+'.ini').read().splitlines()
        except:
            _g=()
        for _a in range(len(_g)):
            _g[_a]=_i+'.'+_g[_a]
            exec(_g[_a])
        _g='\n'.join(_g)
        _f=open(_f+'.txt').read()
        _f=(_f,_e,_g)
        _f="\n\n".join(_f)
        exec(f'{_i}.__doc__=_f')
del _a,_c,_e,_f,_g,_i,_k