# Functional Toolbox for Python

This is a collection of functional-style tools I've found useful in Python.

Designed to complement the functools, functional, and itertools from the standard library,
and the 'fn' package (https://github.com/kachayev/fn.py) which is available via pip

Note despite being functional in appearance, some of the implementations are stateful,
most notably 'once' which caches an expensively-calculated value the first time it is called
for future invocations.

Also, some of the modules in here could be handy in an imperative context, for example
`validation` and `cmdline_parsing`.

# Reason I Built This

Because I don't want to keep writing out the same old looping and branching constructs
over again, and having to test them each and every time.

Instead, I encapsulate my problem-specific logic in a function, and
then let a set of well-tested algorithms loose on them.
If that algorithm is there in the standard library or a third-party library,
I use that.  Otherwise I add the algorithm to this.

This results in better test coverage for whatever I'm doing, and less repetition in code.

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
