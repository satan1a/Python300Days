"""生成器，生成从 3 开始的无限奇数序列"""
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


"""筛选函数"""
def __not_divisible(n):
    return lambda x: x % n > 0


"""生成器，不断返回下一个素数"""
def primes():
    yield 2
    it = _odd_iter()    # 初始序列
    while True:
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(__not_divisible(n), it)     # 构造新序列


if __name__ == '__main__':
    number = int(input("请输入要打印的素数范围(最大值)：\n"))
    for n in primes():
        if n < number:
            print(n)
        else:
            break

