
"""Functional Toolbox


Currying
========

Some functions in this are described as 'curried'.

This means they take one or more arguments, and return a function that can take
arguments too.  In Python function currying isn't part of the language, so it
has to be performed using a lexical closure.

Usually, the last level of returned function will take just one argument, which
is the actual item to be processed.

For example, a here's a curried function that adds a fixed number to its target,
and an example of how to use it:

>>> def add(x):
...     return lambda y: x + y
>>> list(map(add(1), [1, 2, 3, 4, 5]))
[2, 3, 4, 5, 6]


Partial Application
===================

If a function isn't curried, you can simulate it by using the 'partial' function
in 'functools':

>>> from functools import partial
>>> def multiply(x, y):
...     return x * y
>>> list(map(partial(multiply, 2), [1, 2, 3, 4, 5]))
[2, 4, 6, 8, 10]
"""
