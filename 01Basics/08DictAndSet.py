# dictionary
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 添加数据和赋值
d['Adam'] = 67
d['Jack'] = 90
d['Jack'] = 88

# 判断存在
print('Thomas' in d)
# get()
print(d.get('Thomas'))
# 指定value
print(d.get('Thomas', -1))

# 删除
d.pop('Bob')
print(d)

# list不能作为key, 因为可变

# set 一组key的集合
# 创建
s = set([1, 2, 3])
print(s)

# 重复元素被过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 添加key
s.add(4)
print(s)

# 移除
s.remove(4)
print(s)

# 并集和交集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 可变和不可变
a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
b = a.replace('a', 'A') # 实际上创建了新的字符串
print(a)
print(b)
