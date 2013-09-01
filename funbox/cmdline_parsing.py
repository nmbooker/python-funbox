#! /usr/bin/env python

"""Command line parsing.
"""

def is_flag(arg):
    """Return whether arg looks like a flag.

    >>> is_flag('-a')
    True
    >>> is_flag('--foo')
    True
    >>> is_flag('--')
    True

    >>> is_flag('abc')
    False
    >>> is_flag('')
    False
    >>> is_flag('foo-')
    False
    """
    return arg.startswith('-')

def arg_is_natural_num(arg):
    """Return whether the string arg contains a natural number.

    >>> arg_is_natural_num('123')
    True
    >>> arg_is_natural_num('0')
    True
    >>> arg_is_natural_num('-1')
    False
    >>> arg_is_natural_num('1.5')
    False
    >>> arg_is_natural_num('foo2')
    False
    >>> arg_is_natural_num('2foo')
    False
    """
    return arg.isdigit()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
