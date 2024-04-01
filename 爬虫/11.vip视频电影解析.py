import tkinter as tk

import requests
import re
import webbrowser
# 创建一个窗口
root = tk.Tk()
# 设置窗口大小
root.geometry("800x300+200+200")
# 设置窗口标题
root.title("在线观看电影软件")


def show():
    num = num_int_var.get()
    url = url_str_var.get()
    if num == 1:
        link = 'https://jiexi.pengdouw.com/jiexi1/?url=' + url
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)
        print(html_data)
    elif num == 2:
        link = 'https://jiexi.pengdouw.com/jiexi2/?url=' + url
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)
        print(html_data)
    elif num == 3:
        link = 'https://jiexi.pengdouw.com/jiexi3/?url=' + url
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)
        print(html_data)

# 设置读取一张图片
img = tk.PhotoImage(file='img\\xx.png')
# 布局图片
tk.Label(root, image=img, height=150).pack()
# 设置标签框
choose_frame = tk.LabelFrame(root)
choose_frame.pack(pady=10, fill='both')

tk.Label(choose_frame, text='选择接口:', font=('黑体', 20)).pack(side=tk.LEFT)
# 设置可变变量
num_int_var = tk.IntVar()
# 设置默认值
num_int_var.set(1)
# 设置选择
tk.Radiobutton(choose_frame, text="①号通用vip引擎系统【稳定通用】", variable=num_int_var, value=1).pack(side=tk.LEFT,
                                                                                                      padx=5)
tk.Radiobutton(choose_frame, text="②号通用vip引擎系统【稳定通用】", variable=num_int_var, value=2).pack(side=tk.LEFT,
                                                                                                      padx=5)
tk.Radiobutton(choose_frame, text="③号通用vip引擎系统【稳定通用】", variable=num_int_var, value=3).pack(side=tk.LEFT,
                                                                                                      padx=5)

# 输入标签框
input_frame = tk.LabelFrame(root)
input_frame.pack(pady=10, fill='both')
# 设置可变变量
url_str_var = tk.StringVar()
tk.Label(input_frame, text='播放地址:', font=('黑体', 20)).pack(side=tk.LEFT)
tk.Entry(input_frame, width=100, relief='flat', textvariable=url_str_var).pack(side=tk.LEFT, fill='both')

# 设置点击解析的按钮
tk.Button(root, text='Go点击解析在线播放', relief='flat', bg='#ff9090', font=('黑体', 15), command=show).pack(fill='both')
# 让窗口持续展现
root.mainloop()
