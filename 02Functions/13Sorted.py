print(sorted([36, 5, -12, 9, -21]))
# 接收key函数
print(sorted([36, 5, -12, 9, -21], key = abs))
# 按ascii码顺序
print(sorted(['bob', 'about', 'Zoo', 'Credit'])) 
# 忽略大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))
# 反向排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))

# 练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
    return t[1]
L2 = sorted(L, key = by_name)
L3 = sorted(L, key = by_score, reverse = True)
print(L2)
print(L3)
