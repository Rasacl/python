# readline 方法可以一次性读取一行 方法执行后 会把文件指针移动到下一行，准备再次读取
# with open(r'F:\python\python_senior\文件\222.txt', 'r') as f:
#     while True:
#         text = f.readline()
#         if not text:
#             break
#         print(text, end='')

# readlines 方法一次性读取多行，然后返回一个包含多行的列表,其中每一行的数据是一个元素
with open(r'F:\python\python_senior\文件\222.txt', 'r') as f:
    lines = f.readlines()
    print(lines,1111)
    for line in lines:
        print(line, end='')
