r'''
..module:: supriya.tools.patterntools.patterns.Pheapsort
    :synopsis:
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
'''
import heapq

from supriya.tools.patterntools.patterns.Pseq import Pseq


class Pheapsort(Pseq):
    r''' A pattern that performs a heapsort on :param:sequence, yielding the heap along
    the way.

    :param sequence: any sequence to sort
    :param n: number of repetitions
    '''
    def get_sequence(self):
        r''' heap-sorts the :param:sequence
        returns a generator which yields the heap per iteration
        '''
        h = []
        for value in self.sequence:
            heapq.heappush(h, value)
            yield h
