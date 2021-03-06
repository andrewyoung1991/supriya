# -*- encoding: utf-8 -*-
from supriya.tools import synthdeftools
from supriya.tools import ugentools


def test_SynthDefCompiler_parameters_01():

    sc_synthdef = synthdeftools.SuperColliderSynthDef(
        'test',
        r'''
        | freq = 440 |
        Out.ar(0, SinOsc.ar(freq: freq))
        '''
        )
    sc_compiled_synthdef = sc_synthdef.compile()

    with synthdeftools.SynthDefBuilder(freq=440) as builder:
        sine = ugentools.SinOsc.ar(frequency=builder['freq'])
        ugentools.Out.ar(bus=0, source=sine)
    py_synthdef = builder.build('test')
    py_compiled_synthdef = py_synthdef.compile()

    assert py_synthdef.indexed_parameters == (
        (
            0,
            synthdeftools.Parameter(
                name='freq',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=440.0,
                ),
            ),
        )

    test_compiled_synthdef = bytes(
        b'SCgf'
        b'\x00\x00\x00\x02'
        b'\x00\x01'
            b'\x04test'
                b'\x00\x00\x00\x01'
                    b'\x00\x00\x00\x00'
                b'\x00\x00\x00\x01'
                    b'C\xdc\x00\x00'
                b'\x00\x00\x00\x01'
                    b'\x04freq'
                    b'\x00\x00\x00\x00'
                b'\x00\x00\x00\x03'
                    b'\x07Control'
                        b'\x01'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x01'
                    b'\x06SinOsc'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x03Out'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x00'
                b'\x00\x00',
        )

    assert sc_compiled_synthdef == test_compiled_synthdef
    assert py_compiled_synthdef == test_compiled_synthdef


def test_SynthDefCompiler_parameters_02():

    sc_synthdef = synthdeftools.SuperColliderSynthDef(
        'test',
        r'''
        arg freq=1200, out=23;
        Out.ar(out, SinOsc.ar(freq: freq));
        '''
        )
    sc_compiled_synthdef = sc_synthdef.compile()

    builder = synthdeftools.SynthDefBuilder(
        freq=1200,
        out=23,
        )
    sine = ugentools.SinOsc.ar(frequency=builder['freq'])
    out = ugentools.Out.ar(bus=builder['out'], source=sine)
    builder.add_ugens(out)
    py_synthdef = builder.build('test')
    py_compiled_synthdef = py_synthdef.compile()

    assert py_synthdef.indexed_parameters == (
        (
            0,
            synthdeftools.Parameter(
                name='freq',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=1200.0,
                ),
            ),
        (
            1,
            synthdeftools.Parameter(
                name='out',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=23.0,
                ),
            ),
        )

    test_compiled_synthdef = bytes(
        b'SCgf'
        b'\x00\x00\x00\x02'
        b'\x00\x01'
            b'\x04test'
                b'\x00\x00\x00\x01'
                    b'\x00\x00\x00\x00'
                b'\x00\x00\x00\x02'
                    b'D\x96\x00\x00'
                    b'A\xb8\x00\x00'
                b'\x00\x00\x00\x02'
                    b'\x04freq'
                        b'\x00\x00\x00\x00'
                    b'\x03out'
                        b'\x00\x00\x00\x01'
                b'\x00\x00\x00\x03'
                    b'\x07Control'
                        b'\x01'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00'
                        b'\x01'
                        b'\x01'
                    b'\x06SinOsc'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x03Out'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x00'
                b'\x00\x00',
        )

    assert sc_compiled_synthdef == test_compiled_synthdef
    assert py_compiled_synthdef == test_compiled_synthdef


