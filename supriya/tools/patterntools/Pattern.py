import itertools as it
import random

from .Stream import Routine, FuncStream


def repeater(iterable, n):
    """ cycles through the values of :param:iterable :param:n times
    :param iterable: a _finite_ sequence
    :param n: number of times to cycle through items in :param:iterable
    """
    repeat = it.repeat(iterable, n)
    for seq in repeat:
        yield from seq

def fold(value, low, high):
    if value < low:
        value = low + value
    elif value > high:
        value = value - high
    else:
        return value
    if value < low or value > high:
        return fold(value, low, high)

def clip(value, low, high):
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value

class _PatternBase(object):
    def __init__(self, repetitions=None):
        self.repetitions = repetitions

    def __iter__(self):
        return self

    def __next__(self):
        return self

    def __hash__(self):
        return hash(self.__str__())

    @property
    def is_infinite(self):
        return self.repetitions is None

    def reset(self):
        return self


class _BaseBind(dict, _PatternBase):

    __registry = {}

    def __init__(self, name, **elements):
        self._name = name
        super(Pbind, self).__init__(**elements)
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
        message_class = namedtuple("Event", self.keys())
        def get_stream(message_class):
            while True:
                message = {}
                for key, value in streams.items():
                    if hasattr(value, "__next__"):
                        value = next(value)
                    message[key] = value
                yield message_class(**message)
        return Routine(FuncStream(get_stream, message_class))

    @classmethod
    def get_registry(cls):
        return cls.__registry

    @classmethod
    def _register_instance(cls, instance):
        registry = cls.get_registry()
        registry.update({instance._name: instance})


class Pattern(_PatternBase):
    def __init__(self, sequence, **kwargs):
        self.sequence = sequence
        super(Pattern, self).__init__(**kwargs)

    def __str__(self):
        return "{0}(repetitions={1}, sequence={2})".format(self.__class__.__name__,
                self.repetitions, self.sequence)
    __repr__ = __str__

    def get_sequence(self):
        return self.sequence

    def as_stream(self):
        seq = self.get_sequence()
        if not self.is_infinite:
            routine_param = repeater(seq, self.repetitions)
        else:
            routine_param = it.cycle(seq)
        return Routine(routine_param)


class NonSequenceStreamMixin(object):
    def get_sequence(self):
        raise NotImplemented

    def as_stream(self):
        seq = FuncStream(self.get_generator())  # should return a function
        if not self.is_infinite:
            return Routine(repeater(seq, self.repetitions))
        return seq


class _BaseRange(NonSequenceStreamMixin, _PatternBase):
    def __init__(self, low, high, **kwargs):
        self.low = low
        self.high = high
        super(_PatternBase, self).__init__(**kwargs)

    def __str__(self):
        return "{0}(reptetitions={1}, low={2}, high={3})".format(self.__class__.__name__,
                self.reptetitions, self.low, self.high)
    __repr__ = __str__


class _BaseWeightedPattern(NonSequenceStreamMixin, Pattern):
    def __init__(self, weights, *args, **kwargs):
        self.weights = weights
        super(_BaseWeightedSequence, self).__init__(*args, **kwargs)

    def windex(self):
        # get the weights between 0 and 1
        max_weight, min_weight = max(self.weights), min(self.weights)
        diver = max_weight - min_weight
        weights = map(lambda x: (x - min_weight) / diver, self.weights)
        return tuple(zip(*sorted(enumerate(weights), key=lambda x: x[-1])))


####################
# RANDOM PATTERNS
####################

class Pwhite(_BaseRange):
    """ a basic random number generator

    :param low: the low value of the random range
    :param high: the high value of the random range
    :param repetitions: a length (if the sequence is not infinite)
    :returns: random floating point number between high and low
    """
    def get_sequence(self):
        return lambda: random.uniform(self.low, self.high)

class Pbrown(_PatternBase, NonSequenceStreamMixin):
    def __init__(self, low, high, step, **kwargs):
        self.low = low
        self.high = high
        self.step = step
        super(Pbrown, self).__init__(**kwargs)
        self._lastval = None

class Pgauss(_PatternBase, NonSequenceStreamMixin):
    """ a basic random number generator

    :param mean: the mean value of the distrobution (mu)
    :param dev: the deviation of the distrobution (sigma)
    :param repetitions: a length (if the sequence is not infinite)
    :returns: random floating point number between high and low
    """
    def __init__(self, mean, dev, **kwargs):
        self.mean = mean
        self.dev = dev
        super(Pgauss, self).__init__(**kwargs)

    def get_sequence(self):
        return lambda: random.gauss(self.low, self.high)


