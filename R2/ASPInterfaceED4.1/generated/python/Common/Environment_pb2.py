# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Common/Environment.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Common/Environment.proto',
  package='Common',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18\x43ommon/Environment.proto\x12\x06\x43ommon\x1a#Tools/Extension/SystemOptions.proto*\xa3\x01\n\x0cTrafficStyle\x12\x19\n\x15TRAFFIC_STYLE_UNKNOWN\x10\x00\x12$\n TRAFFIC_STYLE_RIGHT_HAND_TRAFFIC\x10\x01\x12#\n\x1fTRAFFIC_STYLE_LEFT_HAND_TRAFFIC\x10\x02\x1a-\x9a\xb5\x18)\n\'Describes the traffic style / directionb\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])

_TRAFFICSTYLE = _descriptor.EnumDescriptor(
  name='TrafficStyle',
  full_name='Common.TrafficStyle',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRAFFIC_STYLE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRAFFIC_STYLE_RIGHT_HAND_TRAFFIC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRAFFIC_STYLE_LEFT_HAND_TRAFFIC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=b'\232\265\030)\n\'Describes the traffic style / direction',
  serialized_start=74,
  serialized_end=237,
)
_sym_db.RegisterEnumDescriptor(_TRAFFICSTYLE)

TrafficStyle = enum_type_wrapper.EnumTypeWrapper(_TRAFFICSTYLE)
TRAFFIC_STYLE_UNKNOWN = 0
TRAFFIC_STYLE_RIGHT_HAND_TRAFFIC = 1
TRAFFIC_STYLE_LEFT_HAND_TRAFFIC = 2


DESCRIPTOR.enum_types_by_name['TrafficStyle'] = _TRAFFICSTYLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


_TRAFFICSTYLE._options = None
# @@protoc_insertion_point(module_scope)
