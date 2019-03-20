# 定义一个门票系统

# - 门票的原价是100元
# - 当周末的时候门票涨价20%
# - 小孩子半票
# - 计算2个成人和1个小孩的平日票价

class Ticket():
    def __init__(self, weekend=False, child=False):
        self.exp = 100
        if weekend:
            self.inc = 1.2
        else:
            self.inc = 1

        if child:
            self.discount = 0.5
        else:
            self.discount = 1

    def cal_price(self, num):
        return self.exp * self.inc * self.discount * num


adult = Ticket()
child = Ticket(child=True)

print("两个成年人和一个小孩子平日的价格是{}".format(adult.cal_price(2) + child.cal_price(1)))



# 游戏编程: 按下一要求定义一个乌龟类和鱼类并尝试编程

# - 假设游戏场景为范围(x,y)为0<=x<=10,0<=y<=10
# - 游戏生成一只乌龟和10条鱼
# - 他们的移动方向均随机
# - 乌龟的最大移动能力是2(乌龟可以随机选择移动是1还是2), 鱼的最大移动能力是1
# - 当移动到场景边缘,自动向反方向移动
# - 乌龟初始化体力为100(上限)
# - 乌龟每移动一次,体力消耗1
# - 当乌龟和鱼重叠, 乌龟吃掉鱼, 乌龟体力增加20
# - 鱼不计算体力
# - 当乌龟体力值为0或者鱼的数量为0时,游戏结束

import random as r


class Turtle(object):
    def __init__(self):
        self.power = 100

        # 初始化乌龟的位置
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = r.choice([1, 2, -1, -2]) + self.x
        new_y = r.choice([1, 2, -1, -2]) + self.y

        # 判断乌龟的移动是否超超出了边界

        if new_x < 0:
            self.x = 0 - (new_x - 0)  # 相当于取反的过程
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y  # 没有超出边界

        self.power -= 1  # 消耗的体力
        return (self.x, self.y)

    def eat(self):
        self.power += 20
        if self.power >= 100:  # 判断不让体力值超出边界
            self.power = 100


class Fish(object):

    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])

        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x

        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        return (self.x, self.y)


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print("鱼被吃完了,游戏结束")
        break
    if not turtle.power:
        print("乌龟体力耗尽了,游戏结束")
        break

    pos = turtle.move()  # 乌龟移动的具体位置

    # 在迭代器中做列表的删除元素是非常危险的, 经常会出现一些意想不到的问题, 因为迭代器是直接引用列表元素的数据做的操作
    # 所以 我们这里把列表拷贝一份传给迭代器, 然后再对原列表做操作
    for each_fish in fish[:]:  # 用列表的切片,做一些浅拷贝的动作
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print("有一条鱼被吃掉了")



# 定义一个点(point)和直线(Line)类,使用getLen方法获取两点构成直线的长度

import math


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Line(object):
    def __init__(self, p1, p2):
        self.x = p1.get_x() - p2.get_x()
        self.y = p1.get_y() - p2.get_y()

        self.len = math.sqrt(self.x * self.x + self.y * self.y)

    def get_len(self):
        return self.len


p1 = Point(2, 3)
p2 = Point(5, 7)
line = Line(p1, p2)
line.get_len()