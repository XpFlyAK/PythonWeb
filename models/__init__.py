# -*- coding: UTF-8 -*-
# -*- coding: UTF-8 -*-
import json

"""
    本函数把一个 dict 或者 list 写入文件
    data 是 dict 或者 list
    path 是保存文件的路径
    """


# json 是一个序列化/反序列化(上课会讲这两个名词) list/dict 的库
# indent 是缩进
# ensure_ascii=False 用于保存中文
def save(data, path):
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as r:
        r.write(s)


"""
 本函数从一个文件中载入数据并转化为 dict 或者 list
 path 是保存文件的路径
 """


def load(path):
    with open(path, 'r', encoding='utf-8') as r:
        j = json.loads(r.read())
        return j


# Model 是用于存储数据的基类
class Model(object):
    # @classmethod 说明这是一个 类方法
    # 类方法的调用方式是  类名.类方法()
    @classmethod
    # classmethod 有一个参数是 class
    # 所以我们可以得到 class 的名字
    def db_path(cls):
        name = cls.__name__
        path = '{}/{}.txt'.format('db', name)
        return path

    @classmethod
    def new(cls, form):
        m = cls(form)
        return m

    @classmethod
    def all(cls):
        path = cls.db_path()
        model = load(path)
        object_array = [cls.new(m) for m in model]
        return object_array

    """
     save 函数用于把一个 Model 的实例保存到文件中
     """

    def save(self):
        object_array = self.all()
        object_array.append(self)
        path = self.db_path()
        # __dict__ 是包含了对象所有属性和值的字典
        data = [x.__dict__ for x in object_array]
        save(data, path)

        """
       这是一个 魔法函数
       不明白就看书或者 搜
       当你调用 str(o) 的时候
       实际上调用了 o.__str__()
       当没有 __str__ 的时候
       就调用 __repr__
       """

    def __repr__(self):
        class_name = self.__class__.__name__
        object_arrray = ['{}:({})'.format(k, v) for k, v in self.__dict__.items()]
        string = '\n'.join(object_arrray)
        return '<{} \n:\n {}>'.format(class_name, string)
