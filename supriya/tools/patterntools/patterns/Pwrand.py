"""
"""
import random

from supriya.tools.patterntools.patterns._BaseWeightedPattern import _BaseWeightedPattern


class Pwrand(_BaseWeightedPattern):
    """ chooses an element from the :param:sequence based on probabilites defined by
    the :weights: parameter

    :param n: a length (if the sequence is not infinite)
    :param sequence: an iterable (MUST BE INDEXABLE!)
    :param weights: a list of probabilites
    :returns: randomly selected elements from sequence
    """
    def get_sequence(self):
        def choose():
            rand = random.random()
            for index, weight in self.windex:
                if rand < weight:
                    return self.sequence[index]
        return choose
