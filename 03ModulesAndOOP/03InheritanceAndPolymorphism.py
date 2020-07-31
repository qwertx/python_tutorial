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

# 子类的run()覆盖了父类的run()
# 即多态
dog = Dog()
dog.run()
cat = Cat()
cat.run()

# 定义class实际上就相当于定义了一种数据类型
a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

# 用isinstance()判断一个变量是否是某个类型
isinstance(a, list)
isinstance(b, Animal)
isinstance(c, Dog)
isinstance(c, Animal)

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())

# 不需要传入Animal类型也能运行
# 例：只要有read()方法，都被视为file-like object，不一定要传入真正的文件对象
class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())