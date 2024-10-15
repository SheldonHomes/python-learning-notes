"""
魔术方法：魔术方法是 Python 类中内置的一些特殊方法，它们以双下划线开头和结尾，例如 ``__init__``、``__str__``、``__repr__`` 等。

常见的魔术方法有：
1. ``__init__``：构造方法，在创建对象时被调用。
    使用例：
    ``class 类名: ``
        ``def __init__(self, 参数1, 参数2, ...):``
            ``self.属性1 = 参数1``
            ``self.属性2 = 参数2``
            ``...``
    通过使用 ``__init__`` 方法，可以在创建对象时初始化对象的属性。比如：
    ``对象名 = 类名(参数1, 参数2, ...)``
2. ``__str__``：字符串表示方法，用于返回对象的字符串表示。通过 str(object) 以及内置函数 format() 和 print() 调用以生成一个对象的“非正式”或格式良好的字符串表示。返回值必须是字符串对象。
    使用例：
    ``class 类名: ``
        ``def __str__(self):``
            ``return "自定义字符串表示"``
    通过使用 ``__str__`` 方法，可以在使用 ``print`` 函数打印对象时返回自定义的字符串表示。比如：
    ``print(对象名)``
3. ``__repr__``：官方字符串表示方法，用于返回对象的官方字符串表示。是由 repr() 内置函数调用，用来输出一个对象的“官方”字符串表示。返回值必须是字符串对象，此方法通常被用于调试。内置类型 object 所定义的默认实现会调用 object.__repr__()。
    使用例：
    ``class 类名: ``
        ``def __repr__(self):``
            ``return "官方字符串表示"``
    通过使用 ``__repr__`` 方法，可以在使用 ``repr`` 函数打印对象时返回自定义的官方字符串表示。比如：
    ``print(repr(对象名))``
注： __str__ 和 __repr__ 的区别
    1. 当默认情况，即 __repr__ 没有被覆盖的情况下，无法满足需求时，才会调用 __str__。
    2. __repr__ 方法的目标是保证准确性，而 __str__ 方法的目标是可读性。
    3. __repr__ 方法通常用于调试，因为它会返回一个合法的 Python 表达式，可以用来重新创建这个对象。而 __str__ 方法通常用于打印，因为它会返回一个对用户友好的字符串表示。
    4. 如果 __str__ 没有被定义，那么 __repr__ 的返回值也会被用于 __str__。
4. ``__len__``：长度方法，用于返回对象的长度。
    使用例：
    ``class 类名: ``
        ``def __len__(self):``
            ``return 长度``
    通过使用 ``__len__`` 方法，可以在使用 ``len`` 函数获取对象的长度时返回自定义的长度。比如：
    ``print(len(对象名))``
5. ``__getitem__``、``__setitem__``：索引方法，用于返回对象的索引值和为对象赋值。
    使用例：
    ``class 类名: ``
        ``def __getitem__(self, 索引):``
            ``return 索引值``
        ``def __setitem__(self, 索引, 值):``
            ``self.属性[索引] = 值``
    通过使用 ``__getitem__`` 和 ``__setitem__`` 方法，可以在使用索引访问对象和为对象赋值时返回自定义的索引值和赋值。比如：
    ``print(对象名[索引])``
    ``对象名[索引] = 值``
6. ``__lt__``、``__gt__``: 比较方法，用于比较两个对象的大小。其中，``__lt__`` 表示小于，``__gt__`` 表示大于。返回值为布尔值。(less than, greater than)
    使用例：
    ``class 类名: ``
        ``def __lt__(self, 对象名):``
            ``return 比较结果``
        ``def __gt__(self, 对象名):``
            ``return 比较结果``
    通过使用 ``__lt__`` 和 ``__gt__`` 方法，可以在使用比较运算符（< 和 >）比较两个对象时返回自定义的比较结果。比如：
    ``print(对象名1 < 对象名2)``
    ``print(对象名1 > 对象名2)``
        __le__: 小于等于方法，用于比较两个对象的大小。返回值为布尔值。(less than or equal to)
        __ge__: 大于等于方法，用于比较两个对象的大小。返回值为布尔值。(greater than or equal to)
7. ``__eq__``：等于方法，用于比较两个对象是否相等。返回值为布尔值。
    使用例：
    ``class 类名: ``
        ``def __eq__(self, 对象名):``
            ``return 比较结果``
    通过使用 ``__eq__`` 方法，可以在使用比较运算符（==）比较两个对象时返回自定义的比较结果。比如：
    ``print(对象名1 == 对象名2)``
8. ``__call__``：调用方法，用于将对象作为函数调用。
    使用例：
    ``class 类名: ``
        ``def __call__(self, 参数1, 参数2, ...):``
            ``return 返回值``
    通过使用 ``__call__`` 方法，可以在使用对象名(参数1, 参数2, ...) 调用时返回自定义的返回值，实现让对象像函数一样被调用的效果。比如：
    ``对象名 = 类名(参数1, 参数2, ...)``
    ``print(对象名())``
    实际应用中可以用于创建可调用对象、函数封装器、缓存机制等。
9. ``__iter__``、``__next__``：迭代方法，用于实现对象的迭代功能。
    ``__iter__`` 方法用于返回一个迭代器对象，该迭代器对象需要实现 ``__next__`` 方法，即``__next__`` 方法用于处理迭代对象，返回迭代值。
    使用例：
    ``class 类名: ``
        ``def __iter__(self):``
            ``return 迭代器对象``
        ``def __next__(self):``
            ``if self.current >= self.end:``
                ``raise StopIteration``
            ``self.current += 1``
            ``return self.current - 1``
    通过使用 ``__iter__`` 和 ``__next__`` 方法，可以在使用 for 循环迭代对象时返回自定义的迭代器对象和迭代值。比如：
    ``对象名 = 类名()`` - 创建可迭代对象，在该过程中，类已经通过 ``__iter__`` 方法返回了迭代器对象
    ``for 值 in 对象名:`` - 在 for 循环中，迭代器对象会通过 ``__next__`` 方法返回迭代值
        ``print(值)``
    ``__iter__`` 方法与 ``__next__`` 方法通常一起使用，用于实现对象的迭代功能。
    在复杂的迭代器实现中，还可以使用 ``yield`` 关键字来生成迭代值，从而实现更高效的迭代器。
    实际应用中，可以用来创建自定义数据结构、结合上下文管理器``with``实现资源管理、避免内存过大逐步处理大数据等。

yield: 生成器函数，用于生成迭代值。在函数中使用 yield 关键字，每次调用 yield 时，函数会暂停并返回 yield 后的值，下次调用时从上次暂停的位置继续执行。相比于普通函数一次性返回所有值（比如用 return 返回一个列表），生成器能在需要时才生成数据，具有延迟计算和节省内存的优势。也可以通过 next() 手动获取生成器的值，就像使用 __next__()
    
"""

