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