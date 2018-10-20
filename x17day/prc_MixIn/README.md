# 多重继承 和 MixIn模式
## 多重继承
- 首先，继承是面向对象的一个重要方式，继承可实现父类的功能。但继承本身应该表达和应用为两种意思：<br/>
    - 子类 is a 父类 （Dog is Animal）
    - 子类 有 父类的 功能（Bird can Fly）

- 多重继承是指：子类同时继承多个父类，子类通过多重继承可以同时获得多个父类的所有功能。
## MixIn 模式
但问题在于，有时候我们继承父类，只是想格外为子类添加功能，想表达清楚继承关系而又不想设计多层次复杂的继承关系（比如Dog is Animal, Dog is a Mammalia Animal, Dog is a Runable Mammalia Animal）<br/>
此时我们使用 MixIn 来设计这些“mix-ix”混入其中的类。<br/>
- 比如，命名原先的 Runnable 类为 RunnableMixIn 类。Dog 能跑Runnable, 但Dog不是一种Runnable。Runnable是一种功能。
- 因此，使用MixIn命名类、实现多重继承时需要注意：<br/>
    - 必须表示为一种<strong>功能</strong>，而不是一种物品
    - 功能、责任必须<strong>单一</strong>, 若有多个功能，则写为多个MixIn类
    - 它<strong>不依赖于子类的实现</strong>
    - 子类即使不继承它，也可以工作，只是少了某种功能