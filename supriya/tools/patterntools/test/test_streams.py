import itertools as it

import pytest
from supriya.tools.patterntools.streams import FuncStream, Routine


@pytest.mark.parametrize("func,args,expected", [
    (lambda x: x, (4, ), 4),
    (lambda x, y: x + y, (1, 2), 3),
    (lambda x: x **2, (8, ), 64)
    ])
def test_funcstream(func, args, expected):
    stream = FuncStream(func, *args)
    for _ in range(10):
        assert next(stream) == expected


@pytest.mark.parametrize("func,args,expected", [
    (lambda x: x, (4, ), 4),
    (lambda x, y: x + y, (1, 2), 3),
    (lambda x: x **2, (8, ), 64)
    ])
def test_funcstream_argshift(func, args, expected):
    stream = FuncStream(func)
    stream << args
    for _ in range(10):
        assert next(stream) == expected


@pytest.mark.parametrize("gen", [
    range(5), range(20), (i for i in [1.4, 2.3, 1.56])
    ])
def test_routine(gen):
    expect, gen = it.tee(gen)
    stream = Routine(gen)
    for item in stream:
        assert item == next(expect)


@pytest.mark.parametrize("gen,routine,expect", [
    (range(5), Routine(range(2)), [0, 1, 2, 3, 4, 0, 1])
    ])
def test_embeded_routines(gen, routine, expect):
    stream = Routine(gen)
    stream << routine
    expect = iter(expect)
    for item in stream:
        assert item == next(expect)

@pytest.mark.parametrize("gen", [
    range(5), range(12)
    ])
def test_reset_routine(gen):
    stream = Routine(gen)
    expect_1, expect_2 = it.tee(gen)
    for item in stream:
        assert item == next(expect_1)

    with pytest.raises(StopIteration):
        next(stream)

    stream.reset()
    for item in stream:
        assert item == next(expect_2)

    with pytest.raises(StopIteration):
        next(stream)

