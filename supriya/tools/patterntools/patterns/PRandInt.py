"""
"""
import random

from supriya.tools.patterntools.patterns._BaseRange import _BaseRange


class PRandInt(_BaseRange):
    """ a basic random number generator

    :param low: the low value of the random range
    :param high: the high value of the random range
    :param n: a length (if the sequence is not infinite)
    :returns: random integer number between high and low
    """
    def get_sequence(self):
        return lambda: random.randrange(self.low, self.high)
