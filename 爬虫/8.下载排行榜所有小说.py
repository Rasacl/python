import parsel
import requests
import re
import os
# 导入线程池
import concurrent.futures


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


def main(home_url):
    noval_url_list = get_novel_list(home_url)
    for novalUrl in noval_url_list:
        noval_urls = f'https://www.bqgka.com{novalUrl}'
        name, url_list = get_list_url(noval_urls)
        print(name, url_list)
        for url in url_list:
            index_url = 'https://www.bqgka.com' + url
            # 请求章节内容
            title, content = get_content(index_url)
            save(name, title, content)


if __name__ == '__main__':
    noval_url = 'https://www.bqgka.com/top/'
    main(noval_url)
