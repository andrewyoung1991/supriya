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
        windexed = self.windex()
        _, weights = list(zip(*windexed))
        def choose():
            rnd = random.random() * sum(weights)
            for i, w in self.windex():
                rnd -= w
                if rnd < 0:
                    return self.sequence[i]
        return choose
