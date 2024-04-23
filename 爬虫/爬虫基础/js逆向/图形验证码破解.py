'''
案例 超级鹰登陆

请求参数
user: admin
pass: 123456
imgtxt: x4Gg
act: 1

破解步骤
  1. 发送请求获取验证码图片
  2. 识别验证码内容
  3. 发送登陆请求
'''

import requests
import ddddocr
session = requests.Session()
# 1. 发送请求获取验证码图片
img_url = 'https://www.chaojiying.com/include/code/code.php?u=1'
img_response = session.get(url=img_url)

ocr = ddddocr.DdddOcr()
text = ocr.classification(img_response.content)

with open('code.jpg', 'wb') as f:
    f.write(img_response.content)

# 3. 发送登陆请求
url = 'https://www.chaojiying.com/user/login/'

params = {
    'user': 'Rascal',
    'pass': 'chen991029',
    'imgtext': text,
    'act': 1
}

response = requests.post(url=url, data=params)
print(response.text)