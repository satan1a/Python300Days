"""
author: satan1a
date: 2018_9_28
today: 高阶函数的练习
"""

"""
引入：在python中，函数名也是变量

"""
f = abs
print(f)


"""
引入：变量开可以指向函数，函数的参数能接受变量，一个函数接收另一个函数作为参数，则称其为高阶函数
如下：将 abs() 函数传入自己定义的 add() 函数中，则称 add() 函数为高阶函数
"""


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 6, abs))



