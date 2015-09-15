"""
"""
import itertools as it

from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.streams import Routine
from supriya.tools.patterntools import utils


class Pseq(_PatternBase):
    """ a basic cyclical sequence generator.
    takes :param: sequence and loops through its values.

    :param sequence: an iterable
    :param n: a length (if the sequence is not infinite)
    :returns: elements of :param:sequence in order
    """
    def __init__(self, sequence, **kwargs):
        self.sequence = sequence
        super(Pseq, self).__init__(**kwargs)

    def __str__(self):
        return "{0}(n={1}, sequence={2})".format(self.__class__.__name__,
                self.n, self.sequence)
    __repr__ = __str__

    def get_sequence(self):
        return self.sequence

    def as_stream(self):
        seq = self.get_sequence()
        if not self.is_infinite:
            routine_param = utils.repeater(seq, self.n)
        else:
            routine_param = it.cycle(seq)
        return Routine(routine_param)
