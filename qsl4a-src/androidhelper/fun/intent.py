def makeIntent(self,action,uri=None,type=None,extras=None,categories=None,packagename=None,classname=None,flags=None):
    return self._rpc("makeIntent",action,uri,type,self._intentExtras(extras),categories,packagename,classname,flags)

def pathToUri(self,path,fileProvider=True,uriObject=False):
    result=self._rpc("pathToUri",path,fileProvider)
    if uriObject:
        return sl4a.Result(result.id,self.Uri(result.result),result.error)
    else:
        return result

def Uri(self,*s):
    self.Uri=self.Intent._uri
    return self.Uri(*s)

def _intentExtras(self,*s):
    self._intentExtras=self.Intent._intentExtras
    return self._intentExtras(*s)