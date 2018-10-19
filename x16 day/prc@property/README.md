# 使用@property
## 负责把一个方法变成属性调用
- 首先，把一个getter方法（return self._xxx）变成属性，只需加上 @property
- 再用 @property 创建的对象再创建一个装饰器 @xxx.yyy 将一个yyy方法变成属性赋值