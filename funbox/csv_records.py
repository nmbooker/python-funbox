#! /usr/bin/env python

"""Tools for transforming CSV records and lists of CSV records.
"""

try:
    from itertools import izip
except ImportError:
    # For Python 3 compatibility
    izip = zip

def add_column(existing_rows, new_column):
    """Take an existing iterable of rows, and add a new column of data to it.

    >>> old = [['fred', 43], ['wilma', 34]]
    >>> gender_column = ['male', 'female']
    >>> list(add_column(old, gender_column))
    [['fred', 43, 'male'], ['wilma', 34, 'female']]
    """
    for row, new_field in izip(existing_rows, new_column):
        row_copy = row[:]
        row_copy.append(new_field)
        yield row_copy

if __name__ == "__main__":
    import doctest
    doctest.testmod()
