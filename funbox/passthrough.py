#! /usr/bin/env python

"""Provides ways of applying certain values through a function, while leaving others unchanged.

Say you want to convert a list of strings to uppercase, but some entries might
be None for whatever reason, but you want to keep those None values.

Here's a function that converts a string to uppercase:

>>> from operator import methodcaller
>>> toUpper = methodcaller('upper')

Here's how you might use it to uppercase non-None values in a list, keeping
None values intact:

>>> input_strings = ['a', 'b', 'cde', 'f', None, 'g', 'h', None]
>>> [passnone(toUpper)(s) for s in input_strings]
['A', 'B', 'CDE', 'F', None, 'G', 'H', None]

Note that passnone is curried, so you can use map instead:
>>> list(map(passnone(toUpper), input_strings))
['A', 'B', 'CDE', 'F', None, 'G', 'H', None]

Or you could use imap from itertools.

For more complex usage, consider using Option from fn.monad.
"""

from .flogic import fnot

def passnone(f, default=None):
    """passnone(f)(val) returns None if val is None, else f(val).
    """
    def passnone_f(val):
        """Return f(val) if val is not None, else None
        """
        return default if val is None else f(val)
    return passnone_f


def apply_if(predicate, function):
    """apply_if(predicate, function)(val) -> a value or None

    apply_if :: ((a|None -> bool), (a -> b)) -> a|None -> b|None

    If predicate(val) is True or True-like, returns function(val)
    Otherwise returns val as-is.


    >>> contains_a = lambda astr : 'a' in astr
    >>> to_upper = lambda astr : astr.upper()
    >>> strings = ['a', 'b', 'C', 'dear', 'apple', 'rod']
    >>> list(map(apply_if(contains_a, to_upper), strings))
    ['A', 'b', 'C', 'DEAR', 'APPLE', 'rod']
    """
    def pass_if_pf(val):
        return function(val) if predicate(val) else val
    return pass_if_pf

def pass_if(predicate, function):
    """pass_if(predicate, function)(val) -> a value or None

    pass_if :: ((a|None -> bool), (a -> b)) -> a|None -> b|None

    If predicate(val) is False or False-like, returns function(val)
    Otherwise returns val as-is.

    >>> contains_a = lambda astr : 'a' in astr
    >>> to_upper = lambda astr : astr.upper()
    >>> strings = ['a', 'b', 'C', 'dear', 'apple', 'rod']
    >>> list(map(pass_if(contains_a, to_upper), strings))
    ['a', 'B', 'C', 'dear', 'apple', 'ROD']
    """
    return apply_if(fnot(predicate), function)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
