# -*- coding: utf-8 -*-

age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 如果某个判断为True 会忽略剩下的语句
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

x = 3
if x: # if x is not 0 or '' or []
    print('True')

# 强制类型转换
s = input('birth: ') # input默认返回str
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

# 练习
height = 1.75
weight = 80.5
bmi = weight / (height * height)
if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')