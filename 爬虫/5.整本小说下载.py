import requests
import re
import os

# 请求链接 小说目录页
list_url = 'https://www.bqgka.com/book/3315/'
# 模拟浏览器 headers 请求头
headers = {
    # User-Agent 用户代理，浏览器基本的用户信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
# 发送请求
html_data = requests.get(list_url, headers=headers).text
# 提取章节url
url_list = re.findall('<dd><a href ="(.*?)">', html_data)
# 提取小说名字
name = re.findall('<span class="title">(.*?)</span>', html_data)[0]
# 自动创建一个文件夹
file = f'{name}\\'
if not os.path.exists(file):
    os.mkdir(file)  # makedirs 函数可以创建多个目录
# for循环爬取
for url in url_list:
    # 请求章节内容
    index_url = 'https://www.bqgka.com' + url
    # 发送请求
    response = requests.get(url=index_url, headers=headers)
    # 提取标题
    title = re.findall('<h1 class="wap_none">(.*?)</h1>', response.text)[0]
    # 提取内容 re.S 多行匹配模式
    content = \
    re.findall('<div id="chaptercontent" class="Readarea ReadAjax_content">(.*?)<p class="readinline">', response.text,
               re.S)[0].replace('<br /><br />', '\n')
    # 保存内容 file + name 保存所有内容在一起 file + title 分段落保存
    with open(file + name + '.text', mode='a', encoding='utf-8') as f:
        f.write(title + '\n' + content + '\n')
