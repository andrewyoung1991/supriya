# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.MultiOutUGen import MultiOutUGen


class UnpackFFT(MultiOutUGen):
    r'''

    ::

        >>> unpack_fft = ugentools.UnpackFFT.ar(
        ...     bufsize=bufsize,
        ...     chain=chain,
        ...     frombin=0,
        ...     tobin=tobin,
        ...     )
        >>> unpack_fft
        UnpackFFT.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'chain',
        'bufsize',
        'frombin',
        'tobin',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        bufsize=None,
        chain=None,
        frombin=0,
        tobin=None,
        ):
        MultiOutUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            bufsize=bufsize,
            chain=chain,
            frombin=frombin,
            tobin=tobin,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        bufsize=None,
        chain=None,
        frombin=0,
        tobin=None,
        ):
        r'''Constructs a UnpackFFT.

        ::

            >>> unpack_fft = ugentools.UnpackFFT.new(
            ...     bufsize=bufsize,
            ...     chain=chain,
            ...     frombin=0,
            ...     tobin=tobin,
            ...     )
            >>> unpack_fft
            UnpackFFT.new()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = None
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            bufsize=bufsize,
            chain=chain,
            frombin=frombin,
            tobin=tobin,
            )
        return ugen

    # def newFromDesc(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def bufsize(self):
        r'''Gets `bufsize` input of UnpackFFT.

        ::

            >>> unpack_fft = ugentools.UnpackFFT.ar(
            ...     bufsize=bufsize,
            ...     chain=chain,
            ...     frombin=0,
            ...     tobin=tobin,
            ...     )
            >>> unpack_fft.bufsize

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('bufsize')
        return self._inputs[index]

    @property
    def chain(self):
        r'''Gets `chain` input of UnpackFFT.

        ::

            >>> unpack_fft = ugentools.UnpackFFT.ar(
            ...     bufsize=bufsize,
            ...     chain=chain,
            ...     frombin=0,
            ...     tobin=tobin,
            ...     )
            >>> unpack_fft.chain

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('chain')
        return self._inputs[index]

    @property
    def frombin(self):
        r'''Gets `frombin` input of UnpackFFT.

        ::

            >>> unpack_fft = ugentools.UnpackFFT.ar(
            ...     bufsize=bufsize,
            ...     chain=chain,
            ...     frombin=0,
            ...     tobin=tobin,
            ...     )
            >>> unpack_fft.frombin
            0.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('frombin')
        return self._inputs[index]

    @property
    def tobin(self):
        r'''Gets `tobin` input of UnpackFFT.

        ::

            >>> unpack_fft = ugentools.UnpackFFT.ar(
            ...     bufsize=bufsize,
            ...     chain=chain,
            ...     frombin=0,
            ...     tobin=tobin,
            ...     )
            >>> unpack_fft.tobin

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('tobin')
        return self._inputs[index]