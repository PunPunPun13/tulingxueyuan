import rand_math_1
import rand_zimu1


print('请选择游戏\n1.数字游戏\n2.字母游戏')
game = input('输入1或2：')
if game == '1':
    # 实例化对象
    game_num = rand_math_1.GameNum()
    game_num.num_game(0,0)
elif game =='2':
    game_zimu = rand_zimu1.GameZiMu()
    game_zimu.a()
    game_zimu.k()
else:
    print('输入错误')