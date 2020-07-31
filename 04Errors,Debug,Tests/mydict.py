# “测试驱动开发”（TDD：Test-Driven Development）
# 单元测试用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
# 编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问
class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value