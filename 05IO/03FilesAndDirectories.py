import os

# posix == Linux/Unix/OSX, nt == Windows
print(os.name)

# os.uname 获取详细的系统信息
# uname()在windows上不提供

# 环境变量
print(os.environ)
# 获取某个环境变量的值，用os.environ.get('key')
print(os.environ.get('PATH'))
print(os.environ.get('notexist', 'default'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 创建一个新目录要把新目录的完整路径表示出来
os.path.join(r'C:\Users\O\Desktop\python\Liao\05IO', 'testdir')
os.mkdir(r'C:\Users\O\Desktop\python\Liao\05IO\testdir')
# 删掉一个目录
os.rmdir(r'C:\Users\O\Desktop\python\Liao\05IO\testdir')


# 合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作

# 把两个路径合成一个时，要通过os.path.join()函数
# 这样可以正确处理不同操作系统的路径分隔符
# 在Linux/Unix/Mac下是 part-1/part-2
# Windows下会返回 part-1\part-2

# 同样地在拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
print(os.path.split(r'C:\Users\O\Desktop\python\Liao\05IO\file.txt'))
# os.path.splitext()可以直接得到文件扩展名
print(os.path.splitext(r'C:\Users\O\Desktop\python\Liao\05IO\file.txt')[1])


# 对文件重命名
# os.rename('test.txt', 'test.py')
# 删掉文件
# os.remove('test.py')
# 没有复制文件的函数，需要引入shutil模块，可以看做是os模块的补充


# 过滤文件
# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])
# 要当前目录下列出所有的.py文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# 练习1

# 练习2
def fileName():
    for x in os.listdir('.'):
        if os.path.isdir(x):

            fileName()
        else:
