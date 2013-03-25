# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import core_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='stream.proto',
  package='rsctrl.stream',
  serialized_pb='\n\x0cstream.proto\x12\rrsctrl.stream\x1a\ncore.proto\"C\n\x10StreamFileDetail\x12\x1f\n\x04\x66ile\x18\x01 \x02(\x0b\x32\x11.rsctrl.core.File\x12\x0e\n\x06offset\x18\x05 \x02(\x04\"E\n\x10StreamVoipDetail\x12\x0f\n\x07peer_id\x18\x01 \x02(\t\x12\x10\n\x08\x64uration\x18\x02 \x02(\x04\x12\x0e\n\x06offset\x18\x03 \x02(\x04\"\xf1\x01\n\nStreamDesc\x12\x11\n\tstream_id\x18\x01 \x02(\r\x12.\n\x0bstream_type\x18\x02 \x02(\x0e\x32\x19.rsctrl.stream.StreamType\x12\x30\n\x0cstream_state\x18\x03 \x02(\x0e\x32\x1a.rsctrl.stream.StreamState\x12\x10\n\x08rate_kbs\x18\x04 \x02(\x02\x12-\n\x04\x66ile\x18\x05 \x01(\x0b\x32\x1f.rsctrl.stream.StreamFileDetail\x12-\n\x04voip\x18\x06 \x01(\x0b\x32\x1f.rsctrl.stream.StreamVoipDetail\"\xaf\x01\n\nStreamData\x12\x11\n\tstream_id\x18\x01 \x02(\r\x12\x30\n\x0cstream_state\x18\x02 \x02(\x0e\x32\x1a.rsctrl.stream.StreamState\x12)\n\tsend_time\x18\x03 \x02(\x0b\x32\x16.rsctrl.core.Timestamp\x12\x0e\n\x06offset\x18\x04 \x02(\x04\x12\x0c\n\x04size\x18\x05 \x02(\r\x12\x13\n\x0bstream_data\x18\x06 \x02(\x0c\"q\n\x16RequestStartFileStream\x12\x1f\n\x04\x66ile\x18\x01 \x02(\x0b\x32\x11.rsctrl.core.File\x12\x10\n\x08rate_kbs\x18\x02 \x02(\x02\x12\x12\n\nstart_byte\x18\x03 \x01(\x04\x12\x10\n\x08\x65nd_byte\x18\x04 \x01(\x04\"g\n\x14ResponseStreamDetail\x12#\n\x06status\x18\x01 \x02(\x0b\x32\x13.rsctrl.core.Status\x12*\n\x07streams\x18\x02 \x03(\x0b\x32\x19.rsctrl.stream.StreamDesc\"\xfe\x01\n\x14RequestControlStream\x12\x11\n\tstream_id\x18\x01 \x02(\r\x12@\n\x06\x61\x63tion\x18\x02 \x02(\x0e\x32\x30.rsctrl.stream.RequestControlStream.StreamAction\x12\x10\n\x08rate_kbs\x18\x03 \x01(\x02\x12\x11\n\tseek_byte\x18\x04 \x01(\x04\"l\n\x0cStreamAction\x12\x10\n\x0cSTREAM_START\x10\x01\x12\x0f\n\x0bSTREAM_STOP\x10\x02\x12\x10\n\x0cSTREAM_PAUSE\x10\x03\x12\x16\n\x12STREAM_CHANGE_RATE\x10\x04\x12\x0f\n\x0bSTREAM_SEEK\x10\x05\"E\n\x12RequestListStreams\x12/\n\x0crequest_type\x18\x01 \x02(\x0e\x32\x19.rsctrl.stream.StreamType\"b\n\x12ResponseStreamData\x12#\n\x06status\x18\x01 \x02(\x0b\x32\x13.rsctrl.core.Status\x12\'\n\x04\x64\x61ta\x18\x02 \x02(\x0b\x32\x19.rsctrl.stream.StreamData*o\n\rRequestMsgIds\x12 \n\x1cMsgId_RequestStartFileStream\x10\x01\x12\x1e\n\x1aMsgId_RequestControlStream\x10\x02\x12\x1c\n\x18MsgId_RequestListStreams\x10\x03*N\n\x0eResponseMsgIds\x12\x1e\n\x1aMsgId_ResponseStreamDetail\x10\x01\x12\x1c\n\x18MsgId_ResponseStreamData\x10\x65*e\n\nStreamType\x12\x13\n\x0fSTREAM_TYPE_ALL\x10\x01\x12\x15\n\x11STREAM_TYPE_FILES\x10\x02\x12\x14\n\x10STREAM_TYPE_VOIP\x10\x03\x12\x15\n\x11STREAM_TYPE_OTHER\x10\x04*o\n\x0bStreamState\x12\x16\n\x12STREAM_STATE_ERROR\x10\x00\x12\x14\n\x10STREAM_STATE_RUN\x10\x01\x12\x17\n\x13STREAM_STATE_PAUSED\x10\x02\x12\x19\n\x15STREAM_STATE_FINISHED\x10\x03')

