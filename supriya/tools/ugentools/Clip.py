# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.UGen import UGen


class Clip(UGen):
    r'''Clips a signal outside given thresholds.

    ::

        >>> source = ugentools.SinOsc.ar()
        >>> clip = ugentools.Clip.ar(
        ...     maximum=0.9,
        ...     minimum=0.1,
        ...     source=source,
        ...     )
        >>> clip
        Clip.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Trigger Utility UGens'

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'minimum',
        'maximum',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        maximum=1,
        minimum=0,
        source=0,
        ):
        UGen.__init__(
            self,
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        maximum=1,
        minimum=0,
        source=None,
        ):
        r'''Constucts an audio-rate Clip ugen.

        ::

            >>> source = ugentools.SinOsc.ar(frequency=[440, 442])
            >>> clip = ugentools.Clip.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> clip
            UGenArray({2})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )
        return ugen

    @classmethod
    def ir(
        cls,
        maximum=1,
        minimum=0,
        source=None,
        ):
        r'''Constucts a scalar-rate Clip ugen.

        ::

            >>> source = [ugentools.Rand.ir(), ugentools.Rand.ir()]
            >>> clip = ugentools.Clip.ir(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> clip
            UGenArray({2})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.SCALAR
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        maximum=1,
        minimum=0,
        source=None,
        ):
        r'''Constucts a control-rate Clip ugen.

        ::

            >>> source = ugentools.SinOsc.kr(frequency=[4, 2])
            >>> clip = ugentools.Clip.kr(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> clip
            UGenArray({2})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            maximum=maximum,
            minimum=minimum,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def maximum(self):
        r'''Gets `maximum` input of Clip.

        ::

            >>> source = ugentools.SinOsc.ar()
            >>> clip = ugentools.Clip.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> clip.maximum
            0.9

        Returns input.
        '''
        index = self._ordered_input_names.index('maximum')
        return self._inputs[index]

    @property
    def minimum(self):
        r'''Gets `minimum` input of Clip.

        ::

            >>> source = ugentools.SinOsc.ar()
            >>> clip = ugentools.Clip.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> clip.minimum
            0.1

        Returns input.
        '''
        index = self._ordered_input_names.index('minimum')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `minimum` input of Clip.

        ::

            >>> source = ugentools.SinOsc.ar()
            >>> clip = ugentools.Clip.ar(
            ...     maximum=0.9,
            ...     minimum=0.1,
            ...     source=source,
            ...     )
            >>> clip.source
            OutputProxy(
                source=SinOsc(
                    calculation_rate=CalculationRate.AUDIO,
                    frequency=440.0,
                    phase=0.0
                    ),
                output_index=0
                )

        Returns input.
        '''
        index = self._ordered_input_names.index('source')
        return self._inputs[index]