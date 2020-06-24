# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VisionCore/Road/SceneClassification.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='VisionCore/Road/SceneClassification.proto',
  package='VisionCore.Road',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n)VisionCore/Road/SceneClassification.proto\x12\x0fVisionCore.Road\x1a#Tools/Extension/SystemOptions.proto\"\xcc\x01\n\x18RoadClassificationResult\x12K\n\x0bis_detected\x18\x01 \x01(\x08\x42\x36\x92\xb5\x18\x32*0Describes if the scene includes the class or not\x12\x63\n\nconfidence\x18\x02 \x01(\rBO\x92\xb5\x18\x02\x08\x08\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00Y@\x92\xb5\x18\x03\"\x01%\x92\xb5\x18\x31*/Classification confidence for the current frame\"\xf3\x01\n\tRoadCover\x12P\n\x04snow\x18\x01 \x01(\x0b\x32).VisionCore.Road.RoadClassificationResultB\x17\x92\xb5\x18\x13*\x11Snow covered road\x12L\n\x06gravel\x18\x02 \x01(\x0b\x32).VisionCore.Road.RoadClassificationResultB\x11\x92\xb5\x18\r*\x0bGravel road\x12\x46\n\x03wet\x18\x03 \x01(\x0b\x32).VisionCore.Road.RoadClassificationResultB\x0e\x92\xb5\x18\n*\x08Wet road\"\xf6\x02\n\x13SceneClassification\x12V\n\nroad_cover\x18\x01 \x01(\x0b\x32\x1a.VisionCore.Road.RoadCoverB&\x92\xb5\x18\"* Road cover classification result\x12]\n\x06tunnel\x18\x02 \x01(\x0b\x32).VisionCore.Road.RoadClassificationResultB\"\x92\xb5\x18\x1e*\x1cTunnel classification result\x12W\n\x03\x66og\x18\x03 \x01(\x0b\x32).VisionCore.Road.RoadClassificationResultB\x1f\x92\xb5\x18\x1b*\x19\x46og classification result:O\x8a\xb5\x18\x02(\x02\x8a\xb5\x18\x32\"0Output describing the scene ahead of the vehicle\x8a\xb5\x18\x03\x08\xfe\x03\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\x62\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])




_ROADCLASSIFICATIONRESULT = _descriptor.Descriptor(
  name='RoadClassificationResult',
  full_name='VisionCore.Road.RoadClassificationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_detected', full_name='VisionCore.Road.RoadClassificationResult.is_detected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\0302*0Describes if the scene includes the class or not', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='VisionCore.Road.RoadClassificationResult.confidence', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\010\222\265\030\tQ\000\000\000\000\000\000Y@\222\265\030\003\"\001%\222\265\0301*/Classification confidence for the current frame', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=304,
)


_ROADCOVER = _descriptor.Descriptor(
  name='RoadCover',
  full_name='VisionCore.Road.RoadCover',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='snow', full_name='VisionCore.Road.RoadCover.snow', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\023*\021Snow covered road', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gravel', full_name='VisionCore.Road.RoadCover.gravel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\r*\013Gravel road', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wet', full_name='VisionCore.Road.RoadCover.wet', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\n*\010Wet road', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=307,
  serialized_end=550,
)


_SCENECLASSIFICATION = _descriptor.Descriptor(
  name='SceneClassification',
  full_name='VisionCore.Road.SceneClassification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='road_cover', full_name='VisionCore.Road.SceneClassification.road_cover', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\"* Road cover classification result', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tunnel', full_name='VisionCore.Road.SceneClassification.tunnel', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\036*\034Tunnel classification result', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fog', full_name='VisionCore.Road.SceneClassification.fog', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\033*\031Fog classification result', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\002\212\265\0302\"0Output describing the scene ahead of the vehicle\212\265\030\003\010\376\003\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=553,
  serialized_end=927,
)

_ROADCOVER.fields_by_name['snow'].message_type = _ROADCLASSIFICATIONRESULT
_ROADCOVER.fields_by_name['gravel'].message_type = _ROADCLASSIFICATIONRESULT
_ROADCOVER.fields_by_name['wet'].message_type = _ROADCLASSIFICATIONRESULT
_SCENECLASSIFICATION.fields_by_name['road_cover'].message_type = _ROADCOVER
_SCENECLASSIFICATION.fields_by_name['tunnel'].message_type = _ROADCLASSIFICATIONRESULT
_SCENECLASSIFICATION.fields_by_name['fog'].message_type = _ROADCLASSIFICATIONRESULT
DESCRIPTOR.message_types_by_name['RoadClassificationResult'] = _ROADCLASSIFICATIONRESULT
DESCRIPTOR.message_types_by_name['RoadCover'] = _ROADCOVER
DESCRIPTOR.message_types_by_name['SceneClassification'] = _SCENECLASSIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoadClassificationResult = _reflection.GeneratedProtocolMessageType('RoadClassificationResult', (_message.Message,), {
  'DESCRIPTOR' : _ROADCLASSIFICATIONRESULT,
  '__module__' : 'VisionCore.Road.SceneClassification_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Road.RoadClassificationResult)
  })
_sym_db.RegisterMessage(RoadClassificationResult)

RoadCover = _reflection.GeneratedProtocolMessageType('RoadCover', (_message.Message,), {
  'DESCRIPTOR' : _ROADCOVER,
  '__module__' : 'VisionCore.Road.SceneClassification_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Road.RoadCover)
  })
_sym_db.RegisterMessage(RoadCover)

SceneClassification = _reflection.GeneratedProtocolMessageType('SceneClassification', (_message.Message,), {
  'DESCRIPTOR' : _SCENECLASSIFICATION,
  '__module__' : 'VisionCore.Road.SceneClassification_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Road.SceneClassification)
  })
_sym_db.RegisterMessage(SceneClassification)


_ROADCLASSIFICATIONRESULT.fields_by_name['is_detected']._options = None
_ROADCLASSIFICATIONRESULT.fields_by_name['confidence']._options = None
_ROADCOVER.fields_by_name['snow']._options = None
_ROADCOVER.fields_by_name['gravel']._options = None
_ROADCOVER.fields_by_name['wet']._options = None
_SCENECLASSIFICATION.fields_by_name['road_cover']._options = None
_SCENECLASSIFICATION.fields_by_name['tunnel']._options = None
_SCENECLASSIFICATION.fields_by_name['fog']._options = None
_SCENECLASSIFICATION._options = None
# @@protoc_insertion_point(module_scope)