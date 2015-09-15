"""
"""
from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class Pif(_PatternBase, NonSequenceStreamMixin):
    """ evaluates :param:condition and returns the
    """
    def __init__(self, condition, if_true, if_false, default, **kwargs):
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false
        self.default = default
        super(Pif, self).__init__(**kwargs)

    def evaluate_condition(self):
        return self.condition() if callable(self.condition) else self.condition

    def get_sequence(self):
        def get_stream():
            val = self.evaluate_condition()
            if val is True:
                return self.if_true
            elif val is False:
                return self.if_false
            return self.default
        return get_stream
