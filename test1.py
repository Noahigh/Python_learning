# -*- coding: cp936 -*-

# test
# ����
rule_14 = {'���':['��', '�����', '��Ӿ', '�ڰ�ɫ']}
s = len(rule_14['���'])

# �û����������ʻ�
prompt = "�ü������ݴ�����һ�°� > " #��ʾ����
user_guess = {'guess':[]} #�����û��²⼯
n = 0 #�����ж��Ƿ���Ϲ���
m = 0 #�ж��Ƿ�Ϊ��һ�����룬��ʾ��ͬ����ʾ����
while True:
    if m == 0: #��һ������   
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
            
print(user_guess) #��ӡ�û�����Ĵʵ�
num = len(user_guess['guess'])
print("һ�������ˣ�" + str(num) + "���ʻ㡣")


# �ж��Ƿ������ر����Ķ���
# ���û�����ó��ļ��н���ѭ��

for value in user_guess['guess']: 
    if value in rule_14['���']:
        n += 1
        if n == s:
            print("��������һֻ����~")
#        else:
#            print(n)
#            print("ERROR")
    else:
        print("�����Ĳ���׼ȷӴ~")
