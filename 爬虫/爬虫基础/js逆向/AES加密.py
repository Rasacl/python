import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


# 要加密的内容
content = "1234567"

# 加密的所需秘钥， 需要以字节形式表示
key = "227V2xYeHTARSh1R".encode('utf-8')

# 创建一个AES加密对象
aes = AES.new(
    key=key, # 秘钥
    mode=AES.MODE_ECB  # 加密模式为ECB
)

# 将要加密的内容转换为字节形式 并进行填充
raw = pad(content.encode('utf-8'),16)
# 使用AES对象对填充后的数据进行加密
encrypted = aes.encrypt(raw)
# 对加密的结果进行base64编码转换为字符串， 以便进行传输和存储
res = base64.b64encode(encrypted)
# 打印加密后的结果
print(res.decode())