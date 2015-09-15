"""
"""
from supriya.tools.patterntools.patterns.Pseq import Pseq


class Pflat(Pseq):
    """ takes a n-dimensional sequence of sequences and flattens the output into
    a single stream.

    :param sequence: an iterable containing iterables
    :param n: a length (if the sequence is not infinite)
    :returns: all atomic (non sequence) elements of :param:sequence and subpatterns
    """
    def get_sequence(self):
        for pattern in self.sequence:
            if hasattr(pattern, "as_stream"):
                yield from pattern.as_stream()
            elif hasattr(pattern, "__iter__"):
                yield from iter(pattern)
            else:
                yield pattern
