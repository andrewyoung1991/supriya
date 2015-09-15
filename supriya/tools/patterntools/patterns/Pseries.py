r'''
..module:: supriya.tools.patterntools.patterns.Pseries
    :synopsis:
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
'''
import heapq

from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class Pseries(_PatternBase, NonSequenceStreamMixin):
    r''' A pattern that generates an optionally terminating series

    :param start: starting value
    :param step: distance between successive steps
    :param n: length of the sequence
    '''
    def get_sequence(self):
        r'''
        returns a generator which yields the next value of the series
        '''
        val = self.start
        while True:
            yield val
            val += self.step

