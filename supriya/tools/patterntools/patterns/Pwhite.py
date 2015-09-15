"""
"""
import random

from supriya.tools.patterntools.patterns._BaseRange import _BaseRange


class Pwhite(_BaseRange):
    """ a basic random number generator

    :param low: the low value of the random range
    :param high: the high value of the random range
    :param n: a length (if the sequence is not infinite)
    :returns: random floating point number between high and low
    """
    def get_sequence(self):
        return lambda: random.uniform(self.low, self.high)
