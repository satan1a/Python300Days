class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    """定义内部方法，实现“数据以及逻辑操作的封装”"""
    def get_score(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        else:
            return 'Satan1a!'

satan1a = Student("satan1a", 66)
print(satan1a.get_score())


