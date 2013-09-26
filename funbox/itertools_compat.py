
"""itertools compatibility for Python 2 and 3, for imap and ifilter.

Just use:
    from funbox.itertools_compat import imap, ifilter

instead of:
    from itertools import imap, ifilter

>>> list(imap(int, ['1', '2', '3']))
[1, 2, 3]

>>> is_even = lambda x: (x % 2 == 0)
>>> list(ifilter(is_even, [1, 2, 3, 4]))
[2, 4]
"""

try:
    from itertools import imap
except ImportError:
    imap = map

try:
    from itertools import ifilter
except ImportError:
    ifilter = filter

if __name__ == "__main__":
    import doctest
    doctest.testmod()
