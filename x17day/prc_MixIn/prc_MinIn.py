class Animal(object):
    pass


"""
Run 和 Fly 都是功能单一、不依赖于子类实现、不影响子类工作的类，因此可定义为 MixIn
"""


class RunnableMixIn(object):
    def run(self):
        print(" is running ...")


class FlyableMixIn(object):
    def fly(self):
        print(" is flying ...")


class Bird(Animal, RunnableMixIn, FlyableMixIn):
    pass


swallow = Bird()
swallow.run()
swallow.fly()
