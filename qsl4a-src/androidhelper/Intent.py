'Common Intent Constants , for more Intent Constants, please refer https://developer.android.google.cn/reference/android/content/Intent.html .\n\nYou can use them like droid.startActivityIntent(droid.makeIntent(action=droid.Intent.ACTION_VIEW,uri="http://www.baidu.com",flags=droid.Intent.FLAG_ACTIVITY_NEW_DOCUMENT).result) .'

ACTION_MAIN='android.intent.action.MAIN'
ACTION_VIEW='android.intent.action.VIEW'
ACTION_EDIT='android.intent.action.EDIT'
ACTION_PICK='android.intent.action.PICK'
ACTION_CHOOSER='android.intent.action.CHOOSER'
ACTION_INSERT='android.intent.action.INSERT'
ACTION_DELETE='android.intent.action.DELETE'
ACTION_RUN='android.intent.action.RUN'
ACTION_SEND='android.intent.action.SEND'
ACTION_SYNC='android.intent.action.SYNC'
ACTION_SEARCH='android.intent.action.SEARCH'

FLAG_ACTIVITY_SINGLE_TOP = 536870912
FLAG_ACTIVITY_MULTIPLE_TASK = 134217728
FLAG_ACTIVITY_NEW_DOCUMENT = 524288
FLAG_ACTIVITY_CLEAR_TASK = 32768
FLAG_ACTIVITY_NEW_TASK = 268435456

EXTRA_TEXT='android.intent.extra.TEXT'
EXTRA_STREAM='android.intent.extra.STREAM'
EXTRA_SUBJECT='android.intent.extra.SUBJECT'
EXTRA_EMAIL='android.intent.extra.EMAIL'
EXTRA_HTML_TEXT='android.intent.extra.HTML_TEXT'

def _intentExtras(Extras):
    if not isinstance(Extras,dict):
        return Extras
    for Key in Extras.keys():
        Val = Extras[Key]
        if isinstance( Val ,( bytes, bytearray )):
            Extras[Key]='\x00byte\x00'+_encode(Val).decode()
        elif isinstance( Val, str ):
            if Val[0:1]=='\x00':
                Extras[Key]='\x00str\x00'+Val
        elif isinstance( Extras, dict ):
            Extras[Key]=_intentExtras(Val)
        elif isinstance( Val, Uri ):
            Extras[Key]='\x00uri\x00'+Val
    return Extras

class _uri(str):
    def __new__(cls,arg):
        HEAD='\x00uri\x00'
        if arg[:5]!=HEAD:
            arg=HEAD+arg
        return super(_uri,cls).__new__(cls,arg)
    def __repr__(self):
        return 'Uri("'+self[5:]+'")'
    def __str__(self):
        return self[5:]

from .__init__ import Android as _encode
_uri.__doc__=_encode.Uri.__doc__
from base64 import b64encode as _encode