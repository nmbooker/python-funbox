#! /usr/bin/env python

"""Functions useful for dealing with pairs.

The pairs this deals with are precisely 2-tuples.

Some of these functions may appear to work with lists and other
indexable sequences, or sequences of length other than two,
but please don't rely on it remaining so in the future.
"""

def fst(pair):
    """Return the first element of pair
    """
    return pair[0]

def snd(pair):
    """Return the second element of pair
    """
    return pair[1]

def lift_fst(f):
    """Lift a function f onto the first element of a 2-tuple.
    >>> lift_fst(list)(('abc', 'def'))
    (['a', 'b', 'c'], 'def')
    """
    return lambda pair: (f(pair[0]), pair[1])

def lift_snd(f):
    """Lift a function f onto the second element of a 2-tuple.
    >>> lift_snd(list)(('abc', 'def'))
    ('abc', ['d', 'e', 'f'])
    """
    return lambda pair: (pair[0], f(pair[1]))

def swap(pair):
    """Swap the items in a pair.  Return tuple.

    >>> swap((1, 2))
    (2, 1)
    """
    x, y = pair
    return y, x

if __name__ == "__main__":
    import doctest
    doctest.testmod()