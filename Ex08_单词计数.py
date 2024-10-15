"""
单词计数：
从“D:\\Python Projects\\PYLearning\\test”中的“test_text.txt”文件中读取文本，统计文本中dingzhen单词出现的次数，并输出结果。

"""

# 方式1
with open("D:\\Python Projects\\PYLearning\\test\\test_text.txt", "r", encoding="utf-8") as f:
    count = f.read().count("dingzhen")
    print("方式1——dingzhen单词出现的次数为：", count)

# 方式2
with open("D:\\Python Projects\\PYLearning\\test\\test_text.txt", "r", encoding="utf-8") as f:
    count = 0
    for line in f.readlines():
        count += line.strip().count("dingzhen")
    print("方式2——dingzhen单词出现的次数为：", count)
