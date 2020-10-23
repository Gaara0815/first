import os
import win32gui  # pywin32-221.win-amd64-py3.7.exe
import win32con
from ctypes import *
import win32clipboard as w
import time
from PIL import Image  # pip install pillow


# pip install -i https://pypi.douban.com/simple pillow
# import win32api

# 发送文字
def setText(info):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, info)
    w.CloseClipboard()


# 发送图片
def setImage(imgpath):
    im = Image.open(imgpath)
    im.save('1.bmp')
    aString = windll.user32.LoadImageW(0, r"1.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)

    if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_BITMAP, aString)
        w.CloseClipboard()
# 发送图片
def setImage2(imgpath):
    im = Image.open(imgpath)
    im.save('2.bmp')
    aString = windll.user32.LoadImageW(0, r"2.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)

    if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_BITMAP, aString)
        w.CloseClipboard()

# 定位QQ窗口，进行昵称备注的搜索，再回车弹出此好友窗口
def searchByUser(uname):
    hwnd = win32gui.FindWindow('TXGuiFoundation', 'QQ')
    # hwnd = win32gui.FindWindow('ChatWnd', uname)
    setText(uname)
    win32gui.SendMessage(hwnd, 258, 22, 2080193)
    win32gui.SendMessage(hwnd, 770, 0, 0)
    time.sleep(0.5)
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 定位好友窗口，昵称备注
def sendByUser(uname):
    hwnd = win32gui.FindWindow('TXGuiFoundation', uname)
    # hwnd = win32gui.FindWindow('ChatWnd', uname)
    win32gui.SendMessage(hwnd, 258, 22, 2080193)
    win32gui.SendMessage(hwnd, 770, 0, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 发送完信息之后关闭窗口（新的窗口的标题将不是昵称）
def closeByUser(uname):
    hwnd = win32gui.FindWindow('TXGuiFoundation', uname)
    win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)



# searchByUser('3417781932')
# setText('~~~给GANGAN神说个事情~~~')
# sendByUser('3417781932')
# setText('~~~给GANGAN神说个事情~~~')
# time.sleep(3)




# 获取无后缀的图片名称
def getNosuffixImgName(imgname):
    return os.path.splitext(imgname)[0]

# directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# File_Path = os.getcwd() + '\\' + directory_time + '\\'
# imgdir = File_Path
# print(imgdir)
# imgs = os.listdir(imgdir)
# for img in imgs:
#     print(img)
#     sendByUser('3417781932')
#     setImage(imgdir + img)
#     time.sleep(1)
