#! /usr/bin/env python

"""Further iterator tools.
"""

import itertools
from ..itertools_compat import ifilter, imap, ifilterfalse
from .. import pairs
import functools


def itercons(new_head, tail):
    """Cons a value onto the beginning of an iterator.

    Like itertools.chain([new_head], tail)

    >>> list(itercons(1, [2, 3, 4]))
    [1, 2, 3, 4]
    """
    return itertools.chain([new_head], tail)


def diverge(right_function, items):
    """Return a pair of iterators: (left, right)

    right will yield values where right_function(val) is truthy.
    left will yield values where right_function(val) is falsey.

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


def partition_strict(left_function, items):
    """Like 'partition' but returns two lists instead of lazy iterators.

    Should be faster than partition because it only goes through 'items' once.

    >>> is_odd = lambda x : (x % 2)
    >>> partition_strict(is_odd, [1, 2, 3, 4, 5, 6])
    ([1, 3, 5], [2, 4, 6])
    """
    left = []
    right = []
    for item in items:
        (left if left_function(item) else right).append(item)
    return (left, right)


def sift(sieves, items):
    """Progressively sift out values into a series of chunks.

    This will help getting a list of people by age range for example,
    by pulling out each age range in turn.

    The order of sieves matters.  An item will go into the first group
    whose predicate it satisfies.

    >>> from ..op import lt
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


def sift_strict(sieves, items):
    """Strict version of 'sift' - you get [(label, list)] instead of
    [(label, iterator)].

    Profiling suggests that this is slightly faster when len(sieves) == 2,
    but the greater the number of sieves, the bigger the advantage of using
    sift_strict over sift.

    Here I sift with just two levels (low and gargantuan):
        devbox% python profilem.py
        Test it does what we want...
        Partition to high and low 1 lots of 1000000 numbers...
        0.57293009758
        Partition strictly to high and low 1 lots of 1000000 numbers...
        0.493767023087

    And then I adjust my script to have six levels (low, med, high, huge,
    massive, gargantuan):

        Test it does what we want...
        Partition to high and low 1 lots of 1000000 numbers...
        1.74753117561
        Partition strictly to high and low 1 lots of 1000000 numbers...
        1.38616394997

    Note the much more marked difference between the two figures - add
    a little more than 0.1 of a second for each extra sieve.

    If you're going to run this repeatedly over a million numbers, the
    improvements will soon stack up.

    >>> from ..op import lt
    >>> sieves = [('< 10', lt(10)), ('10 <= x < 50', lt(50)), ('>= 50', sift_rest)]
    >>> sifted = list(sift_strict(sieves, [1,2,9,10,11,10,9,11,49,50,49,100]))
    >>> len(sifted)
    3
    >>> sifted[0]
    ('< 10', [1, 2, 9, 9])
    >>> sifted[1]
    ('10 <= x < 50', [10, 11, 10, 11, 49, 49])
    >>> sifted[2]
    ('>= 50', [50, 100])
    """
    # The only implementation difference between this and
    # sift is the partition function used.
    return _sift(sieves, items, partition_fun=partition_strict)


def _sift(sieves, items, partition_fun):
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


def concat(iterables):
    """Return iterables concatenated into one iterable.

    >>> list(concat([[1, 2, 3], [4, 5, 6]]))
    [1, 2, 3, 4, 5, 6]
    """
    return itertools.chain(*iterables)


def concat_map(f, xs):
    """Map function f over an iterable xs and concatenate the results.

    This is useful if you want to return a variable number of items
    into your output list from your input list.

    For example you may be building a list of arguments for a program
    that takes the same option multiple times with a different
    argument each time:

    >>> dash_a_option = lambda x: ['-a', x]
    >>> list(concat_map(dash_a_option, ['a', 'b', 'c']))
    ['-a', 'a', '-a', 'b', '-a', 'c']
    """
    return concat(imap(f, xs))


def at_least(number, iterator):
    """Return whether at least number items in iterator are truthy.

    This consumes the iterator lazily, exiting as soon as the count
    hits the given number.  So in some cases it will be quicker than
    len(list(iterator)) >= number

    >>> at_least(2, [False, 3, None, ''])
    False
    >>> at_least(2, [False, 3, None, 'something'])
    True

    It's really designed for use with generator expressions:
    >>> at_least(2, (x > 10 for x in range(11)))
    False
    >>> at_least(2, (x > 10 for x in range(13)))
    True
    """
    count = 0
    for item in iterator:
        if item:
            count += 1
        if count >= number:
            return True
    return False


def at_most(number, iterator):
    """Return whether at most number items in iterator are truthy.

    This consumes the iterator lazily, exiting as soon as the count hits
    the given number.
    >>> at_most(2, [False, 3, None, ''])
    True
    >>> at_most(2, [False, 3, True, 'something'])
    False

    It's really designed for use with generator expressions:
    >>> at_most(2, (x > 10 for x in range(13)))
    True
    >>> at_most(2, (x > 10 for x in range(14)))
    False
    """
    count = 0
    for item in iterator:
        if item:
            count += 1
        if count > number:
            return False
    return True



if __name__ == "__main__":
    import doctest
    doctest.testmod()
