import os
import re

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    "Cookie": 'dy_did = e3d78f71023cb067c670d69b00001701; dy_did = e3d78f71023cb067c670d69b00001701'
}


def read_file():
    filename = '07c38d15-4ffb-405b-9da5-db1e043c603b'

    # 使用正则表达式匹配所有的 HTTPS 链接
    # 这个正则表达式会匹配以 https:// 开头的链接，直到遇到换行符或文件结束
    pattern = re.compile(r'https?://[^\s]+')

    # 读取文件内容
    with open(filename, 'r') as file:
        content = file.read()

        # 使用正则表达式查找所有的匹配项
    links = pattern.findall(content)
    return links


def merge_vides(links):
    # 设置视频片段的保存目录
    output_dir = 'video_segments'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for ts in links:
        # 获取视频片段内容
        ts_data = requests.get(url=ts, headers=headers).content
        with open('video_segments\\output.mp4', mode='ab') as f:
            # 写入数据
            f.write(ts_data)


if __name__ == '__main__':
    links = read_file()
    merge_vides(links)
