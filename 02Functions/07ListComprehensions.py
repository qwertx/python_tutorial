# -*- coding: utf-8 -*-

print(list(range(1, 11)))

# 使用循环
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 使用列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下所有文件和目录名
import os
print([d for d in os.listdir('.')])

# 迭代两个及以上变量使用循环
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

# 使用列表生成式
print([k + ' = ' + v for k, v in d.items()])

# 变为小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L2)
