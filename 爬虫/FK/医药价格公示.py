import json

import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'
}

url = "https://jyapi.gdmede.com.cn:446/public/priceInfoPublicPage/index"

params = {
    "pageNum": 1,
    "pageSize": 1000,
    "showSearch": '',
    "searchValue": '',
    "prodType": '',
    "prodId": '',
    "yPid": '',
    "nameCn": '',
    "price": '',
    "spec": '',
    "smlName": '',
    "warpName": '',
    "facName": '',
    "attrName": '',
    "convert": '',
    "prodTrade": '',
    "wh": '',
    "priceUnit": '',
    "nhiGroupCode": '',
    "convertPer": '',
    "convertSpec": '',
    "convertUnit": '',
    "ybType": '',
    "qualityEvaluation": '',
    "jgAttCou": '',
    "type": '',
    "sourceStr": '',
    "briskFlag": ''
}

response = requests.get(url, params=params, headers=headers)
content = response.content.decode()
data_list_pattern = r"dataList:\s*\[(.*?)\]"
data_list_match = re.search(data_list_pattern, content)
if data_list_match:
    data_list_str = data_list_match.group(1)
    json_data = f'[{data_list_str}]'
    data_list = json.loads(json_data)
    print(len(data_list), data_list)

else:
    print("没有找到dataList")
