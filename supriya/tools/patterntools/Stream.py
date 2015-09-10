import itertools as it


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


class FuncStream(_Stream):
    """ evaluates :param:function with the positional arguments :param:args

    the `<<` operator can be used to change the positional arguments passed to
    :param:function. the arguments must be in the form of a tuple.

    :param function: a function to evaluate per iteration
    :param args: positional arguments to pass to :param:function
    """
    def __init__(self, function, *args):
        self._function = function
        self._func_args = args

    def __next__(self):
        return self._function(*self._func_args)

    def __lshift__(self, other):
        # overloading the syntax for << here to add args to the function
        assert isinstance(other, tuple), "other must be a tuple"
        self._func_args = other
        return self

    def __rshift__(self, other):
        # evaluates the :param:function with the arguments other
        assert isinstance(other, tuple), "other must be a tuple"
        return self._function(*other)



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

