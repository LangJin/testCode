"""
分别输入2个数字，计算他们的和
"""
a = float(input("请输入第一个数字："))
b = float(input("请输入第二个数组："))
print("他们的和是：",a + b)

"""
请实现一个计算输入的内容的长度是奇数还是偶数
"""
print("0：表示偶数；1：表示奇数；")
lstr = input("请输入您要计算的内容：")
print(len(lstr)%2)
