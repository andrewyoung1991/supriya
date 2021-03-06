# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.UGen import UGen


class Normalizer(UGen):
    r'''A dynamics flattener.

    ::

        >>> source = ugentools.In.ar(0)
        >>> normalizer = ugentools.Normalizer.ar(
        ...     duration=0.01,
        ...     level=1,
        ...     source=source,
        ...     )
        >>> normalizer
        Normalizer.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Dynamics UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'level',
        'duration',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        duration=0.01,
        level=1,
        source=None,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            duration=duration,
            level=level,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        duration=0.01,
        level=1,
        source=None,
        ):
        r'''Constructs an audio-rate Normalizer.

        ::

            >>> source = ugentools.In.ar(bus=0, channel_count=2)
            >>> normalizer = ugentools.Normalizer.ar(
            ...     duration=0.01,
            ...     level=1,
            ...     source=source,
            ...     )
            >>> normalizer
            UGenArray({2})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            duration=duration,
            level=level,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        r'''Gets `duration` input of Normalizer.

        ::

            >>> source = ugentools.In.ar(0)
            >>> normalizer = ugentools.Normalizer.ar(
            ...     duration=0.01,
            ...     level=1,
            ...     source=source,
            ...     )
            >>> normalizer.duration
            0.01

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('duration')
        return self._inputs[index]

    @property
    def level(self):
        r'''Gets `level` input of Normalizer.

        ::

            >>> source = ugentools.In.ar(0)
            >>> normalizer = ugentools.Normalizer.ar(
            ...     duration=0.01,
            ...     level=1,
            ...     source=source,
            ...     )
            >>> normalizer.level
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('level')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of Normalizer.

        ::

            >>> source = ugentools.In.ar(0)
            >>> normalizer = ugentools.Normalizer.ar(
            ...     duration=0.01,
            ...     level=1,
            ...     source=source,
            ...     )
            >>> normalizer.source
            OutputProxy(
                source=In(
                    bus=0.0,
                    calculation_rate=CalculationRate.AUDIO,
                    channel_count=1
                    ),
                output_index=0
                )

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]