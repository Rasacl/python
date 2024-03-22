# 装饰器的使用方法
'''
1. 先定义一个装饰器函数（帽子）（可以是类、偏函数实现）
2。在定义你的业务函数或者类 --真正要执行的
3。最后把这个帽子待在这个函数的头像
'''
#装饰器模版
def my_decorator(func):
    def wrapper(*args, **kwargs): # *args, **kwargs 是元组解构
        # 执行被装饰函数之前的操作
        res = func(*args,**kwargs)
        # 执行被装饰函数之后的操作
        return res
    return wrapper


# 日志打印装饰器
# 本质是闭包函数
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"正在执行函数：{func.__name__}")
        func(*args, **kwargs)
        print('计算完了e')
    return wrapper


# 第一种方法
@log_decorator
def test_function(x,y):
    print("这是一个测试函数")
    print('{} + {} = {}'.format( x,y,x+y))
test_function(1, 2)  # 添加参数1和2来调用test_function


