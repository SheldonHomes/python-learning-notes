"""
Python 在3.5 版本引入了类型注解（ Type Annotations ）的概念，允许我们在代码中为变量、函数参数和返回值指定类型。
类型注解：在代码中涉及数据交互的地方，明确地指定数据的类型，从而避免数据类型错误。
主要功能：
    1. 帮助第三方 IDE 或者文本编辑器对代码进行类型检查，从而提前发现潜在的错误。
    2. 提高代码的可读性，让其他开发者更容易理解代码的意图。
    3. 增强代码的可维护性，便于后续的代码重构和优化。

使用类型注解：
    1. 变量类型注解：在变量名后面加上冒号和类型名。
        例：``x: int = 10``
    2. 函数参数类型注解：在参数名后面加上冒号和类型名。
        例：``def greet(name: str) -> None: ...``
    3. 函数返回值类型注解：在函数名后面加上冒号和类型名。
        例：``def add(a: int, b: int) -> int: ...``
    4. 类型别名：使用 ``type`` 关键字定义类型别名。
        例：
        ``MyType = List[int]``
        ``def process_data(data: MyType) -> None: ...``
    5. 类型提示：使用 ``typing`` 模块中的类型提示。
        例：
        ``from typing import List, Tuple, Optional``
        ``def process_data(data: List[Tuple[int, str]]) -> Optional[int]: ...``

注：
1. 对于类中的属性和方法，可以使用 ``@property`` 装饰器来定义只读属性，并使用类型注解来指定属性的类型。
    例：
    ``class MyClass:``
        ``@property``
        ``def my_property(self) -> int:``
            ``...``
2. 如果要在类中的方法中指定某个参数为该类的对象，可以用``'类名'``来表示。
    例：
    ``class MyClass:``
        ``def my_method(self, other: 'MyClass') -> None:``
            ``...``
3. Union 类型：使用 ``Union`` 类型来表示一个变量可以是多种类型中的任意一种。
    例：
    ``from typing import Union``
    ``def process_data(data: Union[int, str]) -> None: ...``
4. Optional 类型：使用 ``Optional`` 类型来表示一个变量可以是某种类型或者 ``None`` 。
    例：
    ``from typing import Optional``
    ``def process_data(data: Optional[int]) -> None: ...``
            
文档注解：文档注解（ Docstring ）是用于描述函数、类或模块的文档字符串，它可以帮助其他开发者理解代码的功能和用法。
一般情况下，文档注解应该包含以下内容：
    1. 函数或类的功能描述。
    2. 参数的描述，包括参数名、类型和含义。
    3. 返回值的描述，包括返回值的类型和含义。
    4. 异常的描述，包括可能抛出的异常类型和含义。
    5. 示例代码。
常用的文档注解格式有： reStructuredText（ reST ）和 Google 风格的文档注解。
VSCode 使用的是 Google 风格的文档注解， PyCharm 使用的是 reST 风格的文档注解。
此处统一使用 reST 风格的文档注解。

reST 风格的文档注解：
    1. 使用三引号（ """ """ ）将文档注解包裹起来。
    2. 在文档注解中，可以使用特定的标记来描述参数、返回值和异常等。
        - ``:param 参数名: 参数描述``
        - ``:type 参数名: 参数类型``
        - ``:return: 返回值描述``
        - ``:rtype: 返回值类型``
        - ``:raises 异常类型: 异常描述``
    3. 在文档注解中，可以使用特定的标记来描述示例代码。
        - ``示例数据类型`` ：使用``包含文本可以将文本标记为字面量
        - ``:code:示例编程语言`` ：使用:code:前缀可以将代码块标记为代码
        - ``**示例文本**`` ：使用**前缀可以将文本标记为粗体
        - ``*示例文本*`` ：使用*前缀可以将文本标记为斜体
        - ``:math:示例数学公式`` ：使用:math:前缀可以将数学公式标记为数学公式，根据生成器的配置，可能使用 MathJax, KaTeX 渲染， 或者使用本地 LaTeX 编译成 SVG 嵌入。
        
VSCode 中可以使用用户代码片段来自定义文档注解模板，方便快速生成文档注解。

"""

# 变量类型注解
x: int = 10

# 函数参数类型注解
def greet(name: str) -> None:
    print(f"Hello, {name}!")

# 函数返回值类型注解
def add(a: int, b: int) -> int:
    return a + b

# 类型别名
MyType = list[int]

def process_data(data: MyType) -> None:
    print(data)
    
# 类型提示
from typing import List, Tuple, Optional

def process_data(data: List[Tuple[int, str]]) -> Optional[int]:
    if data:
        return data[0][0]
    else:
        return None
print(process_data([(1, 'a'), (2, 'b')]))

# 结合@property装饰器使用类型注解来处理类中的可读属性
class TestClass():
    def __init__(self) -> None:
        self._age = 0
        
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, value: int) -> None:
        self._age = value

test = TestClass()
test.age = 20
print(test.age)

# 文档注释演示
class MyClass:
    """
    MyClass - a class that shows how docstring is used.
    
    MyClass class provides a mothod to print MyClass and its object's location.
    
    Methods
    ---------
    **my_method**(other: ``MyClass``) -> ``None``: a method to print MyClass and its object's location.
    
    Usage Example
    -------------
    Here's an example of how to use the MyClass class:
    .. code-block:: python
        # Create an instance of the class
        obj = MyClass()
    
        # Call methods
        result = obj.my_method(class_name)
        print(result)
    
    :author: Sheldon Homes
    :version: 0.0.1
    """
    def my_method(self, other: 'MyClass') -> None:
        """
        a method to print MyClass and its object's location.
        
        :param other: an instance of MyClass
        :type other: ``MyClass``
        :return: None
        :rtype: None
        """
        print(f"Hello, {other}!")
        
my_class = MyClass()

my_class.my_method(my_class)