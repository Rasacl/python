import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

# 设置允许跨域
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Content-Type': '*'
}


def get_response_data(url, params, headers, timeout):
    """获取响应数据"""
    response = requests.post(url, json=params, headers=headers, timeout=timeout)
    response.raise_for_status()  # 如果响应状态不是200，将引发HTTPError异常
    return response.json()


def fetch_drug_data(drug_name):
    """获取药品数据"""
    zhong_cheng_yao_list = []
    pages = 1
    is_continue = True
    while is_continue:
        parms = {
            "drugGenname": "",
            "prodentpName": "",
            "medListCodg": "",
            "regName": drug_name,
            "valiFlag": 1,
            "pageNum": pages,
            "pageSize": 100
        }
        data = get_response_data('https://ggfwpz.ylbzj.cq.gov.cn/hsa-pss-pw/web/pw/terms/queryWmBypage',
                                 parms, headers, 30)
        if len(data) < 1:
            break

        datalist = data['data']['data']
        medListCodg_list = [item['medListCodg'] for item in datalist]
        for index, medListCodg_num in enumerate(medListCodg_list):
            parms1 = {
                "medListCodg": medListCodg_num
            }
            data_1 = get_response_data('https://ggfwpz.ylbzj.cq.gov.cn/hsa-pss-pw/web/pw/terms/queryDetilInfo',
                                       parms1, headers, 30)
            datalist_1 = data_1['data']

            merged_dict = datalist[index].copy()
            merged_dict.update(datalist_1)
            zhong_cheng_yao_list.append(merged_dict)
            print(
                '已将药品名称为' + f'{drug_name}' + '写入excel，' + '共计写入' + f'{len(zhong_cheng_yao_list)}' + '条')
        if len(datalist) < 100:
            break
        else:
            pages += 1
    return zhong_cheng_yao_list


def get_zhong_cheng_yao_parallel(drug_names):
    """多线程获取中成药数据"""
    with ThreadPoolExecutor() as executor:
        # 使用map方法并行执行任务
        results = executor.map(fetch_drug_data, drug_names)
    # 将结果合并
    zhong_cheng_yao_list = []
    for result in results:
        zhong_cheng_yao_list.extend(result)
    return zhong_cheng_yao_list


if __name__ == '__main__':
    excel_file = pd.ExcelFile('重庆药品爬取名称.xlsx')
    sheet_name = '西药中成药'
    df_zhongchengyao_name = excel_file.parse(sheet_name)
    drug_names = df_zhongchengyao_name['药品名称'].tolist()

    data = get_zhong_cheng_yao_parallel(drug_names)
    df = pd.DataFrame(data)
    df = df[
        ['medListCodg',
         'drugGenname',
         'regName',
         'drugSpec',
         'minPacCnt',
         'pacmatl',
         'minPacunt',
         'prodentpName',
         'chrgitmLv',
         'hilistPricUplmtAmt',
         'memo'
         ]
    ]
    df.columns = \
        ['医疗目录编码',
         '药品通用名',
         '注册名称',
         '药品规格',
         '包装数量',
         '包装材质',
         '包装单位',
         '生产企业名称',
         '费用等级',
         '医保支付标准',
         '医保目录备注'
         ]

    df.to_excel('重庆药品库_西药中成药.xlsx', index=False)
    # df
    # print(df)
