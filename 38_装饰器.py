"""
装饰器：装饰器是一种特殊类型的函数，它接受一个函数作为参数，并返回一个新的函数，通常用于修改或增强函数的行为。

装饰器通常用于以下场景：
    1. 记录函数的执行时间
    2. 检查函数的输入参数
    3. 控制函数的访问权限
    4. 增加函数的功能

装饰器的语法：``@装饰器函数名``

常见的装饰器：
    1. ``@staticmethod`` :
        功能：将类中的方法定义为静态方法，静态方法不需要类的实例作为第一个参数（即不需要 self ），并且无法访问类或实例的任何属性。
        用途：当一个方法不依赖于类的状态（实例属性或类属性）时，可以使用 @staticmethod。
        示例：
            ``@staticmethod``
            ``def static_method_name():``
            ``    pass``
    2. ``@classmethod`` :
        功能：定义类方法，类方法的第一个参数是类本身（通常命名为 cls ），可以访问类属性和方法，但不能直接访问实例属性。
        用途：通常用于创建工厂方法，或者在类层级上处理逻辑（而不是针对某个实例）。
        示例：
            ``@classmethod``
            ``def class_method_name(cls):``
            ``    pass``
    3. ``@property`` :
        功能：将方法转换为属性，使得属性可以通过点操作符访问，而不是通过调用方法。
        用途：用于定义只读属性，或者需要计算属性值的属性。
        示例：
            ``@property``
            ``def property_name(self):``
            ``    return self._property_name``
    4. ``@abstractmethod`` :
        功能：用于抽象类中，定义抽象方法。抽象方法是必须在子类中实现的方法。
        用途：确保子类实现特定的方法，适用于设计抽象基类时。
        示例：
            ``@abstractmethod``
            ``def abstract_method_name(self):``
            ``    pass``
    5. ``@functools.wraps`` :
        功能：用于装饰器中，确保装饰过的函数保留原始函数的元数据（如函数名、文档字符串等）。
        用途：当你编写自定义装饰器时，使用 @functools.wraps 可以确保被装饰函数的元数据不被覆盖。
        示例：
            ``@functools.wraps(original_function)``
            ``def decorated_function(*args, **kwargs):``
            ``    return original_function(*args, **kwargs)``
    6. ``@contextmanager`` :
        功能：用于定义上下文管理器，使得代码块在进入和退出时可以执行特定的操作。
        用途：用于管理资源，如文件、网络连接等，确保资源在使用后被正确释放。
        示例：
            ``@contextmanager``
            ``def context_manager():``
            ``    # 进入代码块时的操作``
        

注：
1. 静态方法是什么？
    静态方法是一种特殊的方法，它属于类而不是类的实例。静态方法不需要访问类的实例属性或类属性，因此它们不需要 self 参数。静态方法通常用于执行与类相关的操作，但不需要访问类的状态。
    比如：在类中定义一个静态方法来计算两个数的和，这个方法不需要访问类的任何属性，因此可以定义为静态方法。
2. 类方法是什么？
    类方法是属于类的方法，而不是类的实例。类方法就是说，它们可以通过类名直接调用，而不需要通过创建类的实例来调用。
3. 工厂方法是什么？
    工厂方法是一种设计模式，它用于创建对象，而不是直接使用 new 关键字。工厂方法通常用于创建复杂对象，这些对象可能需要多个步骤来创建，或者需要根据不同的条件创建不同的对象。
    比如：我们创建了一个类，这个类有很多子类，我们想要根据不同的条件来创建不同的子类对象，那么我们可以使用工厂方法来实现。
    工厂方法最初来自于 Java ，但在 Python 中我们通常使用类方法来实现工厂方法。
4. 怎么理解 @fununctools.wraps ?
    当你编写自定义装饰器时，装饰器通常会用一个包装函数（即“ wrapper ”）来包装原函数。这种情况下， Python 会把包装函数的元数据覆盖掉原函数的元数据，使得你调用装饰后的函数时，看到的实际上是包装函数的信息，而不是原函数的信息。
    @functools.wraps 的作用就是将原函数的元数据复制到包装函数中，从而使得装饰后的函数仍然看起来像原函数。
5. @contextmanager 跟 with 语句有什么关系？
    @contextmanager 提供了一种简化的方式来创建上下文管理器，而无需手动实现 __enter__() 和 __exit__() 方法。它允许你通过编写一个生成器函数来创建上下文管理器，利用 yield 关键字来分隔资源的分配和释放。
    对于没有实现上下文管理器协议的对象， with 就不能直接被使用，而需要在该对象对应的类中定义 __enter__() 和 __exit__() 方法以后才能使用，而用 @contextmanager 就能在不定义类的情况下，直接装饰方法即可实现使用上下文管理器
6. @staticmethod 和 @classmethod 的区别是什么？
    静态方法不需要传入类实例（ self ）或类本身（ cls ）作为参数。它是一个与类无关的方法，它只是和类绑定在一起，通常用来执行一些逻辑操作，但不依赖于类或实例的状态。
    当你需要一个属于类的工具方法，但它不需要访问类属性或实例属性时，就可以用静态方法。静态方法本质上跟类没有关联性，它可以像普通函数一样使用，但放在类中是为了逻辑组织上的方便。
    类方法的第一个参数必须是类本身（通常约定命名为 cls ）。这个方法可以访问类的属性或修改类的状态（而不是实例的状态）。
    类方法常用于工厂方法，或者需要修改类级别的属性或行为时。因为它接收的是类本身，所以可以用于类的继承结构中，保证方法在子类中也能正确调用。
    简单而言，静态方法更像是类中一个独立的模块，不会影响类的状态或者受类本身影响；而类方法就是一个与类息息相关的方法，调用类方法会迁一而动全身，改变类本身的状态。
7. 怎么自定义装饰器？
    自定义装饰器通常需要两个函数，一个用于包装原函数，另一个用于定义装饰器本身。装饰器函数接受一个函数作为参数，并返回一个新的函数，这个新的函数通常会在原函数执行前后添加一些额外的逻辑。
    比如：我们想要在调用一个函数前后打印一些日志，我们可以定义一个装饰器函数，然后在装饰器函数中添加打印日志的逻辑，最后将原函数作为参数传递给装饰器函数，得到一个新的函数，这个新的函数就是我们自定义的装饰器。

"""

