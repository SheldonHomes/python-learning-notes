"""
continue和break：控制循环暂停或中断的关键字

1.continue
    continue关键字用于终端本次循环，直接进入下一次循环
    示例：
    for i in range(1, 10):
        语句1
        continue
        语句2
    表示在满足条件的情况下，遇到continue就结束当次循环，不执行语句2直接进入下一次循环

2.continue在循环嵌套中的应用
    for i in range(1, 100):
        语句1
        for j in range(1,100):
            语句2
            continue
            语句3
    在嵌套的循环中，Continue只针对当前所在的循环，不针对上层循环，如上面只针对临时变量j所在的循环

3.break
    break关键字用于直接结束循环
    示例：
    for i in range(1, 100)
        语句1
        break
        语句2
    语句3
    表示在满足条件的情况下，遇到break就直接结束循环，即执行完语句1后就直接执行语句3了

4.break在循环嵌套中的应用
    与continue类似

"""

import numpy as np

# 1
# continue输出1-100所有3的倍数
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=' ')
    # 不满足条件利用continue跳过进入下一次循环
    else:
        continue
print('')


# 2
# 定义一个5*5全为0的二维数组
arr = np.zeros((5, 5), dtype=int)
for i in range(0, 5):
    for j in range(0, 5):
        # 使对角线上的数字全为5
        if i == j:
            arr[i][j] = 5
        else:
            continue
# 输出二维数组arr
for i in range(0, 5):
    for j in range(0, 5):
        print(arr[i][j], end='\t')
    print('')
print('')


# 3
# 定义字符串
str1 = "wAsdQeR7805ea"
count = 1
for i in str1:
    # 检索字符串中字符，检索到时退出循环不执行count += 1
    if i == 'R':
        break
    count += 1
print(str1, count)
print('')


# 4
# 
