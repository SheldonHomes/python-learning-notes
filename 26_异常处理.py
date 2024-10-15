"""
异常：程序运行过程中出现的错误
异常处理：程序在运行过程中出现错误时，不终止程序的运行，而是根据我们设定的异常处理机制，执行相应的代码，使程序正常运行
Python本身提供了很多异常类型，我们可以根据需要自定义异常类型

基本语法：
try:
    可能出现异常的代码
except 异常类型1:
    如果出现异常类型1，执行该代码
except 异常类型2:
    如果出现异常类型2，执行该代码

捕获异常的形式：
1. 捕获常规异常
    直接使用try...except语句块，不指定异常类型
2. 捕获指定异常
    使用try...except语句块
    例：
    try:
        可能出现异常的代码
    except 异常类型1 as 异常对象1:
        如果出现异常类型1，执行该代码
3. 捕获多个异常
    使用括号将多个异常类型括起来
4. 捕获所有异常
    一种方法是使用try...except语句块，不指定异常类型，另一种则是指定异常为Exception类型
    例：
    try:
        可能出现异常的代码
    except Exception as 异常对象:
        如果出现异常，执行该代码

异常的else和finally语法：
1. else语句
    如果try语句中没有异常，则执行else语句中的代码
    语法：
    try:
        可能出现异常的代码
    except 异常类型1 as 异常对象1:
        如果出现异常类型1，执行该代码
    else:
        如果没有异常，执行该代码
2. finally语句
    无论try语句中是否有异常，都会执行finally语句中的代码

"""

# 捕获常规异常
try:
    f = open("test.txt", "r")
    f.close()
except:
    print("只读文件打开失败")
    f = open("test.txt", "w")
    f.close()

# 捕获指定异常
try:
    name = int(input("请输入姓名：")) # 如果输入的不是整数，会抛出异常
    print(name)
    # name = 10 / 0 # 如果除数为0，会抛出ZeroDivisionError的异常，下面的except语句不能捕获该异常
except ValueError as e:
    print("输入的姓名不是整数，请重新输入")

print("-----------------------")

# 捕获多个异常
try:
    name = int(input("请输入姓名："))
    print(name)
    print(10 / 0)
except (ZeroDivisionError, ValueError) as e: # 捕获ZeroDivisionError和ValueError异常
    print("输入的姓名不是整数 或 除数为0，请重新输入")

print("-----------------------")

# 捕获所有异常
try:
    name = []
    print(name[0])
    # print(10 / 0)
except Exception as e: # 捕获所有异常
    print("出现异常：", e)

print("-----------------------")

# 异常的else和finally语法
# else语句
try:
    print(10 / 0)
except Exception as e:
    print("出现异常")
else:
    print("没有异常才会执行该代码")

# finally语句
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("出现异常")
finally:
    print("无论是否出现异常，都会执行该代码")