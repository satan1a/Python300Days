# 获取对象信息
## type()
- 返回对象的类型

## isinstance()
- 判断继承的类型
- 能用 type() 判断的基本类型，也能用 isinstance() 判断
- 还能判断一个变量是否是 某些变量中的一种
    - <pre>
        >>>isinstance([1, 2, 3], (list, tuple))
        True
        >>>isinstance((1, 2, 3), (list, tuple))
        True
    </pre>

## dir()
- 获取一个对象的所有属性和方法

## getattr() setattr() hasattr()
- 使用情况：不知道一个对象的信息时，获取信息，且通过是否包含某属性来判断其类型。 比如，使用 hasattr(object_name, "read") 判断对象是否为存在 read() 方法，进而判断对象是否为 流 。
- 因为 Python 这类动态语言的 feel-like object 特性，有 read() 方法的，可能是文件流也可能是网络流或内存中的一个字节流。即只要有正确的 run() 方法。