import pytest

from supriya.tools.patterntools.patterns import Pseq, Pbind


@pytest.mark.parametrize("elements,expected", [
    ({"count": Pseq(range(4), n=1), "const": 4}, [
            {"count": 0, "const": 4}, {"count": 1, "const": 4},
            {"count": 2, "const": 4}, {"count": 3, "const": 4}]),
    ({"count": Pseq(range(4), n=4), "const": 4,
        "foo": Pseq(["hi", "there"], n=1)}, [
            {"count": 0, "const": 4, "foo": "hi"},
            {"count": 1, "const": 4, "foo": "there"}]),
    ])
def test_collector_messages(elements, expected):
    collector = Pbind("test", **elements).as_stream()
    expected = iter(expected)

    for message in collector:
        assert message.__dict__ == next(expected)


@pytest.mark.parametrize("collectors,expected", [
    ([
        # collectors
        Pbind("test_1", count=Pseq(range(2), n=2), const=3),
        Pbind("test_2", count=Pseq(range(3), n=3), const=4)
    ],[
        # expected
        {"test_1": {"count": 0, "const": 3}, "test_2": {"count": 0, "const": 4}},
        {"test_1": {"count": 1, "const": 3}, "test_2": {"count": 1, "const": 4}}
    ]),
    ([
        # collectors
        Pbind("test_3", count=Pseq([1, 4, 2], n=4), const=9),
        Pbind("test_4", count=Pseq(range(3), n=4), const=7)
    ],[
        # expected
        {"test_3": {"count": 1, "const": 9}, "test_4": {"count": 0, "const": 7}},
        {"test_3": {"count": 4, "const": 9}, "test_4": {"count": 1, "const": 7}},
        {"test_3": {"count": 2, "const": 9}, "test_4": {"count": 2, "const": 7}},
        {"test_3": {"count": 1, "const": 9}, "test_4": {"count": 0, "const": 7}},
    ]),
])
def test_collector_bundles(collectors, expected):
    for collector in collectors:
        assert collector._name in Pbind.get_registry()
        assert collector == Pbind.get_registry().get(collector._name)
