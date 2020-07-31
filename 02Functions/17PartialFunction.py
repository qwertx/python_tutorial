# -*- coding: utf-8 -*-

# 使用int()
print(int('12345'))

# 加上base
print(int('12345', base=8))
print(int('12345', 16))

# 定义新函数
def int2(x, base = 2):
    return int(x, base)

print(int2('1000000'))
print(int2('1010101'))

# 使用functools
import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000', base=10))

# 创建偏函数时可以接收函数对象 *args **kw3个参数
int2('10010')
# 相当于
kw = {'base': 2}
int('10010', **kw)

# 又比如
max2 = functools.partial(max, 10)
max2(5, 6, 7)
# 会把10作为*args的一部分自动加到左边
# 相当于
args = (10, 5, 6, 7)
max(*args)