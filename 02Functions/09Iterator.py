# 判断Iterable
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器Iterator
from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

# 使用iter()函数将Iterable变为Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))


# 总结
# Iterator对象表示一个数据流
# 可以使用next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误
# 但无法提前知道序列的长度，只能不断通过next()函数计算下一个数据
# 所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算
# Iterator甚至可以表示一个无限大的数据流

# 区别
# 凡是可作用于for循环的对象都是Iterable类型
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列
# list dict str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象
# for循环本质上就是通过不断调用next()函数实现的

# 以下两个表达完全等价
for x in [1, 2, 3, 4, 5]:
    pass

it = iter([1, 2, 3, 4, 5])
while True:
    try:
        x = next(it)
    except StopIteration:
        break