def test_SynthDefCompiler_parameters_03():
    r'''Multiple parameters, including unused parameters.
    '''

    sc_synthdef = synthdeftools.SuperColliderSynthDef(
        'test',
        r'''
        | damping=0.1, delay_time=1.0, room_size=0.9 |
        Out.ar(0, DelayC.ar(In.ar(0), 5.0, delay_time))
        '''
        )
    sc_compiled_synthdef = sc_synthdef.compile()

    builder = synthdeftools.SynthDefBuilder(
        damping=0.1,
        delay_time=1.0,
        room_size=0.9,
        )
    with builder:
        microphone = ugentools.In.ar(bus=0)
        delay = ugentools.DelayC.ar(
            source=microphone,
            maximum_delay_time=5.0,
            delay_time=builder['delay_time'],
            )
        ugentools.Out.ar(bus=0, source=delay)
    py_synthdef = builder.build('test')
    py_compiled_synthdef = py_synthdef.compile()

    assert py_synthdef.indexed_parameters == (
        (
            0,
            synthdeftools.Parameter(
                name='damping',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=0.1,
                ),
            ),
        (
            1,
            synthdeftools.Parameter(
                name='delay_time',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=1.0,
                ),
            ),
        (
            2,
            synthdeftools.Parameter(
                name='room_size',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=0.9,
                ),
            ),
        )

    test_compiled_synthdef = bytes(
        b'SCgf'
        b'\x00\x00\x00\x02'
        b'\x00\x01'
            b'\x04test'
                b'\x00\x00\x00\x02'
                    b'\x00\x00\x00\x00'
                    b'@\xa0\x00\x00'
                b'\x00\x00\x00\x03'
                    b'=\xcc\xcc\xcd'
                    b'?\x80\x00\x00'
                    b'?fff'
                b'\x00\x00\x00\x03'
                    b'\x07damping'
                        b'\x00\x00\x00\x00'
                    b'\ndelay_time'
                        b'\x00\x00\x00\x01'
                    b'\x09room_size'
                        b'\x00\x00\x00\x02'
                b'\x00\x00\x00\x04'
                    b'\x07Control'
                        b'\x01'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00'
                            b'\x01'
                            b'\x01'
                            b'\x01'
                    b'\x02In'
                        b'\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x06DelayC'
                        b'\x02'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x01'
                            b'\x02'
                    b'\x03Out'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x02'
                            b'\x00\x00\x00\x00'
                b'\x00\x00',
        )

    assert sc_compiled_synthdef == test_compiled_synthdef
    assert py_compiled_synthdef == test_compiled_synthdef


