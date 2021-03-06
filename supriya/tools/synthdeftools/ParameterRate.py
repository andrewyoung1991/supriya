# -*- encoding: utf-8 -*-
from supriya.tools.systemtools.Enumeration import Enumeration


class ParameterRate(Enumeration):
    r'''An enumeration of synthdef control rates.
    '''

    ### CLASS VARIABLES ###

    AUDIO = 2
    CONTROL = 3
    SCALAR = 0
    TRIGGER = 1