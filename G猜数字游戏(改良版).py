# 示例练习 1 改良版 增加判断
"""--- 第一个小游戏 ---"""
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)
if guess == 8:
    print("你是小甲鱼肚子里面的蛔虫吗？！")
    print("哼(￢︿̫̿￢☆)，猜中了也没奖励！")
else:
    if guess > 8:
        print("哥，大了大了(￢︿̫̿￢☆)")
    else:
        print("嘿，小了小了(￢︿̫̿￢☆)")
