#异常 影响程序的正常运行

# 异常的种类
"""
AttributeError 访问一个不存在的属性
IndexError 访问列表中的不存在的索引
KeyError 访问字典中的不存在的键
NameError 访问不存在的变量或对象方法
TypeError 传入的类型与期望的类型不匹配
ValueError 传入的值与期望的值不匹配
ZeroDivisionError 除数为零
keyboardInterrupt 用户中断程序运行
AssertionError 断言语句
RuntimeError 运行时错误
NotImplementedError 方法没有实现
ImportError 导入模块或包失败
SyntaxError 语法错误
IndentationError 缩进错误
OverflowError 数值超出最大范围
TabError 混用制表符和空格
UnicodeError Unicode相关错误
IOError IO错误
OSError 操作系统错误
MemoryError 内存错误
ArithmeticError 算术错误
SystemError 系统错误
"""


# 异常处理
# 异常处理格式一
try:
    print(10 / 0)
    print("这是一条不会执行的语句")
except: # 基类异常 捕获所有异常 或者except ZeroDivisionError 定义捕获的异常类型    except NameError as e  指定异常类型 取别名为e  except Exception as e  万能异常 捕获所有异常
    print("除数不能为零")




#多分支异常
try:
    print(10 / 0)
    print("这是一条不会执行的语句")
except ZeroDivisionError:
    print("除数不能为零")
except NameError:
    print("变量未定义")
except Exception as e:
    print("发生未知异常：", e)


# 异常处理格式二  else 只有在没有异常时才会执行
try:
    print(10 / 0)
    print("这是一条不会执行的语句")
except:
    print("发生未知异常")
else:
    print("没有异常发生")


# 异常处理格式三
try:
    print(10 / 0)
    print("这是一条不会执行的语句")
except:
    print("发生未知异常")
finally:
    print("无论如何，都会执行finally语句")


# 异常处理格式四
try:
    print(10 / 0)
    print("这是一条不会执行的语句")
except:
    print("发生未知异常")
else:
    print("没有异常发生")
finally:
    print("无论如何，都会执行finally语句")



# 异常传递 在主函数中设置异常捕获 子函数抛出的异常会被主函数捕获
# def funa():
#     return int(input('请输入整数'))
# def funb(): # 主函数中捕获异常
#     return funa()
#
# try:
#     print(funb())
# except Exception as e:
#     print("发生未知异常 %s" %e)


# 主动抛出异常
def funa():
    raise Exception('抛出一个异常')



