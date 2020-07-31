###################################################################
# 位置参数
def power(x):
    return x * x

print(power(5))

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 3))


###################################################################
# 默认参数
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5))
print(power(5, 3))

# 必选参数必须在前，默认参数在后
# 当函数有多个参数时，把变化大的参数放前面
# 降低了调用参数的难度
def enroll(name, gender):
    print('name:', name)
    print('gender:',gender)

enroll('Sarah', 'F')

def enroll(name, gender, age = 6, city = 'Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Bob', 'M', 7)

# 不按顺序提供参数
enroll('Adam', 'M', city='Tianjin')

# 默认参数必须指向不可变对象
# 默认参数L在定义时就已存在，重复调用会叠加
def add_end(L = []):
    L.append('END')
    return L

print(add_end([1, 2, 3]))
print(add_end())
print(add_end())

# 修改
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())
print(add_end())


###################################################################
# 可变参数
def calc(numbers): # numbers是list或tuple
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc([1, 2, 3]))
print(calc((1, 3, 5, 7)))

# 改写
# *numbers传入tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2, 3))
print(calc())

# 将已有的list或tuple传入
# *nums表示把nums这个list的所有元素作为可变参数传进去
nums = [1, 2, 3]
print(calc(*nums))


###################################################################
# 关键字参数
# 关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city = 'Beijing')
person('Adam', 45, gender = 'M', job = 'Engineer')

# **extra把extra中所有key-value传入到**kw参数
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


###################################################################
# 命名关键字参数
# 检查是否有某种参数
def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

# 限制关键字传入
# *后面为命名关键字参数
# 必须传入参数名
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Jack', 24, city = 'Beijing', job = 'Engineer')

# 如果有可变参数，后面的命名关键字参数就不需要*分隔符
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

# 命名关键字参数可以有默认值
def person(name, age, *, city = 'Beijing', job):
    print(name, age, city, job)

person('Jack', 24, job='Engineer')


###################################################################
# 参数组合
# 对于任意函数，都可以通过(*args, **kw)进行调用

def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c = 0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
f2(1, 2, d = 99, ext = None)

# 或者
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
