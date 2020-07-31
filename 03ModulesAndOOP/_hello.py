#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Michael Liao'

import sys

def test():
    # sys模块的argv变量用list存储了命令行的所有参数
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

# 模块定义的文档注释可以用特殊变量__doc__访问
# 类似_xxx和__xxx的函数或变量是private

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

# 既可以导入到别的模块，另外也可以自己执行
if __name__ == '__main__':
    test()