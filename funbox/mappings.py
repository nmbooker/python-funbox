#! /usr/bin/env python

"""Functions for transforming dictionaries.

This is to dictionary comprehensions in Python 3 as itertools is to generator
expressions in Python 2 and 3.
This works with Python 2.6, whereas dictionary comprehensions are Python 3 or Python 2.7 and above only.

Notes on currying

I've curried most of the functions in this module, with the exception of
ones that are similar to standard library functions that aren't curried.

Some of those uncurried functions have a
curried version with the same name with _c appended.
So filter_keys_c is a curried version of filter_keys.

Some functions are curried anyway, you'll see where that's the case in the
docstrings e.g. to_dict(funs)(an_object).  These don't necessarily have a _c suffix.
"""

from .itertools_compat import izip
import operator
from functional import partial
from .flogic import fnot

def to_dict(funs):
    """Convert an object to a dict using a dictionary of functions.

    to_dict(funs)(an_object) => a dictionary with keys calculated from functions on an_object

    Note the dictionary is copied, not modified in-place.

    If you want to modify a dictionary in-place, do adict.update(to_dict(funs)(a_dict))

    Use to_dict(funs) in a map, and you can generate a list of dictionaries from a list of objects (which could also be dictionaries).

    :: K is hashable type => {K: (X -> V)} -> [X] -> {K: V}

    Equivalent to the following in Python 3:
     {k: f(an_object) for (k, f) in funs.items()}

    >>> from operator import itemgetter
    >>> funs = {'id': itemgetter('id'), 'fullname': lambda x: '%(forename)s %(surname)s' % x}
    >>> an_object = {'id': 1, 'forename': 'Fred', 'surname': 'Bloggs'}
    >>> result = to_dict(funs)(an_object)
    >>> result['id']
    1
    >>> result['fullname']
    'Fred Bloggs'
    >>> 'forename' in result    # Original keys are left out
    False
    """
    def to_dict_funs(an_object):
        return dict((k, f(an_object)) for (k, f) in funs.items())
    return to_dict_funs


def with_calculated(funs):
    """Return a new dict which is a_dict updated according to the dictionary funs.

    Note the dictionary is copied, not modified in-place.

    >>> funs = {'fullname': lambda x: '%(forename)s %(surname)s' % x}
    >>> a_dict = {'id': 1, 'forename': 'Fred', 'surname': 'Bloggs'}
    >>> result = with_calculated(funs)(a_dict)
    >>> result['id']
    1
    >>> result['fullname']
    'Fred Bloggs'
    >>> result['forename']
    'Fred'
    """
    def with_calculated_funs(a_dict):
        return updated_with(a_dict, to_dict(funs)(a_dict))
    return with_calculated_funs

def updated_with(orig_dict, new_values):
    """Return a copy of orig_dict updated with new_values.

    New keys are added, and the values of existing keys will take the
    values in new_values.

    >>> updated_with({1: 2, 2: 4, 3: 2}, {1: 'two', 4: 'four'})
    {1: 'two', 2: 4, 3: 2, 4: 'four'}
    """
    newdict = dict(orig_dict)
    newdict.update(new_values)
    return newdict

def pull_key(key_fun):
    """Return a new dict with members of objs as values and values generated by key_fun as keys.

    pull_key(key_fun)(objs)

    :: Hashable K => (X -> K) -> Seq[X] -> {K : X}

    Equivalent to the following in Python 3:
      {key_fun(v):v for v in objs}

    >>> from operator import itemgetter
    >>> objs = [{'id': 1, 'name': 'Fred'}, {'id': 3, 'name': 'Wilma'}]
    >>> result = pull_key(itemgetter('id'))(objs)
    >>> sorted(result.keys())
    [1, 3]
    >>> result[1]['id'], result[1]['name']
    (1, 'Fred')
    >>> result[3]['id'], result[3]['name']
    (3, 'Wilma')
    """
    def pull_key_fun(objs):
        return dict((key_fun(value), value) for value in objs)
    return pull_key_fun

def map_values(fun, a_dict):
    """Return copy of a_dict with fun applied to each of its values.

    :: Hashable K => ((X->Y), {K : X}) -> {K : Y}

    Equivalent to the following in Python 3:
      {k:fun(v) for (k, v) in a_dict.items()}

    >>> a_dict = {'a': 2, 'b': 3, 'c': 4}
    >>> times_2 = map_values(lambda x : x*2, a_dict)
    >>> times_2['a']
    4
    >>> times_2['b'], times_2['c']
    (6, 8)
    """
    return dict((k, fun(v)) for (k, v) in a_dict.items())

def map_values_c(fun):
    """Curried version of map_values.

    map_values_c(fun)(a_dict) = map_values(fun, a_dict)
    """
    return partial(map_values, fun)

def coerce_values(spec):
    """coerce_values(spec)(indict) : change some values of indict

    >>> mappings = {'count': int}
    >>> coerced = coerce_values(mappings)({'a': 'foo', 'count': '3000'})
    >>> coerced['count']
    3000
    >>> coerced['a']
    'foo'
    """
    def _coerce_values(indict):
        outdict = dict(indict).copy()
        for k, f in spec.items():
            outdict[k] = f(indict[k])
        return outdict
    return _coerce_values

def without_keys(keys):
    """Return a copy of a_dict with the given keys removed.

    rm_keys(keys)(a_dict)

    :: [K] -> {K:V} -> {K:V}

    Equivalent to the following in Python 3:
      {k:v for (k,v) in a_dict.items() if k not in keys}

    >>> a_dict = {'a': 2, 'b': 3, 'c': 4}
    >>> without_keys(['a', 'b'])(a_dict)
    {'c': 4}
    """
    keys = frozenset(keys)  # frozenset has efficient membership lookup
    return filter_keys_c(fnot(partial(operator.contains, keys)))

def filter_keys(func, a_dict):
    """Return a copy of adict with only entries where the func(key) is True.

    Equivalent to the following in Python 3:
      {k:v for (k, v) in a_dict.items() if func(k)}
    """
    return dict((k, v) for (k, v) in a_dict.items() if func(k))

def filter_keys_c(func):
    """Curried filter_keys.

    filter_keys_c(f)(a_dict) = filter_keys(f, a_dict)
    """
    return partial(filter_keys, func)

def row_to_dict(keys):
    """row_to_dict(keys)(row) => Dictionary built from a row of data.

    keys: A list of key names, in the order they're expected in the row.  Any iterable is OK as long as it is finite and can be iterated over any number of times (a generator is not a good example).
    row: A sequence of data of the same length or longer than keys.

    This function is curried for easy use with map.

    >>> d = row_to_dict(['id', 'forename', 'surname', 'email'])([1, 'Fred', 'Bloggs', 'fred@example.com'])
    >>> sorted(d.keys())
    ['email', 'forename', 'id', 'surname']
    >>> d['email']
    'fred@example.com'
    >>> d['id']
    1
    >>> (d['forename'], d['surname'])
    ('Fred', 'Bloggs')
    """
    return lambda row: dict(izip(keys, row))

def dict_to_row(keys):
    """dict_to_row(keys)(adict) => Row of data containing values of given keys from adict

    >>> dict_to_row(['a', 'c', 'b'])({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    [1, 3, 2]
    """
    return lambda adict: [adict[k] for k in keys]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
