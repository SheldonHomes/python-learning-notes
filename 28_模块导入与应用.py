"""
模块(Module):
即以.py为后缀的Python文件，模块中可以定义函数、类和变量，也可以包含可执行的代码。

模块的作用：
模块可以帮助开发者快速地实现一些功能，避免重复造轮子，提高开发效率。
模块可以被认为是一种工具包，通过代码的封装，将相关的代码组织在一起，方便管理和使用。

模块的分类：
1. 内置模块：Python解释器自带的模块，如sys、os、time等。
2. 标准库模块：Python官方提供的模块，如datetime、random等。
3. 第三方模块：由第三方开发并发布的模块，如requests、numpy等。
4. 自定义模块：开发者自己编写的模块。

模块的导入：
使用import语句导入模块，如import sys、import os、import time等。
语法：
1. 直接导入模块：
    import 模块名
2. 导入模块中的特定函数或变量：
    from 模块名 import 函数名/变量名
3. 导入模块中的所有函数或变量：
    from 模块名 import *
4. 导入模块并重命名：
    import 模块名 as 别名
5. 导入模块中的特定函数或变量并重命名：
    from 模块名 import 函数名/变量名 as 别名
注：
1. 只导入模块的函数或变量，不需要在调用时加模块名。
2. 模块、函数或变量的重命名规则一般是：使用小写字母，单词之间用下划线连接。
3. 模块导入一般写在文件的开头，方便阅读和维护。
4. 模块导入时，Python解释器会按照sys.path中的路径顺序搜索模块。

常见的内置模块：
1. sys：与Python解释器相关的模块，如获取命令行参数、退出程序等。
2. os：与操作系统相关的模块，如文件操作、目录操作等。
3. time：与时间相关的模块，如获取当前时间、时间格式化等。
4. math：与数学相关的模块，如数学运算、三角函数等。
5. random：与随机数相关的模块，如生成随机数、随机选择等。
6. json：与JSON数据相关的模块，如解析JSON数据、生成JSON数据等。
7. re：与正则表达式相关的模块，如匹配字符串、替换字符串等。
8. datetime：与日期时间相关的模块，如获取当前日期时间、日期时间格式化等。
9. hashlib：与加密相关的模块，如MD5加密、SHA1加密等。
10. urllib：与网络请求相关的模块，如发送HTTP请求、解析HTTP响应等。

"""

# 模块导入
# 1. 直接导入模块
import sys
for path in sys.path:
    print(path)  # 输出当前Python解释器的模块搜索路径
print()

# 2. 导入模块中的特定函数或变量
from os import path
# 因为只导入了path函数，所以调用path函数时不需要加模块名
print(path.exists('28_模块导入与自定义.py'))  # 判断文件是否存在
print()

# 3. 导入模块中的所有函数或变量
from time import *
def convert_time(struct_time):
    return strftime("%Y-%m-%d %H:%M:%S", struct_time)
# 因为导入了time模块中的所有函数或变量，所以调用函数时不需要加模块名
print(convert_time(localtime()))  # 获取当前时间并格式化
print(convert_time(gmtime()))  # 获取当前时间的UTC时间
print()

# 4. 导入模块并重命名
import time as t
# 导入的是模块，所以调用函数时需要加模块名
print(convert_time(t.localtime()))  # 获取当前时间
print()

# 5. 导入模块中的特定函数或变量并重命名
from time import localtime as lt
print(convert_time(lt()))  # 获取当前时间