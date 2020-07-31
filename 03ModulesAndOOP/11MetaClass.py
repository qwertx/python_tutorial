# -----------------------------------------------------------------------------------------------
# 1.通过type()创建类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的
# 例
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello, %s.' % name)

# 测试
h = Hello()
h.hello()
# type()函数可以查看一个类型或变量的类型
# Hello是一个class，它的类型就是type
print(type(Hello))
# h是一个实例，它的类型是class Hello
print(type(h))

# class的定义是运行时动态创建的，创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型
# 比如通过type()函数创建出Hello类
def fn(self, name = 'world'):
    print('Hello, %s' % name)

# type()函数依次传入3个参数
# 1.class的名称
# 2.继承的父类集合，如果只有一个父类，别忘了tuple的单元素写法
# 3.class的方法名称与函数绑定
Hello = type('Hello', (object,), dict(hello = fn))
# 测试，和上面完全一样
h = Hello()
h.hello()
print(type(Hello))
print(type(h))
# type()函数创建的类和直接写class完全一样，因为python解释器也是这样创建的
# 动态语言本身支持运行期间动态创建类


# -----------------------------------------------------------------------------------------------
# 2.要控制类的创建行为，可以使用metaclass
# 即先定义metaclass，就可以创建类，最后创建实例

# metaclass是类的模板，所以必须从'type'类型派生
# metaclass的类名按惯例总是以Metaclass结尾

# 这个metaclass给我们自定义的MyList增加一个add方法
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

# 传入关键字参数metaclass会指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象
# 2.类的名字
# 3.类继承的父类集合
# 4.类的方法集合
class MyList(list, metaclass=ListMetaclass):
    pass

# 测试
L = MyList()
L.add(1)
print(L)



# -----------------------------------------------------------------------------------------------
# 一般情况下不需要通过metaclass修改
# 但 ORM-Object Relational Mapping 即对象-关系映射需要
# 把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样不用直接操作SQL语句
# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来

# 父类Model和属性类型StringField、IntegerField是由ORM框架提供的
# 剩下的魔术方法比如save()全部由metaclass自动完成

# 比如现在想定义一个User类来操作对应的数据库表User
# 先写出调用接口（在最下面）
# 按接口来实现该ORM

# Field类负责保存数据库表的字段名和字段类型
class Field(object):

    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):

    def __init__(self, name):
        # 调用Field.__init__()
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):

    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    # 在创建Model类及子类时，调用ModelMetaclass.__new__()创建类
    # 注意是创建类的时候调用，和实例无关
    def __new__(cls, name, bases, attrs):
        # 排除掉对Model类的修改
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        # 在当前类（比如User）中查找定义的类的所有属性
        # 如果找到一个Field属性，就把它保存到一个__mappings__的dict中
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                # v是属于Field类的，因此v遇到print会自动调用Field.__str__()
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 从类属性中删除该Field属性，否则，容易造成运行时错误
        # 实例的属性会遮盖类的同名属性
        # 实例即 {'password': 'my-pwd', 'email': 'test@orm.org', 'name': 'Michael', 'id': 12345}
        # 可以看出也含有同名属性，只是不指向field对象而是指向实际数据类型（str,int等）
        for k in mappings.keys():
            attrs.pop(k)
        # 保存属性和列的映射关系
        # 相当于将这些类属性外面加了一层，以区分实例属性
        attrs['__mappings__'] = mappings
        # 假设表名和类名一致
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    # 这个函数在下面的测试中貌似并未用到
    # 应该是为了将来方便修改数据
    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        # self.__mappings__为一个字典，每个属性对应着Field object
        for k, v in self.__mappings__.items():
            # 这里使用的是User类的属性，在创建类的时候调用了元类
            # 一直保持在self.__mappings__中
            fields.append(v.name) # fieldObject.name
            params.append('?')
            # 这里调用的是u这个对象的属性，User u 本质上是一个字典
            # 即 {'password': 'my-pwd', 'email': 'test@orm.org', 'name': 'Michael', 'id': 12345}
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 接口
class User(Model):
    # 定义类的属性到列的映射：
    # 这些属性创建类的时候就已经存在，和实例无关
    # 每个属性是一个Field对象
    id = IntegerField('id') # 用IntegerField初始化User类的属性
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass
# 如果没有找到，就继续在父类Model中查找metaclass
# 找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类
# 也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到

# Model类中实现了save()方法，把一个实例保存到数据库中
# 因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句

# 测试

# 注意User括号中传入的一大堆东西和User类在元类中创建的'__mappings__'中的属性毫无关系
# 只是key相同而已（为了方便调用）
# 括号中的数据只在实例化的时候使用，是实例的属性而不是类的属性
u = User(id = 12345, name = 'Michael', email = 'test@orm.org', password = 'my-pwd')
u.save()

# 个人理解：
# User类创建：生成类属性，每个属性对应一个Field对象
# 调用ModelMetaclass中的 __new__方法，在类的属性中记录了表名'__table__'和表格的列项目'__mappings__'
# '__mappings__'的内容就是类似id: FieldObject(name属性为id)这样的映射
# 类创建完成后，创建实例对象，调用Model的__init__()，其实是字典的__init__()，将括号中的参数传入，生成一个字典
# 也就是说，u这个User类对象内容和字典完全一样
# 即 {'password': 'my-pwd', 'email': 'test@orm.org', 'name': 'Michael', 'id': 12345}
# 只是内部类属性不同，多了像self.__table__，self.__mappings__等属性，以及save()等方法
# 而args.append(getattr(self, k, None))调用的是u[key]，也就是实例的属性，而不是类的属性

# 这样一个类为一张表，一个对象相当于一条数据
# 数据表格的每一列的项目内容，标题，都固定在类属性中，每次只要填写不同的数据即可