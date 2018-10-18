from types import MethodType

class Student(object):
    pass

def set_age(self, age):
    self.age = age

s = Student()
s.set_age = MethodType(set_age, s)
# 给一个实例绑定一个方法
s.set_age(25)
print(s.age)

s2 = Student()
# 给一个实例绑定的方法，对另一个实例不起作用
# s2.set_age()

# 给类绑定方法后，所有实例都可调用
Student.set_age = set_age
s3 = Student()
s3.set_age(18)
print(s3.age)


