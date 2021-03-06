# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.InfoUGenBase import InfoUGenBase


class NumOutputBuses(InfoUGenBase):
    r'''A number of output buses info unit generator.

    ::

        >>> ugentools.NumOutputBuses.ir()
        NumOutputBuses.ir()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Info UGens'

    __slots__ = ()

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        ):
        InfoUGenBase.__init__(
            self,
            calculation_rate=calculation_rate,
            )