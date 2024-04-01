# https://spa16.scrape.center/
# https://spa16.scrape.center/api/book/?limit=18&offset=18
# 不行

# import requests
#
# url = 'https://spa16.scrape.center/api/book/?limit=18&offset=18'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
# }
# response = requests.get(url,headers=headers)
# print(response)

import httpx

url = 'https://spa16.scrape.center/api/book/?limit=18&offset=18'
client = httpx.Client(http2=True)
response = client.get(url)
print(response.text)

