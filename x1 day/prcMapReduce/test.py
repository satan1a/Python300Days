from functools import reduce


def f(x):
    return pow(x, 3)

numberList = [1, 2, 3, 4, 5]


# r = map(str, numberList)
#
# print(list(r))
#
# print(":-<")

#
def fn(x, y):
    return x * 10 + y

def char2numList(strings):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[strings]

def char2num(string):
    return reduce(fn, map(char2numList, string))


if __name__ == '__main__':
    strings = "123456"
    print("The initial strings:   {0}".format(strings))
    print("The initial type is:   {0}".format(type(strings)))
    print("Transform char to int")
    print("After transformed is:  {0}".format(char2num(strings)))
    print("After type is:         {0}".format(type(char2num(strings))) )
