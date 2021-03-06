# -*- encoding: utf-8 -*-
from supriya.tools.synthdeftools.CalculationRate import CalculationRate
from supriya.tools.ugentools.Filter import Filter


class Lag(Filter):
    r'''A lag generator.

    ::

        >>> source = ugentools.In.kr(bus=0)
        >>> ugentools.Lag.kr(
        ...     lag_time=0.5,
        ...     source=source,
        ...     )
        Lag.kr()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'lag_time',
        )

    _valid_rates = (
        CalculationRate.AUDIO,
        CalculationRate.CONTROL,
        )

    ### INITIALIZER ###

    def __init__(
        self,
        lag_time=0.1,
        calculation_rate=None,
        source=None,
        ):
        Filter.__init__(
            self,
            calculation_rate=calculation_rate,
            source=source,
            lag_time=lag_time,
            )

    ### PRIVATE METHODS ###

    @classmethod
    def _new_single(
        cls,
        lag_time=None,
        calculation_rate=None,
        source=None,
        ):
        if lag_time == 0:
            return source
        source_rate = CalculationRate.from_input(source)
        if source_rate == CalculationRate.SCALAR:
            return source
        ugen = cls(
            lag_time=lag_time,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        lag_time=0.1,
        source=None,
        ):
        r'''Constructs an audio-rate lag.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> ugentools.Lag.ar(
            ...     lag_time=0.5,
            ...     source=source,
            ...     )
            Lag.ar()

        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            lag_time=lag_time,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        lag_time=0.1,
        source=None,
        ):
        r'''Constructs a control-rate lag.

        ::

            >>> source = ugentools.In.kr(bus=0)
            >>> ugentools.Lag.kr(
            ...     lag_time=0.5,
            ...     source=source,
            ...     )
            Lag.kr()

        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            lag_time=lag_time,
            calculation_rate=calculation_rate,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def lag_time(self):
        r'''Gets `lag_time` input of Lag.

        ::

            >>> lag_time = 0.1
            >>> source = ugentools.In.kr(bus=0)
            >>> lag = ugentools.Lag.kr(
            ...     lag_time=lag_time,
            ...     source=source,
            ...     )
            >>> lag.lag_time
            0.1

        Returns input.
        '''
        index = self._ordered_input_names.index('lag_time')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of Lag.

        ::

            >>> source = ugentools.In.kr(bus=0)
            >>> lag = ugentools.Lag.kr(
            ...     source=source,
            ...     )
            >>> lag.source
            OutputProxy(
                source=In(
                    bus=0.0,
                    calculation_rate=CalculationRate.CONTROL,
                    channel_count=1
                    ),
                output_index=0
                )

        Returns input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]