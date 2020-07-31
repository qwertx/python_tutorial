# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# return None 可以简写为 return

# 空函数和pass占位符
def nop():
    pass

age = 20
if age >= 18:
    pass

# 返回多个值

def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 其实返回的是tuple
r = move(100, 100, 60, math.pi / 6)
print(r)

# 练习
def quadratic(a, b, c):
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')
    s = b * b - 4 * a * c
    if s == 0:
        r1 = - b / (2 * a)
        return r1
    elif s < 0:
        return
    else:
        r1 = (-b + math.sqrt(s)) / (2 * a)
        r2 = (-b - math.sqrt(s)) / (2 * a)
        return r1, r2

print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
