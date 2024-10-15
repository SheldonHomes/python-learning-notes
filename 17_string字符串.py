"""
字符串可以通过下标索引取值，不可修改

字符串的基础操作：
1.查找：字符串.index()
2.替换：字符串.replace(字符串1, 字符串2)
3.分割：字符串.split(分隔符字符串)
4.规整（去除前后空格或指定字符串）
    字符串.strip()
    字符串.strip(字符串)
5.统计某一元素的数量：列表.count(元素)
6.统计列表一共多少元素：len(列表)

"""

# 通过下标索引取值
str1 = "dianziyan"
print(f"1: {str1[2]}\t2: {str1[-3]}")

# 查找
print(str1.index("zi"))

# 替换
value = str1.replace("yan", "dingzhen")
print(value)

# 分割
str2 = "nihao dingzhen wocenidema"
split_list = str2.split(" ")
print(split_list)

# 规整
# 规整空格
str3 = "  dingzhen ai dianziyan    "
print(str3)
reshaped_val = str3.strip()
print(reshaped_val)
print()

# 规整指定字符串
str4 = "123dingzhen ai dianziyan213"
print(str4)
reshaped_val = str4.strip("123")
print(reshaped_val)
