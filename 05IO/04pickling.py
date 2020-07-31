# 程序运行时所有的变量都是在内存中
# 把变量从内存中变成可存储或传输的过程称之为序列化
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening
import pickle

d = dict(name = 'Bob', age = 20, score = 88)
# 把任意对象序列化成一个bytes，注意是dumps，有's'
print(pickle.dumps(d))
# pickle.dump()直接把对象序列化后写入一个file-like Object
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 把对象从磁盘读到内存
# pickle.loads()可以反序列化对象
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('dump.txt', 'rb') # 把内容读到一个bytes
d = pickle.load(f)
f.close()
# 这个变量和原来的完全不相干，只是内容相同而已
print(d)

# 跨语言传递：JSON
import json
d = dict(name = 'Bob', age = 20, score = 88)
# 序列化为json格式的str
print(json.dumps(d))
# 反序列化
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
d = json.loads(json_str)
print(d)

# 类的序列化
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# 为Student专门写一个转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
# 将函数传入可选参数default
print(json.dumps(s, default = student2dict))

# 把任意class的实例变为dict
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量
# 定义了__slots__的class除外
print(json.dumps(s, default=lambda obj: obj.__dict__))