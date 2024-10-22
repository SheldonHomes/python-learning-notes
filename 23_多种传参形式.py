"""
四种传参形式：位置参数、关键字参数、不定长参数、缺省参数

1. 
位置参数：按照参数定义的顺序传入
例：
    def 函数名(参数1, 参数2, 参数3):
        函数体
    调用：
    函数名(参数1, 参数2, 参数3)
注：位置参数必须按照定义的顺序传入，且个数必须一致

2.
关键字参数：按照参数名传入
例：
    def 函数名(参数1, 参数2, 参数3):
        函数体
    调用：
    函数名(参数1=值1, 参数2=值2, 参数3=值3)
注：函数调用时，如果有位置参数，位置参数必须在关键字参数之前，但是关键字参数的顺序可以任意

3.
缺省参数：在定义函数时，给参数设置默认值
例：
    def 函数名(参数1, 参数2, 参数3=缺省值):
        函数体
    调用：
    函数名(参数1, 参数2)
    函数名(参数1, 参数2, 参数3=缺省值)
注：调用函数时，如果给缺省参数传值，则修改默认参数值；如果不传值，则使用缺省值
    设置默认值的参数必须在非缺省参数之后

4.
不定长参数：也叫可变参数，用于函数定义时不确定传入参数的个数
包括两种：不定长位置参数、不定长关键字参数
例：
① 不定长位置参数
    def 函数名(*args):
        函数体
    调用：
    函数名(参数1, 参数2, 参数3)
    函数名(参数1, 参数2, 参数3, 参数4)
注：传进的所有参数都会被args以元组的形式保存，args是元组类型，其根据位置参数的顺序保存参数值
② 不定长关键字参数
    def 函数名(**kwargs):
        函数体
    调用：
    函数名(参数1=值1, 参数2=值2, 参数3=值3)
    函数名(参数1=值1, 参数2=值2, 参数3=值3, 参数4=值4)
注：传进的所有参数都会被kwargs以字典的形式保存，kwargs是字典类型，其根据关键字的键值对的顺序保存参数值
除了以上两种，直接在已定义好的可迭代对象前加*或**，也可以将可迭代对象拆分成单个元素传入函数

"""

def test(a, b, c):
    print(a, b, c)

# 位置参数
test(1, 2, 3)
print()

# 关键字参数
test(a=1, c=3, b=2)
# 位置参数和关键字参数混合使用
test(1, c=3, b=2)
print()

# 缺省参数
def test2(a, b, c=3):
    print(a + b + c)
# 使用缺省参数
test2(1, 2)
# 不使用缺省参数
test2(1, 2, 4)
print()

# 不定长参数
# 不定长位置参数
def test3(*args):
    print(f"args: {args} type: {type(args)}")
test3('a') # ('a',)
test3('a', 'b', 'c')  # ('a', 'b', 'c')
# 不定长关键字参数
# kw - keyword
def test4(**kwargs):
    print(f"kwargs: {kwargs} type: {type(kwargs)}")
test4(a=1) # {'a': 1}
test4(a=1, b=2, c=3) # {'a': 1, 'b': 2, 'c': 3}