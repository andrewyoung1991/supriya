"""
"""
from supriya.tools.patterntools import utils


class _PatternBase(object):
    def __init__(self, n=None):
        self.n = n

    def __iter__(self):
        return self.as_stream()

    def __next__(self):
        return self

    def __hash__(self):
        return hash(self.__str__())

    @property
    def is_infinite(self):
        return self.n is None

    def reset(self):
        return self

    def as_stream(self):
        raise NotImplementedError

    # MATHS, note no cover at all...
    @utils.wrap_stream(lambda x, y: x * y)
    def __mul__(self, other):
        return self
    __rmul__ = __mul__

    @utils.wrap_stream(lambda x, y: x + y)
    def __add__(self, other):
        return self
    __radd__ = __add__

    @utils.wrap_stream(lambda x, y: x - y)
    def __sub__(self, other):
        return self

    @utils.wrap_stream(lambda x, y: y - x)
    def __rsub__(self, other):
        return self

    @utils.wrap_stream(lambda x, y: x / y)
    def __div__(self, other):
        return self

    @utils.wrap_stream(lambda x, y: y / x)
    def __rdiv__(self, other):
        return self

    @utils.wrap_stream(lambda x, y: x % y)
    def __mod__(self, other):
        return self

    @utils.wrap_stream(lambda x, y: y % x)
    def __rmod__(self, other):
        return self

    @utils.wrap_stream(lambda x, y: x ** y)
    def __pow__(self, other):
        return self

    @utils.wrap_stream(lambda x, y: y ** x)
    def __rpow__(self, other):
        return self
