import requests

login_url = 'https://passport.china.com/logon'

params = {
    "userName": "17702335386",
    "password": '@Chen991029'
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Referer": "https://passport.china.com/logon"
}


# 发送请求进行登录
response = requests.post(url=login_url, params=params, headers=header)

print(response.content.decode())


# 访问其他的页面

res = requests.get('https://passport.china.com')

print(res.content.decode())