# -*- coding: utf-8 -*-
import functools

# 通过变量调用函数
def now():
    print('2015-3-25')

f = now
print(f)

# 获取函数名字
print(now.__name__)
print(f.__name__)

# 装饰器Decorator:在代码运行期间动态增加功能
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 使用
# 等价于now = log(now)
@log
def now():
    print('2015-3-25')

now()

# decorator本身需要传入参数
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 使用
# 等价于now = log('execute')(now)
@log('execute')
def now():
    print('2015-3-25')

now()

# 经过decorator装饰之后的函数，__name__属性已经改变
# 使用内置的functools.wraps使原始函数的属性复制到wrapper中去
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 练习1
def callLog(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('begin call')
        result = func(*args, **kw)
        print('end call')
        return result
    return wrapper

@callLog
def now():
    print('2015-3-25')

now()

# 练习2
def callLog2(param):
    if isinstance(param, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (param, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator
    else:
        @functools.wraps(param)
        def wrapper(*args, **kw):
            print('call %s():' % param.__name__)
            return param(*args, **kw)
        return wrapper

@callLog2
def f():
    pass

f()

@callLog2('execute')
def f():
    pass

f()