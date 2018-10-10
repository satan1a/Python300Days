class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("{0} is running".format(self.name))

    def print_age(self):
        print("{0}'s age is {1} years old.".format(self.name, self.age))

    def age_add(self):
        self.age = self.age + 1


if __name__ == "__main__":
    dog = Animal("dog Fury", 3)

    # dir() 方法获得一个对象的所有属性和方法
    print(dir(dog))

    # 对象的属性进行操作的方法 getattr() hasattr() setattr()
    setattr(dog, "dog_type", "yellow_dog")
    print(dir(dog))
    print(hasattr(dog, "dog_type"))
    print(getattr(dog, "dog_type"))
    print(getattr(dog, "dog_fly", 404))
