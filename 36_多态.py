"""
面向对象的三种特性：封装、继承、``多态``

多态：同一个方法，不同的对象，调用时表现出来的行为不同
例：
    class A():
        def run(self) -> None:
            函数体1

    class B():
        def run(self) -> None:
            函数体2

    a = A()
    b = B()

    a.run()
    b.run()
在上面的例子中， a.run() 和 b.run() 调用的都是 run() 方法，但是 a.run() 和 b.run() 表现出来的行为是不同的，这就是多态
在 Python 中，多态是通过继承和重写实现的，多态可以让不同的对象通过相同的接口调用，而不需要关心具体类型。

多态涉及到另一个概念：``抽象类``
抽象类是一种特殊的类，它不能被实例化，只能被继承。抽象类中可以定义抽象方法，抽象方法是一种没有实现的方法，它只能被继承，不能被调用。抽象类的作用是定义一个接口，让子类去实现。
如何使用抽象类：
    1. 使用 pass 占位符定义抽象方法
    2. 使用 ABC 模块的 @abstractmethod 装饰器定义抽象方法
    3. 使用 NotImplementedError 异常定义抽象方法

实际开发中，多态的使用场景非常广泛，比如：``回调函数``、``事件处理``、``插件机制``等

"""
from typing import Callable
from abc import ABC, abstractmethod

# 基础多态解释
class Animal: # 动物类
    def cry(self) -> None:
        pass

class Dog(Animal): # 狗类
    def cry(self) -> None:
        print('汪汪汪')

class Cat(Animal): # 猫类
    def cry(self) -> None:
        print('喵喵喵')

# 统一接口
def animal_cry(animal: Animal) -> None:
    animal.cry()

# 多态演示
dog = Dog()
cat = Cat()
animal_cry(dog)
animal_cry(cat)
print('------------------------')

# 多态的开发应用示例1：回调函数
# 定义两个回调函数
def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

# 通用接口，可以接收任何回调函数
def execute_callback(callback: Callable[[int, int], int], a: int, b: int) -> int:
    return callback(a, b)

# 演示效果
# 调用 add 和 sub ，虽然两者行为不同，但是都可以通过 execute_callback 调用
print(execute_callback(add, 1, 2))
print(execute_callback(sub, 1, 2))
print('------------------------')

# 多态的开发应用示例2：事件处理
# 定义一个事件处理类
class EventHandler:
    def handle(self, event: str) -> None:
        raise NotImplementedError('子类未定义该方法')
    
# 定义两个事件处理类
class MouseEventHandler(EventHandler):
    def handle(self, event: str) -> None:
        print(f'鼠标事件处理：{event}')

class KeyboardEventHandler(EventHandler):
    def handle(self, event: str) -> None:
        print(f'键盘事件处理：{event}')

# 定义一个事件处理接口
def event_handler(event: str, handler: EventHandler) -> None:
    return handler.handle(event)

# 演示效果
# 创建两个事件处理对象
mouse_handler = MouseEventHandler()
keyboard_handler = KeyboardEventHandler()
# 通过接口调用事件处理对象
event_handler('鼠标左键点击', mouse_handler)
event_handler('键盘按下A键', keyboard_handler)
print('------------------------')

# 多态的开发应用示例3：插件机制
# 定义插件基类
class Plugin(ABC):
    @abstractmethod
    def perform_action(self) -> None:
        pass

# 定义两个插件类
class PluginA(Plugin):
    def perform_action(self) -> None:
        print('插件A正在运行')

class PluginB(Plugin):
    def perform_action(self) -> None:
        print('插件B正在运行')
        
# 定义插件管理器类
class PluginManager:
    def __init__(self) -> None:
        self.plugins = []
        
    def add_plugin(self, plugin: Plugin) -> None:
        self.plugins.append(plugin)

    def run_plugins(self) -> None:
        plugin: Plugin
        for plugin in self.plugins:
            plugin.perform_action()

# 演示效果
# 创建两个插件对象
plugin_a = PluginA()
plugin_b = PluginB()
# 创建插件管理器对象
plugin_manager = PluginManager()
# 添加插件到插件管理器
plugin_manager.add_plugin(plugin_a)
plugin_manager.add_plugin(plugin_b)
# 运行插件
plugin_manager.run_plugins()