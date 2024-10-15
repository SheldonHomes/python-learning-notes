"""
自定义模块：
对于一些Python没有提供的功能，或是自身程序需要，可以通过自定义模块来实现。
每个Python文件都可以作为一个模块，只需要在文件中定义函数、类和变量，并使用def、class、global等关键字进行声明即可。

注：当导入多个模块，且模块中存在同名函数时，后导入的模块会覆盖先导入的模块的同名函数。

测试模块：
实际开发中，一般会在模块中添加一些测试代码，用于测试模块中的函数和类是否正确，比如在test_module.py中添加如下代码：
test_function(1, 2)
这样会导致在导入模块时，模块中的测试代码也会被执行，为了避免这种情况，可以使用以下方式：
在模块中添加一个判断，判断当前模块是否是主模块，如果是主模块则执行测试代码，否则不执行测试代码。
    语法：
    if __name__ == '__main__':
        test_function(1, 2)
        
什么是主模块(__main__):
在Python中，每个Python文件都可以作为一个模块，当直接运行一个Python文件时，该文件就是主模块，主模块的__name__属性值为'__main__'。
当导入一个模块时，该模块不是主模块，其__name__属性值为模块名。

什么是__all__:
在Python中，每个模块都有一个__all__属性，该属性是一个列表，用于指定模块中可以被导入的函数、类和变量。

"""

import test.test_module as tm
# import test.test_module_1 as tm
import test.test_module_1 as tm1
import test.test_module_2 as tm2
from test.test_module_a import *


# 测试自定义模块
print(tm1.test_function(1, 2))

# 自定义模块的覆盖
print(tm.test_function(1, 2))

# main模块确保自定义模块的测试代码不会被执行
print(tm2.test_function_1(1, 2))

# __all__的使用
# test_module_a.py中定义了test_a和test_b两个函数，但是__all__只指定了test_a，所以只有test_a可以被导入
test_a() # 只能导入test_a函数