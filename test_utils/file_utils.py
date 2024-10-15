"""
This module provides utilities for file operations.

It includes functions and classes to print the content of a file in command line, and to append data to a file.

Functions
---------
**file_info_print**(filepath: ``string``) -> ``none``: prints the content of a file in command line, and if the file does not exist, it prints a message

**file_info_append**(filepath: ``string``, data: ``string``) -> ``none``: appends data to a file

Usage Example
-------------
Here's an example of how to use this module:
.. code:: python
    from file_utils import file_info_print, file_info_append
    file_info_print(filepath)
    file_info_append(filepath, data)

:author: Sheldon Homes
:version: 0.0.1
"""

def file_info_print(filepath: str) -> None:
    """
    the function prints the content of a file in command line, and if the file does not exist, it prints a message
    
    :param filepath: the path of the file to be read
    :type filepath: string
    """
    try:
        f = open(filepath, 'r')
        print(f.read())
    except FileNotFoundError:
        print('file not found')
    finally:
        # detect if the file is opened
        if 'f' in locals():
            f.close()

def file_info_append(filepath: str, data: str) -> None:
    """
    the function appends data to a file
    
    :param filepath: the path of the file to be read
    :type filepath: string
    :param data: the data to be appended
    :type data: string
    """
    with open(filepath, 'a') as f:
        f.write(data)