

from subprocess import Popen as Popen_original
from subprocess import STARTUPINFO

#IDLE_PRIORITY         0x00000040 ok
#BELOW_NORMAL_PRIORITY 0x00004000 ok
#NORMAL_PRIORITY       0x00000020 ok
#ABOVE_NORMAL_PRIORITY 0x00008000 ok
#HIGH_PRIORITY         0x00000080 ok
#REALTIME_PRIORITY     0x00000100 ok
#Global Const SW_HIDE = 0
#Global Const SW_SHOWNORMAL = 1
#Global Const SW_SHOWMINIMIZED = 2
#Global Const SW_SHOWMAXIMIZED = 3

WINDOW_STATES = {"hide":0, "normal":1, "minimized":2,"maximized":3,\
                    "hidden":0,"minimize":2,"maximize":3}
PROCESS_PRIORITIES =[ 0x40,0x00004000,0x00000020,0x00008000,0x00000080,0x00000100]


def Popen(*args, show='normal', priority=2, **kwargs):
  if isinstance ( show, str ) :
    show = WINDOW_STATES[show]
  if show!=1:
    startupinfo = kwargs.get('startupinfo', STARTUPINFO() ) 
    startupinfo.dwFlags |= 1 #subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = show
    kwargs['startupinfo'] = startupinfo
  kwargs['creationflags'] = kwargs.get('creationflags', 0 ) | PROCESS_PRIORITIES[priority]
  return Popen_original(*args, **kwargs)

  
  
