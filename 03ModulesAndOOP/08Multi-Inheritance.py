class Animal(object):
    pass

# 大类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class CarnivorousMixIn(object):
    pass

class HerbivoresMixIn(object):
    pass

# 各种动物多重继承
# 这种设计通常称之为MixIn
# 为了更好地看出继承关系，通常在名字后面加上MixIn
class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

class Bat(Mammal, FlyableMixIn, CarnivorousMixIn):
    pass

class Parrot(Bird, FlyableMixIn, HerbivoresMixIn):
    pass

class Ostrich(Bird, RunnableMixIn, HerbivoresMixIn):
    pass


# 应用举例
# Python自带了TCPServer和UDPServer这两类网络服务
# 而要同时服务多个用户就必须使用多进程或多线程模型
# 这两种模型由ForkingMixIn和ThreadingMixIn提供
# 通过组合，我们就可以创造出合适的服务来

# 例如一个多进程模式的TCP服务定义如下
class MyTCPServer(TCPServer, ForkingMixIn):
    pass
# 一个多线程模式的UDP服务定义如下
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
# 一个更先进的协程模型则可以通过一个CoroutineMixIn实现
class MyTCPServer(TCPServer, CoroutineMixIn):
    pass