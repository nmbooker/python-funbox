#! /usr/bin/env python

"""Date and time formatting and parsing functions.
"""

import datetime
from functional import compose

def convert_format(from_format, to_format):
    """convert_format(from_format, to_format)(timestr) -> str
    
    Convert between two time formats.

    >>> convert_format('%d/%m/%Y', '%Y-%m-%d')('21/12/2112')
    '2112-12-21'
    """
    return compose(strftime(to_format), strptime(from_format))

def strptime(from_format):
    """strptime(from_format)(timestr) -> datetime.datetime

    Return datetime object from timestr according to from_format.

    :: str -> str -> datetime.datetime

    >>> strptime('%d/%m/%Y')('21/12/2112').date()
    datetime.date(2112, 12, 21)
    """
    return lambda timestr: datetime.datetime.strptime(timestr, from_format)

def strftime(to_format):
    """strftime(to_format)(dt_obj) -> str

    Return datetime, time or date object dt_obj formatted with to_format.

    :: str -> (datetime.datetime|datetime.date|datetime.time) -> str

    >>> strftime('%Y-%m-%d')(datetime.date(2112, 12, 21))
    '2112-12-21'
    """
    return lambda dt_obj: dt_obj.strftime(to_format)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
