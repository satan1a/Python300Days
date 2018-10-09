class Animal(object):
    def run(self):
        print("Animal is running")

class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

class Satan1a(Animal):
    def fly(self):
        print("Satan1a is flying")

# all the animal can run twice
def run_twice(Animal):
    Animal.run()
    Animal.run()

# Only Dog can run thrice
# fell-like object
# 但是Python这种动态语言不要求严格的继承体系，
# 不要求传入的一定是 Dog 类型，只要保证传入的对象像Dog类一样，有一个 run() 方法就可以
def run_thrice(Dog):
    Dog.run()
    Dog.run()
    Dog.run()


if __name__ == "__main__":
    animal = Animal()
    dog = Dog()
    cat = Cat()
    satan1a = Satan1a()

    run_twice(animal)
    run_twice(dog)
    run_twice(cat)
    print("\nfeel-like object 鸭子类型 Python不严格要求传入的类型")
    run_thrice(cat)
    print("\n以下不会显示 Satan1a 类里的 fly() 方法")
    run_thrice(satan1a)