#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""

import datetime


class InvalidAgeError(Exception):
    pass

def get_age(birthyear):
    """This function will check if age is greater than or equal to 0

    Args:
        birthyear(int): year that will be compared
        
    Returns:
        age(int): current year - birthyear
        
    Example:
        >>> get_age(2099)
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>raise InvalidAgeError
        InvalidAgeError
    """

    age = datetime.datetime.now().year - birthyear
    if age >= 0:
        return age
    else:
        raise InvalidAgeError
