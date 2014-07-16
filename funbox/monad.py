
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
        return cls(*args, **kwargs)

    def bind(self, f):
        """Monad m a => (a -> m a) -> m a
        """
        return lift(g)(self).join()

    def blind(self, other):
        return self.bind(lambda: other)

    def fail(self, msg):
        raise MonadError(msg)

    def join(self):
        return self.bind(lambda x: x)

    def fmap(self, f):
        return self.bind(lambda x: self.__class__.unit(f(x)))

def lift(f):
    def _lifted(m):
        return m.fmap(f)
    return _lifted
