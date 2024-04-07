'''
 案例分为两部分
    1. 单个视频采集  https://v.douyu.com/show/kDe0W2DgLYn7A4Bz
    斗鱼网站
      通过媒体文件没有视频链接
      查看全部的数据包：是否存在大量的相似的链接（。。。.ts）属于m3u8流媒体文件
       无痕模式 先打开控制台 在nerwork搜索m3u8  真正的m3u8数据包链接地址 https://v.douyu.com/wgapi/vodnc/front/stream/getStreamUrlWeb
    m3u8流媒体文件：
      把完整的视频内容，分割N个视频片段（ts文件） 所有的视频片段都存在一个m3u8文件中
    2. 多个视频采集
'''
import os
import pprint

import requests
# 导入编译js代码的模块
import execjs
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    "Cookie": 'dy_did = e3d78f71023cb067c670d69b00001701; dy_did = e3d78f71023cb067c670d69b00001701'
}


# 获取m3u8 数据包

def get_m3u8():
    url = 'https://v.douyu.com/wgapi/vodnc/front/stream/getStreamUrlWeb'
    # 模拟浏览器请求头

    # 获取sign加密参数，通过python代码调用js代码

    # 读取js代码
    f = open('./douyu.js', 'r', encoding='utf-8').read()
    # 编译js代码
    js_code = execjs.compile(f)
    # 参数
    a = 38483215  # 视频ID
    o = "e3d78f71023cb067c670d69b00001701"  # 固定字符串
    s = int(time.time())  # 时间戳
    print(s)
    sign = js_code.call('ub98484234', a, o, s).split('&sign=')[-1]
    print(sign)
    data = {
        "v": 220320240402,
        "did": "e3d78f71023cb067c670d69b00001701",
        "tt": s,
        "sign": sign,
        "vid": "kDe0W2DgLYn7A4Bz"
    }

    response = requests.post(url=url, headers=headers, data=data)
    # print(response.json())
    # m3u8_high_url = response.json()['data']['thumb_video']['high']['url']
    # return m3u8_high_url
    return 'http://play-tx-ugcpub.douyucdn2.cn/live/high_37523468020230730151055-upload-e8bd/playlist.m3u8?tlink=660b7fdf&tplay=660c0c7f&exper=0&nlimit=5&us=e3d78f71023cb067c670d69b00001701&sign=3cb5f2c7f62ec9ea25ebabdb1c9c56d7&u=0&d=e3d78f71023cb067c670d69b00001701&ct=web&vid=38483215&pt=2&cdn=tx'


def get_m3u8_data(m3u8):
    m3u8_data = requests.get(url=m3u8, headers=headers).text
    # 解析数据 提取ts文件链接
    ts_list = re.findall(',\n(.*?)\n#', m3u8_data)
    ts_name = '/'.join(m3u8.split('/')[:-1])
    if not os.path.exists('video'):
        os.makedirs('video')
    # for循环遍历
    print(m3u8_data, ts_list)
    for ts in ts_list:
        ts_url = ts_name + '/' + ts
        # 获取视频片段内容
        ts_data = requests.get(url=ts_url, headers=headers).content
        with open('video\\舞蹈视频.mp4', mode='ab') as f:
            # 写入数据
            f.write(ts_data)


if __name__ == '__main__':
    m3u8_high_url = get_m3u8()
    get_m3u8_data(m3u8_high_url)
