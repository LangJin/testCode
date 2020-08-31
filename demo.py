"""
print("你好，浪晋的测试小讲堂！",end="1111111")
print(2333)
print(2.333)
print(True,False)
print(None)
print(())
print([])
print({})
print("哈哈",2333,"你好")


name = "张三"
print(name)

res = (1+2+4+5*2/(4*2))%3
print(res)

a = input("请输入：")
print("这是我刚刚输入的值：",a)

# 哈哈哈 今天你吃了嘛
# 单行注释的快捷键 ctrl + / 

a = int("2333")
print(type(a))
"""

# a = len("哈哈哈哈哈哈哈哈哈哈哈哈哈")
# print(a)
"""
b = ("刘巧云","欧阳")
a = (1,2,3,4,"哈哈","希希",True,None,b)
# 少写几个变量
# 每个变量都会占用计算机的内存，变量越多，占的内存越多。
# 下标就是计算机自动的给我们的值编的号，是从0开始
print(a[-1][1])
# print(a.index("希希"))
# print(a.count(1))
# 二维元组，三维元组
# 切片  左闭右开
print(a[0:3])
"""
b = ("刘巧云","欧阳","马超")
a = [1,2,3,4,"哈哈","希希",True,None,b]
print(a)


"""
元组和数组的操作方式一模一样
区别是元组不可以修改，数组可以修改
"""
# name = input("青输入你的名字：")
# a.append(name)
# a.insert(3,name)
# print(a)
c = ["今天","明天","后天"]
# a.extend(c)
# a = a + c
d = [2,1,3,4,5,"哈哈","哈哈"]
# d.sort(reverse=True)
# d.reverse()
# d.clear()
print(d)
d.remove("哈哈")
print(d)

