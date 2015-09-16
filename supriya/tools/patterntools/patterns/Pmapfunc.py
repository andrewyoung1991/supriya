"""
..module:: patterns/Pmapfunc.py
..moduleauthor:: Andrew Young <ayoung@thewulf.org>
"""

from supriya.tools.patterntools.patterns.Pfunc import Pfunc

class Pmapfunc(Pfunc):
    """
    :param initial: the initial argument to pass to :param:function
    :param function: a function that will be recursively fed its result
    :param reset_function: a function that responds to :method:.reset()
    :param n: number of repetitions
    """
    def __init__(self, initial, *args, **kwargs):
        self._initial = initial
        super(Pmapfunc, self).__init__(*args, **kwargs)

    def get_sequence(self):
        initial = self._initial
        while True:
            initial = self.function(initial)
            yield initial
