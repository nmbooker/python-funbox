#! /usr/bin/env python

"""Tools for dealing with lists and other addressable sequences
"""

from . import validation

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

def categorise(functions, unique=False):
    """categorise(functions, unique=False)(sequence) - Split up a sequence according to functions.

    :: ([a -> bool], bool) -> [a] -> [[a]]

    functions: A list of predicates, one for each list you want as output.
    sequence: The sequence you want to categorise.

    Returns a tuple of lists, one list per function, plus a final list
    for items that weren't captured into any of the other lists.

    Each item from the original sequence can appear in more than one list,
    if more than one of the functions return True for it.

    >>> even = lambda x: x % 2 == 0
    >>> multiple_of_3 = lambda x : x % 3 == 0
    >>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> categorise([even, multiple_of_3])(nums)
    [[2, 4, 6, 8, 10], [3, 6, 9], [1, 5, 7]]
    >>> categorise([even, multiple_of_3], unique=True)(nums)
    [[2, 4, 6, 8, 10], [3, 9], [1, 5, 7]]
    >>> categorise([multiple_of_3, even], unique=True)(nums)
    [[3, 6, 9], [2, 4, 8, 10], [1, 5, 7]]
    """
    def categorise_functions(sequence):
        out_lists = [list() for i in range(len(functions) + 1)]
        for item in sequence:
            caught = False
            for idx, fun in enumerate(functions):
                if fun(item):
                    out_lists[idx].append(item)
                    caught = True
                    if unique:
                        break
            if not caught:
                out_lists[-1].append(item)
        return out_lists
    return categorise_functions

if __name__ == "__main__":
    import doctest
    doctest.testmod()
