
"""Provide a monad interface for Python.
"""

class MonadError(Exception):
    pass

class Monad(object):
    """You must override:
    
    * __init__() to implement 'unit'
    * At least one of 'bind()' or 'join()'.
    """
    @classmethod
    def unit(cls, *args, **kwargs):
        """Return the basic case with the value.
        
        Should be implemented via __init__ in your base subclass.
        """
        raise NotImplementedError()

    def bind(self, f):
        """Monad m a => (a -> m a) -> m a
        """
        return lift(g)(self).join()

    def blind(self, other):
        """Bind constant other monad, not a function returning a monad."""
        return self.bind(lambda: other)

    def fail(self, msg):
        """Fail with given message."""
        raise MonadError(msg)

    def join(self):
        """Flatten monad inside monad to just one level of monad."""
        return self.bind(lambda x: x)

    def fmap(self, f):
        return self.bind(lambda x: self.__class__.unit(f(x)))

def liftM(f):
    """Lift function f to take and return a monad.
    """
    def _lifted(m):
        return m.fmap(f)
    return _lifted

def bindl(f):
    def _bound(m):
        return m.bind(f)
    return _bound
