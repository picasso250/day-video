#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk.gdk
import time, os, signal, sys
import hashlib

w = gtk.gdk.get_default_root_window()
sz = w.get_size()
old_digest = None
def screenshot(filename): # 截屏
    global old_digest
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    if (pb != None):
        pb.save(filename+".png","png")
        print "Screenshot saved to "+filename+".png."

        m = hashlib.md5()
        f = open(filename+'.png', 'r')
        m.update(f.read())
        digest = m.digest()
        f.close()

        if digest == old_digest:
            print 'the same with old, skip'
            os.unlink(filename+'.png')
        old_digest = digest

    else:
        print "Unable to get the screenshot."

