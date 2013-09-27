#! /usr/bin/env python

"""Tools for strings.
"""

def join(sep):
    """join(sep)(iterable) Join strings in iterable with sep.

    str -> [str] -> str

    >>> comma_separate = join(', ')
    >>> comma_separate(['a', 'b', 'c', 'd'])
    'a, b, c, d'
    """
    def join_sep(iterable):
        return sep.join(iterable)
    return join_sep


if __name__ == "__main__":
    import doctest
    doctest.testmod()