# 测试 __str__ 和 __repr__ 方法
class TestStrAndRepr:
    def __init__(self, UUID, name):
        self.UUID = UUID
        self.name = name
    
    # 定义 __str__ 方法
    def __str__(self) -> str:
        return f"name: {self.name}"
    
    # 定义 __repr__ 方法
    def __repr__(self) -> str:
        return f"UUID: {self.UUID}, name: {self.name}"

# 创建对象
test_obj = TestStrAndRepr('f089cc61dac47e2bad73cc128125c736c28900ed', '50607328')
# 测试两种方法的输出结果是否相同
print(str(test_obj))
print(repr(test_obj)) # 通过不同的方法实现不同的输出结果，方便调试与用户阅读
print("------------------")

# 测试 __len__ 方法
class TestLen:
    def __init__(self, arr):
        self.arr = arr

    def __len__(self):
        return len(self.arr)
    
# 创建对象
test_obj1 = TestLen([1, 2, 3, 4, 5])
print(len(test_obj1))
print("------------------")

# 测试 __getitem__ 和 __setitem__ 方法
class TestGetAndSet:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        
# 创建对象
test_obj2 = TestGetAndSet()
test_obj2['name'] = '50607328'
print(test_obj2['name'])
print("------------------")

# 测试 __lt__、__gt__、__eq__ 方法
class TestCompare:
    """
    TestCompare - a class to test the comparison methods.
    
    TestCompare class provides methods to compare different values.
    
    Attributes
    ----------
    **value**: ``int``
    the value to be compared.
    
    Methods
    ---------
    **__lt__**(self, other: ``TestCompare``) -> ``bool``: the method to compare if the value is less than the other value.
    
    **__gt__**(self, other: ``TestCompare``) -> ``bool``: the method to compare if the value is greater than the other value.

    **__eq__**(self, other: ``TestCompare``) -> ``bool``: the method to compare if the value is equal to the other value.
    
    Usage Example
    -------------
    Here's an example of how to use the TestCompare class:
    .. code-block:: python
        # Create an instance of the class
        obj1 = TestCompare(args)
        obj2 = TestCompare(args)
    
        # Call methods
        result = obj1 < obj2
        print(result)
    
    :author: Sheldon Homes
    :version: version_num
    """
    def __init__(self, value: int):
        self.value = value

    def __lt__(self, other: 'TestCompare') -> bool:
        return self.value < other.value
    
    def __gt__(self, other: 'TestCompare') -> bool:
        return self.value > other.value
    
    def __eq__(self, other: 'TestCompare') -> bool:
        return self.value == other.value

# 创建对象
test_obj3 = TestCompare(10)
test_obj4 = TestCompare(20)
print(f"lt: {test_obj3 < test_obj4}, gt: {test_obj3 > test_obj4}, eq: {test_obj3 == test_obj4}")

# __call__ 方法
class TestCall:
    def __init__(self, arr):
        self.arr = arr
    def __call__(self):
        return sum(self.arr)
    
