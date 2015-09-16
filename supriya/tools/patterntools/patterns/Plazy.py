"""
"""
from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class Plazy(NonSequenceStreamMixin, _PatternBase):
    """ executes :param:function who's return type is a Pattern

    :param function: a function with the signature () -> Pattern
    :param n: number of times to execute :param:function in a stream
    """
    def __init__(self, function, **kwargs):
        self.function = function
        super(Plazy, self).__init__(**kwargs)

    def get_sequence(self):
        def get_stream():
            try:
                return self.function().as_stream()
            except AttributeError:
                raise ValueError(Pattern)
        return get_stream
