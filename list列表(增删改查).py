# Pyhton list 示例
"""
包含：
创建列表
增加单个、多个元素
插入元素
获取元素
删除元素
弹出元素

"""
# 创建列表
empty = [] #空列表
number = [0,1,2,3] #数字列表
string = ["老李","小王"] #字符串列表
mix = [1,2,3,[4,5,6],"老王","小李子"]

print(empty)
print(number)
print(string)
print(mix)

# 增加元素
number.append(4) #增加单个元素
mix.extend([7,8,9]) #增加多个元素

print(number)
print(mix)

# 获取元素
print("string列表的第二个元素： " + string[1])


# 删除元素
number.remove(1)
print(number)

del number[1]
print(number)

del string
print("string已被删除")

# "弹出"元素   
'''
其实就是元素出栈
默认弹出最后一个元素
可以添加索引值，弹出指定元素
'''
print(mix)
mix.pop()
print(mix)
mix.pop(4)
print(mix)

