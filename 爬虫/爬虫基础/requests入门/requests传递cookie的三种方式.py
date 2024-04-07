import requests

login_url = 'https://passport.china.com/logon'

params = {
    "userName": "17702335386",
    "password": '@Chen991029'
}

'''
方式一：以字典格式传递
   requests.get(cookies=cookies)
方式二：字符串方式传递
   headers = {
      "cookies": "字符串格式cookie"
    }
    
   request.get()
'''

# =================获取请求的cookies  方式一 =======================
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
#     "Referer": "https://passport.china.com/logon"
# }
# 发送请求进行登录
# response = requests.post(url=login_url, params=params, headers=header)
# print(response.content.decode())
# cookies = response.cookies
# print(response.cookies)
# # 访问其他的页面
# res = requests.get('https://passport.china.com', cookies=cookies)
# print(res.content.decode())



# =================获取请求的cookies  方式二： 直接从接口获取 =======================
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
#     "Referer": "https://passport.china.com/logon",
#     "Cookie":'BAIDU_SSP_lcr=https://www.baidu.com/link?url=x37fWQtuXbDDRlIdHn0Fm182pSRhzWFUaxrWxyLtkHG&wd=&eqid=d02cf9b1000ff3fe0000000366120373; Hm_lvt_cbec92dec763e6774898d6d85460f707=1712456566; area_name=%E5%8C%97%E4%BA%AC%E5%B8%82; SESSION_COOKIE=118; JSESSIONID=13C89A7C662D0FF6D09D74BB09547B2F; lastlogindate=2024-04-07; lastloginip=124.65.151.170; Hm_lpvt_cbec92dec763e6774898d6d85460f707=1712459279; nickname=china_6519aoou16791435; lastlogindate=2024-04-07; lastlogintime="11:08:17"; lastloginip=124.65.151.170; bindMobile="1@177*****386"; CHINACOMID=b90b8702-8f95-4442-97a0-d9fd2b5c17e75; CP_USER=FKBo6w-aaDGTLI0-wO5wDtMmWSe88zPJzIpsuaQNIsJcWE8XiDNXpV4kBmR5HE3sOmdBbK6XTJaR66ii5vCTjV%2F%2FfDWdkLveLIdXkmeDvdq7cRnvK9%2FhjHjvNX3EkwemlRKgISOElBbp5m8q8lc2uP8TxRFfOjhKLn6u-bHksZbjiSCo7gjVgojRU0h4qVsufcr5V5Wvt6y8kMEZ3CpXcnXeSYNYVOSxZ%2FH7vUj3098iC44IuLq2ow%3D%3D; CP_USERINFO=4Gkk4uas%2FGU6V4cAn8Kr14YtZHaRsQ3bb0iKxhYvuaLYLT-rPEFbvbaQzjvqSKm2v8Fd1lQ14weg0PM1aAxGqjzFStaNWwdXEhS3Zzs0jusNqPIZSkWIUHBpa7NyrsBUv2O8QVvh3O4yqW9wAjnfpw%3D%3D; china_variable=jpEe7N32pYz8SAjCjL8fnh2eLZiI1D/EC6dYmS6/lLUOPrHJGj-IxLIHbACvhNcaC9z3Z8pi2hy0JtYoQGGXmsutg32di8lhAZaSKKJ8BFBt-lJZl7B3R-LY1hWhKpza; lastlogintime="11:08:17"'
# }
# # # 访问其他的页面
# res = requests.get('https://passport.china.com', headers=header)
# print(res.content.decode())


# =================获取请求的cookies  方式三： 使用request.session创建一个请求对象 =======================
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "Referer": "https://passport.china.com/logon"
}
# 使用request.session创建一个请求对象
http = requests.session()
# 发送请求进行登录
response = http.post(url=login_url, params=params, headers=header)
print(response.content.decode())
# 访问其他的页面
res = http.get('https://passport.china.com')
print(res.content.decode())