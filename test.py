#for循环 + 内嵌if判断
"""--- 快速输出10以内素数 ---"""

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
    i += 2 #当判断出来第一个基数时，直接进行加2，减少系统资源开销
print(i) #输出i最后的值
