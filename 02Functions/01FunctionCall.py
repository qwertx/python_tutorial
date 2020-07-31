# -*- coding: utf-8 -*-
# 查看帮助信息
# help(abs)

print(abs(-20))
print(abs(12.34))

print(max(1, 2))
print(max(2, 3, 1, -6))

# 类型转换
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

# 函数名其实是函数对象的引用
a = abs
print(a(-1))

n1 = 255
n2 = 1000
print(str(hex(n1)), str(hex(n2)))
