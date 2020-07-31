# 方法1： print()
# 缺点：最后要删掉

def foo(s):
    n = int(s)
    print('>>>n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()

# 方法2： assert()
# 断言表达式为True，否则抛出AssertionError
# 使用-O跳过assert，例：
# python3 -O err.py
# pycharm中写在Run - Edit Configurations - Interpreter options

def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

main()

# 方法3： logging()
# logging不会抛出错误，而且可以输出到文件
# logging.info()就可以输出一段文本
# 信息的级别有debug，info，warning，error
# 当level=INFO时，logging.debug就不起作用了，这样可以放心地输出不同级别的信息
# logging的另一个好处是一条语句可以同时输出到不同的地方，比如console和文件
import logging

logging.basicConfig(level = logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# 方法4： pdb
# 启动：python3 -m pdb err.py
# err.py
# 使用'l'(L)查看代码
# 'n'单步执行
# 'p 变量名'查看变量
# 'q'结束调试
s = '0'
n = int(s)
print(10 / n)


# 方法5： pdb.set_trace()
# 使用pdb.set_trace()设置一个断点
# 序会自动在pdb.set_trace()暂停并进入pdb调试环境
# 可以用'p'查看变量，'c'继续运行
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 行到这里会自动暂停
print(10 / n)

# 方法6： 使用IDE