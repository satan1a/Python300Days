from io import StringIO
from io import BytesIO

f = StringIO()
f.write('Hello')
f.write(' ')
f.write('world')
print(f.getvalue())


f1 = StringIO("Hello\n\n\n\n\nWorld!")
for string in f1.readlines():
    if string == '\n':
        continue
    print(string.strip())


f2 = BytesIO()
f2.write("你好,世界 Hello_World".encode('utf-8'))
print(f2.getvalue())
print(f2.getvalue().decode('utf-8'))
