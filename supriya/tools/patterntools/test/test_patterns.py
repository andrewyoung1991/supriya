import pytest

from ..Pattern import *


@pytest.mark.parametrize("sequence,length", [
    ([1, 2, 3, 4], 4),
    ([1, 2, 3, 4], 7),
    ([1, 2, 3, 4, 5], 12)
    ])
def test_pseq_lengths_are_correct(sequence, length):
    seq = Pseq(sequence, repetitions=length).as_stream()
    expect = lambda i: sequence[i % len(sequence)]
    for i, elem in enumerate(seq):
        assert elem == expect(i)


@pytest.mark.parametrize("sequence,expect", [
    ([[1, 2, 3, 4], [2, 3, 4]], [1, 2, 3, 4, 2, 3, 4]),
    ([Pseq([1, 2, 3, 4], repetitions=1), Pseq([2, 3, 4], repetitions=1)],
        [1, 2, 3, 4, 2, 3, 4]),
    (Pflat([Pseq([2, 3, 4], repetitions=1), Pseq([3, 3, 4], repetitions=1)
        ], repetitions=1).as_stream(),
        [2, 3, 4, 3, 3, 4, 3, 2, 3]),
    ])
def test_pstreamseq_yeilding_correct_values(sequence, expect):
    seq = Pflat(sequence, repetitions=1).as_stream()
    s = iter(expect)
    for elem in seq:
        expected = next(s)
        assert elem == expected
