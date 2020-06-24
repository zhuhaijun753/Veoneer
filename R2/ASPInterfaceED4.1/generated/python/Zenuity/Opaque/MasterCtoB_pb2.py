# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Zenuity/Opaque/MasterCtoB.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Zenuity/Opaque/MasterCtoB.proto',
  package='Zenuity.Opaque',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fZenuity/Opaque/MasterCtoB.proto\x12\x0eZenuity.Opaque\x1a#Tools/Extension/SystemOptions.proto\"\x8f\x02\n\nMasterCtoB\x12\x14\n\x04\x64\x61ta\x18\x02 \x01(\x0c\x42\x06\x92\xb5\x18\x02\x10\x1e:\xea\x01\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\xcd\x01\"\xca\x01Opaque data for transfering Zenuity internal data between Zenuity containers. Size is specified with a margin to the actual current need to be less sensitive here to changes to the Zenuity internal data\x8a\xb5\x18\x02\x08\x34\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\x62\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])




_MASTERCTOB = _descriptor.Descriptor(
  name='MasterCtoB',
  full_name='Zenuity.Opaque.MasterCtoB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Zenuity.Opaque.MasterCtoB.data', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\020\036', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\001\212\265\030\315\001\"\312\001Opaque data for transfering Zenuity internal data between Zenuity containers. Size is specified with a margin to the actual current need to be less sensitive here to changes to the Zenuity internal data\212\265\030\002\0104\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=89,
  serialized_end=360,
)

DESCRIPTOR.message_types_by_name['MasterCtoB'] = _MASTERCTOB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MasterCtoB = _reflection.GeneratedProtocolMessageType('MasterCtoB', (_message.Message,), {
  'DESCRIPTOR' : _MASTERCTOB,
  '__module__' : 'Zenuity.Opaque.MasterCtoB_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.Opaque.MasterCtoB)
  })
_sym_db.RegisterMessage(MasterCtoB)


_MASTERCTOB.fields_by_name['data']._options = None
_MASTERCTOB._options = None
# @@protoc_insertion_point(module_scope)
