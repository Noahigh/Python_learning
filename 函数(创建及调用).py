# Python def 示例
"""
包含：
创建和调用函数
函数的参数
函数的返回值

"""
# 创建函数
def myFirstFunction(): #定义函数名 以下为函数功能
    print("This is my first function!")
    print("I'm so happy!")
    print("Thanks for everything!")

# 调用函数
print("-This is the first to use 'myFirstFunction():'\n")
myFirstFunction()
print("\n")

# 多次调用函数
print("-Use the function three times here:\n")
for i in range(3): #在这里我们调用三次 myFirstFunction() 函数
    myFirstFunction()
print("\n")

# 函数的参数
def mySecondFunction(name): #定义一个带单个参数的函数
    print(name + "是帅锅！\n哈哈哈")

def add(num1, num2): #定义一个带两个参数的函数
    print(num1 + num2)
    
# 函数的返回值
def summary(num3, num4): #定义一个带返回值的函数
    return num3 + num4 #return 返回一个有效的值☞
