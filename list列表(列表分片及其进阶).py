# Pyhton list 示例
"""
列表分片及其进阶

列表分片只是按照用户所给要求对列表进行拷贝，并不会对原有列表产生修改

"""
# 简单分片
basket = ["鸡蛋","鸭蛋","鹅蛋","张全蛋"]
print(basket)

print("basket[0:2] #lsit分片前两个 也可以写成 basket[:2]")
print("basket[2:3] #lsit分片后两个 也可以写成 basket[2:]")

# 进阶
list1 = [0,1,2,3,4,5,6,7,8,9]
print(list1)

print("list1[0:10:2] #对列表list1 按 每前进两个元素取一个元素出来 进行分片")

print("list1[::-1] #对列表list1 按逆向进行反转 进行分片")
