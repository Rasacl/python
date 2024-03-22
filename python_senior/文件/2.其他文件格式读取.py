# f = open(r'F:\python\python_senior\文件\111.txt', 'r', encoding='utf-16 be')
# content = f.read()
# print(content)


# 二进制方式读取文件 二进制不支持中文
f = open(r'F:\python\python_senior\文件\111.txt', 'rb')
content = f.read()
# 把二进制的内容转化为字符串（解码）
content = content.decode('utf-8')
print(content)
f.close()