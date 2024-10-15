"""
集合不支持元素的重复，集合是无序的，集合中的元素必须是不可变类型

定义集合：
    ① {元素1, 元素2, ...}
    ② 变量名称 = set(可迭代对象)
列表使用[]，元组使用()，字符串使用""，集合使用{}

因为集合无序，所以不能通过索引来访问集合中的元素
集合的常用操作：
    ① 添加元素：add()、update()
    ② 删除元素：remove()、discard()、clear()
    ③ 交集、并集、差集、对称差集：intersection()、union()、difference()、symmetric_difference()
    ④ 判断子集、父集：issubset()、issuperset()
    ⑤ 随机获取元素，获取后元素被删除：pop()

"""

# 集合不重复且无序
set_with_repeat = {'dingzhen', 'xuebao', 'dianziyan', 'xuebao', 'dingzhen', 'dianziyan'}
print(set_with_repeat)

# 集合的常用操作
# add()：添加单个元素
set1 = {1, 2, 3}
set1.add(4)
print(set1)
# update()：添加多个元素
set1.update([5, 6, 7])
print(set1)
print()

# 删除元素
# remove()：删除指定元素，如果元素不存在，则报错
set2 = {1, 2, 3, 4, 5}
set2.remove(3)
print(set2)
# set2.remove(6)
# discard()：删除指定元素，如果元素不存在，则不报错
set2.discard(4)
set2.discard(6)
print(set2)
# clear()：清空集合
set2.clear()
print(set2)
print()

# 交集、并集、差集、对称差集
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7, 8}
# intersection()：交集
print(set3.intersection(set4))
# union()：并集
print(set3.union(set4))
# difference()：差集，返回在set3中但不在set4中的元素
print(set3.difference(set4))
print(set4.difference(set3))
# symmetric_difference()：对称差集，返回在set3和set4中但不在两者共有的元素
print(set3.symmetric_difference(set4))
# difference_update()：差集，更新set3，删除set3中与set4共有的元素
set3.difference_update(set4)
print(set3, set4)
print()

# 判断子集、父集
set5 = {1, 2, 3, 4, 5}
set6 = {1, 2, 3}
# issubset()：判断set6是否是set5的子集
print(set6.issubset(set5))
# issuperset()：判断set5是否是set6的父集
print(set5.issuperset(set6))
print()

# 随机获取元素，获取后元素被删除
set7 = {1, 2, 3, 4, 5}
print(set7.pop())
