# Python def ʾ��
"""
Including:
�βκ�ʵ��
�����ĵ�
�ؼ��ֲ���
Ĭ�ϲ���
�ռ�����
"""
# �βκ�ʵ��
def sayyourname(name): #����һ���������ĺ���������� [name] ����һ���β�
    print("Say your name:\n") 
    print(name)

sayyourname("Noah") #���ú���ʱ��Ҫ����ȥһ����������ô����ȥ���Ǹ� [Noah] ����ʵ��

# �����ĵ�
"""
���ã���������ʹ������������˵����
������ʾ��:
"""
def exchangeRate(dollar):
    """
    ��Ԫ�һ������
    �����ݶ�Ϊ7.0
    """
    return dollar * 7.0

exchangeRate(10) #���øú���

exchangeRate.__doc__ #ʹ���������� __doc__ ��ȡ�������ĵ��ַ���

help(exchangeRate) #ʹ�� help() �������鿴�������ĵ�

# �ؼ��ֲ���
def saySomething(name, words): #��������ڶ��޷�׼ȷ����ȷ����λ�õ�����
    print(name + ":\"" + words +"\"")

saySomething("a","b") #��λ����ȷ���ò����������ȷ
saySomething("b","a") #δ��λ����ȷ���ò������������
saySomething(words="b",name="a") #ʹ�ùؼ���ȷ�������������ȷ

# Ĭ�ϲ���
"""
����Ĭ��ֵ�ĺ��������Բ��Ӳ���ֱ��ʹ�ã���ʾ������
"""
def sayHello(words="Hello", people="guys"):
    print(words + " " + people +"!")

sayHello()
sayHello("Hello", "everyone")
sayHello(people="everyone",words="Hi")

# �ռ�����
"""
�������ɱ����
���ã��ڲ�ȷ���������ж��ٸ�
"""
def test(* params): #ֻ�����ռ���������������������
    print("There are %d params" % len(params))
    print(params)
    print("The second param is :", params[1])

test('L', 'O', 'V', 'E', 'U')
test("С����",123,3.14)
test("I","LOVE","U")

def test1(* params, extra = 8): #�Ⱥ����ռ�������Ҳ������������
    print("The params are: ", params)
    print("The addr is: ", extra)

test(1, 2, 3, 4, 5, 6, 7, 8)



