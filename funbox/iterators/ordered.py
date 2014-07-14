#! /usr/bin/env python

"""Functions on iterators, optimised for case when iterators are sorted.
"""

import itertools
from .. import iterators

def partition_o(left_function, items):
    """Return a pair of iterators: left and right

    Items for which left_function returns a true value go into left.
    Items for which left_function returns a false value go into right.

    Items must be sorted such that left_function may be true for an
    initial set of items, but once an item is found such that
    left_function(item) is false, it will remain false for the rest of the
    items.

    In other words the following must hold:
     for all N where 0 <= N < (len(items) - 1) :
        not(func(item[n])) => not(func(item[n+1]))

    For example lambda x: x < 3 is a valid function for [1,2,3,4,5], but
    not for [1,3,4,2,5].

    >>> (left, right) = partition_o(lambda x: x < 3, [-1, 0, 2, 3, 4, 5])
    >>> list(left)
    [-1, 0, 2]
    >>> list(right)
    [3, 4, 5]
    """
    left = itertools.takewhile(left_function, items)
    right = itertools.dropwhile(left_function, items)
    return left, right


if __name__ == "__main__":
    import doctest
    doctest.testmod()
