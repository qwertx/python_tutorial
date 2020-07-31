# 在绑定属性时，如果直接把属性暴露出去，会导致属性可以随便更改
# 可以通过set和get方法来限制参数修改
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print(s.get_score())

# 但以上的调用方法略显复杂
# Python内置的@property装饰器可以把一个方法变成属性调用
# 此时变量名一定是 _xxx 类型的
class Student(object):

    # 把一个getter方法变成属性，只需要加上@property就可以
    @property
    def score(self):
        return self._score

    # @property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # 实际上是 s.set_score(60)
print(s.score) # 实际上是 s.get_score()

# 可以定义只读属性，通过只定义getter方法，不定义setter方法
class Student(object):

    # birth是可读写属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # age是只读属性
    @property
    def age(self):
        return 2015 - self._birth

# 练习
class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        self._width = value

    @property
    def height(self):
        return  self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution