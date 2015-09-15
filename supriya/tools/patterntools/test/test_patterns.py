import pytest

from supriya.tools.patterntools.patterns import *


@pytest.mark.parametrize("sequence,length", [
    ([1, 2, 3, 4], 4),
    ([1, 2, 3, 4], 7),
    ([1, 2, 3, 4, 5], 12)
    ])
def test_pseq_lengths_are_correct(sequence, length):
    seq = Pseq(sequence, n=length).as_stream()
    expect = lambda i: sequence[i % len(sequence)]
    for i, elem in enumerate(seq):
        assert elem == expect(i)


@pytest.mark.parametrize("sequence,expect", [
    ([[1, 2, 3, 4], [2, 3, 4]], [1, 2, 3, 4, 2, 3, 4]),
    ([Pseq([1, 2, 3, 4], n=1) * 2, Pseq([2, 3, 4], n=1)],
        [2, 4, 6, 8, 2, 3, 4]),
    (Pflat([Pseq([2, 3, 4], n=1), Pseq([3, 3, 4], n=1)
        ], n=1).as_stream(),
        [2, 3, 4, 3, 3, 4, 3, 2, 3]),
    ])
def test_pstreamseq_yeilding_correct_values(sequence, expect):
    seq = Pflat(sequence, n=1).as_stream()
    s = iter(expect)
    for elem in seq:
        expected = next(s)
        assert elem == expected


@pytest.mark.parametrize("binder,op", [
    (Pbind("t0", a=Pseq(range(10), n=1), b=Pkey("a", "t0")), lambda x: x),
    (Pbind("t1", a=Pseq(range(10), n=1), b=Pkey("a", "t1") * 10), lambda x: x * 10),
    (Pbind("t2", a=Pseq(range(10), n=1), b=Pkey("a", "t2") + 10), lambda x: x + 10),
    (Pbind("t3", a=Pseq(range(10), n=1), b=Pkey("a", "t3") - 10), lambda x: x - 10),
    (Pbind("t4", a=Pseq(range(10), n=1), b=Pkey("a", "t4") % 2), lambda x: x % 2),
    (Pbind("t5", a=Pseq(range(10), n=1), b=Pkey("a", "t5") ** 2), lambda x: x ** 2)
    ])
def test_pkey_proxies(binder, op):
    for event in binder.as_stream():
        assert op(event.a) == event.b


@pytest.mark.parametrize("pattern,op", [
    (Pseq(range(10), n=1) + Pseq(range(10), n=1), lambda x: x * 2),
    (Pseq(range(10), n=1) * Pseq(range(10), n=1), lambda x: x **2),
    (Pseq(range(10), n=1) % Pseq([2]), lambda x: x % 2),
    ])
def test_adding_sequence(pattern, op):
    for i, thing in enumerate(pattern.as_stream()):
        assert thing == op(i)
