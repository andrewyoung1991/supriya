# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.MultiOutUGen import MultiOutUGen


class BiPanB2(MultiOutUGen):
    r'''A 2D ambisonic b-format panner.

    ::

        >>> in_a = ugentools.SinOsc.ar()
        >>> in_b = ugentools.WhiteNoise.ar()
        >>> bi_pan_b_2 = ugentools.BiPanB2.ar(
        ...     azimuth=-0.5,
        ...     gain=1,
        ...     in_a=in_a,
        ...     in_b=in_b,
        ...     )
        >>> bi_pan_b_2
        UGenArray({3})

    ::

        >>> w, x, y = bi_pan_b_2

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Spatialization UGens'

    __slots__ = ()

    _ordered_input_names = (
        'in_a',
        'in_b',
        'azimuth',
        'gain',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        azimuth=None,
        gain=1,
        in_a=None,
        in_b=None,
        ):
        MultiOutUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            channel_count=3,
            azimuth=azimuth,
            gain=gain,
            in_a=in_a,
            in_b=in_b,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        azimuth=None,
        gain=1,
        in_a=None,
        in_b=None,
        ):
        r'''Constructs an audio-rate BiPanB2.

        ::

            >>> in_a = ugentools.SinOsc.ar()
            >>> in_b = ugentools.WhiteNoise.ar()
            >>> bi_pan_b_2 = ugentools.BiPanB2.ar(
            ...     azimuth=-0.5,
            ...     gain=1,
            ...     in_a=in_a,
            ...     in_b=in_b,
            ...     )
            >>> bi_pan_b_2
            UGenArray({3})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            azimuth=azimuth,
            gain=gain,
            in_a=in_a,
            in_b=in_b,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        azimuth=None,
        gain=1,
        in_a=None,
        in_b=None,
        ):
        r'''Constructs a control-rate BiPanB2.

        ::

            >>> in_a = ugentools.SinOsc.kr()
            >>> in_b = ugentools.WhiteNoise.kr()
            >>> bi_pan_b_2 = ugentools.BiPanB2.kr(
            ...     azimuth=-0.5,
            ...     gain=1,
            ...     in_a=in_a,
            ...     in_b=in_b,
            ...     )
            >>> bi_pan_b_2
            UGenArray({3})

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            azimuth=azimuth,
            gain=gain,
            in_a=in_a,
            in_b=in_b,
            )
        return ugen

    # def newFromDesc(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def azimuth(self):
        r'''Gets `azimuth` input of BiPanB2.

        ::

            >>> in_a = ugentools.SinOsc.ar()
            >>> in_b = ugentools.WhiteNoise.ar()
            >>> bi_pan_b_2 = ugentools.BiPanB2.ar(
            ...     azimuth=-0.5,
            ...     gain=1,
            ...     in_a=in_a,
            ...     in_b=in_b,
            ...     )
            >>> bi_pan_b_2[0].source.azimuth
            -0.5

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('azimuth')
        return self._inputs[index]

    @property
    def gain(self):
        r'''Gets `gain` input of BiPanB2.

        ::

            >>> in_a = ugentools.SinOsc.ar()
            >>> in_b = ugentools.WhiteNoise.ar()
            >>> bi_pan_b_2 = ugentools.BiPanB2.ar(
            ...     azimuth=-0.5,
            ...     gain=1,
            ...     in_a=in_a,
            ...     in_b=in_b,
            ...     )
            >>> bi_pan_b_2[0].source.gain
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('gain')
        return self._inputs[index]

    @property
    def in_a(self):
        r'''Gets `in_a` input of BiPanB2.

        ::

            >>> in_a = ugentools.SinOsc.ar()
            >>> in_b = ugentools.WhiteNoise.ar()
            >>> bi_pan_b_2 = ugentools.BiPanB2.ar(
            ...     azimuth=-0.5,
            ...     gain=1,
            ...     in_a=in_a,
            ...     in_b=in_b,
            ...     )
            >>> bi_pan_b_2[0].source.in_a
            OutputProxy(
                source=SinOsc(
                    calculation_rate=CalculationRate.AUDIO,
                    frequency=440.0,
                    phase=0.0
                    ),
                output_index=0
                )

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('in_a')
        return self._inputs[index]

    @property
    def in_b(self):
        r'''Gets `in_b` input of BiPanB2.

        ::

            >>> in_a = ugentools.SinOsc.ar()
            >>> in_b = ugentools.WhiteNoise.ar()
            >>> bi_pan_b_2 = ugentools.BiPanB2.ar(
            ...     azimuth=-0.5,
            ...     gain=1,
            ...     in_a=in_a,
            ...     in_b=in_b,
            ...     )
            >>> bi_pan_b_2[0].source.in_b
            OutputProxy(
                source=WhiteNoise(
                    calculation_rate=CalculationRate.AUDIO
                    ),
                output_index=0
                )

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('in_b')
        return self._inputs[index]