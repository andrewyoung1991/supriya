# -*- encoding: utf-8 -*-
from supriya.tools.ugentools.DUGen import DUGen


class Dxrand(DUGen):
    r'''A demand-rate random sequence generator.

    ::

        >>> sequence = (1, 2, 3)
        >>> dxrand = ugentools.Dxrand.new(
        ...     repeats=1,
        ...     sequence=sequence,
        ...     )
        >>> dxrand
        Dxrand()

    '''

    ### CLASS VARIABLES ###

    __slots__ = ()

    _ordered_input_names = (
        'repeats',
        'sequence',
        )

    _unexpanded_input_names = (
        'sequence',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        repeats=1,
        sequence=None,
        ):
        DUGen.__init__(
            self,
            repeats=repeats,
            sequence=sequence,
            )

    ### PUBLIC METHODS ###

    @classmethod
    def new(
        cls,
        repeats=1,
        sequence=None,
        ):
        r'''Constructs a Dxrand.

        ::

            >>> sequence = (1, 2, 3)
            >>> dxrand = ugentools.Dxrand.new(
            ...     repeats=1,
            ...     sequence=sequence,
            ...     )
            >>> dxrand
            Dxrand()

        Returns ugen graph.
        '''
        from supriya.tools import synthdeftools
        ugen = cls._new_expanded(
            repeats=repeats,
            sequence=sequence,
            )
        return ugen

    ### PUBLIC PROPERTIES ###

    @property
    def repeats(self):
        r'''Gets `repeats` input of Dxrand.

        ::

            >>> sequence = (1, 2, 3)
            >>> dxrand = ugentools.Dxrand.new(
            ...     repeats=1,
            ...     sequence=sequence,
            ...     )
            >>> dxrand.repeats
            1.0

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('repeats')
        return self._inputs[index]

    @property
    def sequence(self):
        r'''Gets `sequence` input of Dxrand.

        ::

            >>> sequence = (1, 2, 3)
            >>> dxrand = ugentools.Dxrand.new(
            ...     repeats=1,
            ...     sequence=sequence,
            ...     )
            >>> dxrand.sequence
            (1.0, 2.0, 3.0)

        Returns ugen input.
        '''
        index = self._ordered_input_names.index('sequence')
        return tuple(self._inputs[index:])