import requests

url = 'https://ws6.stream.qqmusic.qq.com/C400001KscCI21Tf5L.m4a?guid=7995945978&vkey=2056972AB7A2B9206789C8A1537D6860113381572ABF69435E294CCEFC161CF36CFF558DBA43645F5A2909B4C062E063C58E98B39671AC4F&uin=2441940130&fromtag=120032'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

response = requests.get(url=url, headers=headers)

with open('如果可以.mp3', 'wb') as f:
    f.write(response.content)
