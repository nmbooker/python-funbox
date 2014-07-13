#! /usr/bin/env python

"""Functions on iterators, optimised for case when iterators are sorted.

Note sift_o is hidden as _sift_o at the moment because it is broken.
Please don't use it.
Once fixed, I'll remove the leading underscore again.
"""

import itertools
import iterators

from iterators import sift_rest         # re-export

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

def _sift_o(sieves, items):
    """Progressively sift out values into a series of chunks.

    Status: WIP, BROKEN DO NOT USE

    Example of sieves:

    >>> lt = lambda y: lambda x: x < y
    >>> sieves = [  ('< 10',         lt(10)),
    ...             ('10 <= x < 50', lt(50)),
    ...             ('>= 50',        sift_rest),
    ...          ]

    The predicates in sieves must be ordered, and the items must be ordered,
    such that once an item is found for which a sieve's predicate is false,
    it can't be true for any of the rest of the items.

    This will help getting a list of people by age range for example,
    by pulling out each age range in turn.

    The order of sieves matters.  An item will go into the first group
    whose predicate it satisfies.

    >>> import pairs
    >>> sifted = list(_sift_o(sieves, [1,2,9,10,11,11,49,50,100]))
    >>> len(sifted)
    3
    >>> pairs.lift_snd(list)(sifted[0])
    ('< 10', [1, 2, 9])
    >>> pairs.lift_snd(list)(sifted[1])
    ('10 <= x < 50', [10, 11, 11, 49])
    >>> pairs.lift_snd(list)(sifted[2])
    ('>= 50', [50, 100])

    BUG: The last test case above returns ('>= 50', [100])
    """
    return iterators._sift(sieves, items, partition_fun=partition_o)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
