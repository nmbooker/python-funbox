#! /usr/bin/env python

"""Further iterator tools.
"""

import itertools
from itertools_compat import ifilter, imap
from flogic import fnot
import functools

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
    left = ifilter(fnot(right_function), left_candidates)
    right = ifilter(right_function, right_candidates)
    return left, right

def imap_c(func):
    """imap_c(func)(iterable) = itertools.imap(func, iterable)

    (a -> b) -> iter[a] -> iter[b]

    >>> list(imap_c(int)(['1', '2', '3']))
    [1, 2, 3]
    """
    return functools.partial(imap, func)

def ifilter_c(func):
    """ifilter_c(func)(iterable) = itertools.ifilter(func, iterable)

    (a -> bool) -> iter[a] -> iter[a]

    >>> list(ifilter_c(lambda x: x % 2 == 0)([1, 2, 3, 4]))
    [2, 4]
    """
    return functools.partial(ifilter, func)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
