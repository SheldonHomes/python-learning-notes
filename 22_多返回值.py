"""
如果一个函数有多个返回值，那么在调用这个函数时，使用多个变量来接收返回值

例如：
def 函数名(参数列表):
    return 返回值1,返回值2,返回值3

调用：
变量1,变量2,变量3 = 函数名(参数列表)

return支持返回不同类型的值，但是返回的多个值会被封装成一个元组

"""

def test():
    return 1, 2, 3

# 用多个值接收返回值
a, b, c = test()
print(a, b, c)

# 用一个值接收返回值
d = test()
print(d) # (1, 2, 3)