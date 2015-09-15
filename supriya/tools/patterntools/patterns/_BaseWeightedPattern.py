"""
"""
from supriya.tools.patterntools.patterns.Pseq import Pseq
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class _BaseWeightedPattern(NonSequenceStreamMixin, Pseq):
    def __init__(self, weights, *args, **kwargs):
        self.weights = weights
        super(_BaseWeightedSequence, self).__init__(*args, **kwargs)

    def windex(self):
        # get the weights between 0 and 1
        max_weight, min_weight = max(self.weights), min(self.weights)
        diver = max_weight - min_weight
        weights = map(lambda x: (x - min_weight) / diver, self.weights)
        return tuple(zip(*sorted(enumerate(weights), key=lambda x: x[-1])))
