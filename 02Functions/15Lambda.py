print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 其中lambda x: x * x等价于
def f(x):
    return x * x

# 把匿名函数赋值给一个变量
f = lambda x: x * x
print(f)
print(f(5))

# 把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

# 改写上一节最后的例子
def count():
    fs = []
    for i in range(1, 4):
        fs.append(lambda n = i: n * n)
    return fs 

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())