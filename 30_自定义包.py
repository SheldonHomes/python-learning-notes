"""
Python中包的概念：
    包用于组织模块，把功能相近的模块组织在一起，方便管理和使用。
    从物理上看，包就是一个文件夹，该文件夹下可以包含多个模块，以及一个__init__.py文件。__init__.py文件与模块组合在一起，形成包。
    从逻辑上看，包是一个命名空间，用于管理模块名，防止命名冲突，其本质仍然是模块。

创建自定义包：
    1. 创建一个文件夹，文件夹的名字就是包的名字。
    2. 在文件夹中创建一个__init__.py文件，该文件是一个空文件，也可以在其中定义变量、函数、类等。
    3. 在文件夹中创建模块，模块的名字就是模块的名字。
    
导入自定义包：
    1. 导入包中的模块，格式为：import 包名.模块名
        例：import my_package.my_module1
    2. 通过from...import...语句导入包中的模块，格式为：from 包名 import 模块名
        例：from my_package import my_module1

__init__.py文件：
    __init__.py文件是一个特殊的文件，用于标识该文件夹是一个包。
    通常该文件为空，但也可以为其添加一些功能，比如：
        1. 使用__all__变量定义包的公开接口，即包的公开模块，当使用from 包名 import *语句导入包时，只会导入__all__变量中定义的模块。
        2. 在__init__.py中导入包中的模块，可以直接通过包名访问模块中的函数、变量、类等，而无需指明子模块。
        3. 可以放置一些初始化代码，比如设置默认配置或打印调试信息等，在导入包时自动执行。
    注：__init__.py

"""

# 导入自定义包
# 导入方式1：import 包名.模块名
# import test_package.test_module1
# import test_package.test_module2

# 调用自定义包中的模块
# test_package.test_module1.print_info_1()
# test_package.test_module2.print_info_2()

# 导入方式2：from 包名 import 模块名
# from test_package import test_module1
# from test_package import test_module2

# 调用自定义包中的模块
# test_module1.print_info_1()
# test_module2.print_info_2()

# __init__.py文件的使用
# 因为在__init__.py文件中导入了test_module1和test_module2，所以可以直接通过包名访问模块中的函数、变量、类等，而无需指明子模块。
from test_package import print_info_1, print_info_2
print_info_1()
print_info_2()

# __all__ = ['print_info_1', 'print_info_2']
# from test_package import *
# test_module1.print_info_1()
# test_module2.print_info_2()
