# coding=utf-8
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import socket
from threading import Thread
import os

def get_msg():
    while True:
        try:
            msg = s.recv(1024).decode('utf8')
            f.insert(END, msg)
        except:
            break


def send():
    send_msg = x.get('0.0', END).strip()
    s.send(bytes(send_msg+'', 'utf8'))
    x.delete('0.0', END)


window = Tk()
window.title('聊天室')


def hit1():
    """
关闭窗口
按钮的命令
    """
    window.destroy()
    os._exit(0)

import tkinter as tk
from tkinter import messagebox

def my_close():
    # True or Flase
    res = messagebox.askokcancel('提示', '是否关闭窗口')
    if res == True:

        window.destroy()
        os._exit(0)

# 为右上角的关闭事件添加一个响应函数
window.protocol('WM_DELETE_WINDOW', my_close)

f = scrolledtext.ScrolledText(window, width=56, height=14)  # 输入框1
f.configure(foreground='teal', font=('微软雅黑', 13))
f.grid(column=1, row=2, columnspan=4, padx=18)

a = ttk.Label(window, text='', style="BW.TLabel")  # 第一行
a.grid(column=1, row=1, columnspan=4)

b = ttk.Label(window, text='', style="BW.TLabel")  # 第二行
b.grid(column=1, row=3, columnspan=4)

x = scrolledtext.ScrolledText(window, width=56, height=3)  # 输入框2
x.configure(foreground='teal', font=('微软雅黑', 13))
x.grid(column=1, row=4, columnspan=4, padx=18)

ttk.Button(window, text="Exit", command=hit1).grid(column=1, row=5, sticky='W', padx=20, pady=12, columnspan=2)
ttk.Button(window, text="Sure", command=send).grid(column=4, row=5, sticky='W', padx=20, pady=12, columnspan=2)

# sockect 接入
Host = '127.0.0.1'
Port = 8848

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

receive_thread = Thread(target=get_msg)
receive_thread.start()
window.mainloop()
