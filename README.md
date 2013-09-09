# Functional Toolbox for Python

This is a collection of highly-generic functions I've found useful in Python.

Most of the functions here are pure, and so can be used in a functional style of
programming (though they're useful in imperative code too).

You may also want to install the 'functional' and 'fn' packages from PyPI
and to look at the standard library modules functools, itertools and maybe operator.

# Reason I Built This

Because I don't want to repeat myself in my programs.  Instead, I put any generic functions
I write in here, along with tests and examples of usage.

I also hope that others, including yourself, will contribute functions to this library
(see the 'Contributions' section below).

# Overview of Modules

## funbox.flogic

`flogic` is a module of functions for composing functions that return boolean with boolean
operations.  Currently only fnot() is implemented, but `f_and` and `f_or` are
fair game for inclusion should I need them.

## funbox.mappings

Functions that are specifically for working on and generating dictionaries.

## funbox.once

Make a function call once if necessary, and reuse its result many times.

## funbox.passthrough

Pass through values unchanged under some conditions, but call a function on them
otherwise.

## `funbox.cmdline_parsing`

Occasionally I want to check command line arguments without consuming them via
a more heavyweight library like argparse or optparse; for example when I'm wrapping
another program and so passing most of them on to it.
These functions help with that.

## funbox.validation

Functions that help validating data and data types.

## `funbox.csv_records`

Functions for dealing with lists of records in the form of lists.  For example
`add_column` will add a column of data to an existing table of records.
There's also funbox.mappings that deals with records in the form of dictionaries.

## funbox.iterators

Functions for manipulating iterators.

## funbox.lists

Functions for manipulating finite, usually indexable, sequences.

# Contributions

I welcome patches to add new functions, or to fix bugs or improve performance in existing ones.

If you want to enhance the interface of an existing function, please contribute
yours under a different name.  For example you might want to curry a function
that I've left as flat, call it `funcname_curried` or `funcname_c`.  In other words, I've got code
using this library, and I don't want it to break.

Although the functions in here are ripe for using in a functional programming
style, it doesn't mean you have to implement them functionally.
I do, however, ask that you provide a rigorous doctest or, if it's more complex, a unittest,
to check it works as expected, however you implement it.


# Copyright and License

The MIT License (MIT)

Copyright (c) 2013 Nicholas Booker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
