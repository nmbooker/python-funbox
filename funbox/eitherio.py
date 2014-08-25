"""IO for Python using Either.
"""

def interact_either(items):
    """Left strings are sent to stderr, Right strings to stdout.

    Note this is hard to doctest because of the use of IO.
    """
    for item in items:
        out_file = (sys.stdout if item.is_right() else sys.stderr)
        string = (item.value if item.is_right() else item.message)
        out_file.write(string)
