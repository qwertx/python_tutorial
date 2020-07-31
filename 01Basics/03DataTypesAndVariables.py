# 转义字符
print('I\'m ok.')
print('I\'m learning\npython.')
print('\\\n\\')
print('\\\t\\')
# 使用 r' ' 来使内部字符串不转义
print(r'\\\t\\')
# 使用 ''' ''' 表示多行内容
print('''line1
...line2
...line3''')
# 布尔值
print(True and True)
print(True and False)
print(False and False)
print(5 > 3 and 3 > 1)

print(True or True)
print(True or False)
print(False or False)
print(5 > 3 or 1 > 3)

print(not True)
print(not False)
print(not 1 > 2)

age = 20
if age >= 18:
    print('adult')
else:
    print('teenager')

#空值
print(None)

#变量
a = 1
t_007 = 'T007'
Answer = True

#改变变量类型
a = 123
print(a)
a = 'ABC'
print(a)

#变量在内存中的表示
a = 'ABC'
b = a
a = 'XYZ'
print(b)

#常量
PI = 3.14159265359

# 两种除法
print(10 / 3)
print(9 / 3)
print(10 // 3)

#求余
print(10 % 3)

#练习
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
