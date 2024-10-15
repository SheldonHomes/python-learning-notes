"""
创建一个自定义包，名称为test_utils，包中包含两个模块str_utils.py和file_utils.py

str_utils.py为字符串工具模块，包含两个函数：
    1. str_reverse(str)：接受传入字符串，将字符串反转
    2. str_slice(str, start, end)：接受传入字符串，以及起始位置和结束位置，返回字符串切片

file_utils.py为文件工具模块，包含两个函数：
    1. file_info_print(file_path)：接受传入文件路径，打印文件信息，如果文件不存在则捕获异常并打印异常信息
    2. file_info_append(file_path, data)：接受传入文件路径和数据，将数据追加到文件末尾

文件内容：
test_utils\__init__.py
test_utils\str_utils.py
test_utils\file_utils.py

使用自定义包中的函数：
    1. 调用str_reverse函数，传入字符串"hello world"，打印反转后的字符串
    2. 调用str_slice函数，传入字符串"hello world"，起始位置为2，结束位置为5，打印切片后的字符串
    3. 调用file_info_print函数，传入文件路径"test_utils\test.txt"，打印文件信息
    4. 调用file_info_append函数，传入文件路径"test_utils\test.txt"和字符串"hello world"，将字符串追加到文件末尾

"""

from test_utils import str_reverse, str_slice, file_info_print, file_info_append

print(str_reverse("hello world"))
print(str_slice("hello world", 2, 5))
file_info_print("test_utils\\test.txt")
file_info_append("test_utils\\test.txt", "hello world")