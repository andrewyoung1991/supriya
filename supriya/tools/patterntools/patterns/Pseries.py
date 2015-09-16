r'''
..module:: supriya.tools.patterntools.patterns.Pseries
    :synopsis:
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
'''
import itertools as it

from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.streams.Routine import Routine
from supriya.tools.patterntools import utils


class Pseries(_PatternBase):
    r''' A pattern that generates an optionally terminating series

    :param start: starting value
    :param step: distance between successive steps
    :param n: length of the sequence
    '''
    def __init__(self, start, step, **kwargs):
        self.start = start
        self.step = step
        super(Pseries, self).__init__(**kwargs)

    def get_sequence(self):
        r'''
        returns a generator which yields the next value of the series
        '''
        val = self.start
        while True:
            yield val
            val += self.step

    def as_stream(self):
        seq = self.get_sequence()
        if not self.is_infinite:
            routine_param = utils.repeater(seq, self.n)
        else:
            routine_param = it.cycle(seq)
        return Routine(routine_param)
