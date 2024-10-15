"""
要求1
1.定义一个变量，类型为整型，内容为1~10之间的随机数
2.基于input语句输入猜想的数字，通过if和elif的组合，判断数字是否与随机数一致
注：一共三次机会

要求2
定义一个数字（1~10，随机产生）通过三次判断猜出来数字
    1.数字随机产生，范围1~10
    2.通过三层嵌套实现猜数字

"""

# 1
# 获取随机数
import random

num_rand = random.randint(1, 10)

# 获取用户输入的数字并判断
if num_rand == int (input("猜猜我心里想的是什么数字？一到十里面猜一个吧：")):
    print("第一次就猜对了！恭喜喵！")
elif num_rand == int (input("没对喵，再猜一次喵：")):
    print("猜对了！恭喜喵！")
elif num_rand == int (input("还是没对喵，最后一次猜了喵：")):
    print("终于猜对了喵！恭喜喵！")
else:
    print(f"可惜喵……答案是{num_rand}喵")
print('\n', end='')

# 2
# 获取随机数
num_rand = random.randint(1, 10)

# 获取用户输入的数字并判断
num_usr = int (input("从1到10里面猜一个喵喵想的数字喵！"))
if num_rand == num_usr:
    print("一次就猜中了！好厉害喵！")
else:
    if num_usr > num_rand:
        print("数字大了喵，", end='')
    else:
        print("数字小了喵，", end='')
    # 再次获取用户输入的数据
    num_usr = int (input("再猜一次喵："))
    if num_usr == num_rand:
        print("这回猜对了！也很不错了喵！")
    else:
        if num_usr > num_rand:
            print("数字大了喵，", end='')
        else:
            print("数字小了喵，", end='')
        num_usr = int (input("还有一次机会喵："))
        if num_usr == num_rand:
            print("终于猜对了喵！恭喜喵！")
        else:
            print(f"可惜喵……答案是{num_rand}喵")
    