# 数值类型 整数 float 布尔值 None
# 数据结构类型 列表 元组 字典 集合

a = 123
print(type(str(a))) # 把a转换为字符串

st = '123'
print(type(int(st))) # 把st转换为整数

print(type(float(a))) # 把a转换为浮点数

# input 输入函数 print 输出函数
# 输入特点 当程序执行到input的时候，等待用户输入，输入完成才会向下执行 input接收到用户输入后，一般存储到变量，方便使用 input会把接收到的任意用户输入都视为字符串类型
name = input('请输入你的名字：')
print('你好', name)

x = int(input('请输入一个整数: '))
print(x)

y = eval(input('请输入一个数: '))
print(y)