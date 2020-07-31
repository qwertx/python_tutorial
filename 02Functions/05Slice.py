L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 不包括最后一个索引
print(L[0:3])
print(L[:3])
print(L[1:3])

# 倒数切片
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])

# 复制
L[:]

# tuple切片
(0, 1, 2, 3, 4, 5)[:3]

# 字符串切片
'ABCDEFG'[:3]
'ABCDEFG'[::2]