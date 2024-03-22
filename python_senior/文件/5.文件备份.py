# f1 = open(r'F:\python\python_senior\文件\111.txt', 'r')
# f2 = open(r'F:\python\python_senior\文件\222.txt', 'w')
# text = f1.read()
# f2.write(text)
#
# f1.close()
# f2.close()

# 任意文件备份
old_name= input('请输入您要备份的文件名：')
index = old_name.rfind('.') # rfind 从右向左查找，找到最后一个点的位置 找不到返回-1
new_name = old_name[:index] + '[备份]' + old_name[index:]
f1 = open(old_name, 'rb')
f2 = open(new_name, 'wb')

while True:
    text = f1.read(1024)
    if not text:
        break

    f2.write(text)

f1.close()
f2.close()
