class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

a = Animal()

# 使用type()函数判断对象类型
print(type(123))
print(type('str'))
print(type(None))

# 如果一个变量指向函数或者类，也可以用type()判断
print(type(abs))
print(type(a))

# if判断
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)
print(type('abc') == type(123))

# 判断一个对象是否是函数
import types
def fn():
    pass

print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 使用isinstance()判断继承关系
class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(d, Dog) and isinstance(d, Animal))
print(isinstance(d, Husky))

# 基本类型也能用isinstance()判断
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# isinstance()还可以判断一个变量是否是某些类型中的一种
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 使用dir()获得一个对象的所有属性和方法
print(dir('ABC'))
# 类似__xxx__的属性和方法在Python中有特殊用途
# 比如调用len()时实际上调用了该对象的__len__()方法
print(len('ABC'))
# 等价于
print('ABC'.__len__())

# 也可以自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))

# 普通的属性或方法
print('ABC'.lower())

# 使用getattr()/setattr()/hasattr()可以直接操作一个对象的状态
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))
print(obj.x)
print(hasattr(obj, 'y'))
setattr(obj, 'y', 19)
print(hasattr(obj, 'y'))
getattr(obj, 'y')
print(obj.y)

# 试图获取不存在的属性，会抛出AttributeError错误
# 传入一个default参数，如果属性不存在，就返回默认值
print(getattr(obj, 'z', 404))
# 也可以获得对象的方法
print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn) # fn指向obj.power
print(fn()) # 调用fn()与调用obj.power()是一样的

# 只有在不知道对象信息的时候，我们才会去获取对象信息
# 可以写 sum = obj.x + obj.y
# 就不要写 sum = getattr(obj, 'x') + getattr(obj, 'y')
# 正确的用法
def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None