# @staticmethod 演示
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathHelper.add(2, 3))  # 输出: 5
print("------------------------")

# @classmethod 演示
# 假设我们正在开发一个游戏，不同类型的游戏角色（比如战士、法师、弓箭手）都有各自的攻击方式。我们可以使用工厂方法来根据玩家的选择创建不同的角色对象，而不用每次显式地去实例化不同的类。
# 工厂类
class Character:
    @classmethod
    def create_character(cls, character_type):
        if character_type == 'warrior':
            return Warrior()
        elif character_type == 'mage':
            return Mage()
        elif character_type == 'archer':
            return Archer()
        else:
            raise ValueError(f'Unknown character type: {character_type}')

class Warrior(Character):
    def attack(self):
        return 'Slash a Sword'
    
    # 假设战士职业有一个特殊技能，在子类中也可以重写覆盖工厂逻辑
    @classmethod
    def create_character(cls, character_type):
        if character_type == 'warrior_spell':
            return 'Roar of War'
        return super().create_character(character_type)

class Mage(Character):
    def attack(self):
        return 'Cast Fireballs'

class Archer(Character):
    def attack(self):
        return 'Shoot Arrows'
    
# 使用工厂方法创建角色
warrior1 = Character.create_character('warrior')
mage = Character.create_character('mage')
archer = Character.create_character('archer')

print(warrior1.attack())  # 输出: Slash a Sword
print(mage.attack())  # 输出: Cast Fireballs
print(archer.attack())  # 输出: Shoot Arrows
print('------------------------')

# 使用类方法复写工厂逻辑，使得战士职业拥有特殊技能
warrior_spell = Warrior.create_character('warrior_spell')
warrior2 = Warrior.create_character('warrior')

