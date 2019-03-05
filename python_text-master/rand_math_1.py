import random
import math

'''
输入一个三位数与程序随机数比较大小
1如果大于程序随机数，则分别输出这个三位数的个位\十位\百位
2如果等于程序随机数，则提示中奖，记100分
3如果小于程序随机数，则将120个字符输入到文本文件中
    （规则是每一条字符串的长度为12，单独占一行，并且前四个是字母，后8个是数字）
'''

def line():
    # 定义一个空字符串用于拼接字符
    str_num = ''
    # 循环前四个随机字母(用ascii对应的值来随机再转换为字母）
    for i in range(4):
        # 随机小写字母的ascii值
        num = random.randrange(97,123)
        # 将ascii值转换成对应的字母
        str_s = chr(num)
        # 依次拼接得到的随机字母
        str_num = str_num + str_s
        print(str_num)
    # 循环后8个随机数字
    for i in range(8):
        num = random.randrange(0, 10)
        str_num = str_num + str(num)
    # print(str_num)
    return str_num


# 输入函数
num = input("请输入一个三位数： ")
#程序随机数
random_num = random.randrange(100,1000)
# 检测输入是否是纯数字
if num.isdigit() and 100<= int(num) <=999:  #输入函数返回的是字符类型，不能与整形直接比较，需要强制类型转换
    num = int(num)
    random_num = int(random_num)

    # 判断随机数与输入的大小
    if num > random_num:
        # 求百位数字方法是地板除100或用数学模块当中的floor（）函数
        bai = int(num)//100
        print(bai)
        # 求十位数字方法是先把三位数字取100的余数，再地板除10
        shi = num%100//10
        print(shi)
        # 求个位数字方法是直接取10的余
        ge = num%10
        print(ge)
        print('这个三位数的个位是{}十位是{}百位是{}'.format(ge,shi,bai))
        print (random_num)
    if num == random_num:
        print('你中奖了',random_num)
    if num < random_num:
        # 由于120个字符每行12个可知只需存入10行就可以
        for i in range(10):
            str_line = line()
            # print(str_line)
            # 执行文件存入操作
            with open('str_num.txt','a') as f:
                f.write(str_line+'\n')


else:
    print('请按规定输入输入')


