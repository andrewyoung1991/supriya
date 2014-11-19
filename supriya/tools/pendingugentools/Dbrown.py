# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.DUGen import DUGen


class Dbrown(DUGen):
    r'''

    ::

        >>> dbrown = ugentools.Dbrown.(
        ...     )
        >>> dbrown

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = ()

    _valid_calculation_rates = None

    ### INITIALIZER ###

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        hi=1,
        length="float('inf')",
        lo=0,
        step=0.01,
        ):
        r'''Constructs a Dbrown.

        ::

            >>> dbrown = ugentools.Dbrown.new(
            ...     hi=1,
            ...     length="float('inf')",
            ...     lo=0,
            ...     step=0.01,
            ...     )
            >>> dbrown

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = None
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            hi=hi,
            length=length,
            lo=lo,
            step=step,
            )
        return ugen