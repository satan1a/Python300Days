class Animal(object):
    # 类属性 name
    name = "Little White"

dog = Animal()

# 打印类属性
print(dog.name)

# 给实例 dog 绑定实例属性 name，与 类属性同名
dog.name = "Big Black"
print(dog.name)

# 同名的类属性和实例属性，删除实例属性，将会显示类属性的值
del dog.name
print(dog.name)


