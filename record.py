# todo caught C-c signal

import gtk.gdk
import time, os

def screenshot(filename):
    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
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
    time.sleep(1)

