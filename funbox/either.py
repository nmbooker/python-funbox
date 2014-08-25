"""Either for Python.

>>> from . import monad
>>> inverse = lambda x: Left('Division by zero') if x == 0 else Right(1.0 / x)
>>> Right(2.0).bind(inverse)
Right(0.5)
>>> Right(0).bind(inverse)
Left('Division by zero')
>>> Left('Nothing to divide by').bind(inverse)
Left('Nothing to divide by')
"""

from . import monad

class Either(monad.Monad):
    def __init__(self, x):
        self._x = x

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._x)

    @classmethod
    def unit(cls, x):
        return Right(x)

    def is_left(self):
        return not self.is_right()

class Left(Either):
    @property
    def message(self):
        return self._x

    def bind(self, f):
        return self

    def is_right(self):
        return False

class Right(Either):
    @property
    def value(self):
        return self._x

    def bind(self, f):
        return f(self._x)

    def is_right(self):
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
