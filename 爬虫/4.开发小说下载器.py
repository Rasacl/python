# 采集网站 https://www.bqgka.com/book/3315/1.html
# 采集内容 标题/内容

# 代码实现 1.发送请求 2.解析HTML内容 3.提取信息 4.保存到文件

# 导入数据请求模块
import requests
# 导入正则表达式模块
import re
# 导入数据解析模块
import parsel
# 确定请求链接
url = 'https://www.bqgka.com/book/3315/1.html'
headers = {
    # User-Agent 用户代理，浏览器基本的用户信息
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}
# 发送请求
response = requests.get(url=url, headers=headers)
# <Response [200]> 响应对象， 表示请求成功
# response.text 返回页面的HTML内容

# 解析数据
# re正则表达式 提取标题和内容： 直接对于字符串数据进行解析 re.findall() 匹配所有结果
# css选择器 BeautifulSoup： 根据标签属性提取数据
# xpath节点提取： 提取标签节点，然后提取数据

# 正则提取
# 提取标题
# titles = re.findall('<h1 class="wap_none">(.*?)</h1>', response.text)[0]
# # 提取内容 re.S 多行匹配模式
# contents = re.findall('<div id="chaptercontent" class="Readarea ReadAjax_content">(.*?)<p class="readinline">', response.text, re.S)[0].replace('<br /><br />','\n')
# print(titles)
# print(contents)
# print(response.text)



# css选择器提取
# 获取下来的response.text<HTML字符串数据> 转成可解析的对象
# get 提取第一个标签内容 返回字符串
# getall 提取所有标签内容 返回列表
# selector = parsel.Selector(response.text)
# # 提取标题
# title = selector.css('.reader h1::text').get()
#
# # 提取内容
# content = '\n'.join(selector.css('#chaptercontent::text').getall())
# print(content)

# xpath节点提取
selector = parsel.Selector(response.text)
# 提取标题
title = selector.xpath('//*[@class="wap_none"]/text()').get()

# 提取内容
content = '\n'.join(selector.xpath('//*[@id="chaptercontent"]/text()').getall())


# 保存内容
  # title <> 文件名 '.text' 文件名  'a' 追加模式  'w' 写入模式 'r' 读取模式 'rb' 二进制读取模式 'wb' 二进制写入模式
  # 'ab' 二进制追加模式 'r+b' 二进制读写模式 'w+' 读写模式 'a+' 追加读写模式  'wb+' 二进制读写模式 'ab+' 二进制追加读写模式 enconding='utf-8' 指定编码 as 重命名
with open(title + '.text', mode='a',encoding='utf-8') as f:
  f.write(title + '\n' + content + '\n')