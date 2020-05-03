# coding: utf-8
# 导入模块
import urllib.request
import urllib.parse
import json
import tkinter
import tkinter as tk
from tkinter import *
import pyperclip
from tkinter import messagebox
import time

# 创建tk窗口
window = tk.Tk()
w = window.winfo_screenwidth()  # 获得屏幕宽度
s = window.winfo_screenheight()  # 获得屏幕高度
window.title('')
tkw = 600  # 窗口宽
tkh = 550  # 窗口高
tkx = (w - tkw) / 2
tky = (s - tkh) / 2
window.geometry("%dx%d+%d+%d" % (tkw, tkh, tkx, tky))
window.resizable(width=False, height=False)
var = tk.StringVar()
a = tk.Label(window, text='输入内容', bg='Silver', font=('微软雅黑', 12), width=60, height=1)
a.pack()
f = Text(window, height=10, width=71, bg='PaleGoldenrod', font=('微软雅黑', 12))
f.pack()
b = tk.Label(window, text='翻译结果', bg='Silver', font=('微软雅黑', 12), width=60, height=1, )
b.pack()
x = Text(window, height=10, width=71, bg='PaleGoldenrod', font=('微软雅黑', 12))
x.pack()


def hit1():
    """
关闭窗口
按钮的命令
    """
    window.destroy()


def hit2():
    """
清空
    """
    f.delete('1.0', END)


def hit3():
    """
复制
    """
    pyperclip.copy(x.get('1.0', END))
    print(messagebox.showwarning("", '复制成功...\nCtrl+V粘贴'))


def get_data(words):
    """

    :param words:
    :return:
    """
    data = {"type": "AUTO", "i": words, "doctype": "json", "xmlVersion": "1.8", "keyfrom:fanyi": "web", "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON", "typoResult": "true"}
    data = urllib.parse.urlencode(data).encode('utf-8')
    return data


def url_open(url, data):
    """

    :param url:
    :param data:
    :return:
    """
    req = urllib.request.Request(url, data)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 "
                   "Safari/537.36")  # 伪装
    response = urllib.request.urlopen(req)
    html = response.read()
    html = html.decode("utf-8")
    return html


def get_json_data(html):
    """

    :param html:
    :return:
    """
    result = json.loads(html)
    result = result['translateResult']
    result = result[0][0]['tgt']
    return result


def main():
    """
主程序
    """
    x.delete('1.0', END)
    if f.get('1.0', END) != '' and f.get('1.0', END) != ' ':  # 判断是否是空的
        words = f.get('1.0', END)
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"
        data = get_data(words)
        html = url_open(url, data)
        result = get_json_data(html)
        x.insert(INSERT, result)
        time.sleep(1)


Button(window, bd=1, text="退出", width=9, activebackground='pink', bg='OldLace', font=('微软雅黑', 10),
       command=hit1).place(x=40, y=500)

Button(window, bd=1, text="清空", width=9, activebackground='pink', bg='OldLace', font=('微软雅黑', 10),
       command=hit2).place(x=190, y=500)

Button(window, bd=1, text="复制", width=9, activebackground='pink', bg='OldLace', font=('微软雅黑', 10),
       command=hit3).place(x=340, y=500)

Button(window, bd=1, text="确定", width=9, activebackground='LightCyan', bg='OldLace', font=('微软雅黑', 10),
       command=main).place(x=480, y=500)

if __name__ == "__main__":
    while True:
        window.mainloop()
