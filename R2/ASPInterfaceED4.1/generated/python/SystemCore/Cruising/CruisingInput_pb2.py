# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SystemCore/Cruising/CruisingInput.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='SystemCore/Cruising/CruisingInput.proto',
  package='SystemCore.Cruising',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\'SystemCore/Cruising/CruisingInput.proto\x12\x13SystemCore.Cruising\x1a#Tools/Extension/SystemOptions.proto\"\xad\x05\n\x12TrafficAssistInput\x12|\n\x06\x65nable\x18\x01 \x01(\x08\x42l\x92\xb5\x18h*fPlatform ok to enable Traffic Assist.All criteria are met for Traffic Assistto go from Off to Standby.\x12M\n\x10steering_enabled\x18\x02 \x01(\x08\x42\x33\x92\xb5\x18/*-Request steering support from Traffic Assist.\x12\xc2\x02\n\x1b\x64river_in_the_loop_detected\x18\x03 \x01(\x08\x42\x9c\x02\x92\xb5\x18\x97\x02*\x94\x02\x44river confirmed to be in control of vehicle during Traffic Assist steering support. Detection might be done by DMC, steering wheel sensor or any other suitable method. driver_in_the_loop_detected has to be true often enough to not cause Hands Off warnings or maneuver aborts.\x12L\n\x1atraffic_assist_is_steering\x18\x04 \x01(\x08\x42(\x92\xb5\x18$*\"TA steering confirmed by platform.:7\x8a\xb5\x18\x1a\"\x18Inputs to Traffic Assist\x8a\xb5\x18\x02(\x03\x8a\xb5\x18\x03\x08\x89\x06\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\"\xfa\x03\n\x15LaneChangeAssistInput\x12\x84\x01\n\x06\x65nable\x18\x01 \x01(\x08\x42t\x92\xb5\x18p*nPlatform ok to enable Lane Change Assist.All criteria are met for Lane Change Assistto go from Off to Standby.\x12L\n\x1dlane_change_request_by_driver\x18\x02 \x01(\x0e\x32%.SystemCore.Cruising.LateralDirection\x12\x61\n#lane_change_abort_request_by_driver\x18\x03 \x01(\x08\x42\x34\x92\xb5\x18\x30*.Lane change aborted by driver specified in R79\x12l\n\x1arear_radar_detection_range\x18\x04 \x01(\rBH\x92\xb5\x18\x02\x08\x08\x92\xb5\x18\x03\"\x01m\x92\xb5\x18\x37*5The current radial detection range of the rear radars:;\x8a\xb5\x18\x1e\"\x1cInputs to Lane Change Assist\x8a\xb5\x18\x02(\x03\x8a\xb5\x18\x03\x08\x8a\x06\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\"\xdc\x01\n\x1aRiskMitigationSupportInput\x12|\n\nrms_status\x18\x01 \x01(\x0e\x32\x1e.SystemCore.Cruising.RmsStatusBH\x92\xb5\x18\x44*BInformation if RMS is off, standby or requested intervention level:@\x8a\xb5\x18#\"!Inputs to Risk Mitigation Support\x8a\xb5\x18\x02(\x03\x8a\xb5\x18\x03\x08\x8b\x06\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\"\xb1\x01\n\x17\x44riverAlertControlInput\x12W\n\rdac_activated\x18\x01 \x01(\x08\x42@\x92\xb5\x18<*:Indicates that Driver Alert Control is activated from HMI.:=\x8a\xb5\x18 \"\x1eInputs to Driver Alert Control\x8a\xb5\x18\x02(\x03\x8a\xb5\x18\x03\x08\x8c\x06\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00*g\n\x10LateralDirection\x12\x1a\n\x16LATERAL_DIRECTION_NONE\x10\x00\x12\x1a\n\x16LATERAL_DIRECTION_LEFT\x10\x01\x12\x1b\n\x17LATERAL_DIRECTION_RIGHT\x10\x02*\xf7\x01\n\tRmsStatus\x12\x12\n\x0eRMS_STATUS_OFF\x10\x00\x12\x16\n\x12RMS_STATUS_STANDBY\x10\x01\x12\x16\n\x12RMS_STATUS_LEVEL_1\x10\x02\x12\x16\n\x12RMS_STATUS_LEVEL_2\x10\x03\x12\x16\n\x12RMS_STATUS_LEVEL_3\x10\x04\x12\x16\n\x12RMS_STATUS_LEVEL_4\x10\x05\x12\x16\n\x12RMS_STATUS_LEVEL_5\x10\x06\x12\x16\n\x12RMS_STATUS_LEVEL_6\x10\x07\x12\x16\n\x12RMS_STATUS_LEVEL_7\x10\x08\x12\x16\n\x12RMS_STATUS_LEVEL_8\x10\tb\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])

