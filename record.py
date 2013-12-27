#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk.gdk
import time, os, signal, sys

interval = 2

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

w = gtk.gdk.get_default_root_window()
sz = w.get_size()
def screenshot(filename):
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save(filename+".png","png")
        print "Screenshot saved to "+filename+".png."
    else:
        print "Unable to get the screenshot."

screenshots_root = 'screenshots'
if not os.path.exists(screenshots_root):
    os.mkdir(screenshots_root)
while True:
    screenshot(screenshots_root+'/'+str(time.time()))
    time.sleep(interval)

