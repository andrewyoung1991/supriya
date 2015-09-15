"""
"""
from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class _BaseRange(NonSequenceStreamMixin, _PatternBase):
    def __init__(self, low, high, **kwargs):
        self.low = low
        self.high = high
        super(_PatternBase, self).__init__(**kwargs)

    def __str__(self):
        return "{0}(reptetitions={1}, low={2}, high={3})".format(self.__class__.__name__,
                self.reptetitions, self.low, self.high)
    __repr__ = __str__
