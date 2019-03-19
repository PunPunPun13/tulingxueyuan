# 编写一个程序,求 100~999 之间的所有水仙花数

# 如果一个3位数等于其各位数字的立方和,则称这个数为水仙花数.例如 153 = 1^3 + 5^3 + 3^3, 因此 153 就是一个水仙花数

for i in range(100, 1000):
    temp = list(str(i))
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)


# 三色球问题

# 有红,黄,蓝三种颜色的球,其中红球3个,黄球3个,蓝球6个.先将这12个球混合放在一个盒子中,从中任意摸出8个球,编程计算摸出球的各种颜色搭配.

for red in range(0, 4):
    for yellow in range(0, 4):
        for blue in range(2, 7):
            if red + yellow + blue == 8:
                print("red:{}".format(red))
                print("yellow:{}".format(yellow))
                print("blue:{}".format(blue))