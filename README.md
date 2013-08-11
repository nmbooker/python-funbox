# Functional Toolbox for Python

This is a collection of functional-style tools I've found useful in Python.

Designed to complement the functools, functional, and itertools from the standard library,
and the 'fn' package (https://github.com/kachayev/fn.py) which is available via pip

Note despite being functional in appearance, some of the implementations are stateful,
most notably 'once' which caches an expensively-calculated value the first time it is called
for future invocations.
