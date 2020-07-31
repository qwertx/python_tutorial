# __slots__ 和 __len__ 前面已经学过了
# 现在来学一些其他具有特殊用途的函数，可以帮助我们定制类

# 01---------------------------------------------------------------
# __str__定义打印出来的字符串
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))

# __str__定义
def __str__(self):
    return 'Student object (name: %s)' % self.name
# 绑定到class
Student.__str__ = __str__
print(Student('Michael'))

# 在交互窗口不用print而直接写变量名时调用了__repr__()
# 区别是__str__()返回用户看到的字符串
# 而__repr__()返回程序开发者看到的字符串，是为调试服务的

# 将__repr__定义为与__str__一样
Student.__repr__ = __str__


# 02---------------------------------------------------------------
# __iter__()方法用于实现for循环，该方法返回一个迭代对象
# for循环会不断调用该迭代对象的__next__方法，直到遇见StopIteration错误
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration
        return self.a

# 用法
for n in Fib():
    print(n)


# 03---------------------------------------------------------------
# __getitem__()方法用来使对象像list一样通过下标访问

# 如果把对象看成dict，__getitem__的参数也可能是类似key的object，例如str
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。
# 最后，还有一个__delitem__()方法，用于删除某个元素

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        # 实现不完整的一个切片
        # 没有处理负数和步长
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib()
# 测试索引
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[10])
print(f[100])
# 测试切片
print(f[0:5])
print(f[:10])


# 04---------------------------------------------------------------
# __getattr__()方法用来动态返回一个属性
# 当调用不存在的属性时，Python解释器会试图调用__getattr__来尝试获得属性

# 但只有在没有找到属性的情况下，才调用__getattr__
# 已有的属性，比如name，不会在__getattr__中查找
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        # 返回函数也是完全可以的
        if attr == 'age':
            return lambda: 25
        # 如果不写这一句，尝试获得其他属性会一律返回None
        # 比如 s.abc
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()
print(s.name)
print(s.score)
print(s.age()) # 注意调用的区别

# 作用：调用REST API
# 类似 http://api.server/user/friends
# 或 http://api.server/user/timeline/list
# 可以利用完全动态的__getattr__写一个链式调用
class Chain(object):

    def __init__(self, path = ''):
        self.path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self.path, path))

    def __str__(self):
        return self.path

    __repr__ = __str__

# 调用
print(Chain().status.user.timeline.list)

# 如果类似于 GET /users/:user/repos 可以返回一个匿名函数传递用户名
class Chain(object):

    def __init__(self, path = ''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return lambda x: Chain('%s/%s/:%s' % (self._path, path, x))
        else:
            return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().users('michael').repos)

# 05---------------------------------------------------------------
# __call__()方法直接对实例进行调用
# __call__()还可以定义参数，其实函数和对象没有本质的区别
# 如果把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，和类的实例一样
# 这样就模糊了对象和函数的界限
# 一般不需要严格区分一个变量是对象还是函数，但需要判断一个对象是否能被调用
# 能被调用的对象就是一个Callable对象

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

# 调用
s = Student('Michael')
s()