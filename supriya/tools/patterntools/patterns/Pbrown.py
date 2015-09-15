"""
"""
import random

from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class Pbrown(_PatternBase, NonSequenceStreamMixin):
    """
    """
    def __init__(self, low=0.0, high=1.0, step=0.125, **kwargs):
        self.low = low
        self.high = high
        self.step = step
        super(Pbrown, self).__init__(**kwargs)
        self._lastval = None

    @property
    def lastval(self):
        if self._lastval is None:
            self._lastval = self.low
        return self._lastval

    @lastval.setter
    def lastval(self, other):
        self._lastval = other
        return self._lastval

    def get_sequence(self):
        def seq():
            rand = (random.random() * self.step) * random.choice([-1, 1])
            self.lastval = utils.fold(self.lastval + rand, self.low, self.high)
            return self.lastval
        return seq
