# -*- coding: utf-8 -*-
# 导入模块
import json
import time
import tkinter as tk
import urllib.parse
import urllib.request
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import pyperclip

# 创建tk窗口
window = tk.Tk()
w = window.winfo_screenwidth()  # 获得屏幕宽度
s = window.winfo_screenheight()  # 获得屏幕高度
tkx = (w - 600) / 2
tky = (s - 450) / 2
window.geometry("%dx%d+%d+%d" % (600, 430, tkx, tky))
window.resizable(width=False, height=False)

localtime = ('The Startup Time  ' +
             time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 窗口标题
window.title(localtime)
# ----------------------------------------------------------------------------------#
style = ttk.Style()
style.configure("BW.TLabel", foreground="gray", font=('微软雅黑', 12))  # style

a = ttk.Label(window, text='The Input', style="BW.TLabel")  # 第一行
a.grid(column=1, row=1, columnspan=4)

b = ttk.Label(window, text='The Result / 0 Time', style="BW.TLabel")  # 第二行
b.grid(column=1, row=3, columnspan=4)
# ----------------------------------------------------------------------------------#
W = 56
H = 7

f = scrolledtext.ScrolledText(window, width=W, height=H)  # 输入框1
f.configure(foreground='teal', font=('微软雅黑', 13))
f.grid(column=1, row=2, columnspan=4, padx=18)

x = scrolledtext.ScrolledText(window, width=W, height=H)  # 输入框2
x.configure(foreground='teal', font=('微软雅黑', 13))
x.grid(column=1, row=4, columnspan=4, padx=18)

x.bind('<KeyPress>', lambda e: 'break')  # 禁用输入
# ---------------------------------------------------------------------------------#
counter = 0


def hit1():
    """
关闭窗口
按钮的命令
    """
    window.destroy()
    sys.exit(0)


def hit2():
    """
清空
    """
    x.delete('1.0', END)
    f.delete('1.0', END)


def hit3():
    """
复制
    """

    if x.get('2.0', END).strip() == '':
        x.delete('1.0', END)
        x.insert('1.27', 'Nothing To Copy ▶')
        x.tag_add("tag2", '1.0', '1.26')
        x.tag_config("tag2", foreground="grey", underline=True)

    else:
        x.delete('1.0', '1.27')
        pyperclip.copy(x.get('2.0', END).strip())
        x.insert('1.27', 'Copy Successful ▶')
        x.tag_add("tag2", '1.0', '1.26')
        x.tag_config("tag2", foreground="grey", underline=True)


def hit5():
    """
历史记录
    """
    fy1 = open('历史记录.GSJ', 'r+', encoding='gbk')  # 设置文件对象
    fy2 = fy1.read()
    window2 = tk.Tk()
    w2 = window2.winfo_screenwidth()  # 获得屏幕宽度
    s2 = window2.winfo_screenheight()  # 获得屏幕高度
    tkx2 = (w2 - 600) / 2
    tky2 = (s2 - 460) / 2
    window2.geometry("%dx%d+%d+%d" % (600, 460, tkx2, tky2))
    window2.resizable(width=False, height=False)

    localtime2 = ('The Startup Time  ' +
                  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 窗口标题
    window2.title(localtime2)

    x2 = scrolledtext.ScrolledText(window2, width=56, height=17)  # 输入框2
    x2.configure(foreground='teal', font=('微软雅黑', 13))
    x2.grid(column=1, row=1, columnspan=2, padx=18)

    x2.bind('<KeyPress>', lambda e: 'break')  # 禁用输入
    x2.insert('1.0', fy2)
    ttk.Button(window2, text="Exit", command=window2.destroy).grid(column=1, row=2, sticky='W', padx=20, pady=20)

    def hitt1():
        x2.delete('1.0', END)
        with open('历史记录.GSJ', 'w') as fy9:
            fy9.close()

    ttk.Button(window2, text="Empty", command=hitt1).grid(column=2, row=2, sticky='E', padx=30, pady=20)


def get_data(words):
    """

    :param words:
    :return:
    """
    data = {"type": "AUTO", "i": words, "doctype": "json", "xmlVersion": "1.8", "keyfrom:fanyi": "web", "ue": "UTF-8",
            "action": "FY_BY_CLICKBUTTON", "typoResult": "true"}

    data = urllib.parse.urlencode(data).encode('utf-8')
    time.sleep(0.1)
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
    time.sleep(0.1)
    return html


def get_json_data(html):
    """

    :param html:
    :return:
    """
    result = json.loads(html)
    result = result['translateResult']
    result = result[0][0]['tgt']
    time.sleep(0.1)
    return result


def main():
    """
计数
    """
    if f.get('1.0', END).strip() != '':
        global counter
        counter += 1
        if counter == 1:
            b.config(text='The Result / ' + str(counter) + ' Time')
        elif counter != 1:
            b.config(text='The Result / ' + str(counter) + ' Times')
    """
############################################主程序##################################################
    """

    data = f.get('1.0', END)
    with open('写入翻译.GSJ', 'w') as fy:  # 设置文件对象
        fy.writelines(data)
    lines = open('写入翻译.GSJ').readlines()  # 打开文件，读入每一答行
    fp = open('翻译转换.GSJ', 'w')  # 打开你要写得文件pp2.txt
    for sfy in lines:
        fp.write(sfy
                 .replace('。', '，')
                 .replace('。', '，')
                 .replace('.', '，')
                 .replace('．', '，')
                 .replace(';', '｝')
                 .replace('；', '｝')
                 .replace('？', '｝')
                 .replace('?', '｝')
                 .replace('!', '｝')
                 .replace('！', '｝')
                 )  # replace是替换，write是写入

    fp.close()  # 关闭文件
    fy = open('翻译转换.GSJ', encoding='gbk')  # 设置文件对象
    fy2 = fy.read()
    x.delete('1.0', END)

    if f.get('1.0', END).strip() != '':  # 判断是否是空的
        localtime2 = time.asctime(time.localtime(time.time()))
        words = fy2
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top"
        data = get_data(words)
        html = url_open(url, data)
        result = get_json_data(html)
        x.insert(INSERT, localtime2 + " ▶" + '\n' + result)
        x.tag_add("tag2", '1.0', '1.26')
        x.tag_config("tag2", foreground="grey", underline=True)
        time.sleep(0.1)
    else:
        localtime2 = time.asctime(time.localtime(time.time()))
        x.insert(INSERT, localtime2 + " ▶" + '\n')
        x.tag_add("tag2", '1.0', '1.26')
        x.tag_config("tag2", foreground="grey", underline=True)
    mian34()


def mian34():
    data = f.get('1.0', END)
    data1 = x.get('2.0', END)
    with open('历史记录.GSJ', 'a') as lsjl:  # 设置文件对象
        localtime3 = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        if x.get('2.0', END).strip() != '':
            lsjl.write(localtime3 + ' :  ' + data)
            lsjl.write(localtime3 + ' :  ' + data1)


# ##############################################################################################

def hit11():
    """
主题１
    """
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="orange", font=('楷体', 12))  # style
    f.configure(foreground='teal', font=('楷体', 14))
    x.configure(foreground='teal', font=('楷体', 14))


def hit12():
    """
主题２
    """
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="purple", font=('宋体', 12))  # style
    f.configure(foreground='teal', font=('宋体', 14))
    x.configure(foreground='teal', font=('宋体', 14))


def hit13():
    """
主题３
    """
    style = ttk.Style()
    style.configure("BW.TLabel", foreground="gray", font=('微软雅黑', 12))  # style
    f.configure(foreground='teal', font=('微软雅黑', 13))
    x.configure(foreground='teal', font=('微软雅黑', 13))


menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="历史记录", command=hit5)
fileMenu.add_separator()
fileMenu.add_command(label="退出", command=hit1)
menuBar.add_cascade(label="File", menu=fileMenu)
editmenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='主题1', command=hit11)
editmenu.add_command(label='主题2', command=hit12)
editmenu.add_command(label='默认主题', command=hit13)

ttk.Button(window, text="Exit", command=hit1).grid(column=1, row=5, sticky='W', padx=20, pady=12)

ttk.Button(window, text="Empty", command=hit2).grid(column=2, row=5, sticky='W', padx=20, pady=12)

ttk.Button(window, text="Copy", command=hit3).grid(column=3, row=5, sticky='W', padx=20, pady=12)

ttk.Button(window, text="Translate", command=main).grid(column=4, row=5, sticky='W', padx=20, pady=12)

if __name__ == "__main__":
    while True:
        window.mainloop()
