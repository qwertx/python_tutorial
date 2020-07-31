# StringIO顾名思义就是在内存中读写str
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
# getvalue()方法用于获得写入后的str
print(f.getvalue())

# 读取StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


# BytesIO实现了在内存中读写bytes
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# 读取BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))