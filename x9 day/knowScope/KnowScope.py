class TestScope(object):

    # 单下划线开头，非公开，不应被直接调用。虽然可以被调用，但是请视为私有
    def _private_function(self):
        print("It's private!")

    # 双下划线开头，私有，不能被外部访问
    def __absolute_private_function(self):
        print("It's absolutely private!")

    def public_function(self):
        print("It's public!")

testClass = TestScope()
