#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 module"""


def simple_lookup(var1, var2):
    """No key access.

    Args:
        var1(mixed): This is an argument variable.
        var2(mixed): This is an argument variable.
        
    Returns:
        Returns an exception.

    Example:
        >>> simple_lookup([1,2], 4)
        Warning: Your index/key doesn't exist.
        [1,2]
        >>> simple_lookup({}, 'banana')
        Warning: Your index/key doesn't exist.
        {}
    """
    try:
        return var1[var2]
    except(IndexError, KeyError):
        print "Warning: Your index/key doesn't exist."
        return var1