_REQUESTMSGIDS = descriptor.EnumDescriptor(
  name='RequestMsgIds',
  full_name='rsctrl.stream.RequestMsgIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='MsgId_RequestStartFileStream', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MsgId_RequestControlStream', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MsgId_RequestListStreams', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1253,
  serialized_end=1364,
)


_RESPONSEMSGIDS = descriptor.EnumDescriptor(
  name='ResponseMsgIds',
  full_name='rsctrl.stream.ResponseMsgIds',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='MsgId_ResponseStreamDetail', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='MsgId_ResponseStreamData', index=1, number=101,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1366,
  serialized_end=1444,
)


_STREAMTYPE = descriptor.EnumDescriptor(
  name='StreamType',
  full_name='rsctrl.stream.StreamType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STREAM_TYPE_ALL', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_TYPE_FILES', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_TYPE_VOIP', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_TYPE_OTHER', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1446,
  serialized_end=1547,
)


_STREAMSTATE = descriptor.EnumDescriptor(
  name='StreamState',
  full_name='rsctrl.stream.StreamState',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STREAM_STATE_ERROR', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_STATE_RUN', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_STATE_PAUSED', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_STATE_FINISHED', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1549,
  serialized_end=1660,
)


MsgId_RequestStartFileStream = 1
MsgId_RequestControlStream = 2
MsgId_RequestListStreams = 3
MsgId_ResponseStreamDetail = 1
MsgId_ResponseStreamData = 101
STREAM_TYPE_ALL = 1
STREAM_TYPE_FILES = 2
STREAM_TYPE_VOIP = 3
STREAM_TYPE_OTHER = 4
STREAM_STATE_ERROR = 0
STREAM_STATE_RUN = 1
STREAM_STATE_PAUSED = 2
STREAM_STATE_FINISHED = 3


_REQUESTCONTROLSTREAM_STREAMACTION = descriptor.EnumDescriptor(
  name='StreamAction',
  full_name='rsctrl.stream.RequestControlStream.StreamAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='STREAM_START', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_STOP', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_PAUSE', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_CHANGE_RATE', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STREAM_SEEK', index=4, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=972,
  serialized_end=1080,
)


_STREAMFILEDETAIL = descriptor.Descriptor(
  name='StreamFileDetail',
  full_name='rsctrl.stream.StreamFileDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='file', full_name='rsctrl.stream.StreamFileDetail.file', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='rsctrl.stream.StreamFileDetail.offset', index=1,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=43,
  serialized_end=110,
)


_STREAMVOIPDETAIL = descriptor.Descriptor(
  name='StreamVoipDetail',
  full_name='rsctrl.stream.StreamVoipDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='peer_id', full_name='rsctrl.stream.StreamVoipDetail.peer_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='duration', full_name='rsctrl.stream.StreamVoipDetail.duration', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='rsctrl.stream.StreamVoipDetail.offset', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=112,
  serialized_end=181,
)


_STREAMDESC = descriptor.Descriptor(
  name='StreamDesc',
  full_name='rsctrl.stream.StreamDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stream_id', full_name='rsctrl.stream.StreamDesc.stream_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stream_type', full_name='rsctrl.stream.StreamDesc.stream_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stream_state', full_name='rsctrl.stream.StreamDesc.stream_state', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rate_kbs', full_name='rsctrl.stream.StreamDesc.rate_kbs', index=3,
      number=4, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='file', full_name='rsctrl.stream.StreamDesc.file', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='voip', full_name='rsctrl.stream.StreamDesc.voip', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=184,
  serialized_end=425,
)


_STREAMDATA = descriptor.Descriptor(
  name='StreamData',
  full_name='rsctrl.stream.StreamData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stream_id', full_name='rsctrl.stream.StreamData.stream_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stream_state', full_name='rsctrl.stream.StreamData.stream_state', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='send_time', full_name='rsctrl.stream.StreamData.send_time', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='rsctrl.stream.StreamData.offset', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='rsctrl.stream.StreamData.size', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stream_data', full_name='rsctrl.stream.StreamData.stream_data', index=5,
      number=6, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=428,
  serialized_end=603,
)


_REQUESTSTARTFILESTREAM = descriptor.Descriptor(
  name='RequestStartFileStream',
  full_name='rsctrl.stream.RequestStartFileStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='file', full_name='rsctrl.stream.RequestStartFileStream.file', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rate_kbs', full_name='rsctrl.stream.RequestStartFileStream.rate_kbs', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='start_byte', full_name='rsctrl.stream.RequestStartFileStream.start_byte', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='end_byte', full_name='rsctrl.stream.RequestStartFileStream.end_byte', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=605,
  serialized_end=718,
)


