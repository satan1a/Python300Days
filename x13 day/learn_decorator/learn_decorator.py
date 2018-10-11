import logging

"""
定义了新的方法，处理日志
但是这样不再调用真正的业务逻辑 say_something() 函数
后面使用装饰器进行改进
"""


# def use_logging(func):
#     logging.warning("{0} is running :-）".format(func.__name__))
#     func()
#
# def say_something():
#     print("Satan1a Number One!")
#
#
# use_logging(say_something)


"""
定义简单的装饰器
将业务逻辑函数包裹其中
面向切面编程
"""


# def use_logging(func):
#     """一个简单的装饰器"""
#     def wrapper():
#         logging.warning("{0} is running :-）".format(func.__name__))
#         return func()
#     return wrapper
#
# def say_something():
#     print("Satan1a Number One!")
#
#
# say = use_logging(say_something)    # 装饰器返回的是 wrapper，因此这个语句相当于 say = wrapper
# say()

"""
使用 @ 语法糖
可以省略 say = use_logging(say_something) 这句，直接调用 say_something() 即可
此时，我们真正的业务逻辑函数 say_something() 不需进行任何修改，只需要加上修饰器即可
原理是：Python 的函数能像普通的对象一样能作为参数传递给其他函数，可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内

"""


def use_logging(func):
    """一个简单的装饰器"""
    def wrapper():
        logging.warning("{0} is running :-）".format(func.__name__))
        return func()
    return wrapper

@use_logging    # 使用 @语法糖 可以省略 say = use_logging(say_something) 这句，直接调用 say_something() 即可
def say_something():
    print("Satan1a Number One!")

@use_logging
def test_something():
    print("It's just a test")

@use_logging
def test_something_two():
    print("It's just a anther test")


say_something()
test_something()
test_something_two()


"""
在装饰器返回的 wrapper 函数中
*args   接收多个参数
**kwargs    接受多个关键词参数(即已经赋值的，当作关键字使用的)

"""

# def foo(name, age=12, height=1.5):
#     print("I am {0}, age {1}, height {2}".format(name, age, height))
#
# def use_logging(func):
#     """一个简单的装饰器"""
#     def wrapper(*args, **kwargs):
#         # args 是一个数组，kwargs 是一个字典
#         logging.warning("{0} is running :-）".format(func.__name__))
#         return func(*args, **kwargs)
#     return wrapper
#
#
# foo("Satan1a")


"""
带参数的装饰器
实际上可以看作对原有装饰器的一个函数封装
"""

# def use_logging(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             if level == "warn":
#                 logging.warning("{0} is running :-）".format(func.__name__))
#             if level == "critical":
#                 logging.critical("{0} is running :-）".format(func.__name__))
#             else:
#                 logging.error("No Such Level")
#             return func(*args, **kwargs)
#         return wrapper
#
#     return decorator
#
#
# @use_logging(level="critical")    # @use_logging(level="critical") 等价于 @decorator
# def foo(name, age=12, height=1.5):
#     print("I am {0}, age {1}, height {2}".format(name, age, height))
#
#
# foo("Satan1a")


"""
类装饰器
装饰器不仅可以是函数，还可以是类，可附加在函数上
相比函数装饰器，类装饰器具有 灵活度大、高内聚、封装性等优点
使用类装饰器主要依靠类的 __call__ 方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法
"""


# class Foo(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         print("class decorator running")
#         self.func()
#         print("class decorator ending")
#
# @Foo
# def bar():
#     print("Wang wang!")
#
# bar()


"""
functools.wraps
wraps本身也是一个装饰器，它能把原函数的元信息拷贝到装饰器里面的 func 函数中，
这使得装饰器里面的 func 函数也有和原函数 foo 一样的元信息了.
元信息比如：docstring(__doc__)、__name__
"""


# from functools import wraps
# def logged(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__)      # 输出 'f'
#         print(func.__doc__)       # 输出 'does some math'
#         return func(*args, **kwargs)
#     return with_logging
#
# @logged
# def f(x):
#    """does some math"""
#    return x + x * x
#
# f(1)


"""
装饰器顺序
一个函数可以同时定义多个装饰器
执行顺序：从内到外
"""
# @a
# @b
# @c
# def f ():
#     pass

# 等效于：f = a(b(c(f)))