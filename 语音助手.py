import tkinter as tk
import urllib.parse
import urllib.request
from tkinter import *
from tkinter import messagebox
import random
import winreg

y = 500
z = 500
win = tk.Tk()

w = win.winfo_screenwidth()  # 获得屏幕宽度
s = win.winfo_screenheight()  # 获得屏幕高度
win.title('文字转语音')
tkw = y  # 窗口宽
tkh = z  # 窗口高
tkx = (w - tkw) / 2
tky = (s - tkh) / 2
win.geometry("%dx%d+%d+%d" % (tkw, tkh, tkx, tky))
win.resizable(width=False, height=False)

t = Text(win, height=y // (69 // 3), width=z // (15 // 2), bg='PaleGoldenrod', font=('微软雅黑', 12))
t.pack()


def hit1():
    win.destroy()


num = random.randint(0, 9)


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders', )
    return winreg.QueryValueEx(key, "Desktop")[0]


Desktop = get_desktop()


def hit2():
    txt = t.get('1.0', END)
    text = txt
    api = 'http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&text='
    b = b'/:?='
    text = urllib.parse.quote(text, b)
    url = api + text
    dat = urllib.request.urlopen(url).read()

    g = random.randint(1, 9999999999)
    j = f"/音频{g}.mp3"
    with open(Desktop + j, 'wb') as f:
        f.write(dat)

    print(messagebox.showinfo("", j.lstrip('/') + '\n已保存到桌面!\n数字是为了防止混淆!\n您可以重新命名!'))


a = 40
Button(win, text="退出", width=9, activebackground='pink', bg='OldLace', font=('微软雅黑', 10),
       command=hit1).place(x=a, y=460)
Button(win, text="确定", width=9, activebackground='LightCyan', bg='OldLace', font=('微软雅黑', 10),
       command=hit2).place(x=a + 345, y=460)
win.mainloop()
