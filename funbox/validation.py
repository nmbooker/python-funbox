#! /usr/bin/env python

"""Validation functions."""

def is_natural_number(n):
    """Return whether n is an integer >= 0

    >>> is_natural_number(0)
    True
    >>> is_natural_number(1)
    True
    >>> is_natural_number(8474372938474373823483927843392837439)
    True
    >>> is_natural_number('1')
    False
    >>> is_natural_number(-1)
    False
    >>> is_natural_number(1.5)
    False
    """
    return is_int(n) and n >= 0

def is_int(n):
    """Return whether n is an int or long type
    >>> is_int(0)
    True
    >>> is_int(1)
    True
    >>> is_int(-1)
    True
    >>> is_int(8474372938474373823483927843392837439)
    True
    >>> is_int(1.5)
    False
    >>> is_int('1')
    False
    """
    int_types = (int,)
    try:
        int_types += (long,)
    except NameError:
        # This takes care of there not being a 'long' type in Python 3
        pass
    return isinstance(n, int_types)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
