# 示例练习 1 增强版 增加随机数
"""--- 第一个小游戏 （增强版）---"""
import random

secret = random.randint(1,10)
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
while guess != secret:
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print("你是小甲鱼肚子里面的蛔虫吗？！")
        print("哼(￢︿̫̿￢☆)，猜中了也没奖励！")
    else:
        if guess > secret:
            print("哥，大了大了(￢︿̫̿￢☆)")
        else:
            print("嘿，小了小了(￢︿̫̿￢☆)")
print("游戏结束，不玩啦(●'◡'●)")        
