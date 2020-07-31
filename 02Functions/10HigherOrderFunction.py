# 变量可以指向函数
f = abs
print(f)
print(f(-10))

# 函数名也是变量
# abs = 10
# abs(-10)
# 报错

# 一个函数接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))

# 传入函数作为可变参数
from math import sqrt
def test(x, *fs):
    s = [f(x) for f in fs]
    return s

print(test(2, sqrt, abs))