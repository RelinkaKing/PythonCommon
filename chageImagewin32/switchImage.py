#coding:utf-8

import Image
import win32api,win32gui,win32con
import time

def setscreenpic(pic):
    # open register
    regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel/Desktop",0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
    win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)

g_times = 0
while True:
 g_times = g_times+1
 g_times = g_times%5
 picDir = 'D:/backgroud/'
 picDir = picDir+str(g_times+1)+'.jpg'
 setscreenpic(picDir)
 time.sleep(60*60)