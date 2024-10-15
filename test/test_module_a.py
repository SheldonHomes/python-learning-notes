"""
@File	:	test_module_1.py
@Time	:	2024/09/26
@Author	:	Sheldon Homes
@Version	:	0.0.1
@License	:	(C)Copyright 2024-2024, test
"""

def test_a():
    """
    test function for module a
    
    :return: None
    :rtype: None
    """
    print("testA")
    
def test_b():
    """
    test function for module a

    :return: None
    :rtype: None
    """
    print("testB")
    
# testing the __all__ attribute
__all__ = ["test_a"]