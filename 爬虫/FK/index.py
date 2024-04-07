import time

import requests
import pandas as pd

# 读取地区代码列表
code_list = pd.read_json('arr_code.json')['code']

# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}

data = {
    "data": {

        "encData": "3DFBCA4667B978F639BB23B95DCE4CC74CE34C33DC32F1068E9E23CA546C9EA8CCD20943B4DAE96380B41164D761DE9742C84A985FE3BABC31CB352556BB87C9C1495DB24A29AB6BC3A85AB7FCA00F338EE714ACFC4C924F01CF575098AEF167B7A135B72DAC6C2F3CD510E411A3C63A9720F6A86E9EFCBA77082625D345D5DFD130FEBBE62DBFF03225CA796232EA15C36959880C2647559E3C97B56FD4F10F",
        "addr": "",
        "regnCode": "110000",
        "medinsName": "",
        "medinsLvCode": "",
        "medinsTypeCode": "",
        "openElec": "",
        "pageNum": 1,
        "pageSize": 100,
        "queryDataSource": "es"
    },
    "encType": "SM4",
    "signData": "xXOARXSIG6L9nOBsCP9Fj1Fjoh893wQh4N+ccwGjegIBDJIwJu5DijKsWXHwHvr2/QCZu/eQ60jKnvJnHiKlQw==",
    "signType": "SM2",
    "timestamp": 1712110149,
    "version": "1.0.0",
}


def get_loop_regnCode():
    # 创建空列表存储所有数据
    all_data = []

    # 遍历地区代码列表
    for regnCode in code_list:
        data['data']["regnCode"] = regnCode
        # 构建请求数据
        is_contiuen = True
        while is_contiuen:
            time.sleep(2)
            data_list = get_data()
            print(f'爬取了{len(data_list)}条')
            print('当前{}页'.format(data['data']["pageNum"]))
            # 将数据添加到 all_data 中
            all_data.extend(data_list)
            print("已经爬取" + format({regnCode}) + "的第" + format({data['data']["pageNum"]}) + '页' + f'一共{len(all_data)}条')
            data['data']["pageNum"] += 1
            if len(data_list) < 100:
                data['data']["pageNum"] = 1
                is_contiuen = False


    return all_data


def get_data():
    for i in range(3):  # 尝试3次
        try:
            response = requests.post('https://fuwu.nhsa.gov.cn/ebus/fuwu/api/nthl/api/CommQuery/queryFixedHospital',
                                     json=data, headers=headers, timeout=10)
            response.raise_for_status()  # 如果响应状态码不是200，抛出异常
            datas = response.json()
            data_list = datas['data']['list']
            return data_list
        except requests.exceptions.ReadTimeout:
            print("请求超时，正在重试...")


if __name__ == '__main__':
    all_data = get_loop_regnCode()
    # 创建 DataFrame 并打印
    df = pd.DataFrame(all_data)
    print(df)