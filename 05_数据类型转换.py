"""
数据类型的转换：在特定条件下，数据类型之间是可以强制转换的,用法如下：

 强制转换为整型         int(x)
 强制转换为浮点型       float(x)
 强制转换为字符串       str(x)

 注：强制转换的语句都是带有返回值的
"""

# 1.数字转字符串
name_type = str(65)
print(type(name_type), name_type)

# 2.字符串转数字
number = int("65")
print(type(number), number)