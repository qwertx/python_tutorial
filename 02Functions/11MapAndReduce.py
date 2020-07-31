# map(function, Iterable)
# 传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# 使用循环
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

# 将list中的数字转换为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# reduce
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

# 求和可以用内置的sum()
# 将一串数字变为整数
def fn(x, y):
    return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

# 将str转为int
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('13579'))

# 使用lambda简化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(str2int('13579'))

# 练习1
def normalize(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2
def prod(L):
    return reduce(lambda x, y: x * y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 练习3
# str2int()定义在上面
def str2float(s):
    L = s.split('.')
    return str2int(L[0]) + str2int(L[1]) / (10 ** len(L[1]))

print('str2float(\'123.456\') =', str2float('123.456'))