#! /usr/bin/env python

"""Further iterator tools.
"""

import itertools

def itercons(new_head, tail):
    """Cons a value onto the beginning of an iterator.

    Like itertools.chain([new_head], tail)

    >>> list(itercons(1, [2, 3, 4]))
    [1, 2, 3, 4]
    """
    return itertools.chain([new_head], tail)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
