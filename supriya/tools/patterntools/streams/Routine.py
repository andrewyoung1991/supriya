"""
..module::
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
"""
import itertools as it
from supriya.tools.patterntools.streams._Stream import _Stream


class Routine(_Stream):
    """
    :param iterator: an iterator or generator function
    """
    def __init__(self, iterator):
        self._backup, self._iterator = it.tee(iterator)

    def __add__(self, stream):
        return Routine(it.chain(self, stream))

    def __next__(self):
        return next(self._iterator)

    def __str__(self):
        return "{0}({1})".format(self.__class__.__name__, self._iterator)

    def reset(self):
        """ `resets` the iterator by assigning its backup to :param:self._iterator and
        copying the backup to :param:self._backup
        """
        self._backup, self._iterator = it.tee(self._backup)
        return self

    def __lshift__(self, other):
        # overloading the syntax for << here to embed a stream within this stream
        self._backup, self._iterator = it.tee(it.chain(self._iterator, other))
        return self

    def __rshift__(self, other):
        # overloading the syntax for >> here to embed this stream within another stream
        other._backup, other._iterator = it.tee(it.chain(other._iterator,
                                                            self._iterator))
        return other
