import pytest

from ..PatternCollector import PCollector
from ..Pattern import PSeq


@pytest.mark.parametrize("elements,expected", [
    ({"count": PSeq(4, sequence=range(4)), "const": 4}, [
            {"count": 0, "const": 4}, {"count": 1, "const": 4},
            {"count": 2, "const": 4}, {"count": 3, "const": 4}]),
    ({"count": PSeq(4, sequence=list(range(4))), "const": 4,
        "foo": PSeq(2, sequence=["hi", "there"])}, [
            {"count": 0, "const": 4, "foo": "hi"},
            {"count": 1, "const": 4, "foo": "there"}]),
    ])
def test_collector_messages(elements, expected):
    collector = PCollector("test", **elements).as_stream()
    expected = iter(expected)

    for message in collector:
        assert message.__dict__ == next(expected)


@pytest.mark.parametrize("collectors,expected", [
    ([
        # collectors
        PCollector("test_1", count=PSeq(2, sequence=range(2)), const=3),
        PCollector("test_2", count=PSeq(3, sequence=range(3)), const=4)
    ],[
        # expected
        {"test_1": {"count": 0, "const": 3}, "test_2": {"count": 0, "const": 4}},
        {"test_1": {"count": 1, "const": 3}, "test_2": {"count": 1, "const": 4}}
    ]),
    ([
        # collectors
        PCollector("test_3", count=PSeq(4, sequence=[1, 4, 2]), const=9),
        PCollector("test_4", count=PSeq(4, sequence=range(3)), const=7)
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
        assert collector._name in PCollector.get_registry()
        assert collector == PCollector.get_registry().get(collector._name)
    expected = iter(expected)
    bundles = PCollector.make_registry_bundle()
    for bundle in bundles:
        expect = next(expected)
        for key, value in expect.items():
            assert hasattr(bundle, key)
            assert getattr(bundle, key).__dict__ == value
