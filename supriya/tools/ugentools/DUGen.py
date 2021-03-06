# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.CalculationRate import CalculationRate
from supriya.tools.ugentools.UGen import UGen


class DUGen(UGen):
    r'''Abstract base class of demand-rate UGens.
    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Demand UGens'

    __slots__ = ()

    _ordered_input_names = ()

    _valid_calculation_rates = (
        CalculationRate.DEMAND,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        **kwargs
        ):
        UGen.__init__(
            self,
            calculation_rate=CalculationRate.DEMAND,
            **kwargs
            )