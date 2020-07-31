# raise语句如果不带参数，就会把当前错误原样抛出
def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

# 理解：
# 第4行，判断 n == 0 时，抛出了ValueError被bar()中的except捕获
# 所以先打印出12行的信息
# 13行的raise将ValueError再次抛出，被解释器捕获，打印出错误信息
# 也就是第5行的内容

# 还可以把一种类型的错误转化成另一种类型
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')