# doctest模块可以直接提取注释中的代码并执行测试
# 例：
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)

# 用doctest来测试上次编写的Dict类:
class Dict(dict):
    '''
    Simple dict but also support access by x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a = 1, b = 2, c = '3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

# 练习
def fact(n):
    '''
    Caculates factorial of a positive integer

    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(5)
    120
    >>> fact(17)
    355687428096000
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(2.5)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# 当模块正常导入时，doctest不会被执行。只有在命令行直接运行时，才执行doctest。
# 没有输出说明我们编写的doctest运行都是正确的