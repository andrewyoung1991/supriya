"""
..module:: patterns/Psine.py
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
"""
import math
from supriya.tools.patterntools.patterns.Pseries import Pseries


class Psine(Pseries):
    """
    :param start: starting angle (in degrees)
    :param step: distance between successive steps
    :param n: length of the sequence
    """
    def get_sequence(self):
        val = self.start
        while True:
            yield math.sin(math.radians(val))
            val += self.step
