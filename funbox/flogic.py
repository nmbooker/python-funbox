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

def f_all(predicate, iterable):
    """Return whether predicate(i) is True for all i in iterable

    >>> is_odd = lambda num: (num % 2 == 1)
    >>> f_all(is_odd, [])
    True
    >>> f_all(is_odd, [1, 3, 5, 7, 9])
    True
    >>> f_all(is_odd, [2, 1, 3, 5, 7, 9])
    False
    """
    return all(predicate(i) for i in iterable)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
