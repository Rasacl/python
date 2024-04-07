# python 实现百度文库爬取，保存到word文档
import requests

url = 'https://wenku.baidu.com/gsearch/rec/pcviewdocrec2023'

# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

data = {
"sessionId": "1922214026-1953198754--",
"docId": "7b5a9d000366f5335a8102d276a20029bd6463e0",
"query": "跟植物有关的现代诗（精选88首）",
"recPositions": "catalog,toplist"
}

response = requests.get(url=url, headers=headers, params=data)
num = 0
for index in response.json()['data']["catalogDoc"]:
    pic = index['pic']
    # 保存图片
    img_content = requests.get(url=pic, headers=headers).content
    with open('imgs\\' + str(num) + '.jpg', mode='wb') as f:
        f.write(img_content)
    num += 1