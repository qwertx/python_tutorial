# -*- coding: utf-8 -*-

# list
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# index
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])

# append
classmates.append('Adam')
print(classmates)

# 指定位置
classmates.insert(1, 'Jack')
print(classmates)

# pop
classmates.pop()
print(classmates)
# 指定位置
classmates.pop(1)
print(classmates)

# 替换
classmates[1] = 'Sarah'
print(classmates)

# 不同的数据类型
L = ['Apple', 123, True]
print(L)

# 嵌套
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

# 或者
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][1])

# 空
L = []
print(len(L))

# tuple 不可变 所以更加安全
classmates = ('Michael', 'Bob', 'Tracy')
t = (1, 2)
t = ()

# 单元素必须加','
t = (1) # 数字
t = (1, ) # tuple

# "可变"的tuple
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])
