"""
字典：包含键值对的数据结构，可以通过键来访问值，不能通过索引来访问
字典不允许重复的键，但允许重复的值

字典的格式：
{键1: 值1, 键2: 值2, 键3: 值3, ...}

字典的创建：
1. 使用花括号{}或dict()创建空字典
2. 使用花括号{}创建有初始值的字典
3. 使用dict()函数创建字典

字典的嵌套：
字典中可以包含字典，即字典的值可以是字典

字典的常用操作：
1. 获取字典的值：通过键来获取值
2. 增加字典的键值对：通过键来增加值 语法：字典名[键] = 值
3. 修改字典的键值对：通过键来修改值 语法：字典名[键] = 值
4. 删除字典的键值对：通过键来删除值 语法：del 字典名[键] 或 字典名.pop(键)
5. 获取字典的所有键：使用keys()方法
6. 获取字典的所有值：使用values()方法
7. 清空字典：使用clear()方法
8. 获取可遍历的键值对：使用items()方法

"""

# 创建字典
# 1. 使用花括号{}创建空字典
dict1 = {}
dict2 = dict()
print(dict1, dict2)
# 2. 使用花括号{}创建有初始值的字典
dict2 = {'name': 'Dingzhen', 'age': 23, 'gender': 'male'}
print(dict2)
# 3. 使用dict()函数创建字典
dict3 = dict(name='Dingzhen', age=23, gender='male')
print(dict3)

# 获取字典的值
print(dict2['name'])
print(dict2['age'])
print()

# 字典的嵌套
dict4 = {
    'name': 'Dingzhen',
    'age': 23,
    'gender': 'male',
    'hobby': {
        'music': 'rap',
        'cigeratte': 'electric',
        'sport': 'smoking'
    }
}
# 获取嵌套字典的值
print(dict4['hobby']['music'])
print()

# 字典的常用操作
# 1. 增加字典的键值对
dict2['address'] = 'LiTang'
print(dict2)
# 2. 修改字典的键值对
dict2['age'] = 24
print(dict2)
# 3. 删除字典的键值对
del dict2['gender']
print(dict2)
dict2.pop('age')
print(dict2)
# 4. 清空字典
dict2.clear()
print(dict2)
# 5. 获取字典的所有键
print(dict4.keys())
# 6. 获取字典的所有值
print(dict4.values())

# 字典的遍历
for key in dict4:
    if key == 'hobby':
        print('hobby:')
        for k, v in dict4[key].items():
            print(k, v)
    else:
        print(key, dict4[key])