# 这行代码是什么意思?
# if not(money < 100)

money >= 100


# 假设有 x = 1 , y = 2, z = 3,如何快速将三个变量的值相互交换?

x = 1
y = 2
z = 3

# print(x)
# print(y)
# print(z)

x,y,z = z,x,y # 把等号右边的值,赋值给左边

print(x)
print(y)
print(z)


# 成员资格运算符'in'的用法

ls = range(100)

if not 100 in ls:
    print(True)
else:
    print(False)


# range()函数

ls = range(0, 10, 2)
for i in ls:
    print (i)


# 下面的循环会打印多少次"Tuling"

for i in range(0, 10, 2):
    print("Tuling")


# 目测一下程序会打印什么?

while True:
    while True:
        break
        print(1)
    print(2)
    break
print(3)


# 从代码效率的方面考虑,一下代码有什么问题,如何改进?
    i = 0
    string = "ILoveTuling"
    while i < len(string):
        print (i)
        i += 1

i = 0
string = "ILoveTuling"
while i < len(string):
    print (i)
    i += 1

i = 0
string = 'ILoveTuling'
leng = len(string)
while i < leng:  # 减少了重复计算 string 的长度
    print (i)
    i += 1


# 设计一个验证用户密码的程序,
# 用户只有三次机会输入错误,
# 不过如果用户输入的内容包括 " * "则不计算在内

password = "abc012"

times = 3
while times:
    input_password = input("请输入密码")

    if '*' in input_password:
        print("密码中不能包含*号")
    else:
        if input_password == password:
            print("密码正确")
            break
        else:
            print("密码错误")
            times -= 1

password = "abc012"
times = 3
while times:
    input_password = input("请输入用户密码")
    if '*' in input_password:
        print("密码中不能含有*号")
    elif input_password == password:
        print("密码正确")
        break
    else:
        print("密码错误")
        times -= 1