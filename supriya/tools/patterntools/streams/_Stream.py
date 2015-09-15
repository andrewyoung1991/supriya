"""
..module::
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
"""


class _Stream(object):
    """ base implementation of a stream. streams are iterators that calculate
    a single value at a time.
    - when a stream runs out, it returns None.
    - a stream responds to :method:.next() by returning its next value
    - a stream responds to :method:.reset() by resetting itself to its initial state
    - a stream can 'take over' another stream with `yield from <stream>`
    """
    def __iter__(self):
        return self

    def __next__(self):
        return self
    next = __next__

    def reset(self):
        return self

    def collect(self, n):
        return [next(self) for _ in range(n)]
