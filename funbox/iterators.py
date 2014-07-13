#! /usr/bin/env python

"""Further iterator tools.
"""

import itertools
from itertools_compat import ifilter, imap, ifilterfalse
import pairs
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
    left = ifilterfalse(right_function, left_candidates)
    right = ifilter(right_function, right_candidates)
    return left, right

def partition(left_function, items):
    """Like 'diverge' except the values passing left_function go into the
    left hand side of the tuple, and otherwise go into the right.

    >>> is_odd = lambda x : (x % 2)
    >>> (odds, evens) = partition(is_odd, [1, 2, 3, 4, 5, 6])
    >>> list(evens)
    [2, 4, 6]
    >>> list(odds)
    [1, 3, 5]
    """
    return pairs.swap(diverge(left_function, items))

def sift(sieves, items):
    """Progressively sift out values into a series of chunks.

    This will help getting a list of people by age range for example,
    by pulling out each age range in turn.

    The order of sieves matters.  An item will go into the first group
    whose predicate it satisfies.

    >>> import pairs
    >>> lt = lambda y: lambda x: x < y
    >>> sieves = [('< 10', lt(10)), ('10 <= x < 50', lt(50)), ('>= 50', sift_rest)]
    >>> sifted = list(sift(sieves, [1,2,9,10,11,10,9,11,49,50,49,100]))
    >>> len(sifted)
    3
    >>> pairs.lift_snd(list)(sifted[0])
    ('< 10', [1, 2, 9, 9])
    >>> pairs.lift_snd(list)(sifted[1])
    ('10 <= x < 50', [10, 11, 10, 11, 49, 49])
    >>> pairs.lift_snd(list)(sifted[2])
    ('>= 50', [50, 100])
    """
    return _sift(sieves, items, partition_fun=partition)

def _sift(sieves, items, partition_fun=partition):
    rest = items
    for (label, predicate) in sieves:
        (matching, rest) = partition_fun(predicate, rest)
        yield (label, matching)


def sift_rest(x):
    """Predicate to consume the rest of an sequence in a sift operaton.

    >>> [(x, list(y)) for (x,y) in sift([('catchall', sift_rest)], range(6))]
    [('catchall', [0, 1, 2, 3, 4, 5])]
    """
    return True

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