_LATERALDIRECTION = _descriptor.EnumDescriptor(
  name='LateralDirection',
  full_name='SystemCore.Cruising.LateralDirection',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LATERAL_DIRECTION_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LATERAL_DIRECTION_LEFT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LATERAL_DIRECTION_RIGHT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1701,
  serialized_end=1804,
)
_sym_db.RegisterEnumDescriptor(_LATERALDIRECTION)

LateralDirection = enum_type_wrapper.EnumTypeWrapper(_LATERALDIRECTION)
_RMSSTATUS = _descriptor.EnumDescriptor(
  name='RmsStatus',
  full_name='SystemCore.Cruising.RmsStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_OFF', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_STANDBY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_1', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_2', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_3', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_4', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_5', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_6', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_7', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RMS_STATUS_LEVEL_8', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1807,
  serialized_end=2054,
)
_sym_db.RegisterEnumDescriptor(_RMSSTATUS)

RmsStatus = enum_type_wrapper.EnumTypeWrapper(_RMSSTATUS)
LATERAL_DIRECTION_NONE = 0
LATERAL_DIRECTION_LEFT = 1
LATERAL_DIRECTION_RIGHT = 2
RMS_STATUS_OFF = 0
RMS_STATUS_STANDBY = 1
RMS_STATUS_LEVEL_1 = 2
RMS_STATUS_LEVEL_2 = 3
RMS_STATUS_LEVEL_3 = 4
RMS_STATUS_LEVEL_4 = 5
RMS_STATUS_LEVEL_5 = 6
RMS_STATUS_LEVEL_6 = 7
RMS_STATUS_LEVEL_7 = 8
RMS_STATUS_LEVEL_8 = 9



_TRAFFICASSISTINPUT = _descriptor.Descriptor(
  name='TrafficAssistInput',
  full_name='SystemCore.Cruising.TrafficAssistInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='SystemCore.Cruising.TrafficAssistInput.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030h*fPlatform ok to enable Traffic Assist.All criteria are met for Traffic Assistto go from Off to Standby.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='steering_enabled', full_name='SystemCore.Cruising.TrafficAssistInput.steering_enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030/*-Request steering support from Traffic Assist.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='driver_in_the_loop_detected', full_name='SystemCore.Cruising.TrafficAssistInput.driver_in_the_loop_detected', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\227\002*\224\002Driver confirmed to be in control of vehicle during Traffic Assist steering support. Detection might be done by DMC, steering wheel sensor or any other suitable method. driver_in_the_loop_detected has to be true often enough to not cause Hands Off warnings or maneuver aborts.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='traffic_assist_is_steering', full_name='SystemCore.Cruising.TrafficAssistInput.traffic_assist_is_steering', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030$*\"TA steering confirmed by platform.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\032\"\030Inputs to Traffic Assist\212\265\030\002(\003\212\265\030\003\010\211\006\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=787,
)


_LANECHANGEASSISTINPUT = _descriptor.Descriptor(
  name='LaneChangeAssistInput',
  full_name='SystemCore.Cruising.LaneChangeAssistInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='enable', full_name='SystemCore.Cruising.LaneChangeAssistInput.enable', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030p*nPlatform ok to enable Lane Change Assist.All criteria are met for Lane Change Assistto go from Off to Standby.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_change_request_by_driver', full_name='SystemCore.Cruising.LaneChangeAssistInput.lane_change_request_by_driver', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_change_abort_request_by_driver', full_name='SystemCore.Cruising.LaneChangeAssistInput.lane_change_abort_request_by_driver', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\0300*.Lane change aborted by driver specified in R79', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rear_radar_detection_range', full_name='SystemCore.Cruising.LaneChangeAssistInput.rear_radar_detection_range', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\010\222\265\030\003\"\001m\222\265\0307*5The current radial detection range of the rear radars', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\036\"\034Inputs to Lane Change Assist\212\265\030\002(\003\212\265\030\003\010\212\006\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=790,
  serialized_end=1296,
)


_RISKMITIGATIONSUPPORTINPUT = _descriptor.Descriptor(
  name='RiskMitigationSupportInput',
  full_name='SystemCore.Cruising.RiskMitigationSupportInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rms_status', full_name='SystemCore.Cruising.RiskMitigationSupportInput.rms_status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030D*BInformation if RMS is off, standby or requested intervention level', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030#\"!Inputs to Risk Mitigation Support\212\265\030\002(\003\212\265\030\003\010\213\006\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1299,
  serialized_end=1519,
)


