"""
面向对象的三种特性：``封装``、继承、多态

封装：将属性和方法封装到类中，对外隐藏实现细节，只暴露出必要的接口。
在 Python 中，类通过私有成员与公共成员来封装属性和方法。
    私有成员变量：以双下划线开头，如 __name ，只能在类的内部访问。
    私有成员方法：以双下划线开头，如 __func() ，只能在类的内部调用。
封装的好处：封装能够保护类的内部实现，防止外部代码对类的内部进行非法操作。

"""

# 封装演示
# 定义手机类
class Phone:
    # 私有成员变量
    __current_voltage = 0.5 # 当前电压
    
    # 私有成员方法
    def __using_single_cpu(self):
        print('使用单核CPU运行')
        
    def __using_double_cpu(self):
        print('使用双核CPU运行')

    # 公共成员方法
    # 虽然私有成员变量与私有成员方法不能在类的外部直接访问，但可以通过公共成员方法间接访问
    def using_cpu(self):
        if self.__current_voltage <= 0.5:
            self.__using_single_cpu()
        else:
            self.__using_double_cpu()
            
# 创建手机对象
phone = Phone()

# 测试私有成员变量与私有成员方法是否能在外部直接访问
try:
    print(phone.__current_voltage)
except AttributeError as e:
    print(e)

try:
    phone.__using_single_cpu()
except AttributeError as e:
    print(e)
            
# 公共成员方法可以间接访问私有成员变量与私有成员方法
phone.using_cpu()
print("----------------------")

