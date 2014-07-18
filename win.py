#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, os, signal, sys
import hashlib

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



import time
import os, win32gui, win32ui, win32con, win32api  
    
def window_capture(dpath):
    
    # 截屏函数,调用方法window_capture('d:\\') ,参数为指定保存的目录 
    # 返回图片文件名,文件名格式:日期.jpg 如:2009328224853.jpg 
    
    hwnd = 0 
    hwndDC = win32gui.GetWindowDC(hwnd)   
    mfcDC=win32ui.CreateDCFromHandle(hwndDC)   
    saveDC=mfcDC.CreateCompatibleDC()   
    saveBitMap = win32ui.CreateBitmap()   
    MoniterDev=win32api.EnumDisplayMonitors(None,None)  
    w = MoniterDev[0][2][2]  
    h = MoniterDev[0][2][3]  
    #print w,h　　　＃图片大小  
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)   
    saveDC.SelectObject(saveBitMap)   
    saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)  
    cc=time.gmtime()  
    bmpname=str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'.bmp'
    saveBitMap.SaveBitmapFile(saveDC, dpath+bmpname)
