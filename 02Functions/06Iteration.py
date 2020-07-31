# 迭代key
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 迭代value
for value in d.values():
    print(value)

# 同时迭代
for k, v in d.items():
    print(k, v)

# 用于字符串
for ch in 'ABC':
    print(ch)

# 判断是否能够迭代
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# 下标循环
# enumerate()将list变为索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# 同时迭代两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)