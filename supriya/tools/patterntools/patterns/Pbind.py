"""
"""
from supriya.tools.patterntools.patterns._BaseBind import _BaseBind
from supriya.tools.patterntools import utils


class Pbind(_BaseBind):
    """ binds many patterns to arbitrary keys.
    when converted to a stream with :method:.as_stream(), yields :class:Events instances
    returning the next value on each value.

    :param name: a unique key with which to refer to this pattern by
    :param elements: key, pattern mappings
    :returns: :class:Event objects
    """
    def get_sequence(self):
        """ converts all of the bound values into streams
        """
        iterators = {}
        for key, value in self.items():
            if hasattr(value, "as_stream"):
                value = value.as_stream()
            elif utils.isiterable(value):
                value = iter(value)
            iterators[key] = value
        return iterators
