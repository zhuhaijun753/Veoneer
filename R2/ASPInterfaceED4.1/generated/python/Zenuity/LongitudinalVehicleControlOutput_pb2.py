# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Zenuity/LongitudinalVehicleControlOutput.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Zenuity/LongitudinalVehicleControlOutput.proto',
  package='Zenuity.LongitudinalVehicleControl',
  syntax='proto3',
  serialized_options=b'\202\265\030]\n[This file contains platfrom dependent output signalsof longitudinal vehicle control module.',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n.Zenuity/LongitudinalVehicleControlOutput.proto\x12\"Zenuity.LongitudinalVehicleControl\x1a#Tools/Extension/SystemOptions.proto\"\x91\x0b\n\x11StopAndGoRequests\x12k\n$driver_away_release_request_to_brake\x18\x01 \x01(\x08\x42=\x92\xb5\x18\x39*7Request for drive away, if true drive away is requested\x12^\n\x15hold_request_to_brake\x18\x02 \x01(\x08\x42?\x92\xb5\x18;*9Request to stand still, if true, stand still is requested\x12\x64\n!park_request_from_veh_mtn_control\x18\x03 \x01(\x08\x42\x39\x92\xb5\x18\x35*3Request to park vehicle, if true, request is active\x12r\n\x1a\x62rake_acceleration_request\x18\x04 \x01(\x11\x42N\x92\xb5\x18\x1f*\x1d\x41\x63\x63\x65leration request to brake\x92\xb5\x18\x07\"\x05m/s\xc2\xb2\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\tI{\x14\xaeG\xe1z\x14\xc0\x92\xb5\x18\tQq=\n\xd7\xa3p\x14@\x12\xd4\x01\n\"latest_active_acceleration_request\x18\x05 \x01(\x11\x42\xa7\x01\x92\xb5\x18x*vInforms which the intended acceleration of the actuators is at the moment, includes rate limitation, internal feedback\x92\xb5\x18\x07\"\x05m/s\xc2\xb2\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\tI{\x14\xaeG\xe1z\x14\xc0\x92\xb5\x18\tQq=\n\xd7\xa3p\x14@\x12\xe5\x01\n!actutor_active_for_lgt_controller\x18\x06 \x01(\x0e\x32\x42.Zenuity.LongitudinalVehicleControl.ActuatorActiveForLgtControllerBv\x92\xb5\x18r*pInforms which actuator that\xe2\x80\x99s primarily active for speed control, none, powertrain or brake, internal feedback\x12m\n#propulsion_torque_negative_gradient\x18\x07 \x01(\x11\x42@\x92\xb5\x18\x30*.None rate limited torque request to Powertrain\x92\xb5\x18\x08\"\x06Nm/s\xc2\xb2\x12h\n$propulstion_torque_positive_gradient\x18\x08 \x01(\x11\x42:\x92\xb5\x18**(Negative rate limit to powertrain torque\x92\xb5\x18\x08\"\x06Nm/s\xc2\xb2\x12Y\n\x19propulsion_torque_request\x18\t \x01(\x11\x42\x36\x92\xb5\x18**(Positive rate limit to powertrain torque\x92\xb5\x18\x04\"\x02Nm\x12\x99\x01\n\x11lcp_health_status\x18\n \x01(\x08\x42~\x92\xb5\x18z*xFaultManagement event output from LCP for the HealthStatus reporting.  True if LCP Health Status is OK, otherwise false.:F\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02\x08!\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\x8a\xb5\x18*\"(Requests signals for stop and go vehicle*\x84\x02\n\x1e\x41\x63tuatorActiveForLgtController\x12G\nCACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_ACTUATOR_NOT_ENABLED_FOR_CONTROL\x10\x00\x12N\nJACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_PROPULSION_ACTUATOR_ENABLED_FOR_CONTROL\x10\x01\x12I\nEACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_BRAKE_ACTUATOR_ENABLED_FOR_CONTROL\x10\x02\x42\x61\x82\xb5\x18]\n[This file contains platfrom dependent output signalsof longitudinal vehicle control module.b\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])

_ACTUATORACTIVEFORLGTCONTROLLER = _descriptor.EnumDescriptor(
  name='ActuatorActiveForLgtController',
  full_name='Zenuity.LongitudinalVehicleControl.ActuatorActiveForLgtController',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_ACTUATOR_NOT_ENABLED_FOR_CONTROL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_PROPULSION_ACTUATOR_ENABLED_FOR_CONTROL', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_BRAKE_ACTUATOR_ENABLED_FOR_CONTROL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1552,
  serialized_end=1812,
)
_sym_db.RegisterEnumDescriptor(_ACTUATORACTIVEFORLGTCONTROLLER)

