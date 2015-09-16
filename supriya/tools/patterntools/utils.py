import itertools as it
import functools
import collections


def isiterable(value):
    """ returns true if :param:value is iterable
    """
    return isinstance(value, collections.Iterable)


def repeater(iterable, n):
    """ cycles through the values of :param:iterable :param:n times
    :param iterable: a _finite_ sequence
    :param n: number of times to cycle through items in :param:iterable
    """
    repeat = it.repeat(iterable, n)
    for seq in repeat:
        yield from seq


def wrap(value, low, high):
    """
    inline double sc_wrap(double in, double lo, double hi)
    {
        double range;
        // avoid the divide if possible
        if (in >= hi) {
            range = hi - lo;
            in -= range;
            if (in < hi) return in;
        } else if (in < lo) {
            range = hi - lo;
            in += range;
            if (in >= lo) return in;
        } else return in;

        if (hi == lo) return lo;
        return in - range * sc_floor((in - lo)/range);
    }
    """
    _range = high - low
    if high <= value:
        value -= _range
    elif value < low:
        value += _range
    else:
        return value

    if value < high and low <= value:
        return value
    if high == low:
        return low
    return value - _range * ((value - low) // _range)


def fold(value, low, high):
    """
    inline float sc_fold(float in, float lo, float hi)
    {
        float x, c, range, range2;
        x = in - lo;

        // avoid the divide if possible
        if (in >= hi) {
            in = hi + hi - in;
            if (in >= lo) return in;
        } else if (in < lo) {
            in = lo + lo - in;
            if (in < hi) return in;
        } else return in;

        if (hi == lo) return lo;
        // ok do the divide
        range = hi - lo;
        range2 = range + range;
        c = x - range2 * sc_floor(x / range2);
        if (c>=range) c = range2 - c;
        return c + lo;
    }
    """
    x = value - low
    if high <= value:
        value = (high * 2) - value
    elif value < low:
        value = (low * 2) - value
    else:
        return value

    if value < high and low <= value:
        return value

    if high == low:
        return low

    range_1 = high - low
    range_2 = range_1 * 2
    c = x - range_2 * (x // range_2)
    if range_1 <= c:
        c = range_2 - c

    return c + low


def clip(value, low, high):
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value


def distort(value):
    return value / (1.0 + abs(value))

def curve(value):
    if value <= 0.0:
        return 0.0
    elif 1.0 <= value:
        return 1.0
    return value **3


def wrap_stream(function):
    def wrapper(inner_func):
        @functools.wraps(inner_func)
        def closure(self, other):
            pattern = mash_patterns(function, self, other)
            pattern.n = self.n
            return pattern
        return closure
    return wrapper


def mash_patterns(operation, *patterns):
    from supriya.tools.patterntools.Pattern import Pseq
    _ab = []
    for thing in patterns:
        if isiterable(thing):
            _a = iter(thing)
        else:
            _a = it.repeat(thing)
        _ab.append(_a)
    return Pseq(map(operation, *_ab))

