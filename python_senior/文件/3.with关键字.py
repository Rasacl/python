# whit 作用同try...finally
with open(r'F:\python\python_senior\文件\111.txt', 'r') as f:  # as 取别名
    print(f.read())
# 无需f.close() 会自动关闭文件
print(f.closed)
