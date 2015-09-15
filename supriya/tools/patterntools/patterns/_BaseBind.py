"""
"""
import collections

from supriya.tools.patterntools.patterns._PatternBase import _PatternBase
from supriya.tools.patterntools.streams import FuncStream, Routine


class _BaseBind(dict, _PatternBase):
    """
    """
    __registry = {}

    def __init__(self, name, **elements):
        self._name = name
        super(_BaseBind, self).__init__(**elements)
        type(self)._register_instance(self)

    def __getattr__(self, attr):
        return self.__getitem__(attr)

    def __setattr__(self, attr, value):
        try:
            return super(_BaseBind, self).__setattr__(attr, value)
        except AttributeError as err:
            if atter in self:
                return self.__setitem__(attr, value)
            raise AttributeError(err)

    def __str__(self):
        items = super(_BaseBind, self).__str__()
        return "{0}({1})".format(self.__class__.__name__, items)

    def get_sequence(self):
        raise NotImplementedError

    def as_stream(self):
        streams = self.get_sequence()
        message_class = collections.namedtuple("Payload", self.keys())
        def get_stream(message_class):
            while True:
                message = {}
                for key, value in streams.items():
                    if hasattr(value, "__next__"):
                        value = next(value)
                    message[key] = value
                yield message_class(**message)
        return Routine((next(event) for event in FuncStream(get_stream, message_class)))

    @classmethod
    def get_registry(cls):
        return cls.__registry

    @classmethod
    def _register_instance(cls, instance):
        registry = cls.get_registry()
        registry.update({instance._name: instance})
