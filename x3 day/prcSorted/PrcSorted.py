"""
@author satan1a
@date 2018_10_1
"""


numberList = [36, 5, -12, 9, -21]
stringList = ['bob', 'about', 'Zoo', 'Credit']

print(sorted(numberList))

print(sorted(numberList, key=abs))

print(sorted(stringList))

print(sorted(stringList, key=str.lower))

print(sorted(stringList, key=str.lower, reverse=True))

