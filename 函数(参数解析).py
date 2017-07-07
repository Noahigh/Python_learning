# Python def 示例
"""
Including:
形参和实参
函数文档
关键字参数
默认参数
收集参数
"""
# 形参和实参
def sayyourname(name): #定义一个带参数的函数，里面的 [name] 就是一个形参
    print("Say your name:\n") 
    print(name)

sayyourname("Noah") #调用函数时需要传进去一个参数，那么传进去的那个 [Noah] 就是实参

# 函数文档
"""
作用：方便其他使用这个函数的人的理解
以下是示例:
"""
def exchangeRate(dollar):
    """
    美元兑换人民币
    汇率暂定为7.0
    """
    return dollar * 7.0

exchangeRate(10) #调用该函数

exchangeRate.__doc__ #使用特殊属性 __doc__ 获取函数的文档字符串

help(exchangeRate) #使用 help() 函数来查看函数多文档

# 关键字参数
def saySomething(name, words): #解决参数众多无法准确无误确认其位置的问题
    print(name + ":\"" + words +"\"")

saySomething("a","b") #按位置正确放置参数，输出正确
saySomething("b","a") #未按位置正确放置参数，输出有误
saySomething(words="b",name="a") #使用关键字确定参数，输出正确

# 默认参数
"""
带有默认值的函数，可以不加参数直接使用，起到示例作用
"""
def sayHello(words="Hello", people="guys"):
    print(words + " " + people +"!")

sayHello()
sayHello("Hello", "everyone")
sayHello(people="everyone",words="Hi")

# 收集参数
"""
又名：可变参数
作用：在不确定函数里有多少个
"""
def test(* params): #只含有收集参数，不含有其他参数
    print("There are %d params" % len(params))
    print(params)
    print("The second param is :", params[1])

test('L', 'O', 'V', 'E', 'U')
test("小甲鱼",123,3.14)
test("I","LOVE","U")

def test1(* params, extra = 8): #既含有收集参数，也含有其他参数
    print("The params are: ", params)
    print("The addr is: ", extra)

test(1, 2, 3, 4, 5, 6, 7, 8)



