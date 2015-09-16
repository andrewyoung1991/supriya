"""
"""
import random

from supriya.tools.patterntools.patterns.Pseq import Pseq
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class Prand(NonSequenceStreamMixin, Pseq):
    """ chooses a random element from the sequence

    :param sequence: a sequence of values
    :param n: a length (if the sequence is not infinite)
    :returns: a random element of the sequence
    """
    def get_sequence(self):
        return lambda: random.choice(self.sequence)
