# 因为错误是class，捕获一个错误就是捕获到该class的一个实例
# 所以我们自己编写的函数也可以抛出错误
# 尽量使用Python内置的错误类型

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')