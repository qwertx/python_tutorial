import unittest

from mydict import Dict

# 测试类从unittest.TestCase继承
# 以test开头的方法就是测试方法，不以test开头的方法测试的时候不会被执行
# 对每一类测试都需要编写一个test_xxx()方法
# 只需要调用这些方法就可以断言输出是否是我们所期望的

# 最常用的断言就是assertEqual()
# 例：self.assertEqual(abs(-1), 1)
# 或者期待抛出指定类型的Error：
# with self.assertRaises(AttributeError):
#     value = d['empty']
class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a = 1, b = 'test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 访问不存在的Key，断言会抛出KeyError
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        # 通过'.'（属性）访问不存在的Key，期待抛出AttributeError
        with self.assertRaises(AttributeError):
            value = d.empty

    # setUp()和tearDown()会分别在每调用一个测试方法的前后分别被执行
    # 用法举例：如果测试需要启动一个数据库，就可以在setUp()方法中连接数据库，在tearDown()方法中关闭数据库
    # 就不必在每个测试方法中重复相同的代码
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

# 使脚本可以自己运行
# 也可以使用python3 -m unittest mydict_test运行
if __name__ == '__main__':
    unittest.main()