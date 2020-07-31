# 面向过程
std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}
def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

# 面向对象
# 类的方法和普通函数一样，可以传入默认参数、可变参数、关键字参数和命名关键字参数
# 实例的变量名如果以__开头，就变成伪private
# Python解释器对外把__name变量改成了_Student__name，其实仍然可以访问
# 不同版本的Python解释器可能会把__name改成不同的变量名，所以不要这样做
# 但是__xxx__是特殊变量，可以直接访问
# 以单下划线开头的实例变量名，外部可以访问，但最好视为private，不要从外部修改
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
print(bart.get_grade())
lisa.print_score()

# Python允许对实例变量绑定任何数据
bart.age = 9
print(bart.age)

# 这里设置的__name变量和class内部的__name变量不是一个变量
# 内部的__name变量已经被Python解释器自动改成了_Student__name
bart.__name = 'New Name'
print(bart.__name)
print(bart.get_name())