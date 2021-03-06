# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VisionCore/Common/EgoMotion.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='VisionCore/Common/EgoMotion.proto',
  package='VisionCore.Common',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!VisionCore/Common/EgoMotion.proto\x12\x11VisionCore.Common\x1a#Tools/Extension/SystemOptions.proto\"\xcc\x0c\n\x0f\x45goMotionOutput\x12\x91\x01\n\x15longitudinal_velocity\x18\x01 \x01(\x11\x42r\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x05\"\x03m/s\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00>\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00^@\x92\xb5\x18;*9Longitudinal velocity i.e. speed along the X-axis in AFAC\x12\xa6\x01\n\x19longitudinal_acceleration\x18\x02 \x01(\x11\x42\x82\x01\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x07\"\x05m/s\xc2\xb2\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x34\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00\x34@\x92\xb5\x18I*GLongitudinal acceleration i.e. velocity change along the X-axis in AFAC\x12\x87\x01\n\x10lateral_velocity\x18\x03 \x01(\x11\x42m\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x05\"\x03m/s\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00>\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00>@\x92\xb5\x18\x36*4Lateral velocity i.e. speed along the Y-axis in AFAC\x12\x9b\x01\n\x14lateral_acceleration\x18\x04 \x01(\x11\x42}\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x07\"\x05m/s\xc2\xb2\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x34\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00\x34@\x92\xb5\x18\x44*BLateral acceleration i.e. velocity change along the Y-axis in AFAC\x12y\n\x08yaw_rate\x18\x05 \x01(\x11\x42g\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x08\x32\x06\x30.0001\x92\xb5\x18\x07\"\x05rad/s\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\xf8\xbf\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00\xf8?\x92\xb5\x18,**Rotational speed around the Z-axis in AFAC\x12_\n\x0cis_available\x18\x06 \x01(\x08\x42I\x92\xb5\x18\x45*CIs data contained in the message available or is it just dummy data\x12\x44\n\ttimestamp\x18\x07 \x01(\rB1\x92\xb5\x18\x03\"\x01?\x92\xb5\x18&*$The time-stamp for the current frame\x12\xd6\x01\n\x1clongitudinal_velocity_status\x18\x08 \x01(\x0e\x32,.VisionCore.Common.EgoMotionGateKeeperStatusB\x81\x01\x92\xb5\x18}*{Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for longitudinal speed\x12\xc6\x01\n\x13\x61\x63\x63\x65leration_status\x18\t \x01(\x0e\x32,.VisionCore.Common.EgoMotionGateKeeperStatusB{\x92\xb5\x18w*uIndication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for acceleration\x12\xbe\x01\n\x0fyaw_rate_status\x18\n \x01(\x0e\x32,.VisionCore.Common.EgoMotionGateKeeperStatusBw\x92\xb5\x18s*qIndication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for yaw rate:O\x8a\xb5\x18\x02(\x02\x8a\xb5\x18\x32\"0Motion estimation based on vehicle input signals\x8a\xb5\x18\x03\x08\xcc\x03\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00*\xb8\x01\n\x19\x45goMotionGateKeeperStatus\x12)\n%EGO_MOTION_GATE_KEEPER_STATUS_UNKNOWN\x10\x00\x12\x39\n5EGO_MOTION_GATE_KEEPER_STATUS_SUCCESSFUL_VERIFICATION\x10\x01\x12\x35\n1EGO_MOTION_GATE_KEEPER_STATUS_VERIFICATION_FAILED\x10\x02\x62\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])

_EGOMOTIONGATEKEEPERSTATUS = _descriptor.EnumDescriptor(
  name='EgoMotionGateKeeperStatus',
  full_name='VisionCore.Common.EgoMotionGateKeeperStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EGO_MOTION_GATE_KEEPER_STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EGO_MOTION_GATE_KEEPER_STATUS_SUCCESSFUL_VERIFICATION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EGO_MOTION_GATE_KEEPER_STATUS_VERIFICATION_FAILED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1709,
  serialized_end=1893,
)
_sym_db.RegisterEnumDescriptor(_EGOMOTIONGATEKEEPERSTATUS)

EgoMotionGateKeeperStatus = enum_type_wrapper.EnumTypeWrapper(_EGOMOTIONGATEKEEPERSTATUS)
EGO_MOTION_GATE_KEEPER_STATUS_UNKNOWN = 0
EGO_MOTION_GATE_KEEPER_STATUS_SUCCESSFUL_VERIFICATION = 1
EGO_MOTION_GATE_KEEPER_STATUS_VERIFICATION_FAILED = 2



