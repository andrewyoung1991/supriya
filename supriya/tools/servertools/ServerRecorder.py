# -*- encoding: utf-8 -*-
import os
from supriya.tools.systemtools.SupriyaObject import SupriyaObject


class ServerRecorder(SupriyaObject):

    ### CLASS VARIABLES ###

    __documentation_section__ = 'Server Internals'

    __slots__ = (
        '_channel_count',
        '_current_channel_count',
        '_current_header_format',
        '_current_file_path',
        '_current_sample_format',
        '_header_format',
        '_is_recording',
        '_record_buffer',
        '_record_node',
        '_record_synthdef',
        '_sample_format',
        '_server',
        )

    ### INITIALIZER ###

    def __init__(self, server):
        from supriya.tools import soundfiletools
        self._server = server
        server_options = server.server_options
        # setup settings
        self._channel_count = server_options.output_bus_channel_count
        self._header_format = soundfiletools.HeaderFormat.AIFF
        self._is_recording = False
        self._record_node = None
        self._record_buffer = None
        self._record_synthdef = None
        self._sample_format = soundfiletools.SampleFormat.INT24
        # cache settings
        self._current_channel_count = self._channel_count
        self._current_file_path = None
        self._current_header_format = self._header_format
        self._current_sample_format = self._sample_format

    ### PRIVATE METHODS ###

    def _cache_properties(
        self,
        channel_count=None,
        header_format=None,
        sample_format=None,
        ):
        from supriya.tools import soundfiletools
        if channel_count is None:
            channel_count = self.channel_count
        self._current_channel_count = channel_count
        if header_format is None:
            header_format = self.header_format
        self._current_header_format = soundfiletools.HeaderFormat.from_expr(
            header_format)
        if sample_format is None:
            sample_format = self.sample_format
        self._current_sample_format = soundfiletools.SampleFormat.from_expr(
            sample_format)

    def _get_file_path(self, file_path=None):
        if file_path is not None:
            file_path = os.path.abspath(os.path.expanduser(file_path))
        return file_path

    def _get_record_id(self):
        return 23

    def _setup_buffer(self):
        from supriya.tools import requesttools
        from supriya.tools import servertools
        buffer_id = self._get_record_id()
        buffer_ = servertools.Buffer(buffer_id)
        frame_count = 65536
        buffer_.allocate(
            frame_count=frame_count,
            channel_count=self.current_channel_count,
            )
        completion_message = requesttools.BufferWriteRequest(
            buffer_id=buffer_id,
            file_path=self.current_file_path,
            frame_count=0,
            header_format=self.current_header_format,
            leave_open=True,
            sample_format=self.current_sample_format,
            starting_frame=0,
            )
        completion_message.communicate(
            server=self.server,
            sync=True,
            )
        self._record_buffer = buffer_

    def _setup_node(self):
        from supriya.tools import servertools
        synth = servertools.Synth(self.record_synthdef)
        synth.allocate(
            add_action=servertools.AddAction.ADD_TO_TAIL,
            target_node=self.server.root_node,
            node_id_is_permanent=True,
            )
        self._record_node = synth

    def _setup_synthdef(self):
        from supriya.tools import synthdeftools
        from supriya.tools import ugentools
        with synthdeftools.SynthDefBuilder() as builder:
            source = ugentools.In.ar(
                bus=0,
                channel_count=self.current_channel_count,
                )
            buffer_id = int(self.record_buffer)
            ugentools.DiskOut.ar(
                buffer_id=buffer_id,
                source=source,
                )
        synthdef = builder.build()
        synthdef.allocate(server=self.server)
        self._record_synthdef = synthdef

    ### PUBLIC METHODS ###

    def pause(self):
        if self.is_recording:
            self.record_node.pause()
        else:
            raise Exception

    def prepare(
        self,
        file_path=None,
        channel_count=None,
        header_format=None,
        sample_format=None,
        ):
        if self.is_recording:
            raise Exception
        self._cache_properties(
            channel_count=channel_count,
            header_format=header_format,
            sample_format=sample_format,
            )
        self._current_file_path = self._get_file_path(file_path)
        if self.current_file_path is None:
            raise Exception
        self._setup_buffer()
        self._setup_synthdef()

    def start(
        self,
        file_path=None,
        channel_count=None,
        header_format=None,
        sample_format=None,
        ):
        if self.record_node is not None:
            raise Exception('Already recording.')
        if not self.record_buffer or not self.record_buffer.is_allocated:
            self.prepare(
                file_path=file_path,
                channel_count=channel_count,
                header_format=header_format,
                sample_format=sample_format,
                )
        self._setup_node()
        self._is_recording = True

    def stop(self):
        if not self.is_recording:
            raise Exception
        self.record_node.free()
        self.record_buffer.close()
        self.record_buffer.free()
        self._is_recording = False

    def unpause(self):
        if self.is_recording:
            self.record_node.unpause()
        else:
            raise Exception

    ### PUBLIC PROPERTIES ###

    @property
    def is_recording(self):
        return self._is_recording

    @property
    def record_buffer(self):
        return self._record_buffer

    @property
    def record_node(self):
        return self._record_node

    @property
    def record_synthdef(self):
        return self._record_synthdef

    @property
    def channel_count(self):
        return self._channel_count

    @channel_count.setter
    def channel_count(self, expr):
        channel_count = int(expr)
        assert 0 < channel_count
        self._channel_count = channel_count

    @property
    def sample_format(self):
        return self._sample_format

    @sample_format.setter
    def sample_format(self, expr):
        from supriya.tools import soundfiletools
        sample_format = soundfiletools.SampleFormat.from_expr(expr)
        self._sample_format = sample_format

    @property
    def header_format(self):
        return self._header_format

    @header_format.setter
    def header_format(self, expr):
        from supriya.tools import soundfiletools
        header_format = soundfiletools.HeaderFormat.from_expr(expr)
        self._header_format = header_format

    @property
    def current_channel_count(self):
        return self._current_channel_count

    @property
    def current_file_path(self):
        return self._current_file_path

    @property
    def current_sample_format(self):
        return self._current_sample_format

    @property
    def current_header_format(self):
        return self._current_header_format

    @property
    def server(self):
        return self._server