# yield和return的区别
"""
相同点 都是返回函数执行结果
不同点
    return 结束函数，结束当前执行，返回值
    yield 暂停函数，返回yield后的值，等待下一个send(value)
"""

# yield生成器相比return一次性返回所有结果的优势
# 1. 反应更加迅速 2.节省空间 3.使用更加灵活
