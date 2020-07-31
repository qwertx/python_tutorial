# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码
# 比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1
# 用错误码来表示是否出错十分不便
def some_function():
    pass

def foo():
    r = some_function()
    if r == -1:
        return -1
    return r

def bar():
    r = foo()
    if r == -1:
        print('Error')
    else:
        pass
# 可以看出一旦出错，需要一级一级上报，直到某个函数可以处理该错误

# 使用try
try:
    print('try...')
    r = 10 / 0
    print('result:', r) # 不会执行
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...') # 一定会被执行
print('END')
# 将除数改为2
try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e: # 不会执行
    print('except:', e)
finally:
    print('finally...') # 一定会被执行
print('END')

# 可以有多个except来捕获不同类型的错误
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# except语句块后面加else，当没有错误发生时执行
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException
# except不但捕获该类型的错误，还包括其所有子类

# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

# 使用try...except捕获错误可以跨越多层调用
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()