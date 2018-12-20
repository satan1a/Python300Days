# with open("./todo.list", 'r', encoding='utf-8') as f:
#     '''读取字节'''
#     # strings = f.read(2)
#     stringsList = f.readlines()
#     print(stringsList)
#     for string in stringsList:
#         print(string.strip())
#
# with open("writeTemp.list", "w", encoding="utf-8",) as f:
#     f.write("你好呀，Satan1a")

for i in range(2):
    with open('./todo.list', 'w', encoding='utf-8') as f:
        f.write("谈莹小家伙")
        f.close()

    with open('./todo.list', 'r+', encoding='utf-8') as f1:
        for strings in f1.readlines():
            print(strings)
