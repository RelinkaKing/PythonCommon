from PIL import Image
import win32api, win32gui, win32con
import time 

def setWallPaper(pic):
 # open register
 regKey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)
 win32api.RegSetValueEx(regKey,"WallpaperStyle", 0, win32con.REG_SZ, "2")
 win32api.RegSetValueEx(regKey, "TileWallpaper", 0, win32con.REG_SZ, "0")
 # refresh screen
 win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,pic, win32con.SPIF_SENDWININICHANGE)
 
# setWallPaper('E:\\backPics\\character5.jpg')
g_times = 0
while True:
 g_times = g_times+1
 g_times = g_times%5
 picDir = './pic'
 picDir = picDir+str(g_times+1)+'.jpg'
 setWallPaper(picDir)
 time.sleep(1*10)