_EGOMOTIONOUTPUT = _descriptor.Descriptor(
  name='EgoMotionOutput',
  full_name='VisionCore.Common.EgoMotionOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='longitudinal_velocity', full_name='VisionCore.Common.EgoMotionOutput.longitudinal_velocity', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0062\0040.01\222\265\030\005\"\003m/s\222\265\030\tI\000\000\000\000\000\000>\300\222\265\030\tQ\000\000\000\000\000\000^@\222\265\030;*9Longitudinal velocity i.e. speed along the X-axis in AFAC', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitudinal_acceleration', full_name='VisionCore.Common.EgoMotionOutput.longitudinal_acceleration', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0062\0040.01\222\265\030\007\"\005m/s\302\262\222\265\030\tI\000\000\000\000\000\0004\300\222\265\030\tQ\000\000\000\000\000\0004@\222\265\030I*GLongitudinal acceleration i.e. velocity change along the X-axis in AFAC', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lateral_velocity', full_name='VisionCore.Common.EgoMotionOutput.lateral_velocity', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0062\0040.01\222\265\030\005\"\003m/s\222\265\030\tI\000\000\000\000\000\000>\300\222\265\030\tQ\000\000\000\000\000\000>@\222\265\0306*4Lateral velocity i.e. speed along the Y-axis in AFAC', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lateral_acceleration', full_name='VisionCore.Common.EgoMotionOutput.lateral_acceleration', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0062\0040.01\222\265\030\007\"\005m/s\302\262\222\265\030\tI\000\000\000\000\000\0004\300\222\265\030\tQ\000\000\000\000\000\0004@\222\265\030D*BLateral acceleration i.e. velocity change along the Y-axis in AFAC', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw_rate', full_name='VisionCore.Common.EgoMotionOutput.yaw_rate', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0102\0060.0001\222\265\030\007\"\005rad/s\222\265\030\tI\000\000\000\000\000\000\370\277\222\265\030\tQ\000\000\000\000\000\000\370?\222\265\030,**Rotational speed around the Z-axis in AFAC', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_available', full_name='VisionCore.Common.EgoMotionOutput.is_available', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030E*CIs data contained in the message available or is it just dummy data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='VisionCore.Common.EgoMotionOutput.timestamp', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\003\"\001?\222\265\030&*$The time-stamp for the current frame', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitudinal_velocity_status', full_name='VisionCore.Common.EgoMotionOutput.longitudinal_velocity_status', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030}*{Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for longitudinal speed', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='acceleration_status', full_name='VisionCore.Common.EgoMotionOutput.acceleration_status', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030w*uIndication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for acceleration', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yaw_rate_status', full_name='VisionCore.Common.EgoMotionOutput.yaw_rate_status', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030s*qIndication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for yaw rate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\002\212\265\0302\"0Motion estimation based on vehicle input signals\212\265\030\003\010\314\003\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=1706,
)

_EGOMOTIONOUTPUT.fields_by_name['longitudinal_velocity_status'].enum_type = _EGOMOTIONGATEKEEPERSTATUS
_EGOMOTIONOUTPUT.fields_by_name['acceleration_status'].enum_type = _EGOMOTIONGATEKEEPERSTATUS
_EGOMOTIONOUTPUT.fields_by_name['yaw_rate_status'].enum_type = _EGOMOTIONGATEKEEPERSTATUS
DESCRIPTOR.message_types_by_name['EgoMotionOutput'] = _EGOMOTIONOUTPUT
DESCRIPTOR.enum_types_by_name['EgoMotionGateKeeperStatus'] = _EGOMOTIONGATEKEEPERSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EgoMotionOutput = _reflection.GeneratedProtocolMessageType('EgoMotionOutput', (_message.Message,), {
  'DESCRIPTOR' : _EGOMOTIONOUTPUT,
  '__module__' : 'VisionCore.Common.EgoMotion_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Common.EgoMotionOutput)
  })
_sym_db.RegisterMessage(EgoMotionOutput)


_EGOMOTIONOUTPUT.fields_by_name['longitudinal_velocity']._options = None
_EGOMOTIONOUTPUT.fields_by_name['longitudinal_acceleration']._options = None
_EGOMOTIONOUTPUT.fields_by_name['lateral_velocity']._options = None
_EGOMOTIONOUTPUT.fields_by_name['lateral_acceleration']._options = None
_EGOMOTIONOUTPUT.fields_by_name['yaw_rate']._options = None
_EGOMOTIONOUTPUT.fields_by_name['is_available']._options = None
_EGOMOTIONOUTPUT.fields_by_name['timestamp']._options = None
_EGOMOTIONOUTPUT.fields_by_name['longitudinal_velocity_status']._options = None
_EGOMOTIONOUTPUT.fields_by_name['acceleration_status']._options = None
_EGOMOTIONOUTPUT.fields_by_name['yaw_rate_status']._options = None
_EGOMOTIONOUTPUT._options = None
# @@protoc_insertion_point(module_scope)
