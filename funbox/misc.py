#! /usr/bin/env python

"""Miscellaneous useful functions.
"""

def always(value):
    """always(value)(*args, **kwargs) always returns value

    >>> always(1)()
    1
    >>> always('foo')('fe', 'fi', 0xf0, akw='fum')
    'foo'
    """
    return lambda *args, **kwargs : value

if __name__ == "__main__":
    import doctest
    doctest.testmod()
