import math
#print(math)
'''
# celi() 向上取整操作
print(math.ceil(5.01))
print(math.ceil(5.9))


#floor() 向下取整操作
print(math.floor(5.01))
print(math.floor(5.9))

# 查看系统保留关键字，不可以用来当做变量的命名
import keyword
print(keyword.kwlist)

# round() 四舍五入操作  python内置函数
print(round(5.01))
print(round(5.5))
print(round(5.9))


# sqrt() 开平方  返回浮点数  
print(math.sqrt(4))


# pow() 与幂运算差不多， 计算一个数的几次方  有两个参数，第一个是底数，第二个是指数
print(math.pow(4, 3))  #4的三次方
#  幂运算  函数返回浮点行， 幂运算返回整型
print(4**3)

# fabs() 对一个数值获取他的绝对值   返回的也是浮点数
print(math.fabs(-1))
print(math.fabs(3))
print(math.fabs(0))

# abs() 获取绝对值操作  不是数学模块当中的，是python内置函数  返回值由本身类型而定
print(abs(-1))
print(abs(-2.5))
print(abs(0))
print(abs(4))

# fsum() 对整个序列求和 返回浮点数
print(math.fsum([1,4,5,5,7]))

# sum() python 内置求和  返回值由本身类型而定
print(sum([1,4,5,5,7]))

# math.modf() 将一个浮点数拆分为整数部分和小数部分组成元祖 (小数在前，整数部分在后)
print(math.modf(4.5))
print(type(math.modf(0)))
print(math.modf(3))
help(math.modf)

# copysign() 将第二个数的符号（正负号）传给第一个数  返回第一个数值的浮点数
print(math.copysign(2,-3))
print(math.copysign(-2,3))

# 打印自然对数e 和π的值
print(math.e)
print(math.pi)
'''
import random
# random() 获取0-1之间的随机小数  包含0不包含1
for i in range(10):
    # print(random.random())
    # 随机指定开始和结束之间的整数值
    # print(random.randint(1,9))
    # random.randrange() 获取指定开始和结束之间的整数值。可以指定间隔值
    #print(random.randrange(1, 9))
    #print(random.randrange(1,9,3))
    #uniform() 随机获取指定范围内的值（包括小数）
    print(random.uniform(1,9))
'''
# choice() 随机获取列表中的值
print(random.choice([1,5,367,86]))
# shuffle() 随机打乱序列 返回值是None
list1 = [1,5,367,86]
print(list1)
print(random.shuffle(list1))
print(list1)
'''

hoho..

