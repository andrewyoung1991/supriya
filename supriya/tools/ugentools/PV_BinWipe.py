# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.PV_ChainUGen import PV_ChainUGen


class PV_BinWipe(PV_ChainUGen):
    r'''Copies low bins from one input and the high bins of the other.

    ::

        >>> pv_chain_a = ugentools.FFT(
        ...     source=ugentools.WhiteNoise.ar(),
        ...     )
        >>> pv_chain_b = ugentools.FFT(
        ...     source=ugentools.LFSaw.ar(),
        ...     )
        >>> pv_bin_wipe = ugentools.PV_BinWipe(
        ...     pv_chain_a=pv_chain_a,
        ...     pv_chain_b=pv_chain_b,
        ...     wipe=0,
        ...     )
        >>> pv_bin_wipe
        PV_BinWipe.kr()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = 'FFT UGens'

    __slots__ = ()

    _ordered_input_names = (
        'pv_chain_a',
        'pv_chain_b',
        'wipe',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        pv_chain_a=None,
        pv_chain_b=None,
        wipe=0,
        ):
        PV_ChainUGen.__init__(
            self,
            pv_chain_a=pv_chain_a,
            pv_chain_b=pv_chain_b,
            wipe=wipe,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        pv_chain_a=None,
        pv_chain_b=None,
        wipe=0,
        ):
        r'''Constructs a PV_BinWipe.

        ::

            >>> pv_chain_a = ugentools.FFT(
            ...     source=ugentools.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = ugentools.FFT(
            ...     source=ugentools.LFSaw.ar(),
            ...     )
            >>> pv_bin_wipe = ugentools.PV_BinWipe.new(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     wipe=0,
            ...     )
            >>> pv_bin_wipe
            PV_BinWipe.kr()

        Returns ugen graph.
        '''
        ugen = cls._new_expanded(
            pv_chain_a=pv_chain_a,
            pv_chain_b=pv_chain_b,
            wipe=wipe,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def pv_chain_a(self):
        r'''Gets `pv_chain_a` input of PV_BinWipe.

        ::

            >>> pv_chain_a = ugentools.FFT(
            ...     source=ugentools.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = ugentools.FFT(
            ...     source=ugentools.LFSaw.ar(),
            ...     )
            >>> pv_bin_wipe = ugentools.PV_BinWipe(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     wipe=0,
            ...     )
            >>> pv_bin_wipe.pv_chain_a
            OutputProxy(
                source=FFT(
                    buffer_id=OutputProxy(
                        source=LocalBuf(
                            frame_count=2048.0,
                            channel_count=1.0,
                            calculation_rate=CalculationRate.SCALAR
                            ),
                        output_index=0
                        ),
                    source=OutputProxy(
                        source=WhiteNoise(
                            calculation_rate=CalculationRate.AUDIO
                            ),
                        output_index=0
                        ),
                    active=1.0,
                    hop=0.5,
                    window_size=0.0,
                    window_type=0.0
                    ),
                output_index=0
                )


        Returns ugen input.
        '''
        index = self._ordered_input_names.index('pv_chain_a')
        return self._inputs[index]

    @property
    def pv_chain_b(self):
        r'''Gets `pv_chain_b` input of PV_BinWipe.

        ::

            >>> pv_chain_a = ugentools.FFT(
            ...     source=ugentools.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = ugentools.FFT(
            ...     source=ugentools.LFSaw.ar(),
            ...     )
            >>> pv_bin_wipe = ugentools.PV_BinWipe(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     wipe=0,
            ...     )
            >>> pv_bin_wipe.pv_chain_b
            OutputProxy(
                source=FFT(
                    buffer_id=OutputProxy(
                        source=LocalBuf(
                            frame_count=2048.0,
                            channel_count=1.0,
                            calculation_rate=CalculationRate.SCALAR
                            ),
                        output_index=0
                        ),
                    source=OutputProxy(
                        source=LFSaw(
                            calculation_rate=CalculationRate.AUDIO,
                            frequency=440.0,
                            initial_phase=0.0
                            ),
                        output_index=0
                        ),
                    active=1.0,
                    hop=0.5,
                    window_size=0.0,
                    window_type=0.0
                    ),
                output_index=0
                )


        Returns ugen input.
        '''
        index = self._ordered_input_names.index('pv_chain_b')
        return self._inputs[index]

    @property
    def wipe(self):
        r'''Gets `wipe` input of PV_BinWipe.

        ::

            >>> pv_chain_a = ugentools.FFT(
            ...     source=ugentools.WhiteNoise.ar(),
            ...     )
            >>> pv_chain_b = ugentools.FFT(
            ...     source=ugentools.LFSaw.ar(),
            ...     )
            >>> pv_bin_wipe = ugentools.PV_BinWipe(
            ...     pv_chain_a=pv_chain_a,
            ...     pv_chain_b=pv_chain_b,
            ...     wipe=0,
            ...     )
            >>> pv_bin_wipe.wipe
            0.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('wipe')
        return self._inputs[index]