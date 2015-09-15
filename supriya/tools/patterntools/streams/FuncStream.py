"""
..module::
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
"""
from supriya.tools.patterntools.streams._Stream import _Stream


class FuncStream(_Stream):
    """ evaluates :param:function with the positional arguments :param:args

    the `<<` operator can be used to change the positional arguments passed to
    :param:function. the arguments must be in the form of a tuple.

    :param function: a function to evaluate per iteration
    :param args: positional arguments to pass to :param:function
    """
    def __init__(self, function, *args):
        self._function = function
        self._func_args = args

    def __next__(self):
        return self._function(*self._func_args)

    def __lshift__(self, other):
        # overloading the syntax for << here to add args to the function
        assert isinstance(other, tuple), "other must be a tuple"
        self._func_args = other
        return self

    def __rshift__(self, other):
        # evaluates the :param:function with the arguments other
        assert isinstance(other, tuple), "other must be a tuple"
        return self._function(*other)
