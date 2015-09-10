from collections import namedtuple, Iterable

def isiterable(value):
    return isinstance(value, Iterable)


class _BaseCollector(dict):
    """ a collector takes n kwargs and when converted to an iterator that yeilds the
    next element of all its iterables.
    """
    def __getattr__(self, attr):
        return self.__getitem__(attr)

    def __setattr__(self, attr, value):
        try:
            return super(_BaseCollector, self).__setattr__(attr, value)
        except AttributeError:
            return self.__setitem__(attr, value)

    def __str__(self):
        return "{0}({1})".format(self.__class__.__name__,
            ", ".join("{0}={1}".format(key, value) for key, value in self.items()))
    __repr__ = __str__

    def _make_streams(self):
        """ coverts all of the iterable values to iterators
        :returns: a dict where all iterables have been cast to iterators
        """
        iterators = {}
        for key, value in self.items():
            if isiterable(value):
                value = iter(value)
            iterators[key] = value
        return iterators

    def make_message(self):
        """ collects all of the kwargs, converts them to iterators
        """
        streams = self._make_streams()
        message_class = namedtuple("Event", self.keys())
        while True:
            message = {}
            for key, value in streams.items():
                if hasattr(value, "__next__"):
                    value = next(value)
                message[key] = value
            yield message_class(**message)


class _BaseCollectorRegistry(dict):
    __registry = {}

    def __init__(self, name, **elements):
        self._name = name
        super(_BaseCollectorRegistry, self).__init__(**elements)
        type(self)._register_instance(self)

    @classmethod
    def get_registry(cls):
        return cls.__registry

    @classmethod
    def _register_instance(cls, instance):
        registry = cls.get_registry()
        registry.update({instance._name: instance})

    @classmethod
    def _make_registry_streams(cls):
        iterators = {}
        for key, value in cls.__registry.items():
            if isiterable(value):
                value = iter(value)
            iterators[key] = value
        return iterators

    @classmethod
    def make_registry_bundle(cls):
        bundle_class = namedtuple("Bundle", cls.__registry.keys())
        streams = cls._make_registry_streams()
        while True:
            bundle = {}
            for name, message in streams.items():
                if hasattr(message, "__next__"):
                    message = next(message)
                bundle[name] = message
            yield bundle_class(**bundle)


class PCollector(_BaseCollectorRegistry, _BaseCollector):
    """
    """
    pass
