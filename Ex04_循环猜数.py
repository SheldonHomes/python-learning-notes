"""
要求：
设置一个范围1-100的随机数变量，通过while循环配合input语句判断输入的数字是否等于随机数
1.无限次机会，直到猜中为止
2.每一次猜不中会提示大了或小了
3.猜完数字后提示猜了几次

"""

# 定义随机数变量
import random
num_rand = random.randint(1,100)

# 定义接收变量与计次变量
num = int (input("猜一个1-100之间的数字喵："))
count = 1
# 利用while循环判断输入数字
while num != num_rand:
    print("不对喵，", end='')
    if num > num_rand:
        print("数字大了，再猜一次喵！")
    else:
        print("数字小了，再猜一次喵！")
    num = int (input("输入数字喵："))
    count += 1
# 输出次数
print("猜对了喵！", end='')
if count >= 5:
    print(f"一共用了{count}次才猜对，笨比喵")
else:
    print(f"一共用了{count}就猜对了，天才喵")
