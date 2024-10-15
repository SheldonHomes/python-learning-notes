"""
类与对象：类是对象的模板，对象是类的实例。类中定义了对象的属性和方法，对象通过调用类中的方法来操作属性。

类中包含：
    1. 类的属性，也叫成员变量
    2. 类的方法，也叫成员函数
    3. 类的构造函数，也叫初始化函数
    4. 类的析构函数，也叫销毁函数

类的定义：
    class 类名:
        属性 = 值
        
        def 方法名(self, 参数列表):
            方法体
        
        def __init__(self, 参数列表):
            初始化函数体

        def __del__(self):
            析构函数体

self 关键字：在类的方法中， self 代表类的实例对象本身，通过 self 可以访问类的属性和方法。
在构造类的方法时，第一个参数必须是 self ，表示类的实例对象本身。
如果在方法内部需要使用类的属性，必须使用 self.属性名 的方式来访问。

类的使用：
    1. 先创建一个类的实例对象
        ``对象名 = 类名()``
    2. 通过对象名来访问类的属性和方法
        ``对象名.属性名 = 值``
        ``对象名.方法名(参数列表)``

面向对象编程：面向对象编程是一种编程范式，它将程序中的数据和行为封装在一起，通过对象来操作数据和行为。

类中一些特殊的方法：
1. 构造方法：构造方法是一个特殊的方法，它在创建对象时自动调用，用于初始化对象的属性。
    构造方法的名称必须是 ``__init__`` ，它接受一个参数 self ，表示类的实例对象本身。
    构造方法可以接受多个参数，用于初始化对象的属性。
    使用方式：
    ``def __init__(self, 参数列表):``
    ``    self.属性名 = 参数值``
2. 析构方法：析构方法是一个特殊的方法，它在对象被销毁时自动调用，用于清理对象的资源。
    析构方法的名称必须是 ``__del__`` ，它不接受任何参数。
    使用方式：
    ``def __del__(self):``
    ``    清理对象的资源``
3. 类的属性：类的属性是类的成员变量，用于存储对象的状态。
    类的属性可以是公开的，也可以是私有的。
    公开的属性可以直接通过对象名来访问和修改。
    私有的属性只能在类的内部访问和修改，不能通过对象名来访问和修改。
    使用方式：
    ``class 类名:``
    ``    公开的属性名 = 值``
    ``    __私有的属性名 = 值``

"""

# 定义一个类Person，包含name和age两个属性
class Person:
    """
    Person - A test class to demonstrate class and object.
    
    Person class provides a person's attributes(attributes) and actions(methods).
    
    Attributes
    ----------
    **name**: ``String``
        A person's name. default is ``None``.
    **age**: ``Int``
        A person's age. default is ``0``.
    **__species**: ``String``
        A person's species. default is ``Human`` and it is a private attribute, can not be accessed directly.
    
    Methods
    ---------
    **__init__**(self, name: ``String``, age: ``Int``) -> ``None``: the constructor of the class, initialize the attributes of the class.
        
    **action**(self) -> ``None``: perform an action, print "Person object is performing an action".
    
    **__del__**(self) -> ``None``: the destructor of the class, print "Person object is being destroyed".
    
    Usage Example
    -------------
    Here's an example of how to use the Person class:   
    .. code-block:: python
        # Create an instance of the class
        obj = Person(args)
        print(obj.name, obj.age)

        # Call methods
        obj.action(self)
    
    :author: Sheldon Homes
    :version: 0.0.1
    """
    name = None
    age = 0
    __species = "Human"
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print("Person对象被创建")
    
    def action(self):
        print("Person对象执行动作")
    
    def __del__(self):
        print("Person对象被销毁")

import time

# 创建一个Person对象p1
p1 = Person("冬雪莲", 33) # 调用构造函数，初始化对象的属性
print(p1.name, p1.age)

# 向p1对象中添加属性name和age
p1.name = "丁真"
p1.age = 22

# 打印p1对象的属性
print(p1.name, p1.age)
# 打印p1对象的私有属性
print(p1._Person__species) # 私有属性可以通过 _类名__属性名 的方式来访问

# 调用p1对象的方法
p1.action()
# 程序结束时，自动调用p1对象的析构函数
time.sleep(30)