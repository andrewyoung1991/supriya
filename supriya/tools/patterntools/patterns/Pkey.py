"""
"""
from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.patterns.Pbind import Pbind
from supriya.tools.patterntools.patterns.utils import NonSequenceStreamMixin
from supriya.tools.patterntools.streams import Routine


class Pkey(_PatternBase):
    """
    proxies a pattern stored in the key of a binding pattern

    :param pattern_key: the key to the pattern object you'd like to alias values from
    :param binding_key: the key (name) of the binnding class
    """
    def __init__(self, pattern_key, binding_key, **kwargs):
        self.binding_key = binding_key
        self.pattern_key = pattern_key
        super(Pkey, self).__init__(**kwargs)

    def get_sequence(self):
        """ okay, i understand this isn't 100% how the supercollider implementation
        works. but the code is very similar. the end game here is to make a FuncStream
        out of the aliased pattern and any maths. this is especially difficult in python
        because of the priority of math and, unlike supercollider, nothing is lazy.
        """
        def seq():
            binder = Pbind.get_registry().get(self.binding_key)
            yield from binder[self.pattern_key].as_stream()
        return seq

    def as_stream(self):
        stream = self.get_sequence()
        return Routine(stream())
