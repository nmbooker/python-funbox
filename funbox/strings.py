#! /usr/bin/env python

"""Tools for strings.
"""

import re as _re
from . import once as _once

_WORDS_RE = _once.Once(_re.compile, r'\w+')

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

def words(string):
    r"""Return string split into words.

    >>> words('abc def     ghi\njkl\n')
    ['abc', 'def', 'ghi', 'jkl']
    """
    return _WORDS_RE().findall(string)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
