#!/usr/bin/env python

"""Maybe for Python.

Lets you return and propagate null values through a series of operations.

>>> from . import monad
>>> inverse = lambda x: Nothing() if x == 0 else Just(1.0 / x)
>>> Just(2.0).bind(inverse)
Just(0.5)
>>> Just(0).bind(inverse)
Nothing()
>>> Nothing().bind(inverse)
Nothing()
>>> add_1 = lambda x : x + 1
>>> monad.liftM(add_1)(Just(0))
Just(1)
>>> monad.liftM(add_1)(Nothing())
Nothing()
"""

from . import monad

class Maybe(monad.Monad):
    @classmethod
    def unit(cls, x):
        return Just(x)

class Just(Maybe):
    def __init__(self, x):
        self._x = x

    @property
    def value(self):
        return self._x

    def bind(self, f):
        return f(self.value)

    def __repr__(self):
        return "Just(%r)" % self.value

class Nothing(Maybe):
    def __init__(self):
        pass

    def bind(self, f):
        return self

    def __repr__(self):
        return "Nothing()"

if __name__ == "__main__":
    import doctest
    doctest.testmod()
