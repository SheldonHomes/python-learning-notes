"""
文件编码：
编码即一种规则集合，将字符转换为二进制数据，解码即其逆过程。
常见的编码有：ASCII、GB2312、GBK、UTF-8等，其中UTF-8是Unicode的国际编码，支持全球所有语言。

文件操作：主要包括打开、读取、写入、关闭等操作。
1. 打开文件：使用open()函数，可以打开一个已经创建的文件或者创建一个新文件，如只读、写入、追加等。
语法：open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
参数说明：
    file：文件路径
    mode：打开文件的模式，如'r'表示只读，'w'表示写入，'a'表示追加等
    buffering：缓冲区大小，-1表示使用系统默认值
    encoding：文件编码，如'utf-8'表示使用UTF-8编码
    errors：错误处理方式，如'ignore'表示忽略错误
    newline：换行符处理方式，如'\n'表示换行
    closefd：是否关闭文件描述符，True表示关闭
    opener：自定义打开文件的方式
示例：
f = open('test.txt', 'r', encoding='utf-8')
注：
r 只读 文件的指针会放在文件的开头，即默认状态
w 写入 文件不存在则创建，文件存在则清空文件并从头开始写，即覆盖
a 追加 文件不存在则创建，文件存在则在文件末尾追加内容，即不覆盖
b 二进制模式 如rb、wb、ab等
+ 表示同时支持读和写 如r+、w+、a+等
关于buffering参数：
-1 系统默认缓冲 Python会根据文件模式和系统的默认设置来自动选择合适的缓冲机制，通常文本模式下是全缓冲，二进制模式下则根据文件大小和系统设置决定缓冲策略
0  无缓冲      只适用于以二进制模式打开的文件，表示不使用缓冲，每次读写操作都会直接与文件系统交互
1  行缓冲      只适用于以文本模式打开的文件，每写入一行（遇到换行符\n时）都会刷新缓冲区，将数据写入磁盘。适用于交互式操作，例如终端输出
>1 指定缓冲大小 可以指定一个大于1的整数，表示缓冲区的大小，单位是字节。适用于需要控制缓冲区大小的场景，例如大文件读写

2. 读取文件：使用read()、readline()、readlines()等方法，可以读取文件内容。
read()：读取整个文件内容，返回一个字符串
语法：file.read(size=-1)
参数说明：
    size：读取的字节数，-1表示读取整个文件
readlines()：一行一行地读取整个文件的内容，返回一个列表，每个元素为一行内容
语法：file.readlines(hint=-1)
参数说明：
    hint：读取的行数，-1表示读取整个文件（不可变更）
readline()：读取文件的一行内容，返回一个字符串
语法：file.readline(size=-1)
参数说明：
    size：读取的字节数，-1表示读取整行内容

3. 写入文件：使用write()、writelines()、等方法，可以向文件写入内容。
write()：向文件写入一个字符串
语法：file.write(s)
参数说明：
    s：要写入的字符串
writelines()：向文件写入一个字符串列表
语法：file.writelines(sequence)
参数说明：
    sequence：要写入的字符串列表
flush()：将缓冲区内容写入文件
语法：file.flush()
注：
'w' 模式：使用 write() 或 writelines() 会覆盖文件原有内容。
'a' 模式：使用 write() 或 writelines() 会在文件末尾追加内容，不会覆盖原有内容。
wirte()和writelines()方法写入文件时，内容不会立即写入文件，而是先写入缓冲区，当缓冲区满时才会写入文件。
可以使用flush()方法将缓冲区内容立即写入文件，也可以设置open()函数的buffering参数为1来控制缓冲，或是关闭文件刷新缓冲区。

4. 追加写入文件：使用'a'模式打开文件，可以向文件末尾追加内容。
注：使用'a'模式打开文件时，如果文件不存在则会创建文件，如果文件存在则会从文件末尾开始写入内容，不会覆盖原有内容。

5. 关闭文件：使用close()方法，可以关闭文件，释放资源。
语法：file.close()

"""

import time

# 打开文件
f = open("D:\\Python Projects\\PYLearning\\test\\test_file.txt", "r", encoding="utf-8")

# 读取文件内容
# read()：读取整个文件内容，返回一个字符串
content = f.read()
print(content) # 输出结果："dingzhen\nxuebao\ndianziyan\nxiaoma\nnianheguo"
f.seek(0, 0)
content = f.read(5)
print(content) # 输出结果："dingz"
print("--------------------------------")

# readlines()：一行一行地读取整个文件的内容，返回一个列表，每个元素为一行内容
f.seek(0, 0)
lines = f.readlines()
print(lines) # 输出结果：['dingzhen\n', 'xuebao\n', 'dianziyan\n', 'xiaoma\n', 'nianheguo']
print("--------------------------------")

# readline()：读取文件的一行内容，返回一个字符串
f.seek(0, 0)
line1 = f.readline()
print(line1) # 输出结果："dingzhen\n"
line2 = f.readline(5)
print(line2) # 输出结果："xueba"
print("--------------------------------")

# for循环读取文件每行内容
f.seek(0, 0)
for line in f:
    print(line, end="")
print("\n--------------------------------")

# 关闭文件
f.close()

# with open语法
# with open语法能自动关闭文件，不需要手动调用close()方法
with open("D:\\Python Projects\\PYLearning\\test\\test_file.txt", "r", encoding="utf-8") as f:
    print("\n----with open语法----")
    print(f.read())

# 写入文件
# 使用write()方法写入文件
f = open("D:\\Python Projects\\PYLearning\\test\\test_file_1.txt", "w", encoding="utf-8")
f.write("hello world\n") # 将内容写入缓冲区
# time.sleep(60) # 等待60秒，观察文件中内容是否写入
f.flush() # 刷新缓冲区
# time.sleep(60) # 等待60秒，观察文件中内容是否写入
f.close() # 关闭文件

# 使用writelines()方法写入文件
f = open("D:\\Python Projects\\PYLearning\\test\\test_file_1.txt", "w", buffering=1, encoding="utf-8") # 设置缓冲区大小为1，即每次写入一行
f.writelines(["hello world\n", "hello python\n"])
f.close() # 关闭文件

# 追加写入文件
f = open("D:\\Python Projects\\PYLearning\\test\\test_file_1.txt", "a", buffering=1, encoding="utf-8")
f.write("hello python\n")
f.close() # 关闭文件