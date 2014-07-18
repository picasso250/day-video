#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time, os, signal, sys

t = time.time()

def handler(signum, frame):
    dt = time.time() - t;
    if dt < 60:
        dt = str(int(dt))+' seconds'
    else:
        dt = int(dt)
        dt = str(int(dt/60))+' min '+ str(dt%60)+' sec'
    print
    print 'Record '+dt
    sys.exit()

signal.signal(signal.SIGINT, handler)

print (os.name)
if os.name == 'nt':
    import win
    def screenshot(path):
        win.window_capture(path)
else:
    import linux
    def screenshot(path):
        linux.screenshot(path)

interval = 2

screenshots_root = 'screenshots'
if not os.path.exists(screenshots_root):
    os.mkdir(screenshots_root)
while True:
    screenshot(screenshots_root+'/'+str(time.time()))
    time.sleep(interval)