# 测试 __call__ 方法
test_obj5 = TestCall([1, 2, 3, 4, 5])
print(test_obj5())
print("------------------")

# __call__ 方法的实例：函数缓存
class Memoize:
    def __init__(self, func):
        self.func = func
        self.cache = {}
        
    def __call__(self, *args):
        if args not in self.cache:
            self.cache[args] = self.func(*args)
        return self.cache[args]
    
# 测试 Memoize 类
# 一个运行时间较长的函数
def long_running_function(x):
    print(f"Computing {x}...") # 模拟耗时操作
    return x * x

# 使用 Memoize 类装饰 long_running_function 函数
memoized_func = Memoize(long_running_function)
print(memoized_func(10))
print(memoized_func(10)) # 第二次调用时，直接从缓存中获取结果，不再重新计算
print("------------------")

# 测试 __iter__ 和 __next__ 方法
class TestIterAndNext:
    def __init__(self, start, end):
        self.current = start # 迭代的起始位置
        self.end = end # 迭代的结束位置

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration # 如果迭代结束，抛出 StopIteration 异常
        self.current += 1 # 迭代器向后移动一位
        return self.current - 1 # 返回当前值

# 创建对象
test_obj6 = TestIterAndNext(0, 5)
for i in test_obj6:
    print(i)
print("------------------")

# __iter__ 和 __next__ 方法的实例1：自定义数据结构
class CustomQueue:
    def __init__(self) -> None:
        self.data = []
        
    def enqueue(self, value: int) -> None:
        self.data.append(value) # 入队
        
    def dequeue(self) -> int:
        if not self.data:
            raise IndexError("Queue is empty")
        return self.data.pop(0) # 出队
    
    def enquene_all(self, values: list) -> None:
        for value in values:
            self.enqueue(value) # 批量入队

    # 定义迭代器
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.index += 1
        return self.data[self.index - 1] # 返回当前值
    
# 创建一个队列对象，并传入数据
queue = CustomQueue()
queue.enquene_all([1, 2, 3, 4, 5])

# 使用迭代器遍历队列中的元素
for i in queue:
    print(i, end=' ') # 通过 __iter__ 和 __next__ 方法，可以像遍历列表一样遍历队列中的元素，而不用担心队列中间的元素被修改导致迭代出错
print("\n------------------")

# __iter__ 和 __next__ 方法的实例2：无限序列生成器（以斐波那契数列生成器为例）
class FibonacciGenerator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib
    
# 创建斐波那契数列生成器对象
fib_gen = FibonacciGenerator()

# 使用迭代器遍历斐波那契数列
for i in range(10):
    print(next(fib_gen), end=' ')
print("\n------------------")

# __iter__ 和 __next__ 方法的实例3：自定义迭代逻辑
class SkipEvenNums:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0
        
    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.nums):
            number = self.nums[self.index]
            self.index += 1
            if number % 2 != 0: # 如果是奇数，则返回
                return number
        raise StopIteration
    
# 创建 SkipEvenNums 对象
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed_numbers = SkipEvenNums(numbers)

# 使用迭代器遍历 SkipEvenNums 对象
for num in processed_numbers:
    print(num, end=' ')
print("\n------------------")

# __iter__ 和 __next__ 方法的实例4：逐行读取大文件
class FileLineIterator:
    def __init__(self, filepath):
        self.file = open(filepath, 'r')
        
    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line
    
# 创建对象
large_file = FileLineIterator('test/test_file.txt')
# 使用迭代器逐行读取文件内容
for line in large_file:
    print(line, end=' ')
    print('The line has already been processed.') # 模拟对每一行进行处理，展示效果
# 输出结果充分地展示了__next__暂停返回的功能，即每次调用next()方法时，都会暂停并等待下一次调用，直到文件读取完毕
print("------------------")

# __iter__ 和 __next__ 方法的实例5：结合上下文管理器实现资源管理
class FileLineIteratorContextManager:
    def __init__(self, filename: str):
        self.filename = filename
    
    # 如果要使用上下文管理器，必须实现 __enter__ 和 __exit__ 方法
    def __enter__(self):
        self.iterator = FileLineIterator(self.filename)
        return self.iterator

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.iterator.file.close()

# 使用上下文管理器逐行读取文件内容
with FileLineIteratorContextManager('test/test_file.txt') as file:
    for line in file:
        print(line, end=' ')
        print('The line has already been processed.') # 模拟对每一行进行处理，展示效果
# 上下文管理器保证了在处理完文件后，文件会被正确关闭，避免了资源泄漏的问题
print("------------------")

# __iter__ 和 __next__ 方法的实例6：结合生成器快速处理数据
class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.num_generator()

    def num_generator(self):
        for i in range(self.start, self.end + 1):
            yield i # 使用 yield 关键字定义一个生成器函数，每次调用 next() 方法时，都会暂停并等待下一次调用
            
# 自定迭代范围
for num in CustomRange(1, 10):
    print(num, end=' ')