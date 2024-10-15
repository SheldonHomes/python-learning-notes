"""
循环：即循环执行部分代码语句块

1.while循环格式：
    while 条件:
        满足条件时执行的代码块

  ① while的条件同样需要布尔类型来判断，True表示继续循环，False表示停止循环
  ② while同if一样需要空格缩进判断

2.while嵌套循环
    while 条件1:
        while 条件2:
            满足条件1、2执行的语句块

"""

import random

# 1
# while循环
num_rand = random.randint(1, 10)
count = 1
# 利用while循环
while num_rand != 10:
    print("没有抽到五星！")
    num_rand = random.randint(1,10)
    count += 1
print("抽到五星了！")
if count >= 9:
    print(f"一共花了{count*10}抽，纯纯大非酋！")
elif count > 3:
    print(f"一共花了{count*10}抽，这运气倒也还行")
else:
    print(f"一共花了{count*10}抽，真正的欧皇！")
print('')


# 2
# 定义数组
arr1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
i = 0
j = 0
# 输出矩阵
while i < 3:
    while j < 3:
        print(arr1[i][j], end=' ')
        j += 1
    print('\t')
    i += 1
    j = 0

