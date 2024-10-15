"""
This module provides utilities for string manipulation.

It includes functions and classes to reverse a string and slice a string more conveniently.

Functions
---------
**str_reverse**(str: ``string``) -> ``string``: reverse the string which is given

**str_slice**(str: ``string``, start: ``int``, end: ``int``) -> ``string``: function_description

Usage Example
-------------
Here's an example of how to use this module:
.. code:: python
    from str_utils import str_reverse, str_slice
    param1 = str_reverse(string)
    param2 = str_slice(string, start, end)

:author: Sheldon Homes
:version: 0.0.1
"""
def str_reverse(str: str) -> str:
    """
    reverse the string which is given
    
    :param str: the string which will be reversed
    :type str: string
    :return: the reversed string
    :rtype: string
    """
    return str[::-1]

def str_slice(str: str, start: int, end: int) -> str:
    """
    slice the string which is given, start from the 'start' parameter and end at the 'end' parameter
    
    :param str: the string which will be sliced
    :type str: string
    :param start: the start index of the slice(excluded)
    :type start: int
    :param end: the end index of the slice(included)
    :type end: int
    :return: the portion of the string which is sliced
    :rtype: string
    """
    return str[start - 1:end + 1]