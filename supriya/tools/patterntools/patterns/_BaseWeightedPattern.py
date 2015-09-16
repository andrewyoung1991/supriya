"""
"""
from supriya.tools.patterntools.patterns.Pseq import Pseq
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class _BaseWeightedPattern(NonSequenceStreamMixin, Pseq):
    def __init__(self, weights, *args, **kwargs):
        self.weights = weights
        super(_BaseWeightedPattern, self).__init__(*args, **kwargs)

    def windex(self):
        # get the weights between 0 and 1
        max_weight = max(self.weights)
        weights = map(lambda x: x / max_weight, self.weights)
        return tuple(sorted(enumerate(weights), key=lambda x: x[-1]))
