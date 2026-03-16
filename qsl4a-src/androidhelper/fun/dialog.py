def dialogShowAlert( self, title = "Alert", message = "The message of the alert .", positiveButtonText = "OK", negativeButtonText = None, neutralButtonText = None, messageIsHtml = False ):
    return self._rpc("dialogShowAlert", title, message, positiveButtonText, negativeButtonText, neutralButtonText, messageIsHtml)

def dialogShowSimpleChoice(self, title = "Alert", message = "The message of the alert .", items = None, positiveButtonText = "OK", negativeButtonText = None, neutralButtonText = None, messageIsHtml = False ):
    return self._rpc("dialogShowSimpleChoice", title, message, items, positiveButtonText, negativeButtonText, neutralButtonText, messageIsHtml)

def dialogShowSingleChoice(self, title = "Alert",message = "The message of the alert .", items = None, selected = -1, positiveButtonText = "OK", negativeButtonText = None, neutralButtonText = None, messageIsHtml = False ):
    return self._rpc("dialogShowSingleChoice", title, message, items, selected, positiveButtonText, negativeButtonText, neutralButtonText, messageIsHtml)

def dialogShowMultiChoice(self, title = "Alert", message = "The message of the alert .", items = None, selected = None, positiveButtonText = "OK", negativeButtonText = None, neutralButtonText = None, messageIsHtml = False ):
    return self._rpc("dialogShowMultiChoice", title, message, items, selected, positiveButtonText, negativeButtonText, neutralButtonText, messageIsHtml)

def dialogSetProgressMessage(self,message):
    return self._rpc("dialogSetProgressMessage",message)

def dialogSetMessageIsHtml(self, messageIsHtml = True):
    return self._rpc("dialogSetMessageIsHtml", messageIsHtml)

def dialogGetInput(self,title="Value",message="Please enter value :",defaultText=None,messageIsHtml=False):
    return self._rpc("dialogGetInput",title,message,defaultText,messageIsHtml)

def dialogSetSingleChoiceItems(self,items,selected=-1):
    return self._rpc("dialogSetSingleChoiceItems",items,selected)

def dialogCreateAlert(self,title=None,message=None):
    return self._rpc("dialogCreateAlert",title,message)

def dialogCreateDatePicker(self,year=1970,month=1,day=1):
    return self._rpc("dialogCreateDatePicker",year,month,day)

def dialogCreateHorizontalProgress(self,title=None,message=None,maximum_progress=100):
    return self._rpc("dialogCreateHorizontalProgress",title,message,maximum_progress)

def dialogCreateInput(self,title="Value",message="Please enter value:",defaultText=None,inputType=None):
    return self._rpc("dialogCreateInput",title,message,defaultText,inputType)

def dialogCreatePassword(self,title="Password",message="Please enter password:"):
    return self._rpc("dialogCreatePassword",title,message)

def dialogCreateSeekBar(self,starting_value=50,maximum_value=100,title="",message=""):
    return self._rpc("dialogCreateSeekBar",starting_value,maximum_value,title,message)

def dialogCreateSpinnerProgress(self,title=None,message=None,maximum_progress=100):
    return self._rpc("dialogCreateSpinnerProgress",title,message,maximum_progress)

def dialogCreateTimePicker(self,hour=0,minute=0,is24hour=False):
    return self._rpc("dialogCreateTimePicker",hour,minute,is24hour)

def dialogDismiss(self):
    return self._rpc("dialogDismiss")

def dialogGetPassword(self,title="Password",message="Please enter password:"):
    return self._rpc("dialogGetPassword",title,message)

def dialogGetResponse(self):
    return self._rpc("dialogGetResponse")

def dialogGetSelectedItems(self):
    return self._rpc("dialogGetSelectedItems")

def dialogSetCurrentProgress(self,current):
    return self._rpc("dialogSetCurrentProgress",current)

def dialogSetItems(self,items):
    return self._rpc("dialogSetItems",items)

def dialogSetMaxProgress(self,max):
    return self._rpc("dialogSetMaxProgress",max)

def dialogSetMultiChoiceItems(self,items,selected=None):
    return self._rpc("dialogSetMultiChoiceItems",items,selected)

def dialogSetNegativeButtonText(self,text):
    return self._rpc("dialogSetNegativeButtonText",text)

def dialogSetNeutralButtonText(self,text):
    return self._rpc("dialogSetNeutralButtonText",text)

def dialogSetPositiveButtonText(self,text):
    return self._rpc("dialogSetPositiveButtonText",text)

def dialogShow(self):
    return self._rpc("dialogShow")