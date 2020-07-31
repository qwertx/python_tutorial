# 仅在Linux/OSX下有效 是一个python可执行程序
#!/usr/bin/env python3

# 按utf-8编码读取代码 同时要保证文本编辑器正在使用utf-8 without BOM编码
# -*- coding: utf-8 -*-

# 关于编码：
# unicode 使用2个字节 ASCII码字符在前面补0即可
# UTF-8使用1-6个字节以节省空间 汉字通常是3个字节
# ASCII码可以看成UTF-8的一部分
# 在计算机内存中统一使用unicode 保存到硬盘或传输时使用utf-8
# 例子：
# 服务器unicode --- 输出utf-8网页 --- 浏览器
# 文件utf-8 --- 读取转为unicode --- 记事本 --- 保存转为utf-8 --- 文件

# 在python 3中，字符串以unicode编码，可以支持多语言
print('包含中文的str')

# 字符转编码
print(ord('A'))
print(ord('中'))

# 编码转字符
print(chr(66))
print(chr(25991))

# 16进制表示
print('\u4e2d\u6587')

# 将str类型(以unicode表示，一个字符对应若干字节)变为以字节为单位的bytes类型数据
# 才能在网络中传输或者保存到硬盘上
print(b'ABC')

# 编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# '中文'.encode('ascii') #报错

# bytes变为str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 计算str字符长度
print(len('ABC'))
print(len('中文'))

# 计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Micheal', 1000000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s永远会起作用
print('Age: %s. Gender: %s' % (25, True))

# %% 转义
print('growth rate: %d %%' % 7)

# 练习
s1 = 72
s2 = 85
r = (s2 - s1) / s1 * 100
print("%.1f%%" % r)