_RESPONSESTREAMDETAIL = descriptor.Descriptor(
  name='ResponseStreamDetail',
  full_name='rsctrl.stream.ResponseStreamDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='rsctrl.stream.ResponseStreamDetail.status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='streams', full_name='rsctrl.stream.ResponseStreamDetail.streams', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=720,
  serialized_end=823,
)


_REQUESTCONTROLSTREAM = descriptor.Descriptor(
  name='RequestControlStream',
  full_name='rsctrl.stream.RequestControlStream',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stream_id', full_name='rsctrl.stream.RequestControlStream.stream_id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='action', full_name='rsctrl.stream.RequestControlStream.action', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='rate_kbs', full_name='rsctrl.stream.RequestControlStream.rate_kbs', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='seek_byte', full_name='rsctrl.stream.RequestControlStream.seek_byte', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REQUESTCONTROLSTREAM_STREAMACTION,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=826,
  serialized_end=1080,
)


_REQUESTLISTSTREAMS = descriptor.Descriptor(
  name='RequestListStreams',
  full_name='rsctrl.stream.RequestListStreams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='request_type', full_name='rsctrl.stream.RequestListStreams.request_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1082,
  serialized_end=1151,
)


_RESPONSESTREAMDATA = descriptor.Descriptor(
  name='ResponseStreamData',
  full_name='rsctrl.stream.ResponseStreamData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='status', full_name='rsctrl.stream.ResponseStreamData.status', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='data', full_name='rsctrl.stream.ResponseStreamData.data', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=1153,
  serialized_end=1251,
)

_STREAMFILEDETAIL.fields_by_name['file'].message_type = core_pb2._FILE
_STREAMDESC.fields_by_name['stream_type'].enum_type = _STREAMTYPE
_STREAMDESC.fields_by_name['stream_state'].enum_type = _STREAMSTATE
_STREAMDESC.fields_by_name['file'].message_type = _STREAMFILEDETAIL
_STREAMDESC.fields_by_name['voip'].message_type = _STREAMVOIPDETAIL
_STREAMDATA.fields_by_name['stream_state'].enum_type = _STREAMSTATE
_STREAMDATA.fields_by_name['send_time'].message_type = core_pb2._TIMESTAMP
_REQUESTSTARTFILESTREAM.fields_by_name['file'].message_type = core_pb2._FILE
_RESPONSESTREAMDETAIL.fields_by_name['status'].message_type = core_pb2._STATUS
_RESPONSESTREAMDETAIL.fields_by_name['streams'].message_type = _STREAMDESC
_REQUESTCONTROLSTREAM.fields_by_name['action'].enum_type = _REQUESTCONTROLSTREAM_STREAMACTION
_REQUESTCONTROLSTREAM_STREAMACTION.containing_type = _REQUESTCONTROLSTREAM;
_REQUESTLISTSTREAMS.fields_by_name['request_type'].enum_type = _STREAMTYPE
_RESPONSESTREAMDATA.fields_by_name['status'].message_type = core_pb2._STATUS
_RESPONSESTREAMDATA.fields_by_name['data'].message_type = _STREAMDATA
DESCRIPTOR.message_types_by_name['StreamFileDetail'] = _STREAMFILEDETAIL
DESCRIPTOR.message_types_by_name['StreamVoipDetail'] = _STREAMVOIPDETAIL
DESCRIPTOR.message_types_by_name['StreamDesc'] = _STREAMDESC
DESCRIPTOR.message_types_by_name['StreamData'] = _STREAMDATA
DESCRIPTOR.message_types_by_name['RequestStartFileStream'] = _REQUESTSTARTFILESTREAM
DESCRIPTOR.message_types_by_name['ResponseStreamDetail'] = _RESPONSESTREAMDETAIL
DESCRIPTOR.message_types_by_name['RequestControlStream'] = _REQUESTCONTROLSTREAM
DESCRIPTOR.message_types_by_name['RequestListStreams'] = _REQUESTLISTSTREAMS
DESCRIPTOR.message_types_by_name['ResponseStreamData'] = _RESPONSESTREAMDATA

class StreamFileDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAMFILEDETAIL
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.StreamFileDetail)

class StreamVoipDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAMVOIPDETAIL
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.StreamVoipDetail)

class StreamDesc(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAMDESC
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.StreamDesc)

class StreamData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STREAMDATA
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.StreamData)

class RequestStartFileStream(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTSTARTFILESTREAM
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.RequestStartFileStream)

class ResponseStreamDetail(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSESTREAMDETAIL
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.ResponseStreamDetail)

class RequestControlStream(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTCONTROLSTREAM
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.RequestControlStream)

class RequestListStreams(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REQUESTLISTSTREAMS
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.RequestListStreams)

class ResponseStreamData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSESTREAMDATA
  
  # @@protoc_insertion_point(class_scope:rsctrl.stream.ResponseStreamData)

# @@protoc_insertion_point(module_scope)