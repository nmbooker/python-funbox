"""IO using Either.

These functions enable you to write pure code to generate stdout and stderr
streams.

Why is this useful?

You can write unit tests or even doctests for your data generation code,
and separate the generation of output from how it gets output.

For the latter, you could for example decide to write a function with
the same interface as write_either that logs Left items to a logging server
and writes Right items to a TCP socket.
"""

def write_either(items):
    """Left strings are sent to stderr, Right strings to stdout.

    Note this is hard to doctest because of the use of IO.
    """
    for item in items:
        out_file = (sys.stdout if item.is_right() else sys.stderr)
        string = (item.value if item.is_right() else item.message)
        out_file.write(string)


def interact_either(func):
    """Take function mapping stdin lines to stdout and stderr chunks.

    Note you must put newline characters on the end of stdout and stderr
    strings.

    Wrap strings for stdout in Right, and strings for stderr in Left.
    """
    write_either(func(iter(sys.stdin)))
