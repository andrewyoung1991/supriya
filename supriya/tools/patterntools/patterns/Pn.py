"""
"""
import itertools as it
from supriya.tools.patterntools.patterns.Pseq import Pseq


class Pn(Pseq):
    """ repeates the :param:sequence :param:repetition # of times

    :param sequence: a _finite_ sequence
    :param n: number of times to cycle through items in :param:sequence
    :returns: element from :param:sequence
    """
    def get_sequence(self):
        repeat = it.repeat(self.sequence, self.n)
        for seq in repeat:
            yield from seq
