# 正常情况下我们可以给一个class的实例绑定任何属性和方法
class Student(object):
    pass

s = Student()
s.name = 'Michael'
print(s.name)

# 还可以给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25)
print(s.age)

# 但是，给一个实例绑定的方法，对另一个实例不起作用
s2 = Student()
# 调用s2.set_age()得到AttributeError

# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self, score):
    self.score = score
Student.set_score = set_score
# 这样所有实例均可调用
s.set_score(100)
print(s.score)
s2.set_score(99)
print(s2.score)

# 如果想要限制实例的属性，可以定义一个特殊的__slots__变量
class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99 报错AttributeError

# 但__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 9999
print(g.score)