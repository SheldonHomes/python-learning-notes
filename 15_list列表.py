"""
List列表
同一列表内可以存入不同数据类型，可以嵌套使用

List列表的常用操作：
1.查询：列表.index(元素)
2.修改：列表[下标] = 值
3.插入：列表.insert(下标, 元素)
4.追加：
    单个：列表.append(元素)
    多个：列表.extend(其他数据容器)
5.删除：
    del 列表[下标]
    列表.pop(下标)
    列表.remove(元素)
6.清空：列表.clear()
7.统计某一元素的数量：列表.count(元素)
8.统计列表一共多少元素：len(列表)

"""

mylist = ["dingzhen", "dianziyan", "xuebao"]

# 查询
print(mylist.index("dingzhen"))

# 修改
mylist[2] = "xiaomazhenzhu"
print(mylist)

# 插入
mylist.insert(1, "weixinpai")
print(mylist)

# 追加
# 追加单个
mylist.append("shuochang")
print(mylist)

# 追加多个
mylist.extend(["zood", "igotsmoke", "yandistance"])
print(mylist)

# 删除
del mylist[1]
element = mylist.pop(2)
print(mylist)
print(element)
mylist.remove("dianziyan")

# 清空
mylist.clear()
print(mylist)

# 统计某一元素的数量
mylist = [1, 1, 0, 0, 0, 2, 2]
print(mylist.count(0))

# 统计列表一共多少元素
print(len(mylist))
