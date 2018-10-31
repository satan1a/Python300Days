from enum import Enum, unique

Animal = Enum('Animal', ('Dog', 'Cat', 'Snake'))

@unique
class MyAniaml(Enum):
    Dog = "Jan"
    Cat = "Satan1a"
    Snake = "Toky"


print(MyAniaml.Dog.value)
print(MyAniaml.Cat.value)

for name, value in Animal.__members__.items():
    print("{0} => {1}".format(name, value))