print(warrior_spell)  # 输出: Roar of War
print(warrior2.attack())  # 输出: Slash a Sword
print('------------------------')

# @functools.wraps 演示
# 定义一个自定义装饰器
def my_decorator1(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

# 定义一个使用自定义装饰器的函数
@my_decorator1
def say_hello(name):
    """This is a function that says hello to someone."""
    print(f"Hello, {name}!")
    
# 调用函数
say_hello("Alice")
# 使用装饰器 my_decorator 包装了原函数 say_hello，却返回了包装函数 wrapper，而不是原函数。
# 这是因为，当调用 say_hello 时，实际上调用的是 wrapper 函数，但 say_hello 原来的 __name__、__doc__ 等元数据丢失了，因此输出的是 wrapper，而不是 say_hello。
# 因此，我们需要使用 functools 模块中的 wraps 装饰器来保留原函数的元数据。
print(say_hello.__name__)  # 输出: wrapper
print(say_hello.__doc__)  # 输出: None
print('------------------------')

# 导入 functools 模块
import functools

# 定义一个自定义装饰器
def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper

# 定义一个使用自定义装饰器的函数
@my_decorator2
def greet(name):
    """This is a function that greets someone."""
    print(f"Hello, {name}!")

# 调用函数
greet("Alice")
# 使用functools.wraps装饰器包装了原函数 greet，成功保留了原函数的元数据。
# @functools.wraps(func) 的作用原理是复制 func 的属性到 wrapper 函数中，包括 __name__、__doc__ 等，因此才能保证输出的是 greet，而不是 wrapper。
print(greet.__name__)  # 输出: greet
print(greet.__doc__)  # 输出: This is a function that greets someone.
print('------------------------')

# @property 演示
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
circle = Circle(5)
# 使用 @property 装饰器将 radius 方法转换为属性，可以直接通过 circle.radius 访问和修改半径。
# 这样做能够更好地封装属性，提供更直观的接口，同时还能在属性被访问或修改时进行额外的操作，也能随时关闭或开启属性的访问权限。
print(circle.radius)  # 输出: 5
circle.radius = 10
print(circle.radius)  # 输出: 10
print('------------------------')

# @abstractmethod 演示
from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Be used outside")

class Desktop(Computer):
    def process(self):
        print("Be used inside")

# 使用 @abstractmethod 装饰器将 process 方法声明为抽象方法，要求子类必须实现该方法。
# 这样做可以确保子类必须实现特定的方法，从而保证了类的接口的一致性。
laptop = Laptop()
desktop = Desktop()

laptop.process()  # 输出: Be used outside
desktop.process()  # 输出: Be used inside
print('------------------------')

# @contextmanager 演示
# 假设要定义一个处理异常的方法，不使用 @contextmanager 装饰器的情况下想要使用 with 语句，就要用类对该方法进行封装， 并实现 __enter__ 和 __exit__ 方法。
class ExceptionHandler:
    def __init__(self, exception_type):
        self.exception_type = exception_type

    def __enter__(self):
        print("Entering the context")
        
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == self.exception_type:
            print(f"Caught an exception of type {exc_type}: {exc_value}")
            print("Exiting the context")
            return True # 返回 True 表示已经处理了异常，不需要再向上抛出
        print("Exiting the context")
        return False  # 返回 False 表示没有处理异常，需要向上抛出

# 使用 with 语句
with ExceptionHandler(ValueError) as handler:
    print("Inside the block")
    raise ValueError("An error occurred")
print('------------------------')

# 如果要用 @contextmanager 装饰器呢？
from contextlib import contextmanager

@contextmanager
def exception_handler(exception_type):
    print("Entering the context")
    try:
        yield
    except exception_type as e:
        print(f"Caught an exception of type {exception_type}: {e}")
    finally:
        print("Exiting the context")

# 使用 with 语句
# 通过使用 @contextmanager 装饰器，可以将处理异常的逻辑封装在一个函数中，并使用 yield 语句将控制权交给 with 语句块。
with exception_handler(ValueError) as handler:
    print("Inside the block")
    raise ValueError("An error occurred")