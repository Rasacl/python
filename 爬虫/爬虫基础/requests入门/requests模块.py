'''
encode 对字符串转换成二进制数据
decode 对二进制数据进行解码


'''

import requests

url = 'https://www.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
'''
response.status_code 响应的状态码
response.headers 响应头信息
response.request.headers 请求头信息
response.request.cookies 请求的cookie信息
response.cookies 响应的cookie信息
'''
# 方式一 response.text  获取到的是字符串
# print(response.text)
# 方式二 response.content 获取到的是原始的二进制数据（bytes类型）需要解码为字符串，decode()方法
print(response.content.decode())
# print(response.headers)
# print(response.request.headers)
