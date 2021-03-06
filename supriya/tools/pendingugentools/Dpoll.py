# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.DUGen import DUGen


class Dpoll(DUGen):
    r'''

    ::

        >>> source = ugentools.In.ar(bus=0)
        >>> dpoll = ugentools.Dpoll.ar(
        ...     label=label,
        ...     run=1,
        ...     source=source,
        ...     trigid=-1,
        ...     )
        >>> dpoll
        Dpoll.ar()

    '''

    ### CLASS VARIABLES ###

    __documentation_section__ = None

    __slots__ = ()

    _ordered_input_names = (
        'source',
        'label',
        'run',
        'trigid',
        )

    _valid_calculation_rates = None

    ### INITIALIZER ###

    def __init__(
        self,
        calculation_rate=None,
        label=None,
        run=1,
        source=None,
        trigid=-1,
        ):
        DUGen.__init__(
            self,
            calculation_rate=calculation_rate,
            label=label,
            run=run,
            source=source,
            trigid=trigid,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        label=None,
        run=1,
        source=None,
        trigid=-1,
        ):
        r'''Constructs a Dpoll.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> dpoll = ugentools.Dpoll.new(
            ...     label=label,
            ...     run=1,
            ...     source=source,
            ...     trigid=-1,
            ...     )
            >>> dpoll
            Dpoll.new()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        calculation_rate = None
        ugen = cls._new_expanded(
            calculation_rate=calculation_rate,
            label=label,
            run=run,
            source=source,
            trigid=trigid,
            )
        return ugen

    # def new1(): ...

    ### PUBLIC PROPERTIES ###

    @property
    def label(self):
        r'''Gets `label` input of Dpoll.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> dpoll = ugentools.Dpoll.ar(
            ...     label=label,
            ...     run=1,
            ...     source=source,
            ...     trigid=-1,
            ...     )
            >>> dpoll.label

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('label')
        return self._inputs[index]

    @property
    def run(self):
        r'''Gets `run` input of Dpoll.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> dpoll = ugentools.Dpoll.ar(
            ...     label=label,
            ...     run=1,
            ...     source=source,
            ...     trigid=-1,
            ...     )
            >>> dpoll.run
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('run')
        return self._inputs[index]

    @property
    def source(self):
        r'''Gets `source` input of Dpoll.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> dpoll = ugentools.Dpoll.ar(
            ...     label=label,
            ...     run=1,
            ...     source=source,
            ...     trigid=-1,
            ...     )
            >>> dpoll.source
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

    @property
    def trigid(self):
        r'''Gets `trigid` input of Dpoll.

        ::

            >>> source = ugentools.In.ar(bus=0)
            >>> dpoll = ugentools.Dpoll.ar(
            ...     label=label,
            ...     run=1,
            ...     source=source,
            ...     trigid=-1,
            ...     )
            >>> dpoll.trigid
            -1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('trigid')
        return self._inputs[index]