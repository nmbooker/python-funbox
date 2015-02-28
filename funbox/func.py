#! /usr/bin/env python

"""Functions for fiddling around with functions.
"""

def flip(func):
    """Flip the order of arguments of a curried function.

    >>> from .op import lt, gt
    >>> lt(3)(2) == flip(lt)(2)(3)
    True
    
    For example, this shows that we could define lt as being equal to flip(gt):
    >>> lt(3)(2) == flip(gt)(3)(2)
    True
    """
    def _flipped(*args_x, **kwargs_x):
        def _flipped_inner(*args_y, **kwargs_y):
            return func(*args_y, **kwargs_y)(*args_x, **kwargs_x)
        return _flipped_inner
    return _flipped


if __name__ == "__main__":
    import doctest
    doctest.testmod()
