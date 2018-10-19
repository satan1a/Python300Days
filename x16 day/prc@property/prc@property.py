class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    # @property 把一个方法 score() 变成属性调用
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value


if __name__ == "__main__":
    s = Student()
    # s.score = 999
    # s.pardon = 999
    # print(s.pardon)
    # print(s.score)