"""
要求：
结合前面学习的input语句，完成如下案例。
    1.通过input语句，获取键盘输入，为变量age赋值。（注意转换成数字类型）
    2.通过if判断是否是成年人，满足条件则输出一下信息：
        欢迎来到原神乐园，原神60级免费，低于60级收费
        请输入你的原神等级：60
        您已满级，无需付费
        祝您游玩愉快！

"""

# 用户输入，利用age变量接收
print("欢迎来到原神乐园，原神60级免费，低于60级收费")
age = input("请输入您的原神等级：")
# 利用if判断age变量是否符合条件，以进行相应的代码块
if int(age) == 60:
    print("您已满级，无需付费")
elif int(age) < 60 and int(age) > 0:
    print("您未满60级，充值648后可进入乐园")
else:
    print("您输入的数字有误！")
print("祝您游玩愉快！")
