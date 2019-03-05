import random
import rand_math_1
print(rand_math_1)


# 定义一个变量用于存取初始分数
source = 0
while 1:
    num = input('输入1,2,3三个数字,输入-1结束：')
    if num == '-1':
        break
    rand_num = random.randrange(1, 4)
    num = int(num)
    rand_num = int(rand_num)
    # if num == -1:
    #     break



    if num>rand_num:
        print('输入的数比随机数大')
    elif num==rand_num:
        source += 100
        print('太棒了，分数为',source)
    elif num<rand_num:
        print('输入的数比随机数小')