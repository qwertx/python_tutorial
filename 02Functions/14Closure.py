# 普通的求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 返回求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 调用
f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

# 每次调用都会返回一个新的函数
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)

# 返回的函数并没有立刻执行，而是直到调用了f()才执行
# 3个函数都返回时，变量i已经变成了3，因此最终结果都为9
# 因此使用闭包时，返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 一定要引用循环变量的话就再创建一个函数，用该函数的参数绑定循环变量当前的值
# 这样无论该循环变量后续如何更改，已绑定到函数参数的值不变
def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs 

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())