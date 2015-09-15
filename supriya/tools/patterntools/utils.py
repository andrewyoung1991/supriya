import itertools as it
import functools
import collections


def isiterable(value):
    """ returns true if :param:value is iterable
    """
    return isinstance(value, collections.Iterable)


def repeater(iterable, n):
    """ cycles through the values of :param:iterable :param:n times
    :param iterable: a _finite_ sequence
    :param n: number of times to cycle through items in :param:iterable
    """
    repeat = it.repeat(iterable, n)
    for seq in repeat:
        yield from seq


def fold(value, low, high):
    if value < low:
        value = low + value
    elif value > high:
        value = value - high
    else:
        return value
    if value < low or value > high:
        return fold(value, low, high)


def clip(value, low, high):
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value


def wrap_stream(function):
    def wrapper(inner_func):
        @functools.wraps(inner_func)
        def closure(self, other):
            pattern = mash_patterns(function, self, other)
            pattern.n = self.n
            return pattern
        return closure
    return wrapper


def mash_patterns(operation, *patterns):
    from supriya.tools.patterntools.Pattern import Pseq
    _ab = []
    for thing in patterns:
        if isiterable(thing):
            _a = iter(thing)
        else:
            _a = it.repeat(thing)
        _ab.append(_a)
    return Pseq(map(operation, *_ab))

