"""
@File	:	test_module_1.py
@Time	:	2024/09/26
@Author	:	Sheldon Homes
@Version	:	0.0.1
@License	:	(C)Copyright 2024-2024, test
"""

def test_function_1(test_param1, test_param2):
    """
    test function for test_module_1 used in '29_自定义模块.py'
    
    :param test_param1: the first parameter
    :type test_param1: int
    :param test_param2: the second parameter
    :type test_param2: int
    :return: the result of test_param1 minus test_param2
    :rtype: int
    """
    print(f"test_function_1: {test_param1} minus {test_param2}")
    return test_param1 - test_param2

# using main module to test the function
if __name__ == '__main__':
    print(test_function_1(1, 2))