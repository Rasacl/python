import os
import time

import requests
import base64
from docx import Document

api_key = 'YXj8HUPGH39jrH1kcEqu5xdX'
secret_key = 'Nz5IucvvI3fg4blHnU31lJSQPSKZDO5n'


def main():
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={api_key}&client_secret={secret_key}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code != 200:
        raise Exception("获取access_token失败: {}".format(response.text))

    access_token = response.json()['access_token']
    return access_token


def get_text_from_image(access_token, file):
    max_retries = 3
    for _ in range(max_retries):
        try:
            request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"

            # 二进制方式打开图片文件
            with open(file, 'rb') as f:
                img = base64.b64encode(f.read()).decode()

            params = {"image": img}
            access_token = access_token
            request_url = request_url + "?access_token=" + access_token
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(request_url, data=params, headers=headers)

            if response.status_code != 200:
                raise Exception("OCR请求失败: {}".format(response.text))

            response_data = response.json()
            if 'words_result' not in response_data:
                raise Exception("未在响应中找到'words_result'键: {}".format(response_data))

            word = '\n'.join(i['words'] for i in response_data['words_result'])
            return word
        except Exception as e:
            if "Open api qps request limit reached" in str(e):
                print("达到QPS限制，等待60秒...")
                time.sleep(10)  # 等待60秒后再次尝试
            else:
                raise  # 重新抛出其他异常
    raise Exception("尝试次数过多，仍然无法获取数据")


if __name__ == '__main__':
    word_list = []
    doc = Document()
    access_token = main()
    files = os.listdir('imgs\\')
    for file in files:
        filename = 'imgs\\' + file
        print(filename)
        word = get_text_from_image(access_token, filename)
        word_list.append(word)
    doc.add_paragraph('\n'.join(word_list))
    doc.save('跟植物有关的现代诗.docx')