ActuatorActiveForLgtController = enum_type_wrapper.EnumTypeWrapper(_ACTUATORACTIVEFORLGTCONTROLLER)
ACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_ACTUATOR_NOT_ENABLED_FOR_CONTROL = 0
ACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_PROPULSION_ACTUATOR_ENABLED_FOR_CONTROL = 1
ACTUATOR_ACTIVE_FOR_LGT_CONTROLLER_BRAKE_ACTUATOR_ENABLED_FOR_CONTROL = 2



_STOPANDGOREQUESTS = _descriptor.Descriptor(
  name='StopAndGoRequests',
  full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='driver_away_release_request_to_brake', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.driver_away_release_request_to_brake', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\0309*7Request for drive away, if true drive away is requested', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hold_request_to_brake', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.hold_request_to_brake', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030;*9Request to stand still, if true, stand still is requested', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='park_request_from_veh_mtn_control', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.park_request_from_veh_mtn_control', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\0305*3Request to park vehicle, if true, request is active', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='brake_acceleration_request', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.brake_acceleration_request', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\037*\035Acceleration request to brake\222\265\030\007\"\005m/s\302\262\222\265\030\002\010\020\222\265\030\tI{\024\256G\341z\024\300\222\265\030\tQq=\n\327\243p\024@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latest_active_acceleration_request', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.latest_active_acceleration_request', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030x*vInforms which the intended acceleration of the actuators is at the moment, includes rate limitation, internal feedback\222\265\030\007\"\005m/s\302\262\222\265\030\002\010\020\222\265\030\tI{\024\256G\341z\024\300\222\265\030\tQq=\n\327\243p\024@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actutor_active_for_lgt_controller', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.actutor_active_for_lgt_controller', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030r*pInforms which actuator that\342\200\231s primarily active for speed control, none, powertrain or brake, internal feedback', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propulsion_torque_negative_gradient', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.propulsion_torque_negative_gradient', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\0300*.None rate limited torque request to Powertrain\222\265\030\010\"\006Nm/s\302\262', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propulstion_torque_positive_gradient', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.propulstion_torque_positive_gradient', index=7,
      number=8, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030**(Negative rate limit to powertrain torque\222\265\030\010\"\006Nm/s\302\262', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='propulsion_torque_request', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.propulsion_torque_request', index=8,
      number=9, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030**(Positive rate limit to powertrain torque\222\265\030\004\"\002Nm', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lcp_health_status', full_name='Zenuity.LongitudinalVehicleControl.StopAndGoRequests.lcp_health_status', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030z*xFaultManagement event output from LCP for the HealthStatus reporting.  True if LCP Health Status is OK, otherwise false.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\001\212\265\030\002\010!\212\265\030\002\020\001\212\265\030\002\030\000\212\265\030*\"(Requests signals for stop and go vehicle',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=124,
  serialized_end=1549,
)

_STOPANDGOREQUESTS.fields_by_name['actutor_active_for_lgt_controller'].enum_type = _ACTUATORACTIVEFORLGTCONTROLLER
DESCRIPTOR.message_types_by_name['StopAndGoRequests'] = _STOPANDGOREQUESTS
DESCRIPTOR.enum_types_by_name['ActuatorActiveForLgtController'] = _ACTUATORACTIVEFORLGTCONTROLLER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StopAndGoRequests = _reflection.GeneratedProtocolMessageType('StopAndGoRequests', (_message.Message,), {
  'DESCRIPTOR' : _STOPANDGOREQUESTS,
  '__module__' : 'Zenuity.LongitudinalVehicleControlOutput_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.LongitudinalVehicleControl.StopAndGoRequests)
  })
_sym_db.RegisterMessage(StopAndGoRequests)


DESCRIPTOR._options = None
_STOPANDGOREQUESTS.fields_by_name['driver_away_release_request_to_brake']._options = None
_STOPANDGOREQUESTS.fields_by_name['hold_request_to_brake']._options = None
_STOPANDGOREQUESTS.fields_by_name['park_request_from_veh_mtn_control']._options = None
_STOPANDGOREQUESTS.fields_by_name['brake_acceleration_request']._options = None
_STOPANDGOREQUESTS.fields_by_name['latest_active_acceleration_request']._options = None
_STOPANDGOREQUESTS.fields_by_name['actutor_active_for_lgt_controller']._options = None
_STOPANDGOREQUESTS.fields_by_name['propulsion_torque_negative_gradient']._options = None
_STOPANDGOREQUESTS.fields_by_name['propulstion_torque_positive_gradient']._options = None
_STOPANDGOREQUESTS.fields_by_name['propulsion_torque_request']._options = None
_STOPANDGOREQUESTS.fields_by_name['lcp_health_status']._options = None
_STOPANDGOREQUESTS._options = None
# @@protoc_insertion_point(module_scope)
