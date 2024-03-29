# 递归函数 求斐波那契数列的第n个数
'''
必须有一个明确的结束条件
每次进入更深一层递归时，问题规模相比上一次递归都应有所减少
相邻两次的重复之前有紧密的联系，前一次要为下一次做准备
递归效率不高，递归层次过多会导致栈溢出
优点: 定义简单 逻辑清醒
'''

# 递推 给递归函数实现拆解 递归每一次都是基于上一次进行下一次的执行
# 回溯 遇到终止条件之前，从最后往前往回返，一级一级的把值返回
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return -1
print(fibonacci(10))