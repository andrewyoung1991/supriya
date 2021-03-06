# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.Filter import Filter


class BRF(Filter):
    r'''A 2nd order Butterworth band-reject filter.

    ::

        >>> source = ugentools.In.ar(bus=0)
        >>> b_r_f =ugentools.BRF.ar(source=source)
        >>> b_r_f
        BRF.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Filter UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'frequency',
        'reciprocal_of_q',
        )

    ### PUBLIC METHODS ###

    def __init__(
        self,
        frequency=440,
        calculation_rate=None,
        reciprocal_of_q=1.0,
        source=None,
        ):
        Filter.__init__(
            self,
            frequency=frequency,
            calculation_rate=calculation_rate,
            reciprocal_of_q=reciprocal_of_q,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        frequency=440,
        reciprocal_of_q=1.0,
        source=None,
        ):
        r'''Constructs an audio-rate band-reject filter.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> b_r_f = ugentools.BRF.ar(
            ...     frequency=440,
            ...     reciprocal_of_q=1.0,
            ...     source=source,
            ...     )
            >>> b_r_f
            BRF.ar()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            frequency=frequency,
            calculation_rate=calculation_rate,
            reciprocal_of_q=reciprocal_of_q,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        frequency=440,
        reciprocal_of_q=1.0,
        source=None,
        ):
        r'''Constructs a control-rate band-reject filter.

        ::

            >>> source = ugentools.In.kr(bus=0)
            >>> b_r_f = ugentools.BRF.kr(
            ...     frequency=440,
            ...     reciprocal_of_q=1.0,
            ...     source=source,
            ...     )
            >>> b_r_f
            BRF.kr()

        Returns unit generator graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            frequency=frequency,
            calculation_rate=calculation_rate,
            reciprocal_of_q=reciprocal_of_q,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def frequency(self):
        r'''Gets `frequency` input of BRF.

        ::

            >>> frequency = 440.0
            >>> source = ugentools.In.ar(bus=0)
            >>> brf = ugentools.BRF.ar(
            ...     frequency=frequency,
            ...     source=source,
            ...     )
            >>> brf.frequency
            440.0

        Returns input.
        '''
        index = self._ordered_input_names.index('frequency')
        return self._inputs[index]

    @property
    def reciprocal_of_q(self):
        r'''Gets `reciprocal_of_q` input of BRF.

        ::

            >>> reciprocal_of_q = 1.0
            >>> source = ugentools.In.ar(bus=0)
            >>> brf = ugentools.BRF.ar(
            ...     reciprocal_of_q=reciprocal_of_q,
            ...     source=source,
            ...     )
            >>> brf.reciprocal_of_q
            1.0

        Returns input.
        '''
        index = self._ordered_input_names.index('reciprocal_of_q')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of BRF.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> brf = ugentools.BRF.ar(
            ...     source=source,
            ...     )
            >>> brf.source
            OutputProxy(
                source=In(
                    bus=0.0,
                    calculation_rate=CalculationRate.AUDIO,
                    channel_count=1
                    ),
                output_index=0
                )

        Returns input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]