def test_SynthDefCompiler_parameters_04():
    r'''Different calculation rates.'''

    sc_synthdef = synthdeftools.SuperColliderSynthDef(
        'trigTest',
        r'''
        |
            a_phase = 0.0,
            freq = 440,
            i_decay_time = 1.0,
            t_trig_a = 0,
            t_trig_b = 0
        |
        var decay = Decay2.kr([t_trig_a, t_trig_b], 0.005, i_decay_time);
        Out.ar(0, SinOsc.ar(freq, a_phase) * decay);
        '''
        )
    sc_compiled_synthdef = bytes(sc_synthdef.compile())

    builder = synthdeftools.SynthDefBuilder(
        a_phase=0.0,
        freq=440,
        i_decay_time=1.0,
        t_trig_a=0,
        t_trig_b=0,
        )
    with builder:
        decay = ugentools.Decay2.kr(
            source=(builder['t_trig_a'], builder['t_trig_b']),
            attack_time=0.005,
            decay_time=builder['i_decay_time'],
            )
        sin_osc = ugentools.SinOsc.ar(
            frequency=builder['freq'],
            phase=builder['a_phase'],
            )
        enveloped_sin_osc = sin_osc * decay
        ugentools.Out.ar(
            bus=0,
            source=enveloped_sin_osc,
            )
    py_synthdef = builder.build('trigTest')
    py_compiled_synthdef = py_synthdef.compile()

    assert py_synthdef.indexed_parameters == (
        (
            3,
            synthdeftools.Parameter(
                name='a_phase',
                parameter_rate=synthdeftools.ParameterRate.AUDIO,
                value=0.0,
                ),
            ),
        (
            4,
            synthdeftools.Parameter(
                name='freq',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=440.0,
                ),
            ),
        (
            0,
            synthdeftools.Parameter(
                name='i_decay_time',
                parameter_rate=synthdeftools.ParameterRate.SCALAR,
                value=1.0,
                ),
            ),
        (
            1,
            synthdeftools.Parameter(
                name='t_trig_a',
                parameter_rate=synthdeftools.ParameterRate.TRIGGER,
                value=0.0,
                ),
            ),
        (
            2,
            synthdeftools.Parameter(
                name='t_trig_b',
                parameter_rate=synthdeftools.ParameterRate.TRIGGER,
                value=0.0,
                ),
            ),
        )

    test_compiled_synthdef = bytes(
        b'SCgf'
        b'\x00\x00\x00\x02'
        b'\x00\x01'
            b'\x08trigTest'
                b'\x00\x00\x00\x02'
                    b';\xa3\xd7\n'
                    b'\x00\x00\x00\x00'
                b'\x00\x00\x00\x05'
                    b'?\x80\x00\x00'  # i_decay_time
                    b'\x00\x00\x00\x00'  # t_trig_a
                    b'\x00\x00\x00\x00'  # t_trig_b
                    b'\x00\x00\x00\x00'  # a_phase
                    b'C\xdc\x00\x00'  # freq
                b'\x00\x00\x00\x05'
                    b'\x07a_phase'
                        b'\x00\x00\x00\x03'
                    b'\x04freq'
                        b'\x00\x00\x00\x04'
                    b'\x0ci_decay_time'
                        b'\x00\x00\x00\x00'
                    b'\x08t_trig_a'
                        b'\x00\x00\x00\x01'
                    b'\x08t_trig_b'
                        b'\x00\x00\x00\x02'
                b'\x00\x00\x00\n'
                    b'\x07Control'
                        b'\x00'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00'
                    b'\x0bTrigControl'
                        b'\x01'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x02'
                        b'\x00\x01'
                            b'\x01'
                            b'\x01'
                    b'\x06Decay2'
                        b'\x01'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\x01'
                    b'\x06Decay2'
                        b'\x01'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x01'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                            b'\x01'
                    b'\x0cAudioControl'
                        b'\x02'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x01'
                        b'\x00\x03'
                            b'\x02'
                    b'\x07Control'
                        b'\x01'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x01'
                        b'\x00\x04'
                            b'\x01'
                    b'\x06SinOsc'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x05'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x04'
                            b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x0cBinaryOpUGen'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x02'
                            b'\x00\x00\x00\x06'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x02'
                            b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x0cBinaryOpUGen'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x02'
                            b'\x00\x00\x00\x06'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x03'
                            b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x03Out'
                        b'\x02'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00'
                            b'\xff\xff\xff\xff'
                            b'\x00\x00\x00\x01'
                            b'\x00\x00\x00\x07'
                            b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x08'
                            b'\x00\x00\x00\x00'
                b'\x00\x00'
        )

    assert sc_compiled_synthdef == test_compiled_synthdef
    assert py_compiled_synthdef == test_compiled_synthdef


def test_SynthDefCompiler_parameters_05():
    r'''Literal array arguments.'''

    builder = synthdeftools.SynthDefBuilder(
        amp=0.1,
        freqs=[300, 400],
        )
    with builder:
        sines = ugentools.SinOsc.ar(
            frequency=builder['freqs'],
            )
        sines = ugentools.Mix.new(sines)
        sines = sines * builder['amp']
        ugentools.Out.ar(
            bus=0,
            source=sines,
            )
    py_synthdef = builder.build('arrayarg')
    py_compiled_synthdef = py_synthdef.compile()

    assert py_synthdef.indexed_parameters == (
        (
            0,
            synthdeftools.Parameter(
                name='amp',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=0.1,
                ),
            ),
        (
            1,
            synthdeftools.Parameter(
                name='freqs',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=(300.0, 400.0)
                ),
            ),
        )

    sc_synthdef = synthdeftools.SuperColliderSynthDef(
        'arrayarg',
        r'''
        |
            amp = 0.1,
            freqs = #[300, 400]
        |
        var sines;
        sines = SinOsc.ar(freqs).sum;
        Out.ar(0, sines * amp);
        ''',
        )
    sc_compiled_synthdef = bytes(sc_synthdef.compile())

    test_compiled_synthdef = bytes(
        b'SCgf'
        b'\x00\x00\x00\x02'
        b'\x00\x01'
            b'\x08arrayarg'
                b'\x00\x00\x00\x01'
                    b'\x00\x00\x00\x00'
                b'\x00\x00\x00\x03'
                    b'=\xcc\xcc\xcd'
                    b'C\x96\x00\x00'
                    b'C\xc8\x00\x00'
                b'\x00\x00\x00\x02'
                    b'\x03amp'
                        b'\x00\x00\x00\x00'
                    b'\x05freqs'
                        b'\x00\x00\x00\x01'
                b'\x00\x00\x00\x06'
                    b'\x07Control'
                        b'\x01'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00'
                            b'\x01'
                            b'\x01'
                            b'\x01'
                    b'\x06SinOsc'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x00'
                                b'\x00\x00\x00\x01'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x06SinOsc'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x00'
                                b'\x00\x00\x00\x02'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x0cBinaryOpUGen'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x01'
                                b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x02'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x0cBinaryOpUGen'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x02'
                            b'\x00\x00\x00\x03'
                                b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x03Out'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x04'
                                b'\x00\x00\x00\x00'
                b'\x00\x00'
        )

    assert sc_compiled_synthdef == test_compiled_synthdef
    assert py_compiled_synthdef == test_compiled_synthdef


