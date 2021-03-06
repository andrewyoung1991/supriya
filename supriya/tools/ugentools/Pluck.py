# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.UGen import UGen


class Pluck(UGen):
    r'''A Karplus-String UGen.

    ::

        >>> source = ugentools.WhiteNoise.ar()
        >>> trigger = ugentools.Dust.kr(2)
        >>> pluck = ugentools.Pluck.ar(
        ...     coefficient=0.5,
        ...     decay_time=1,
        ...     delay_time=0.2,
        ...     maximum_delay_time=0.2,
        ...     source=source,
        ...     trigger=trigger,
        ...     )
        >>> pluck
        Pluck.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Delay UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'trigger',
        'maximum_delay_time',
        'delay_time',
        'decay_time',
        'coefficient',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        coefficient=0.5,
        decay_time=1,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        trigger=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            decay_time=decay_time,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            trigger=trigger,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        coefficient=0.5,
        decay_time=1,
        delay_time=0.2,
        maximum_delay_time=0.2,
        source=None,
        trigger=None,
        ):
        r'''Constructs an audio-rate Pluck.

        ::

            >>> source = ugentools.WhiteNoise.ar()
            >>> trigger = ugentools.Dust.kr(2)
            >>> pluck = ugentools.Pluck.ar(
            ...     coefficient=0.5,
            ...     decay_time=1,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     trigger=trigger,
            ...     )
            >>> pluck
            Pluck.ar()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            coefficient=coefficient,
            decay_time=decay_time,
            delay_time=delay_time,
            maximum_delay_time=maximum_delay_time,
            source=source,
            trigger=trigger,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def coefficient(self):
        r'''Gets `coefficient` input of Pluck.

        ::

            >>> source = ugentools.WhiteNoise.ar()
            >>> trigger = ugentools.Dust.kr(2)
            >>> pluck = ugentools.Pluck.ar(
            ...     coefficient=0.5,
            ...     decay_time=1,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     trigger=trigger,
            ...     )
            >>> pluck.coefficient
            0.5

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('coefficient')
        return self._inputs[index]

    @property
    def decay_time(self):
        r'''Gets `decay_time` input of Pluck.

        ::

            >>> source = ugentools.WhiteNoise.ar()
            >>> trigger = ugentools.Dust.kr(2)
            >>> pluck = ugentools.Pluck.ar(
            ...     coefficient=0.5,
            ...     decay_time=1,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     trigger=trigger,
            ...     )
            >>> pluck.decay_time
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('decay_time')
        return self._inputs[index]

    @property
    def delay_time(self):
        r'''Gets `delay_time` input of Pluck.

        ::

            >>> source = ugentools.WhiteNoise.ar()
            >>> trigger = ugentools.Dust.kr(2)
            >>> pluck = ugentools.Pluck.ar(
            ...     coefficient=0.5,
            ...     decay_time=1,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     trigger=trigger,
            ...     )
            >>> pluck.delay_time
            0.2

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('delay_time')
        return self._inputs[index]

    @property
    def maximum_delay_time(self):
        r'''Gets `maximum_delay_time` input of Pluck.

        ::

            >>> source = ugentools.WhiteNoise.ar()
            >>> trigger = ugentools.Dust.kr(2)
            >>> pluck = ugentools.Pluck.ar(
            ...     coefficient=0.5,
            ...     decay_time=1,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     trigger=trigger,
            ...     )
            >>> pluck.maximum_delay_time
            0.2

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('maximum_delay_time')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of Pluck.

        ::

            >>> source = ugentools.WhiteNoise.ar()
            >>> trigger = ugentools.Dust.kr(2)
            >>> pluck = ugentools.Pluck.ar(
            ...     coefficient=0.5,
            ...     decay_time=1,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     trigger=trigger,
            ...     )
            >>> pluck.source
            OutputProxy(
                source=WhiteNoise(
                    calculation_rate=CalculationRate.AUDIO
                    ),
                output_index=0
                )

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]

    @property
    def trigger(self):
        r'''Gets `trigger` input of Pluck.

        ::

            >>> source = ugentools.WhiteNoise.ar()
            >>> trigger = ugentools.Dust.kr(2)
            >>> pluck = ugentools.Pluck.ar(
            ...     coefficient=0.5,
            ...     decay_time=1,
            ...     delay_time=0.2,
            ...     maximum_delay_time=0.2,
            ...     source=source,
            ...     trigger=trigger,
            ...     )
            >>> pluck.trigger
            OutputProxy(
                source=Dust(
                    calculation_rate=CalculationRate.CONTROL,
                    density=2.0
                    ),
                output_index=0
                )

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('trigger')
        return self._inputs[index]