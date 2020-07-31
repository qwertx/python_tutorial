# 生成器一边循环一边计算，不会创建完整的list
# 可以节省空间

# 列表生成式
L = [x * x for x in range(10)]
print(L)

# generator
g = (x * x for x in range(10))
print(g)

# 打印generator(笨方法)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 聪明的方法
g = (x * x for x in range(10))
for n in g:
    print(n)

# 例子
# 输出斐波那契数列前n个数
# 普通函数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        # 等同于
        # t = (b, a + b)
        # a = t[0]
        # b = t[1]
        n = n + 1
    return 'done'
fib(6)

# generator
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 使用
f = fib(6)
print(f)

# 调用next()执行，遇到yield返回，再次执行时从上次返回的yield处继续执行
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
next(o)
next(o)
next(o)

# 使用for循环迭代
for n in fib(6):
    print(n)

# 必须捕获StopIteration错误才能拿到generator的返回值
# 返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 练习
def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i-1] + L[i] for i in range(len(L))][1:] + [1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break