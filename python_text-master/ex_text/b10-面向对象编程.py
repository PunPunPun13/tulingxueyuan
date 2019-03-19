# 定义一个学生类,有下面的类属性
#     1.姓名
#     2.年龄
#     3.成绩(语文,数学,英语)每课成绩类型为整数 类方法
#     4.获取学生的姓名: get_name()返回类型: str
#     5.获取学生的年纪: get_age()返回类型: int
#     6.返回3门科目中最高的分数, get_course()返回类型: int

class Student(object):
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_scores(self):
        return max(self.scores)


zz = Student("周周", 18, [80, 100, 90])
print(zz.get_name())
print(zz.get_age())
print(zz.get_scores())
# print(min(100,299,499,500))


# 定义一个字典类: DictClass, 完成如下功能

    # 1.删除某个key del_dict(key)
    # 2.判断某个键是否在字典里,如果返回键对应的值, 不在则返回'not found' get_dict()
    # 3.返回键组成的列表,返回类型: list get_key()
    # 4.合并字典, 并且返回合并后字典的values组成的列表, 返回类型list update_dict()

class DictClass(object):

    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        # 判断 key是否在字典里?
        if key not in self.dict.keys():
            return "key不在字典里"
        else:
            self.dict.pop(key)
            return "删除成功"

    def get_dict(self, key):
        if key not in self.dict.keys():
            return "not found"
        else:
            return self.dict[key]

    def get_key(self):
        return self.dict.keys()

    def update_dict(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict.values()


d = DictClass({"a": 1, "b": 2})
print(d.update_dict({"c": 3}))


# 定义一个列表的操作类 ListInfo 包括的方法

# 1.列表元素添加:add_key()  添加的必须是数字或者字符串
# 2.列表元素取值:get_key()
# 3.列表合并:update_list(list)
# 4.删除并且返回最后一个元素:del_key()

class ListInfo(object):

    def __init__(self, list_val):
        self.list = list_val

    def add_key(self, key_name):
        # 添加的key必须是字符串或者是数字
        if isinstance(key_name, (str, int)):
            self.list.append(key_name)
            print(self.list)
            return "Ok"
        else:
            return "我要字符串或者数字"

    def get_key(self, index):
        # 判断传入的索引是否超出了列表
        if index >= 0 and index < len(self.list):
            return self.list[index]
        return "你输入的太多了,想太多了"

    def update_list(self, new_list):
        self.list.extend(new_list)  # 先让对象new_list合并一下
        return self.list  # 重新执行list, return完整的列表

    def del_key(self):
        # 首先要判断我们的列表里面是否还有元素
        if len(self.list) >= 0:
            return self.list.pop(-1)  # 弹出最后一个元素
        else:
            return "列表是空的"


list_info = ListInfo([1, 2, 3, 4, 5])

print(list_info.add_key([1, 4, 5, 6]))
# print(list_info.get_key(3))
# print(list_info.update_list([8,9,10]))
# print(list_info.del_key())



# 定义一个集合的操作类

# 包括的方法

# 1.集合元素添加: add_setinfo()
# 2.集合的交集: get_intersection()
# 3.集合的并集: get_union()
# 4.集合的差集: del_difference()

class SecInfo(object):
    def __init__(self, my_set):
        self.sett = my_set

    def add_setinfo(self, keyname):
        self.sett.add(keyname)
        return self.sett

    def get_intersection(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett & unioninfo
        else:
            return "你传入的不是set"

    def get_union(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett | unioninfo
        return "你传入的不是set"

    def del_difference(self, unioninfo):
        if isinstance(unioninfo, set):
            return self.sett - unioninfo
        return "你传入的不是set"


A = set([1, 2, 3, 4, 5])
B = set([5, 6, 3])
my_set = SecInfo((A))
# print(my_set.add_setinfo(6))
# print(my_set.get_union(B))
# print(my_set.del_difference(B))
print(my_set.del_difference("123"))