# 使用元类 type()
- type() 函数不仅可以返回对象的类型，又<strong>可以创建新的类</strong> <br/>
🌰 ：>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
- type() 创建类的用法：<br/>
依次传入三个参数：<br/>
        - class的名称；
        - 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
        - class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
- 特别地，使用type()函数创建的类和直接写class完全一致，使用type()函数可以动态地创建类（即在程序运行期间）