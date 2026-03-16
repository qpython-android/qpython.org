#Full Screen Method

def fullGetProperty(self,id,property):
    return self._rpc("fullGetProperty",id,property)

def fullGetProperties(self,ids,property):
    return self._rpc("fullGetProperties",ids,property)

def fullSetProperty(self,id,property,value):
    return self._rpc("fullSetProperty",id,property,value)

def fullSetProperties(self,ids,property,value):
    return self._rpc("fullSetProperties",ids,property,value)

def fullGetScreenShot(self, path = None):
    return self._rpc("fullGetScreenShot",path)

def fullSetList(self,id,list,isHtml=False,listType=0):
    return self._rpc("fullSetList",id,list,isHtml,listType)

def fullSetList2(self,id,list,intRes):
    return self._rpc("fullSetList2",id,list,intRes)

def fullSetListSelected(self,id,selected):
    return self._rpc("fullSetListSelected",id,selected)

def fullGetListSelected(self,id):
    return self._rpc("fullGetListSelected",id)

def fullShow(self,layout,title=None,theme=None):
    return self._rpc("fullShow",layout,title,theme)

def fullDismiss(self):
    return self._rpc("fullDismiss")

def fullQuery(self):
    return self._rpc("fullQuery")

def fullQueryDetail(self,id):
    return self._rpc("fullQueryDetail",id)