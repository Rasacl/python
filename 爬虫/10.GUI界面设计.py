import tkinter as tk
from tkinter import ttk

import parsel
import requests
import re
import os
# 导入线程池
import concurrent.futures

# 导入表格模块
import prettytable as pt


def get_response(html_rul):
    '''
    发送请求并获取响应
    :param html_rul:
    :return: response 响应对象
    '''

    # 模拟浏览器 headers 请求头
    headers = {
        # User-Agent 用户代理，浏览器基本的用户信息
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
    # 发送请求
    response = requests.get(html_rul, headers=headers)

    return response


def get_list_url(html_url):
    """
    获取章节url/小说名
    :param html_url: 小说目录页url
    :return:
    """
    # 调用发送请求函数
    html_data = get_response(html_url).text
    # 提取章节url
    url_list = re.findall('<dd><a href ="(.*?)">', html_data)
    # 提取小说名字
    name = re.findall('<span class="title">(.*?)</span>', html_data)[0]

    return name, url_list


def get_content(html_url):
    """
    获取小说内容、小说标题
    :param html_url:
    :return:
    """
    # 调用发送请求函数
    html_data = get_response(html_url).text
    # 提取标题
    title = re.findall('<h1 class="wap_none">(.*?)</h1>', html_data)[0]
    # 提取内容 re.S 多行匹配模式
    content = re.findall('<div id="chaptercontent" class="Readarea ReadAjax_content">(.*?)<p class="readinline">',
                         html_data,
                         re.S)[0].replace('<br /><br />', '\n')

    return title, content


def save(name, title, content):
    """
    保存内容
    :param name: 小说名
    :param title: 章节名
    :param content: 内容
    :return:
    """
    # 自动创建一个文件夹
    file = f'{name}\\'
    if not os.path.exists(file):
        os.mkdir(file)
    # 保存内容 file + name 保存所有内容在一起 file + title 分段落保存
    with open(file + title + '.text', mode='a', encoding='utf-8') as f:
        f.write(title + '\n' + content + '\n')


def get_novel_list(html_url):
    """
    获取小说排行榜所有小说id
    :param html_url:
    :return:
    """
    noval_data = get_response(html_url).text
    selectors = parsel.Selector(noval_data)
    noval_url_list = selectors.css('.blocks ul li a::attr(href)').getall()
    return noval_url_list


def main(noval_id):
    noval_urls = f'https://www.bqgbb.cc{noval_id}'
    name, url_list = get_list_url(noval_urls)
    print(name, url_list)
    for url in url_list:
        index_url = 'https://www.bqgbb.cc/' + url
        # 请求章节内容
        title, content = get_content(index_url)
        save(name, title, content)


def search(word):
    """
    搜索功能
    :param word: 书名或者作者名
    :return:
    """
    search_url = f'https://www.bqgka.com/s?q={word}'
    search_data = get_response(search_url).text
    # 解析数据 提取小说名字、作者、小说ID
    selector = parsel.Selector(search_data)
    # lis = selector.css('.novelslist li')
    noval_info = [
        {
            'num':1,
            'name': '逆天邪神',
            'noval_id': '/book/3031/',
            'writer': "火星引力"
        },
        {
            'num': 2,
            'name': '逆天邪神云澈',
            'noval_id': '/book/12566/',
            'writer': "火星引力"
        },
        {
            'num': 3,
            'name': '逆天邪神叶凡',
            'noval_id': '/book/7364/',
            'writer': "无敌贱客"
        },
        {
            'num': 4,
            'name': '逆天邪神萧澈夏倾月',
            'noval_id': '/book/21113/',
            'writer': "火星引力"
        },
        {
            'num': 5,
            'name': '逆天邪神同人带系统穿越',
            'noval_id': '/book/98399/',
            'writer': "七月雪仙人"
        }
    ]
    tb = pt.PrettyTable()
    tb.field_names = ['序号', '书名', '作者', '书ID']
    num = 0
    for item in noval_info:
        tb.add_row([num, item['name'], item['writer'], item['noval_id']])
        num += 1
    # for li in lis:  # 实现逻辑，现在用假数据
    #     name = li.css('h2::text').get()
    #     noval_id = li.css('h2 a::attr(href)').get()
    #     writer = li.css('h2 a::text').get()
    #     dit = {
    #         'name': name,
    #         'noval_id': noval_id,
    #         'writer': writer
    #     }
    #     noval_info.append(dit)
    # print('您搜索的结果如下：')
    # print(tb)
    return noval_info
    # noval_num = input('请输入你想下载的小说序号：')
    # noval_id = noval_info[int(noval_num)]['noval_id']
    # return noval_id


def show():
    word = name_va.get()
    noval_info = search(word)
    print(noval_info)
    # 往树状图中插入数据
    for index,stu in enumerate(noval_info):
        print(index, stu)
        tree_view.insert('', index+ 1, values=(stu['num'], str(stu['writer']), str(stu['name']), str(stu['noval_id'])))


def download():
    word = name_va.get()
    noval_info = search(word)
    num = num_va.get()
    noval_id = noval_info[int(num)]['noval_id']
    main(noval_id)


if __name__ == '__main__':
    # 创建界面
    root = tk.Tk()
    # 设置标题
    root.title("小说下载器")
    # 设置界面大小
    root.geometry("500x500+200+200")
    # 设置标签
    search_frame = tk.Frame(root)
    search_frame.pack(pady=10)

    # 设置可变变量
    name_va = tk.StringVar()

    # 设置文本
    tk.Label(search_frame, text="书名 作者", font=('微软雅黑', 12)).pack(side=tk.LEFT, padx=10)
    # 设置输入框
    tk.Entry(search_frame, relief='flat', textvariable=name_va).pack(side=tk.LEFT)

    # 查询下载的输入框
    download_frame = tk.Frame(root)
    download_frame.pack(pady=10)
    # 序号获取
    num_va = tk.StringVar()
    # 设置文本
    tk.Label(download_frame, text="下载序号", font=('微软雅黑', 12)).pack(side=tk.LEFT, padx=10)
    # 设置输入框
    tk.Entry(download_frame, relief='flat', textvariable=num_va).pack(side=tk.LEFT)

    # 按钮设置
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # 设置查询按钮
    tk.Button(button_frame, text='查询', font=('微软雅黑', 10), relief='flat', bg='#88e2d6', width=10,
              command=show).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text='下载', font=('微软雅黑', 10), relief='flat', bg='#88e2d6', width=10,
              command=download).pack(side=tk.LEFT, padx=10)

    # 设置标签名字和中文显示内容
    columns = ('num', 'writer', 'name', 'noval_id')
    columns_values = ('序号', '作者', '书名', '书ID')

    tree_view = ttk.Treeview(root, height=49, show='headings', columns=columns)
    # 设置列名
    tree_view.column('num', width=40, anchor='center')
    tree_view.column('writer', width=40, anchor='center')
    tree_view.column('name', width=40, anchor='center')
    tree_view.column('noval_id', width=40, anchor='center')
    # 给列名设置显示的名字
    tree_view.heading('num', text='序号')
    tree_view.heading('writer', text='作者')
    tree_view.heading('name', text='书名')
    tree_view.heading('noval_id', text='书ID')
    tree_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    # 展示界面
    root.mainloop()
