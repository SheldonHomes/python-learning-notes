# initialize the __all__ variable to control what is imported when using from package import *
__all__ = ['test_module1', 'test_module2']

# import modules in order to directly import them from the package
from .test_module1 import print_info_1
from .test_module2 import print_info_2

# initialize the package, e.g. initialize configuration, print test messages, etc.
print("test_package initialized")