_c="""
StartService ()
Start the Accessibility Service .
Return True if start successful .
Return False if start failed .

ServiceEnabled ()
Check if Accessibility Service is Enabled ,
Return True or False .

Click ( x=0, y=0, t=50 )
Accessibility Click the Screen Point with the Coordinates ( x, y ) ,
Default Coordinates ( 0, 0 ) means the Center of the Screen ,
The Coordinates ( x, y ) can be Integers or Decimals such as 0.5 or -1.5 ,
parameter Integer t is the Press Time for Milliseconds , default is 50 .

Slide ( XnYn=None, t=None )
Accessibility Slide the Screen with Multi Points ,
XnYn is a Coordinate Set consisting of n points ( X1, Y1, X2, Y2, …… Xn, Yn ) ,
Coordinates X=Y=0 means the Center of the Screen ,
The Coordinates X and Y can be Integers or Decimals such as 0.5 or -1.5 ,
parameter Integer t is the Slide Time for Milliseconds , default value None means 50*n ( 50n milliseconds ) .

Action ( actionCode )
Do Accessibility Action with the designated Action Code .
Return True for successful execution and False for failed execution .
Some action codes are not supported by certain models .
BACK = 1
HOME = 2
RECENTS = 3
NOTIFICATIONS = 4
QUICK_SETTINGS = 5
POWER_DIALOG = 6
TOGGLE_SPLIT_SCREEN = 7
LOCK_SCREEN = 8
TAKE_SCREENSHOT = 9
KEYCODE_HEADSETHOOK = 10
ACCESSIBILITY_BUTTON = 11
ACCESSIBILITY_BUTTON_CHOOSER = 12
ACCESSIBILITY_SHORTCUT = 13
ACCESSIBILITY_ALL_APPS = 14
DISMISS_NOTIFICATION_SHADE = 15
DPAD_UP = 16
DPAD_DOWN = 17
DPAD_LEFT = 18
DPAD_RIGHT = 19
DPAD_CENTER = 20
MENU = 21
MEDIA_PLAY_PAUSE = 22
"""

for _c in _c[1:-1].split('\n\n'):
    _c='accessibility'+_c
    _e=_c.find(' (')
    _d=_c[:_e]
    _e=_c[_e+2:_c.find(')')]
    _b=[]
    for _a in _e.split(","):
        _b.append(_a.split("=")[0])
    _b=",".join(_b)
    exec(f'''
def {_d}(self,{_e}):
    return self._rpc("{_d}",{_b})
{_d}.__doc__=_c
''')

for _e in _c.split("\n"):
    if _e.find('=')>0:
        exec(f"{_d}.{_e}")

del _a,_b,_c,_d,_e
