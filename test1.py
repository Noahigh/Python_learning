# -*- coding: cp936 -*-

# test
# 规则集
rule_14 = {'企鹅':['鸟', '不会飞', '游泳', '黑白色']}
s = len(rule_14['企鹅'])

# 用户输入描述词汇
prompt = "用几个形容词描述一下吧 > " #提示内容
user_guess = {'guess':[]} #建立用户猜测集
n = 0 #计数判断是否符合规则集
m = 0 #判断是否为第一次输入，显示不同的提示内容
while True:
    if m == 0: #第一次输入   
        lamble = input(prompt)
        if lamble == 'stop':
            break
        else:
            user_guess['guess'].append(lamble)
            m = 1
    else:
        lamble = input(">")
        if lamble == 'stop':
            break
        else:
            user_guess['guess'].append(lamble)
            
print(user_guess) #打印用户输入的词典
num = len(user_guess['guess'])
print("一共输入了：" + str(num) + "个词汇。")


# 判断是否存在相关表述的动物
# 在用户输入得出的集中进行循环

for value in user_guess['guess']: 
    if value in rule_14['企鹅']:
        n += 1
        if n == s:
            print("描述的是一只企鹅吧~")
#        else:
#            print(n)
#            print("ERROR")
    else:
        print("描述的不够准确哟~")
