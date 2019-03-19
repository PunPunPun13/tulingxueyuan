# append()extend()和insert()

a = [1,2,3,4,5]
a.append([6,7,8])
print(a)

b = [1,2,3,4,5]
b.extend([6,7,8]) # 把元素直接添加到B数组的末尾
print(b)

c = [1,2,3,4,5]
c.insert(3, 10)
print(c)


# 假定给出一个列表 member = ["图灵","的","周老师","是最帅的"]

# 想要把member变成 member = ["图灵",99,"的",88,"周老师",77,"是最帅的",666]应该怎么做?

member = ["图灵","的","周老师","是最帅的"]
member.insert(1, 99)
member.insert(3,88)
member.insert(5, 77)
member.append(666)
print(member)


# 请问如何将下边这个列表的'图灵学院'修改为'周老师'? ls = [1, [1, 2, ['图灵学院']], 3, 5, 8, 13, 18]

ls = [1, [1, 2, ['图灵学院']], 3, 5, 8, 13, 18]

ls [1][2][0] = 'Miss周'  # 对列表具体位置直接赋值覆盖
print(ls)


# 将列表推导式还原出来

# ls = [(x, y) for x in range(10) for y in range(10) if x%2 ==0 if y%2!=0]

ls = [(x, y) for x in range(10) for y in range(10) if x%2 ==0 if y%2!=0]
print(ls)


ls = []
for x in range(10):
    for y in range(10):
        if x%2 == 0 and y%2 !=0:
            ls.append((x,y))
print(ls)