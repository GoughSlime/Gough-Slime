import gzip
import json
import tkinter as tk
import urllib.request
from tkinter import *
from tkinter import messagebox


root = Tk()


def main():
    # 输入窗口
    root.title('')  # 窗口标题
    tk.Label(root, bg='pink', text=" 请输入您要查询的地区:", font=('微软雅黑', 12), height=1).grid(row=0,
                                                                                     column=0)  # 设置标签并调整位置
    enter = Entry(root)  # 输入框
    enter.grid(row=1, column=0, padx=0, pady=0)  # 调整位置
    enter.delete(0, END)  # 清空输入框
    enter.insert(0, '中原区')  # 设置默认文本
    # enter_text = enter.get()#获取输入框的内容

    running = 1
    h = root.winfo_screenwidth()  # 获得屏幕宽度
    l = root.winfo_screenheight()  # 获得屏幕高度

    tw = 175  # 窗口宽
    th = 88  # 窗口高
    tx = (h - tw) / 2
    ty = (l - th) / 2
    root.geometry("%dx%d+%d+%d" % (tw, th, tx, ty))
    root.resizable(width=False, height=False)

    def get_weather_data():  # 获取网站数据
        city_name = enter.get()  # 获取输入框的内容
        url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(city_name)
        # print(url1)
        weather_data = urllib.request.urlopen(url1).read()
        # 读取网页数据
        weather_data = gzip.decompress(weather_data).decode('utf-8')
        # 解压网页数据
        weather_dict = json.loads(weather_data)
        # 将json数据转换为dict数据
        if weather_dict.get('desc') == 'invilad-citykey':
            print(messagebox.askokcancel("xing", "你输入的城市名有误，或者天气中心未收录你所在城市"))
        else:
            # print(messagebox.askokcancel('xing','bingguo'))
            show_data(weather_dict, city_name)

    def show_data(weather_dict, city_name):  # 显示数据
        forecast = weather_dict.get('data').get('forecast')  # 获取数据块
        root1 = Tk()  # 副窗口
        root1.geometry('875x280')  # 修改窗口大小
        root1.geometry("-0+0")
        root1.title(city_name + '天气状况')  # 副窗口标题
        root1.resizable(width=False, height=False)
        # 设置日期列表
        for i in range(5):  # 将每一天的数据放入列表中
            l = {(forecast[i].get('date'), '日期'),
                 (forecast[i].get('fengxiang'), '风向'),
                 (str(forecast[i].get('fengli')), '风级'),
                 (forecast[i].get('high'), '最高温'),
                 (forecast[i].get('low'), '最低温'),
                 (forecast[i].get('type'), '天气')}
            group = LabelFrame(root1, text='天气状况', padx=0, pady=0)  # 框架
            group.pack(padx=11, pady=0, side=LEFT)  # 放置框架
            for lang, value in l:  # 将数据放入框架中
                c = Label(group, fg='maroon', bg='silver', text=value + ': ' + lang)
                c.pack(anchor=W)
        Label(root1, text='今日' + weather_dict.get('data').get('ganmao'),
              fg='red', bg='silver').place(x=40, y=20, height=40)  # 温馨提示
        Button(root1, text='确认并退出', font=('微软雅黑', 12), width=10, bd=4, fg='red', bg='DarkTurquoise',
               activebackground='red',
               command=root1.destroy).place(x=500, y=230)  # 退出按钮
        root1.mainloop()

    # 布置按键
    Button(root, text="确认", bd=5, fg='blue', bg='DarkTurquoise', activebackground='green', font=('微软雅黑', 9),
           width=9,
           command=get_weather_data) \
        .grid(row=2, sticky=W)
    Button(root, text='退出', bd=5, fg='red', bg='PaleVioletRed', activebackground='red', font=('微软雅黑', 9),
           width=9,
           command=root.destroy) \
        .grid(row=2, sticky=E)
    if running == 1:
        root.mainloop()


if __name__ == '__main__':
    main()

