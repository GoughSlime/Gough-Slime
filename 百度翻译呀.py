from urllib import request, parse
import json
import tkinter as tk
from tkinter import *

window = tk.Tk()
w = window.winfo_screenwidth()  # 获得屏幕宽度
s = window.winfo_screenheight()  # 获得屏幕高度
window.title('')

tkw = 600  # 窗口宽
tkh = 350  # 窗口高
tkx = (w - tkw) / 2
tky = (s - tkh) / 2
window.geometry("%dx%d+%d+%d" % (tkw, tkh, tkx, tky))

window.resizable(width=False, height=False)
var = tk.StringVar()
y = 500
z = 500
a = tk.Label(window, text='输入单词', bg='Silver', font=('微软雅黑', 12), width=60, height=1)
a.pack()
f = Entry(window, bd=1, bg='PaleGoldenrod', width=100, cursor='plus', relief='sunken')
f.pack()
b = tk.Label(window, text='翻译结果', bg='Silver', font=('微软雅黑', 12), width=60, height=1, )
b.pack()
x = Text(window, height=y // 50, width=z // (15 // 2), bg='PaleGoldenrod', font=('微软雅黑', 12))
x.pack()


def hit1():
    window.destroy()


def hit2():
    x.delete('1.0', '1.end')
    keyword = f.get()
    fanyi(keyword)
    x.delete('1.1', '1.21')


def fanyi(keyword):
    base_url = 'https://fanyi.baidu.com/sug'

    # 构建请求对象
    data = {
        'kw': keyword
    }
    data = parse.urlencode(data)

    # 模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
    req = request.Request(url=base_url, data=bytes(data, encoding='utf-8'), headers=headers)
    res = request.urlopen(req)

    # 获取json字符串
    str_json = res.read().decode('utf-8')
    # 把json转换成字典
    myjson = json.loads(str_json)
    x.insert(INSERT, myjson)


Button(window, text="退出", width=9, activebackground='pink', bg='OldLace', font=('微软雅黑', 10),
       command=hit1).place(x=40, y=300)
Button(window, text="确定", width=9, activebackground='LightCyan', bg='OldLace', font=('微软雅黑', 10),
       command=hit2).place(x=480, y=300)
window.mainloop()
