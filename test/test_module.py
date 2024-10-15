"""
@File	:	test_module.py
@Time	:	2024/09/26
@Author	:	Sheldon Homes
@Version	:	0.0.1
@License	:	(C)Copyright 2024-2024 Sheldon Homes, Test
"""

def test_function(test_param1, test_param2):
    """
    test function for test_module.py used in '29_自定义模块.py'
    
    :param test_param1: the first parameter
    :type test_param1: int
    :param test_param2: the second parameter
    :type test_param2: int
    :return: the sum of test_param1 and test_param2
    :rtype: int
    """
    print(f"test function: add {test_param1} and {test_param2}")
    return test_param1 + test_param2