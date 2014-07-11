
"""itertools compatibility for Python 2 and 3, for imap, izip and ifilter.

Just use:
    from funbox.itertools_compat import imap, izip, ifilter, ifilterfalse

instead of:
    from itertools import imap, izip, ifilter, ifilterfalse

>>> list(imap(int, ['1', '2', '3']))
[1, 2, 3]

>>> is_even = lambda x: (x % 2 == 0)

>>> list(ifilter(is_even, [1, 2, 3, 4]))
[2, 4]

>>> list(ifilterfalse(is_even, [1, 2, 3, 4]))
[1, 3]

>>> list(izip([1,2,3], [4,5,6]))
[(1, 4), (2, 5), (3, 6)]
"""

try:
    from itertools import imap
except ImportError:
    imap = map

try:
    from itertools import ifilter
except ImportError:
    ifilter = filter

try:
    from itertools import izip
except ImportError:
    izip = zip

try:
    from itertools import ifilterfalse
except ImportError:
    from itertools import filterfalse as ifilterfalse

if __name__ == "__main__":
    import doctest
    doctest.testmod()
