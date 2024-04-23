"""
track:
时间 x轴坐标 y轴坐标 滑动的总距离
"78516;278.00;421.00;0.00",
"78674;279.00;420.00;1.00",
"78695;296.00;419.00;18.00",
"78717;382.00;418.00;104.00",
"78739;526.00;418.00;248.00",
"78760;694.00;416.00;416.00"
"""
import json
import random
import time
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

session = requests.Session()


def get_track(start_time):
    """模拟生成浏览器滑动轨道信息"""
    # # 定义开始滑动事件
    # start_time = int(time.time() * 1000)
    # 定义 x轴 和 y轴的起始坐标
    x, y = 200, 300
    # 滑动总距离
    distance = random.randint(422, 438)

    # 保存轨迹信息的列表
    track = ['{};200.00;300.00;0.00'.format(str(start_time)[-5:])]

    # 滑动的距离的长度
    s = 0
    while s < distance:
        start_time = start_time + random.randint(20, 35)
        # 随机生成滑动距离
        w = random.randint(10, 50)
        s += w
        x += w
        t = str(start_time)[-5:]
        if s > distance:
            s = distance
        f = '{};{:.2f};{:.2f};{:.2f}'.format(t, x, y, s)
        track.append(f)
    return track


def aes_encrypt(content):
    """使用AES加密"""
    # 加密的所需秘钥， 需要以字节形式表示
    key = b"227V2xYeHTARSh1R"

    # 创建一个AES加密对象
    aes = AES.new(
        key=key,  # 秘钥
        mode=AES.MODE_ECB  # 加密模式为ECB
    )

    # 将要加密的内容转换为字节形式 并进行填充
    raw = pad(content.encode('utf-8'), 16)
    # 使用AES对象对填充后的数据进行加密
    encrypted = aes.encrypt(raw)
    # 对加密的结果进行base64编码转换为字符串
    res = base64.b64encode(encrypted)
    return res.decode()


def get_uid():
    """获取uid的值"""
    response = session.get('https://user.qunar.com/passport/login.jsp')
    cookie = response.cookies
    uid = cookie['QN1']
    return uid


def get_params():
    """获取请求参数"""
    open_time = int(time.time() * 1000)
    start_time = open_time + random.randint(1000, 3000)
    track = get_track(start_time)
    sin_info = {
        "ori": [],
        "acc": [],
        "endTime": int(time.time() * 1000),
        "openTime": open_time,
        "startTime": start_time,
        "uid": get_uid(),
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "track": track,
        "deviceMotion": [{"isTrusted": True} for i in range(10, 100)]
    }
    str_res = aes_encrypt(json.dumps(sin_info))
    data = {
        "appCode": "register_pc",
        "cs": "pc",
        "orca": 2,
        "data": str_res
    }
    return data


def get_captcha_params(slideToken):
    """获取验证码请求参数"""
    captcha_info = {
        "usersource": "",
        "source": "",
        "ret": "",
        "ref": "",
        "business": "",
        "pid": "",
        "originChannel": "",
        "activityCode": "",
        "origin": "",
        "mobile": "17702335386",
        "prenum": "86",
        "loginSource": 1,
        "slideToken": slideToken,
        "smsType": 0,
        "appcode": "register_pc",
        "bella": "1683616182042##aa61064fe5832cf99c7129850219a38ebc406ad0",
        "captchaType": "",
    }
    return captcha_info


def main():
    """1. 发生请求模拟滑动验证"""
    url = 'https://vercode.qunar.com/inner/captcha/snapshot'
    params = get_params()
    response = session.post(url=url, json=params)
    # 获取滑动验证结果中的token值
    slideToken = response.json()['data']["cst"]
    print(slideToken)
    """2. 发送请求验证码 """
    captcha_info = get_captcha_params(slideToken)
    res = session.post(url='https://user.qunar.com/weblogin/sendLoginCode', data=captcha_info)
    print(res.json())
    login()


def login():
    """登陆"""
    vcode = input('请输入验证码:')
    login_info = {
        "activityCode": "",
        "appcode": "register_pc",
        "business": "",
        "captchaType": "",
        "loginSource": 1,
        "mobile": "17702335386",
        "originChannel": "",
        "piccoloT": "login_register_pc",
        "pid": "",
        "prenum": "86",
        "ref": "",
        "ret": "",
        "slideToken": "5a642fdaa13c2b0564c031ecddef98e0",
        "source": "",
        "type": "3",
        "usersource": "",
        "vcode": vcode
    }
    url = 'https://user.qunar.com/weblogin/verifyMobileVcode'
    response = session.post(url=url, json=login_info)
    print(response.json())


if __name__ == '__main__':
    main()
