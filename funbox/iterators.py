#! /usr/bin/env python

"""Further iterator tools.
"""

import itertools
from flogic import fnot

def itercons(new_head, tail):
    """Cons a value onto the beginning of an iterator.

    Like itertools.chain([new_head], tail)

    >>> list(itercons(1, [2, 3, 4]))
    [1, 2, 3, 4]
    """
    return itertools.chain([new_head], tail)

def diverge(right_function, items):
    """Return a pair of iterators: left and right

    Items for which right_function returns a true value go into the right iterator.
    Items for which right_function returns a false value go into the left iterator.

    >>> is_odd = lambda x : (x % 2)
    >>> (evens, odds) = diverge(is_odd, [1, 2, 3, 4, 5, 6])
    >>> list(evens)
    [2, 4, 6]
    >>> list(odds)
    [1, 3, 5]
    """
    left_candidates, right_candidates = itertools.tee(items)
    left = itertools.ifilter(fnot(right_function), left_candidates)
    right = itertools.ifilter(right_function, right_candidates)
    return left, right

if __name__ == "__main__":
    import doctest
    doctest.testmod()
