"""
请求地址 https://fanyi.baidu.com/v2transapi?from=en&to=zh

请求参数
from: en
to: zh
query: python2
transtype: realtime
simple_means_flag: 3
sign: 652028.856525
token: fd4b968be97772de126b68da4bf862c2
domain: common
ts: 1712908341428
"""

import requests
import time
import execjs

url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
headers = {
    "Referer": "https://fanyi.baidu.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Cookie": '''BIDUPSID=35436D9B15DCC1E5D33153F2A12B61A0; PSTM=1709084158; BAIDUID=35436D9B15DCC1E5BBE8C71EF4BEA124:FG=1; BDUSS=FndXBFald-SEVtdmNZcGs2Mnh1emEtQlprSnI1fkRpS2tNRTFKQy1Pc0pTaFptRVFBQUFBJCQAAAAAAAAAAAEAAACLQluP0-O2-c~rs9SyvLahQzEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAm97mUJve5lbU; BDUSS_BFESS=FndXBFald-SEVtdmNZcGs2Mnh1emEtQlprSnI1fkRpS2tNRTFKQy1Pc0pTaFptRVFBQUFBJCQAAAAAAAAAAAEAAACLQluP0-O2-c~rs9SyvLahQzEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAm97mUJve5lbU; newlogin=1; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_WISE_SIDS=40302_40380_40367_40415_40466_39662_40512_60046_40510; BAIDUID_BFESS=35436D9B15DCC1E5BBE8C71EF4BEA124:FG=1; H_WISE_SIDS_BFESS=40302_40380_40367_40415_40466_39662_40512_60046_40510; ZFY=cFvuA7eHoRlpRXb5LdgpenjaIpjC3ifd:ApLtMl80F6w:C; H_PS_PSSID=40302_40380_40367_40415_39662_40512_60046_40510; BDRCVFR[kSyA9a8U-kc]=mk3SLVN4HKm; delPer=0; PSINO=1; BA_HECTOR=0hag2h2lah84ak242haha40gl267eo1j1hb561t; smallFlowVersion=old; RT="z=1&dm=baidu.com&si=1wqvh15ag3qh&ss=luwd9p43&sl=3&tt=3bv&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=46um&ul=488q&hd=48b9"; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1712908319; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1712908319; APPGUIDE_10_7_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; ab_sr=1.0.1_ZThiZmFkNzkyZjM2MWIyYzc3ZWVhYzUxZGY1YThlZGZjN2M3NmFkZDQ4NDQzOWYzYWVkMTZjYWMwNzQ2YTUzZTAyMmNlMTBkMTNiMjVmYjdiNTZkYjNkOTViODA3ZGU2ZTIyNjFmMjQ3Y2FmNTE3YTY3NmU5NTkzM2M3NzM1MjNmMDNhZmJkZWM3YmRiMzAyMWZlNzAzODQ0YmMzY2M0NTZkNjM5MjU4MGZlOGJlMmVjNjRiNzJiZjJlMzU0YmZi'''
}
name = input('请输入要翻译的内容:')
# 编译代码
js = execjs.compile(open('baidu.js', 'r', encoding='utf-8').read())
sign = js.call('b', name)
params = {
    "from": "en",
    "to": "zh",
    "query": name,
    "transtype": "realtime",
    "simple_means_flag": 3,
    "sign": sign,
    "token": "fd4b968be97772de126b68da4bf862c2",
    "domain": "common",
    "ts": int(time.time() * 1000)
}

response = requests.post(url=url, data=params, headers=headers)

print(response.json())