def test_SynthDefCompiler_parameters_06():
    r'''Literal array arguments.'''

    builder = synthdeftools.SynthDefBuilder(
        amp=0.1,
        freqs=synthdeftools.Parameter(
            lag=0.5,
            value=[300, 400],
            ),
        )
    with builder:
        sines = ugentools.SinOsc.ar(
            frequency=builder['freqs'],
            )
        sines = ugentools.Mix.new(sines)
        sines = sines * builder['amp']
        ugentools.Out.ar(
            bus=0,
            source=sines,
            )
    py_synthdef = builder.build('arrayarg')
    py_compiled_synthdef = py_synthdef.compile()

    assert py_synthdef.indexed_parameters == (
        (
            0,
            synthdeftools.Parameter(
                name='amp',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=0.1,
                ),
            ),
        (
            1,
            synthdeftools.Parameter(
                lag=0.5,
                name='freqs',
                parameter_rate=synthdeftools.ParameterRate.CONTROL,
                value=(300.0, 400.0)
                ),
            ),
        )

    sc_synthdef = synthdeftools.SuperColliderSynthDef(
        'arrayarg',
        r'''
        |
            amp = 0.1,
            freqs = #[300, 400]
        |
        var sines;
        sines = SinOsc.ar(freqs).sum;
        Out.ar(0, sines * amp);
        ''',
        [0, 0.5],
        )
    sc_compiled_synthdef = bytes(sc_synthdef.compile())

    test_compiled_synthdef = bytes(
        b'SCgf'
        b'\x00\x00\x00\x02'
        b'\x00\x01'
            b'\x08arrayarg'
                b'\x00\x00\x00\x02'
                    b'\x00\x00\x00\x00'
                    b'?\x00\x00\x00'
                b'\x00\x00\x00\x03'
                    b'=\xcc\xcc\xcd'
                    b'C\x96\x00\x00'
                    b'C\xc8\x00\x00'
                b'\x00\x00\x00\x02'
                    b'\x03amp'
                        b'\x00\x00\x00\x00'
                    b'\x05freqs'
                        b'\x00\x00\x00\x01'
                b'\x00\x00\x00\x06'
                    b'\nLagControl'
                        b'\x01'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00\x00\x03'
                        b'\x00\x00'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x00'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x01'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x01'
                            b'\x01'
                            b'\x01'
                            b'\x01'
                    b'\x06SinOsc'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x00'
                                b'\x00\x00\x00\x01'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x06SinOsc'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x00'
                                b'\x00\x00\x00\x02'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x0cBinaryOpUGen'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x00'
                            b'\x00\x00\x00\x01'
                                b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x02'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x0cBinaryOpUGen'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x01'
                        b'\x00\x02'
                            b'\x00\x00\x00\x03'
                                b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x00'
                                b'\x00\x00\x00\x00'
                            b'\x02'
                    b'\x03Out'
                        b'\x02'
                        b'\x00\x00\x00\x02'
                        b'\x00\x00\x00\x00'
                        b'\x00\x00'
                            b'\xff\xff\xff\xff'
                                b'\x00\x00\x00\x00'
                            b'\x00\x00\x00\x04'
                                b'\x00\x00\x00\x00'
                b'\x00\x00'
        )

    assert sc_compiled_synthdef == test_compiled_synthdef
    assert py_compiled_synthdef == test_compiled_synthdef