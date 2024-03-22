# 回调函数

def test3(m,n):
    if m == 3:
        n()
    else:
        print('函数不可调用')

def one():
    print('函数一')

def two():
    print('函数二')


test3(3,one)