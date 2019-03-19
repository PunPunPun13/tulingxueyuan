# 写一个程序来管理用于登录系统的用户信息: 登陆名字和密码.登陆用户账号建立后,已存在用户

# 可以用登陆名字和密码重返系统,新用户不能用别人的用户名建立用户账号

# 模拟从数据库里取出来的用户名和密码
user_pass = {"laotie": "password", "huniu": "adminf"}


def create_user(username, password):
    """
    username: 用户建立账号的用户名
    password: 用户建立账号的密码
    """

    # 判断 用户输入的账号是不是已经存在
    usernames = user_pass.keys()

    if username in usernames:
        print("这个用户已经被注册了")
    else:
        # 没有被注册, 那么更新我们的user_pass
        # 实际情况是会做持久化存储到数据库中

        user_pass[username] = password
        print("恭喜你,你已经很荣幸的成为了我们的会员")


# create_user("goudan","888")
# print(user_pass)

def login_user(username, password):
    # 首先要判断登陆的用户名是否存在

    usernames = user_pass.keys()
    if username not in usernames:
        print("扯犊子呢,你丫根本不是我们的会员")
    elif password != user_pass[username]:
        # 判断用户的密码是否正确
        print("你个蠢货,连密码你都记不住")
    else:
        print("恭喜你,登陆成功")


login_user("laotie", "password")