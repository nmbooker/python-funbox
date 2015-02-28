#! /usr/bin/env python

"""Curried operators.

Useful for map, filter, takewhile, iterators.partition, iterators.sift etc

This example may look slightly contrived, but if we were passing data into
something more than a simple list comprehension it's worth having this
kind of abstraction.

>>> from datetime import date
>>> from functional import compose
>>> from operator import attrgetter
>>> from .iterators import partition
>>> today = date(2014, 7, 13)
>>> other_dates = [date(2014, 7, 12), date(2014, 7, 1)]
>>> days_old = compose(attrgetter('days'), take_away_from(today))
>>> # It's in the arguments of functions like partition that these
>>> # curried operators become useful.
>>> (older, newer) = partition(compose(ge(7), days_old), other_dates)
>>> list(older)
[datetime.date(2014, 7, 1)]
>>> list(newer)
[datetime.date(2014, 7, 12)]
"""

from __future__ import division
from functools import partial

def lt(y):
    """lt(y)(x) = x < y

    >>> list(filter(lt(3), [1,2,3,4,5]))
    [1, 2]
    """
    return lambda x : x < y

def le(y):
    """le(y)(x) = x <= y

    >>> list(filter(le(3), [1,2,3,4,5]))
    [1, 2, 3]
    """
    return lambda x : x <= y

def gt(y):
    """gt(y)(x) = x > y

    >>> list(filter(gt(3), [1,2,3,4,5]))
    [4, 5]
    """
    return lambda x : x > y

def ge(y):
    """ge(y)(x) = x > y

    >>> list(filter(ge(3), [1,2,3,4,5]))
    [3, 4, 5]
    """
    return lambda x : x >= y

def eq(y):
    """eq(y)(x) = x == y

    >>> list(filter(eq(3), [1,2,3,4,5]))
    [3]
    """
    return lambda x : x == y

def ne(y):
    """eq(y)(x) = x != y

    >>> list(filter(ne(3), [1,2,3,4,5]))
    [1, 2, 4, 5]
    """
    return lambda x : x != y

def add(y):
    """add(y)(x) = x + y

    Be careful with types where + is not commutative.

    >>> add(2)(3)
    5
    """
    return lambda x : x + y

def mul(y):
    """mul(y)(x) = x * y

    Be careful with types where * is not commutative.

    >>> mul(2)(3)
    6
    >>> mul(5)('a')
    'aaaaa'
    """
    return lambda x : x * y

def take_away(y):
    """take_away(y)(x) = x - y

    Be careful with this because subtraction is not commutative.
    The flipped version of this is 'take_away_from'

    >>> list(map(take_away(2), [1,2,3,4,5]))
    [-1, 0, 1, 2, 3]
    """
    return lambda x : x - y

def take_away_from(y):
    """take_away_from(y)(x) = y - x

    Be careful with this because subtraction is not commutative.
    The flipped version of this is 'take_away'

    >>> list(map(take_away_from(2), [1,2,3,4,5]))
    [1, 0, -1, -2, -3]
    """
    return lambda x : y - x

def divide_by(y):
    """divide_by(y)(x) = x / y

    Note I'm using the future division here - the answer on two ints will
    be a float.

    Be careful with this because division is not commutative.

    You may be interested in func.flip(divide_by) to reverse the arguments.

    >>> divide_by(2)(4)
    2.0
    >>> divide_by(2)(5)
    2.5
    >>> from .func import flip
    >>> flip(divide_by)(5)(2)
    2.5
    """
    return lambda x : x / y

def intdiv_by(y):
    """intdiv_by(y)(x) = x // y

    Be careful with this because division is not commutative.

    You may be interested in func.flip(intdiv_by) to reverse the arguments.

    >>> intdiv_by(2)(4)
    2
    >>> intdiv_by(2)(5)
    2
    >>> from .func import flip
    >>> flip(intdiv_by)(5)(2)
    2
    """
    return lambda x : x // y

def divmod_by(y):
    """divmod_by(y)(x) = divmod(x, y)

    Be careful with this because division is not commutative.

    You may be interested in func.flip(divmod_by) to reverse the arguments.

    >>> divmod_by(2)(4)
    (2, 0)
    >>> divmod_by(2)(5)
    (2, 1)
    >>> from .func import flip
    >>> flip(divmod_by)(5)(2)
    (2, 1)
    """
    return lambda x : divmod(x, y)

def modulo(y):
    """modulo(y)(x) = x % y

    Be careful with this because the % operator is not commutative.

    You may be interested in func.flip(modulo) to reverse the arguments.

    >>> modulo(2)(4)
    0
    >>> modulo(2)(5)
    1
    >>> from .func import flip
    >>> flip(modulo)(5)(2)
    1
    """
    return lambda x : x % y

def fmt(obj):
    """fmt(obj)(form) = form % obj

    With this ordering, this is useful for formatting a fixed object
    in many different ways, for example:

    >>> list(map(fmt(10), ["0x%x", "%d"]))
    ['0xa', '10']

    If you want to format lots of objects according to the same spec,
    use format_as.
    """
    return lambda format_string : format_string % obj

def format_as(format_string):
    """format_as(form)(obj) = form % obj

    Useful to format many objects with the same format string.

    >>> list(map(format_as("0x%x"), [0, 1, 10, 11, 15]))
    ['0x0', '0x1', '0xa', '0xb', '0xf']
    """
    return lambda obj : format_string % obj

if __name__ == "__main__":
    import doctest
    doctest.testmod()
