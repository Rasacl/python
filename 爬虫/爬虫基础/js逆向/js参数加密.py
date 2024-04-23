"""
js加密过程
 pwd = md5(pwd + 'Hq44cyp4mT9Fh5eNrZ67bjifidFhW%fb0ICjx#6gE59@P@Hr8%!WuYBa1yvytq$qh1FEM18qA8Hp9m3VLux9luIYpeYzA2l2W3Z');
"""
import requests
from hashlib import md5

"""密码加密函数"""


def get_md5_password(password):
    data_string = password + 'Hq44cyp4mT9Fh5eNrZ67bjifidFhW%fb0ICjx#6gE59@P@Hr8%!WuYBa1yvytq$qh1FEM18qA8Hp9m3VLux9luIYpeYzA2l2W3Z'
    obj = md5()
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()


params = {
    "email": "2441940130@qq.com",
    "pwd": get_md5_password('1234cn90')
}


print(get_md5_password("cc123456"))