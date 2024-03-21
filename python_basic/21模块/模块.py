# 内置模块 | 标准库 python解释器提供
import builtins
print(dir(builtins))

# 库 第三方模块 pip install 模块名


# 自定义模块

# import 模块名
import a
import b
print(a.s)

# 模块取别名 import 模块名 as 别名

# from 模块名 import 函数名1, 函数名2
# from 模块名 import * 全部导入 *表示导入所有函数


# from import 与import的区别

# py文件的两种功能
b.funb()
'''
1.脚本： 一个文件就是整个程序 直接运行 __name__ == '__main__' 表示代码直接在当前文件里面执行
2.模块： 被其他文件导入，被其他文件调用 __name__ = 文件名 表示代码被其他文件导入，被其他文件调用
'''