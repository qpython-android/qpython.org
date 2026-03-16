def @(self,Args=None):
    return self._rpc("@",Args)
def @Result(self,index=-1):
    return self._rpc("@Result",index)
def @Remove(self,index=-1):
    return self._rpc("@Remove",index)
def @Count(self):
    return self._rpc("@Count")