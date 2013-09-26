#! /usr/bin/env python

"""Calculate a value once if needed, use many times.

You might want to use Once() to encapsulate an expensive operation
such as a database lookup whose value you may want to use zero or many
times.

The key feature of this is the function you specify is called only once,
the first time you request it.

It's like a scoped memoize for functions without referential integrity,
where you may or may not want to use a value, but you might want to use it many times,
within the same function call or transaction.

If your function is pure, with referential integrity, consider using a memoizing
library instead.
"""

import logging

logging.basicConfig()
_logger = logging.getLogger(__name__)

class Once(object):
    """Calls an expensive function once when its value is first requested
    instead of lots of times.  The function is never called if it's not needed.

    e.g.
        records = get_set_of_records_from_db()
        company_id = Once(get_config_from_db, 'main_company_id')
        for record in records:
            record['company_id'] = company_id()
            record.save()

    If there were no records in records, the expensive operation
    get_config_from_db would never need to be called.
    If there is a record in records, then get_config_from_db would
    be called once.
    If there are one million records, get_config_from_db is still
    only called once but its cached result is simply reused 999.999 times.


    Here's an entirely unrealistic example for doctesting purposes:
    >>> def super_expensive_operation(foo):
    ...     # pretend there's a big database query in here
    ...     print("Doing super expensive operation")
    ...     return foo.upper()
    >>> get_a = Once(super_expensive_operation, 'apple')
    >>> for item in []:
    ...     print("%s %s" % (get_a(), item))
    >>> # Note nothing was printed, even from super_expensive_operation

    >>> for item in ['hill', 'bunch', 'basket']:
    ...     print("%s %s" % (get_a(), item))
    Doing super expensive operation
    APPLE hill
    APPLE bunch
    APPLE basket
    >>> # That time APPLE was only calculated once, but was used many times
    """
    def __init__(self, function, *args, **kwargs):
        _logger.debug('args = %r' % (args,))
        _logger.debug('kwargs = %r' % (kwargs,))
        self._function = function
        self._args = args
        self._kwargs = kwargs

    def __call__(self):
        if not hasattr(self, '_result'):
            self._result = self._function(*self._args, **self._kwargs)
        return self._result

if __name__ == "__main__":
    import doctest
    import os
    if os.getenv('DEBUG'):
        _logger.setLevel(logging.DEBUG)
    doctest.testmod()
