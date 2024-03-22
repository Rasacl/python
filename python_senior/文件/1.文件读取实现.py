"""
1 open打开文件，且返回文件操作对象
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
2 read 将文件内容读取到内存里面 read方法执行后 会把文件的指针移动到文件的末尾
read([size]) size是可选参数，表示读取的字节数，返回值是一个字符串，表示读取的内容
3 write 将指定内容写入文件，并返回写入的字符数
write(s)
4 close 关闭文件
close()
"""

# 访问模式 r 只读，w 写，x 写，a 追加，t 文本，b 二进制，+ 读写 ，U 多进程读写
f = open('111.txt')  # 推荐绝对路径 open(r'F:\python\python_senior\文件\111.txt')
text = f.read()
f.close()

# 访问模式举例
# f = open(r'F:\python\python_senior\文件\111.txt')
# str = f.read(10)  # 读取前十个字节
# f.close()

# f = open(r'F:\python\python_senior\文件\111.txt', 'w')  # 以写模式打开文件，如果文件不存在则创建，存在则清空文件内容
# f.write('weld的非凡微软访问人符号位u解放后是夫妻符合客户的积极发挥金额')
# f.close()

# 由于文件读写的时候可能会出现异常，所以可以通过 try-finally 来确保文件被正确关闭
try:
    f = open(r'F:\python\python_senior\文件\111.txt', 'w')
    f.write('发电方式的范围非人非分威风乳房地方')
    print('文件写入成功')
finally:
    f.close()
