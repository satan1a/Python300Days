# map() 与 reduce()
	1. map()
	接收两个参数：
	一个是 函数， 一个是 Iterable，map() 将传入的函数依次作用到 Iterable 序列的每个元素，并把结果作为新的 Iterable 返回

	2. reduce()
	接收两个参数：
    一个是 函数， 一个是 Iterable，reduce() 首先把 Iterable 的前两个元素做函数运算，再把结果和下一个函数做累积计算