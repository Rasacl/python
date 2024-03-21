# if True:
#     print('条件成立执行的代码')
#
#
# print('无论如何都会执行的代码')

# True和False的界定
# 任何非空和非零的对象都为真，解释为True
# 空字符串、0、None对象都为假，解释为False
#
# age = int(input('请输入您的年龄：'))
#
# if age >= 18:
#     print('成年了，可以进入这个房间。')
# else:
#     print('未成年，禁止进入这个房间。')
#
# score = eval(input('请输入你的成绩：'))
# if score >=90 and score <= 100:
#     print('特优')
# elif score >= 80 and score <90 :
#     print('优秀')
# elif score>=70 and score <80 :
#     print('良好')
# elif score >=0 and score <70:
#     print('及格')
# else:
#     print('成绩不作数')



# if嵌套
if True:
    if True:
        print('这是嵌套的if语句')
    else:
        print('这是嵌套的else语句')
else:
    print('这是外层的else语句')


# 比较运算符 == != > < >= <=
# 非运算符 not