class Student(object):
    __slots__ = ('name','age')  # 用 tuple 定义允许绑定的属性名称

s = Student()
s.age = 20
s.name = 'Satan1a'
# s.score = 99  没有放到 __slots__ 中，会报错

class GraduateStudent(Student):
    pass

g = GraduateStudent()
# __slots__ 定义的属性仅对当前类的实例起作用，对继承的子类不起作用
g.score = 99
print(g.score)