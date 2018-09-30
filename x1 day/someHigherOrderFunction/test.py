import uuid

"""
使用 uuid（Universally Unique Identifier）通用唯一识别码用来标识信息
UUID 分为 5 个版本，下面使用的是第四个版本（不接收蚕食而生成随机UUID）
储存在 list 列表中 
"""
randomString = uuid.uuid4()
listOne = list()

for i in range(0, 100):
    randomString = uuid.uuid4()
    listOne.append(randomString)

for element in listOne:
    print("{0} \n".format(element))


