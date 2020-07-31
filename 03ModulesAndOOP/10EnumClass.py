# 一般的常量定义如下，但仍然是变量
JAN = 1
FEB = 2
MAR = 3
# ...
NOV = 11
DEC = 12
# 等等

# 更好的方法是为这样的枚举类型定义一个class类型，每个常量都是class的一个唯一实例
from enum import Enum
# Month类型的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 引用一个常量
Month.Jan
print(Month.Jan.name)
print(Month.Jan.value)
# 枚举它的所有成员
# 注意这里从1开始计数
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
# @unique装饰器可以检查保证没有重复值
from enum import unique

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

# 各种访问方法
day1 = Weekday.Mon
print(day1)
# 用成员名称引用枚举常量
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)

print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
# 直接根据value的值获得枚举常量
print(Weekday(1))
print(day1 == Weekday(1))

# Weekday(7)
# ValueError: 7 is not a valid Weekday

# 遍历
for name, member in Weekday.__members__.items():
    print(name, '=>', member)