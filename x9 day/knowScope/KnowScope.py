class TestScope:

    # 非公开，不应被直接调用
    def _privateFunction(self):
        print("It's private!")

    def publicFunction(self):
        print("It's public!")

testClass = TestScope()
testClass.publicFunction()