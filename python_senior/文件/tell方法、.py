#tell() 方法告诉你文件的当前位置 下一次操作从当前位置开始
# seek(offset,[,from]) 改变当前文件位置(改变指针位置) offset 开始的偏移量 from指定开始移动字节的参考位置 0表示起始位置 1表示当前位置 2表示文件结束

f = open(r'F:\python\python_senior\文件\111.txt', 'r')
text = f.read(10)
print(text)

position = f.tell()
print('当前指针位置',position)
#把指针重新定位到文件开头
position = f.seek(0,0)
text2 = f.read(10)
print(text2)

f.close()