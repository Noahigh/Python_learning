# Pyhton list ʾ��
"""
������
�����б�
���ӵ��������Ԫ��
����Ԫ��
��ȡԪ��
ɾ��Ԫ��
����Ԫ��

"""
# �����б�
empty = [] #���б�
number = [0,1,2,3] #�����б�
string = ["����","С��"] #�ַ����б�
mix = [1,2,3,[4,5,6],"����","С����"]

print(empty)
print(number)
print(string)
print(mix)

# ����Ԫ��
number.append(4) #���ӵ���Ԫ��
mix.extend([7,8,9]) #���Ӷ��Ԫ��

print(number)
print(mix)

# ��ȡԪ��
print("string�б�ĵڶ���Ԫ�أ� " + string[1])


# ɾ��Ԫ��
number.remove(1)
print(number)

del number[1]
print(number)

del string
print("string�ѱ�ɾ��")

# "����"Ԫ��   
'''
��ʵ����Ԫ�س�ջ
Ĭ�ϵ������һ��Ԫ��
�����������ֵ������ָ��Ԫ��
'''
print(mix)
mix.pop()
print(mix)
mix.pop(4)
print(mix)

