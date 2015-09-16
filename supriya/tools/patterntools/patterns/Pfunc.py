"""
"""
from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin


class Pfunc(NonSequenceStreamMixin, _PatternBase):
    """ executes :param:function per iteration as a stream

    :param function: a function to execute per iterator
    :reset_function: a function to execute on self.as_stream().reset()
    :param n: number of time to execute function (if sequence is not infinite)
    :returns: return value of :param:function
    """
    def __init__(self, function, reset_function=None, **kwargs):
        self.function = function
        self.reset_function = reset_function if callable(reset_function) else \
                (lambda: reset_function)
        self.n = n
        super(Pfunc, self).__init__(**kwargs)

    def get_stream(self):
        return self.function

    def as_stream(self):
        stream = super(PFunc, self).as_stream()
        stream.reset = self.reset_function
        return stream
