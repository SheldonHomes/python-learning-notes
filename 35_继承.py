"""
面向对象的三种特性：封装、``继承``、多态

继承：子类继承父类的属性和方法，可以直接使用父类的属性和方法，也可以重写父类的方法。
在 Python 中，使用关键字 ``class 子类名(父类名)`` 来实现继承。
    例： 
    class 子类名(父类名):
        pass
继承的好处：继承能够实现代码的复用，提高开发效率。

多继承：一个子类可以继承多个父类，多个父类之间用逗号分隔。
    例：
    class 子类名(父类名1, 父类名2, 父类名3):
        pass
多继承的注意事项：
    1. 如果多个父类中有同名的方法，那么子类会调用第一个父类的方法。
    2. 如果多个父类中有同名的方法，并且第一个父类的方法没有实现，那么子类会调用第二个父类的方法。
    
注： Python 多继承中的 MRO 机制
    MRO（ Method Resolution Order , 方法解析顺序）是 Python 中用于确定类的方法解析顺序的机制。当子类继承多个父类时， Python 会按照一定的顺序来查找方法。比如：
    class A(B, C, D):
        pass
    在这个例子中， Python 会按照 B -> C -> D 的顺序来查找方法。如果想要确定 MRO 的顺序，可以使用 ``A.mro()`` 来查看。
    对于多继承中的父类属性，如果没有事先通过显式调用父类的构造方法，那么父类的属性不会被子类继承，子类创建的对象无法使用父类的属性。
    
方法重写：子类可以重写父类的方法，即在子类中定义一个与父类方法同名的方法，这样子类的方法就会覆盖父类的方法。
    例：
    class 子类名(父类名):
        def 方法名(self):
            pass

调用父类同名成员：在子类中，如果想要调用父类的方法，可以使用 ``super()`` 函数。
    调用成员变量：使用 ``super().成员变量名``
    调用成员方法：使用 ``super().成员方法名()``
除此之外，还可以使用 ``父类名.成员变量名`` 和 ``父类名.成员方法名()`` 来调用父类的成员。

pass: 在 Python 中， pass 是一个空语句，用于占位，表示什么也不做。
pass 关键字能帮助我们在编写继承的代码时，通过占用位的方式，避免出现语法错误。

"""

class Phone: # 父类
    def __init__(self) -> None:
        self.IMEI = "a1533avda4bgfnn76"
        self.producer = "Apple"
    
    def call_by_4g(self) -> str:
        return "4G通话"
        
    def call(self) -> None:
        print(f"正在使用{self.call_by_4g()}进行通话")
        
class PhoneNew(Phone): # 子类，通过继承Phone类，Phone2024类就拥有了Phone类的属性和方法
    def __init__(self) -> None:
        super().__init__() # 调用父类的构造方法
        self.face_id = True
        self.voltage = 0.5
        self.IMEI = "b100a13d53ad5ffda" # 子类可以重写父类的属性
        
    def call_by_5g(self) -> str:
        return "5G通话" # 这个方法只能在子类中使用，如果定义一个父类对象，是无法调用这个方法的
        
    # 重写父类的方法
    def call(self) -> None:
        if self.voltage >= 0.5:
            print(f"正在使用{self.call_by_5g()}进行通话")
        else:
            print(f"正在使用{self.call_by_4g()}进行通话")

# 创建对象
old_phone = Phone()
new_phone = PhoneNew()

# 测试父类属性能否在子类对象中使用
print(new_phone.producer)
# 测试子类属性能否在父类对象中使用
try:
    print(old_phone.face_id)
except AttributeError as e:
    print(e)
for _ in range(50):
    print("-", end="")
print()

# 测试父类方法能否在子类对象中使用
try:
    print(new_phone.call_by_4g())
except AttributeError as e:
    print(e)
# 测试子类方法能否在父类对象中使用
try:
    print(old_phone.call_by_5g())
except AttributeError as e:
    print(e)
for _ in range(50):
    print("-", end="")
print()

# 重写父类属性方法演示
print(old_phone.IMEI)
print(new_phone.IMEI)
old_phone.call()
new_phone.call()

# 多继承演示
# 手机有多种模块，比如NFC、蓝牙、GPS等，这些模块都可以继承Phone类
class NFCReader():
    def __init__(self) -> None:
        self.nfc = True
        self.nfc_version = "5.0"

    def read_nfc(self) -> str:
        return "读取NFC"

class Bluetooth():
    def __init__(self) -> None:
        self.bluetooth = True
        self.bluetooth_version = "5.4"

    def connect_bluetooth(self) -> str:
        return "连接蓝牙"

class GPSDetector():
    def __init__(self) -> None:
        self.gps = True
        self.gps_version = "4.0"

    def detect_gps(self) -> str:
        return "检测GPS"
    
class Phone2024(PhoneNew, NFCReader, Bluetooth, GPSDetector): # 多继承
    def __init__(self) -> None:
        # NFCReader.__init__(self)
        Bluetooth.__init__(self)
        GPSDetector.__init__(self)
    pass # pass关键字表示什么都不做，可以用来占位

phone2024 = Phone2024()
print(phone2024.read_nfc()) # MRO机制可以保证子类可以调用父类的方法
try:
    print(phone2024.nfc) # 由于没有显式调用父类的构造方法，所以父类的属性不会被继承
except AttributeError as e:
    print(e)
print(phone2024.bluetooth)
print(phone2024.gps)
print(phone2024.call_by_5g())
print(phone2024.call_by_4g())