_DRIVERALERTCONTROLINPUT = _descriptor.Descriptor(
  name='DriverAlertControlInput',
  full_name='SystemCore.Cruising.DriverAlertControlInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dac_activated', full_name='SystemCore.Cruising.DriverAlertControlInput.dac_activated', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030<*:Indicates that Driver Alert Control is activated from HMI.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030 \"\036Inputs to Driver Alert Control\212\265\030\002(\003\212\265\030\003\010\214\006\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1522,
  serialized_end=1699,
)

_LANECHANGEASSISTINPUT.fields_by_name['lane_change_request_by_driver'].enum_type = _LATERALDIRECTION
_RISKMITIGATIONSUPPORTINPUT.fields_by_name['rms_status'].enum_type = _RMSSTATUS
DESCRIPTOR.message_types_by_name['TrafficAssistInput'] = _TRAFFICASSISTINPUT
DESCRIPTOR.message_types_by_name['LaneChangeAssistInput'] = _LANECHANGEASSISTINPUT
DESCRIPTOR.message_types_by_name['RiskMitigationSupportInput'] = _RISKMITIGATIONSUPPORTINPUT
DESCRIPTOR.message_types_by_name['DriverAlertControlInput'] = _DRIVERALERTCONTROLINPUT
DESCRIPTOR.enum_types_by_name['LateralDirection'] = _LATERALDIRECTION
DESCRIPTOR.enum_types_by_name['RmsStatus'] = _RMSSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrafficAssistInput = _reflection.GeneratedProtocolMessageType('TrafficAssistInput', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICASSISTINPUT,
  '__module__' : 'SystemCore.Cruising.CruisingInput_pb2'
  # @@protoc_insertion_point(class_scope:SystemCore.Cruising.TrafficAssistInput)
  })
_sym_db.RegisterMessage(TrafficAssistInput)

LaneChangeAssistInput = _reflection.GeneratedProtocolMessageType('LaneChangeAssistInput', (_message.Message,), {
  'DESCRIPTOR' : _LANECHANGEASSISTINPUT,
  '__module__' : 'SystemCore.Cruising.CruisingInput_pb2'
  # @@protoc_insertion_point(class_scope:SystemCore.Cruising.LaneChangeAssistInput)
  })
_sym_db.RegisterMessage(LaneChangeAssistInput)

RiskMitigationSupportInput = _reflection.GeneratedProtocolMessageType('RiskMitigationSupportInput', (_message.Message,), {
  'DESCRIPTOR' : _RISKMITIGATIONSUPPORTINPUT,
  '__module__' : 'SystemCore.Cruising.CruisingInput_pb2'
  # @@protoc_insertion_point(class_scope:SystemCore.Cruising.RiskMitigationSupportInput)
  })
_sym_db.RegisterMessage(RiskMitigationSupportInput)

DriverAlertControlInput = _reflection.GeneratedProtocolMessageType('DriverAlertControlInput', (_message.Message,), {
  'DESCRIPTOR' : _DRIVERALERTCONTROLINPUT,
  '__module__' : 'SystemCore.Cruising.CruisingInput_pb2'
  # @@protoc_insertion_point(class_scope:SystemCore.Cruising.DriverAlertControlInput)
  })
_sym_db.RegisterMessage(DriverAlertControlInput)


_TRAFFICASSISTINPUT.fields_by_name['enable']._options = None
_TRAFFICASSISTINPUT.fields_by_name['steering_enabled']._options = None
_TRAFFICASSISTINPUT.fields_by_name['driver_in_the_loop_detected']._options = None
_TRAFFICASSISTINPUT.fields_by_name['traffic_assist_is_steering']._options = None
_TRAFFICASSISTINPUT._options = None
_LANECHANGEASSISTINPUT.fields_by_name['enable']._options = None
_LANECHANGEASSISTINPUT.fields_by_name['lane_change_abort_request_by_driver']._options = None
_LANECHANGEASSISTINPUT.fields_by_name['rear_radar_detection_range']._options = None
_LANECHANGEASSISTINPUT._options = None
_RISKMITIGATIONSUPPORTINPUT.fields_by_name['rms_status']._options = None
_RISKMITIGATIONSUPPORTINPUT._options = None
_DRIVERALERTCONTROLINPUT.fields_by_name['dac_activated']._options = None
_DRIVERALERTCONTROLINPUT._options = None
# @@protoc_insertion_point(module_scope)
