# 腾讯招聘数据抓取
"""
https://careers.tencent.com/tencentcareer/api/post/Query
timestamp 1712472925741
countryId
cityId
bgIds
productId
categoryId 40001001,40001002,40001003,40001004,40001005,40001006,40002001,40002002,40003001,40003002,40003003,40004,40005001,40005002,40006,40007,40008,40009,40010,40011
parentCategoryId
attrId 1,2,3,5
keyword
pageIndex 2
pageSize 10
language zh-cn
area cn
"""

import requests
import time

# 使用 'w' 模式打开文件，覆盖写入
f = open('文件.txt', 'a', encoding='utf-8')

for i in range(1, 11):
    params = {
        "timestamp": time.time(),
        "countryId": "",
        "cityId": '',
        "bgIds": "",
        "productId": '',
        "categoryId": '40001001, 40001002, 40001003, 40001004, 40001005, 40001006, 40002001, 40002002, 40003001, 40003002, 40003003, 40004, 40005001, 40005002, 40006, 40007, 40008, 40009, 40010, 40011',
        "parentCategoryId": '',
        "attrId": "1, 2, 3, 5",
        "keyword": '',
        "pageIndex": i,
        "pageSize": 10,
        "language": "zh-cn",
        "area": "cn"
    }
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query'

    response = requests.get(url, params)
    # 获取返回的json数据 使用json方法获取的响应json数据会自动转换为字典
    result = response.json()
    posts = result['Data']['Posts']

    # 遍历所有的岗位数据
    for post in posts:
        f.write(str(post))

f.close()

