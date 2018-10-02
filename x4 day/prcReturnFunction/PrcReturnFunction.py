def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


# 返回的是求和函数
f = lazy_sum(1, 3, 5, 7, 9)

