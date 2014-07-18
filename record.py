#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time, os, signal, sys

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

