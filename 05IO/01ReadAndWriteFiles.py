# 以只读模式打开一个文件对象
f = open('C:/Users/O/Desktop/python/Liao/05IO/test.txt', 'r')
# 如果文件不存在，open()函数就会抛出一个IOError错误
try:
    f = open('C:/Users/O/Desktop/python/Liao/05IO/notfound.txt', 'r')
except IOError as e:
    print('file not found!')

# 用read()方法可以一次读取文件的全部内容
# Python把内容读到内存，用一个str对象表示
print(f.read())
# 调用close()方法关闭文件，文件使用完毕后必须关闭
f.close()

# 为了保证无论是否出错都能正确地关闭文件，使用try ... finally结构
try:
    f = open('C:/Users/O/Desktop/python/Liao/05IO/test2.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

# 使用with语句可以自动调用close()方法
# 效果和try ... finally一样
with open('C:/Users/O/Desktop/python/Liao/05IO/test2.txt', 'r') as f:
    print(f.read(10)) # 读取10个字符


# 如果文件大小不定，反复调用read(size)比较保险
# 如果是配置文件，调用readlines()最方便
with open('C:/Users/O/Desktop/python/Liao/05IO/test3.txt', 'r') as f:
    for line in f.readlines():
        # s.strip(rm)删除s字符串中开头、结尾处、位于rm的字符
        # rm为空时，删除空白符（包括'\n', '\r', '\t', ' ')
        print(line.strip()) # 去掉末尾的'\n'

# 有read()方法的对象在Python中统称为file-like Object
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲

# 读取二进制文件，此处省略了盘符
f = open('/Users/O/Desktop/python/Liao/05IO/bitest.jpg', 'rb')
f.read()
f.close()

# 非UTF-8编码的文本文件，使用r'...'格式避免了转义字符的问题
f = open(r'\Users\O\Desktop\python\Liao\05IO\testgbk.txt', 'r', encoding = 'gbk')
print(f.read())
f.close()

# 文件中有非法字符，会遇到UnicodeDecodeError
# 使用errors参数
f = open(r'\Users\O\Desktop\python\Liao\05IO\testgbk.txt', 'r', encoding = 'gbk', errors = 'ignore')
f.close()

# 写文件，'w'是覆盖，'a'是追加
# 只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘
f = open('C:/Users/O/Desktop/python/Liao/05IO/test.txt', 'w')
f.write('Hello, world!')
f.close()

# 最好用with语句
with open('C:/Users/O/Desktop/python/Liao/05IO/test.txt', 'a') as f:
    f.write('\nHello, world!')