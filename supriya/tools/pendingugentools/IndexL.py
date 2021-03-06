# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.Index import Index


class IndexL(Index):
    r'''

    ::

        >>> source = ugentools.In.ar(bus=0)
        >>> index_l = ugentools.IndexL.ar(
        ...     buffer_id=buffer_id,
        ...     source=source,
        ...     )
        >>> index_l
        IndexL.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'buffer_id',
        'source',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        buffer_id=None,
        source=None,
        ):
        Index.__init__(
            self,
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def ar(
        cls,
        buffer_id=None,
        source=None,
        ):
        r'''Constructs an audio-rate IndexL.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> index_l = ugentools.IndexL.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_l
            IndexL.ar()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.AUDIO
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )
        return ugen

    @classmethod
    def kr(
        cls,
        buffer_id=None,
        source=None,
        ):
        r'''Constructs a control-rate IndexL.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> index_l = ugentools.IndexL.kr(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_l
            IndexL.kr()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = synthdeftools.CalculationRate.CONTROL
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            buffer_id=buffer_id,
            source=source,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def buffer_id(self):
        r'''Gets `buffer_id` input of IndexL.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> index_l = ugentools.IndexL.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_l.buffer_id

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('buffer_id')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of IndexL.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> index_l = ugentools.IndexL.ar(
            ...     buffer_id=buffer_id,
            ...     source=source,
            ...     )
            >>> index_l.source
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