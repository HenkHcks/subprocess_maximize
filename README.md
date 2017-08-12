## subprocess_maximize


This library supplies a Popen implementation that supports process-priority and window-state properties for Windows.
On other operating systems it works like Popen.


Two parameters are added to Popen, `show` for the window-state, and `priority` for the process-priority.
`priority` can have any integer value from `0`(idle) to `5`(realtime), `2` being the default indicating normal priorty.
`show` can either be a value from `0` to `3`, or any of the following keywords: `hide`, `hidden`, `minimize`, `minimized`, `normal`, `maximize`, `maximized`


Any improvements are welcome.




# Usage
 ```
 from subprocess_maximize import Popen
 
 Popen('notepad.exe',show='maximize', priority=0)
 ```
 
 Notes:
 * Currently untested with Python 2.x
 
 
# Install 

 ```
 conda install subprocess_maximize
 ```
 
 or 
 
 ```
 pip install subprocess_maximize
 ```
