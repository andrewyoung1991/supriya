"""
"""
from supriya.tools.patterntools.streams import Routine
from supriya.tools.patterntools import utils


class NonSequenceStreamMixin(object):
    """
    """
    def get_sequence(self):
        raise NotImplemented

    def as_stream(self):
        seq = FuncStream(self.get_sequence())  # should return a function
        if not self.is_infinite:
            return Routine(utils.repeater(seq, self.n))
        return seq
