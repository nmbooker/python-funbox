#! /usr/bin/env python

"""Perform logic on predicate functions.
"""

def fnot(predicate):
    """Not the return value of predicate at call time.

    >>> is_odd = lambda num: bool(num % 2)
    >>> is_even = fnot(is_odd)
    >>> is_odd(2)
    False
    >>> is_even(2)
    True
    """
    return lambda val: not predicate(val)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