class PRandInt(_BaseRange):
    """ a basic random number generator

    :param low: the low value of the random range
    :param high: the high value of the random range
    :param repetitions: a length (if the sequence is not infinite)
    :returns: random integer number between high and low
    """
    def get_sequence(self):
        return lambda: random.randrange(self.low, self.high)


####################
# RANDOM SEQUENCES
####################

class Prand(Pattern, NonSequenceStreamMixin):
    """ chooses a random element from the sequence

    :param sequence: a sequence of values
    :param repetitions: a length (if the sequence is not infinite)
    :returns: a random element of the sequence
    """
    def get_sequence(self):
        return lambda: random.choice(self.sequence)


class Pwrand(_BaseWeightedPattern):
    """ chooses an element from the :param:sequence based on probabilites defined by
    the :weights: parameter

    :param repetitions: a length (if the sequence is not infinite)
    :param sequence: an iterable (MUST BE INDEXABLE!)
    :param weights: a list of probabilites
    :returns: randomly selected elements from sequence
    """
    def get_sequence(self):
        def choose():
            rand = random.random()
            for index, weight in self.windex:
                if rand < weight:
                    return self.sequence[index]
        return choose


####################
# DETERMINISTIC SEQUENCES
####################

class Pseq(Pattern):
    """ a basic cyclical sequence generator.
    takes :param: sequence and loops through its values.

    :param sequence: an iterable
    :param repetitions: a length (if the sequence is not infinite)
    :returns: elements of :param:sequence in order
    """
    pass


class Pflat(Pseq):
    """ takes a n-dimensional sequence of sequences and flattens the output into
    a single stream.

    :param sequence: an iterable containing iterables
    :param repetitions: a length (if the sequence is not infinite)
    :returns: all atomic (non sequence) elements of :param:sequence and subpatterns
    """
    def get_sequence(self):
        for pattern in self.sequence:
            if hasattr(pattern, "as_stream"):
                yield from pattern.as_stream()
            elif hasattr(pattern, "__iter__"):
                yield from iter(pattern)
            else:
                yield pattern


####################
# FUNCTION SEQUENCES
####################
class Pfunc(_PatternBase, NonSequenceStreamMixin):
    """ executes :param:function per iteration as a stream

    :param function: a function to execute per iterator
    :reset_function: a function to execute on self.as_stream().reset()
    :param repetitions: number of time to execute function (if sequence is not infinite)
    :returns: return value of :param:function
    """
    def __init__(self, function, reset_function=None, **kwargs):
        self.function = function
        self.reset_function = reset_function if callable(reset_function) else \
                (lambda: reset_function)
        self.repetitions = repetitions
        super(Pfunc, self).__init__(**kwargs)

    def get_stream(self):
        return self.function

    def as_stream(self):
        stream = super(PFunc, self).as_stream()
        stream.reset = self.reset_function
        return stream


class Plazy(_PatternBase, NonSequenceStreamMixin):
    """ executes :param:function who's return type is a Pattern

    :param function: a function with the signature () -> Sequence
    :param repetitions: number of times to execute :param:function in a stream
    """
    def __init__(self, function, **kwargs):
        self.function = function
        super(Plazy, self).__init__(**kwargs)

    def get_sequence(self):
        def get_stream():
            try:
                return self.function().as_stream()
            except AttributeError:
                raise ValueError(Pattern)
        return get_stream


####################
# UTIL
####################
class Pn(Pattern):
    """ repeates the :param:sequence :param:repetition # of times

    :param sequence: a _finite_ sequence
    :param repetitions: number of times to cycle through items in :param:sequence
    :returns: element from :param:sequence
    """
    def get_sequence(self):
        repeat = it.repeat(self.sequence, self.repetitions)
        for seq in repeat:
            yield from seq


class Pif(_PatternBase, NonSequenceStreamMixin):
    """ evaluates :param:condition and returns the
    """
    def __init__(self, condition, if_true, if_false, default, **kwargs):
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false
        self.default = default
        super(Pif, self).__init__(**kwargs)

    def evaluate_condition(self):
        return self.condition() if callable(self.condition) else self.condition

    def get_sequence(self):
        def get_stream():
            val = self.evaluate_condition()
            if val is True:
                return self.if_true
            elif val is False:
                return self.if_false
            return self.default
        return get_stream


####################
# BINDING
####################
class Pbind(_BaseBind):
    """ binds many patterns to arbitrary keys.
    when converted to a stream with :method:.as_stream(), yields :class:Events instances
    returning the next value on each value.

    :param name: a unique key with which to refer to this pattern by
    :param elements: key, pattern mappings
    :returns: :class:Event objects
    """
    def get_sequence(self):
        """ converts all of the bound values into streams
        """
        iterators = {}
        for key, value in self.items():
            if hasattr(value, "as_stream"):
                value = value.as_stream()
            elif isiterable(value):
                value = iter(value)
            iterators[key] = value
        return iterators
