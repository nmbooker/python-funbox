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
    return isinstance(n, (int, long)) and n >= 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
