"""
"""
import random

from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class Pgauss(NonSequenceStreamMixin, _PatternBase):
    """ a basic random number generator

    :param mean: the mean value of the distrobution (mu)
    :param dev: the deviation of the distrobution (sigma)
    :param n: a length (if the sequence is not infinite)
    :returns: random floating point number between high and low
    """
    def __init__(self, mean, dev, **kwargs):
        self.mean = mean
        self.dev = dev
        super(Pgauss, self).__init__(**kwargs)

    def get_sequence(self):
        return lambda: random.gauss(self.mean, self.dev)
