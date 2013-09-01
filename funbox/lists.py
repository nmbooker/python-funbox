#! /usr/bin/env python

"""Tools for dealing with lists and other addressable sequences
"""

import validation

def all_but_last(n):
    """all_but_last(n)(sequence) => all but the last n items of the sequence

    >>> all_but_last(3)([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4]
    """
    if not validation.is_natural_number(n):
        raise ValueError("n must be an integer from 0 upwards, got %r" % (n,))
    return lambda sequence : sequence[:-n]

def uncons(sequence):
    """uncons(sequence) => (sequence[0], sequence[1:])

    >>> uncons([1, 2, 3, 4, 5])
    (1, [2, 3, 4, 5])
    """
    return sequence[0], sequence[1:]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
