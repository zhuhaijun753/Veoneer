# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Zenuity/Cruising.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='Zenuity/Cruising.proto',
  package='Zenuity.Crusing',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16Zenuity/Cruising.proto\x12\x0fZenuity.Crusing\x1a#Tools/Extension/SystemOptions.proto\"\\\n\x0f\x43\x61ncelReasonAcc\x12\x17\n\x0fno_lead_vehicle\x18\x01 \x01(\x08\x12\x16\n\x0e\x65nd_brake_only\x18\x02 \x01(\x08:\x18\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02\x08\x1e\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\"\xec\x04\n\x13\x41\x63\x63\x65lerationRequest\x12\x16\n\x0erequest_active\x18\x01 \x01(\x08\x12u\n\x14nominal_acceleration\x18\x02 \x01(\x11\x42W\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x07\"\x05m/s\xc2\xb2\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x1e*\x1c\x43urrent acceleration request\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x14\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00\x14@\x12\xa4\x01\n\x08min_jerk\x18\x03 \x01(\x11\x42\x91\x01\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x07\"\x05m/s\xc2\xb3\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18X*VRequest from controller to use no less than this jerk to reach requested acceleration.\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x14\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00\x14@\x12\xa4\x01\n\x08max_jerk\x18\x04 \x01(\x11\x42\x91\x01\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x07\"\x05m/s\xc2\xb3\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18X*VRequest from controller to use no more than this jerk to reach requested acceleration.\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x14\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00\x14@\x12^\n\x12standstill_request\x18\x05 \x01(\x08\x42\x42\x92\xb5\x18>*<Request by ACC to stop vehicle and hold it still with brakes:\x18\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02\x08\x1f\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\"\xcf\x03\n\x0eSelectedTarget\x12\x13\n\x0bis_selected\x18\x01 \x01(\x08\x12\x1d\n\x15is_controlled_towards\x18\x02 \x01(\x08\x12\x8f\x01\n\x0clat_position\x18\x03 \x01(\x11\x42y\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x03\"\x01m\x92\xb5\x18\x05\x32\x03\x30.1\x92\xb5\x18\x45*CLateral distance to selected target, ego vehicle coordinate system.\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x34\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00\x34@\x12\x94\x01\n\x0clon_position\x18\x04 \x01(\x11\x42~\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x03\"\x01m\x92\xb5\x18\x05\x32\x03\x30.1\x92\xb5\x18J*HLongitudinal distance to selected target, ego vehicle coordinate system.\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x00\x00\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00i@\x12`\n\x05speed\x18\x05 \x01(\x11\x42Q\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x05\"\x03m/s\x92\xb5\x18\x05\x32\x03\x30.1\x92\xb5\x18\x1b*\x19Speed of selected target.\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x00\x00\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00N@\"\xdb\x02\n\x14TargetsSelectedByAcc\x12\x38\n\x0f\x63losest_in_lane\x18\x01 \x01(\x0b\x32\x1f.Zenuity.Crusing.SelectedTarget\x12?\n\x16second_closest_in_lane\x18\x02 \x01(\x0b\x32\x1f.Zenuity.Crusing.SelectedTarget\x12/\n\x06\x63ut_in\x18\x03 \x01(\x0b\x32\x1f.Zenuity.Crusing.SelectedTarget\x12=\n\x14\x63losest_in_left_lane\x18\x04 \x01(\x0b\x32\x1f.Zenuity.Crusing.SelectedTarget\x12>\n\x15\x63losest_in_right_lane\x18\x05 \x01(\x0b\x32\x1f.Zenuity.Crusing.SelectedTarget:\x18\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x02\x08 \x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\"\xb5\x01\n\x13TrafficAssistOutput\x12\x45\n\x16turn_indicator_request\x18\x01 \x01(\x0e\x32%.Zenuity.Crusing.TurnIndicatorRequest:W\x8a\xb5\x18\x02(\x01\x8a\xb5\x18:\"8Collection of output signals for Traffic Assist function\x8a\xb5\x18\x03\x08\x9a\x05\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00\"\xc8\x03\n$InformationToDriverFromTrafficAssist\x12;\n\x11hands_off_warning\x18\x01 \x01(\x0e\x32 .Zenuity.Crusing.HandsOffWarning\x12\x39\n\x10lane_change_type\x18\x02 \x01(\x0e\x32\x1f.Zenuity.Crusing.LaneChangeType\x12=\n\x12lane_change_reason\x18\x03 \x01(\x0e\x32!.Zenuity.Crusing.LaneChangeReason\x12T\n\x1elane_change_possible_direction\x18\x04 \x01(\x0e\x32,.Zenuity.Crusing.LaneChangePossibleDirection\x12=\n\x12lane_change_status\x18\x05 \x01(\x0e\x32!.Zenuity.Crusing.LaneChangeStatus:T\x8a\xb5\x18\x02(\x01\x8a\xb5\x18\x37\"5Collection of HMI signals for Traffic Assist function\x8a\xb5\x18\x03\x08\x9b\x05\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00*\xa3\x01\n\x14TurnIndicatorRequest\x12\x1f\n\x1bTURN_INDICATOR_REQUEST_NONE\x10\x00\x12\x1f\n\x1bTURN_INDICATOR_REQUEST_LEFT\x10\x01\x12 \n\x1cTURN_INDICATOR_REQUEST_RIGHT\x10\x02\x12\'\n#TURN_INDICATOR_REQUEST_HAZARD_LIGHT\x10\x03*g\n\x0eLaneChangeType\x12\x1e\n\x1aLANE_CHANGE_TYPE_NO_INTENT\x10\x00\x12\x19\n\x15LANE_CHANGE_TYPE_LEFT\x10\x01\x12\x1a\n\x16LANE_CHANGE_TYPE_RIGHT\x10\x02*\xc3\x04\n\x10LaneChangeReason\x12 \n\x1cLANE_CHANGE_REASON_NO_REASON\x10\x00\x12\'\n#LANE_CHANGE_REASON_DENIED_BY_DRIVER\x10\x01\x12$\n LANE_CHANGE_REASON_LANE_OCCUPIED\x10\x02\x12%\n!LANE_CHANGE_REASON_NO_TARGET_LANE\x10\x03\x12\x31\n-LANE_CHANGE_REASON_TARGET_LANE_NOT_ACCESSIBLE\x10\x04\x12\"\n\x1eLANE_CHANGE_REASON_SPEED_RANGE\x10\x05\x12%\n!LANE_CHANGE_REASON_SENSOR_BLOCKED\x10\x06\x12%\n!LANE_CHANGE_REASON_SYSTEM_FAILURE\x10\x07\x12*\n&LANE_CHANGE_REASON_STEERING_NOT_ACTIVE\x10\x08\x12+\n\'LANE_CHANGE_REASON_DRIVER_NOT_ATTENTIVE\x10\t\x12&\n\"LANE_CHANGE_REASON_DRIVER_OVERRIDE\x10\n\x12 \n\x1cLANE_CHANGE_REASON_ROAD_TYPE\x10\x0b\x12/\n+LANE_CHANGE_REASON_ROAD_TYPE_NOT_DETERMINED\x10\x0c\x12\x1e\n\x1aLANE_CHANGE_REASON_UNKNOWN\x10\r*\xc2\x01\n\x1bLaneChangePossibleDirection\x12\'\n#LANE_CHANGE_POSSIBLE_DIRECTION_NONE\x10\x00\x12\'\n#LANE_CHANGE_POSSIBLE_DIRECTION_LEFT\x10\x01\x12(\n$LANE_CHANGE_POSSIBLE_DIRECTION_RIGHT\x10\x02\x12\'\n#LANE_CHANGE_POSSIBLE_DIRECTION_BOTH\x10\x03*\xd2\x02\n\x10LaneChangeStatus\x12\x1a\n\x16LANE_CHANGE_STATUS_OFF\x10\x00\x12\x1e\n\x1aLANE_CHANGE_STATUS_STANDBY\x10\x01\x12 \n\x1cLANE_CHANGE_STATUS_REQUESTED\x10\x02\x12/\n+LANE_CHANGE_STATUS_LATERAL_MANEUVER_STARTED\x10\x03\x12*\n&LANE_CHANGE_STATUS_IN_LATERAL_MANEUVER\x10\x04\x12\x1f\n\x1bLANE_CHANGE_STATUS_FINISHED\x10\x05\x12\x1f\n\x1bLANE_CHANGE_STATUS_REJECTED\x10\x06\x12\x1f\n\x1bLANE_CHANGE_STATUS_ABORTING\x10\x07\x12 \n\x1cLANE_CHANGE_STATUS_HAND_OVER\x10\x08*\x81\x01\n\x0fHandsOffWarning\x12 \n\x1cHANDS_OFF_WARNING_NO_WARNING\x10\x00\x12%\n!HANDS_OFF_WARNING_WARNING_LEVEL_1\x10\x01\x12%\n!HANDS_OFF_WARNING_WARNING_LEVEL_2\x10\x02\x62\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])

_TURNINDICATORREQUEST = _descriptor.EnumDescriptor(
  name='TurnIndicatorRequest',
  full_name='Zenuity.Crusing.TurnIndicatorRequest',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TURN_INDICATOR_REQUEST_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TURN_INDICATOR_REQUEST_LEFT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TURN_INDICATOR_REQUEST_RIGHT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TURN_INDICATOR_REQUEST_HAZARD_LIGHT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2257,
  serialized_end=2420,
)
_sym_db.RegisterEnumDescriptor(_TURNINDICATORREQUEST)

TurnIndicatorRequest = enum_type_wrapper.EnumTypeWrapper(_TURNINDICATORREQUEST)
_LANECHANGETYPE = _descriptor.EnumDescriptor(
  name='LaneChangeType',
  full_name='Zenuity.Crusing.LaneChangeType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_TYPE_NO_INTENT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_TYPE_LEFT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_TYPE_RIGHT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2422,
  serialized_end=2525,
)
_sym_db.RegisterEnumDescriptor(_LANECHANGETYPE)

LaneChangeType = enum_type_wrapper.EnumTypeWrapper(_LANECHANGETYPE)
_LANECHANGEREASON = _descriptor.EnumDescriptor(
  name='LaneChangeReason',
  full_name='Zenuity.Crusing.LaneChangeReason',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_NO_REASON', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_DENIED_BY_DRIVER', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_LANE_OCCUPIED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_NO_TARGET_LANE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_TARGET_LANE_NOT_ACCESSIBLE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_SPEED_RANGE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_SENSOR_BLOCKED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_SYSTEM_FAILURE', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_STEERING_NOT_ACTIVE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_DRIVER_NOT_ATTENTIVE', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_DRIVER_OVERRIDE', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_ROAD_TYPE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_ROAD_TYPE_NOT_DETERMINED', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_REASON_UNKNOWN', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2528,
  serialized_end=3107,
)
_sym_db.RegisterEnumDescriptor(_LANECHANGEREASON)

LaneChangeReason = enum_type_wrapper.EnumTypeWrapper(_LANECHANGEREASON)
_LANECHANGEPOSSIBLEDIRECTION = _descriptor.EnumDescriptor(
  name='LaneChangePossibleDirection',
  full_name='Zenuity.Crusing.LaneChangePossibleDirection',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_POSSIBLE_DIRECTION_NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_POSSIBLE_DIRECTION_LEFT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_POSSIBLE_DIRECTION_RIGHT', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_POSSIBLE_DIRECTION_BOTH', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3110,
  serialized_end=3304,
)
_sym_db.RegisterEnumDescriptor(_LANECHANGEPOSSIBLEDIRECTION)

LaneChangePossibleDirection = enum_type_wrapper.EnumTypeWrapper(_LANECHANGEPOSSIBLEDIRECTION)
_LANECHANGESTATUS = _descriptor.EnumDescriptor(
  name='LaneChangeStatus',
  full_name='Zenuity.Crusing.LaneChangeStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_OFF', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_STANDBY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_REQUESTED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_LATERAL_MANEUVER_STARTED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_IN_LATERAL_MANEUVER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_FINISHED', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_REJECTED', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_ABORTING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANE_CHANGE_STATUS_HAND_OVER', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3307,
  serialized_end=3645,
)
_sym_db.RegisterEnumDescriptor(_LANECHANGESTATUS)

LaneChangeStatus = enum_type_wrapper.EnumTypeWrapper(_LANECHANGESTATUS)
_HANDSOFFWARNING = _descriptor.EnumDescriptor(
  name='HandsOffWarning',
  full_name='Zenuity.Crusing.HandsOffWarning',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HANDS_OFF_WARNING_NO_WARNING', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HANDS_OFF_WARNING_WARNING_LEVEL_1', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HANDS_OFF_WARNING_WARNING_LEVEL_2', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=3648,
  serialized_end=3777,
)
_sym_db.RegisterEnumDescriptor(_HANDSOFFWARNING)

HandsOffWarning = enum_type_wrapper.EnumTypeWrapper(_HANDSOFFWARNING)
TURN_INDICATOR_REQUEST_NONE = 0
TURN_INDICATOR_REQUEST_LEFT = 1
TURN_INDICATOR_REQUEST_RIGHT = 2
TURN_INDICATOR_REQUEST_HAZARD_LIGHT = 3
LANE_CHANGE_TYPE_NO_INTENT = 0
LANE_CHANGE_TYPE_LEFT = 1
LANE_CHANGE_TYPE_RIGHT = 2
LANE_CHANGE_REASON_NO_REASON = 0
LANE_CHANGE_REASON_DENIED_BY_DRIVER = 1
LANE_CHANGE_REASON_LANE_OCCUPIED = 2
LANE_CHANGE_REASON_NO_TARGET_LANE = 3
LANE_CHANGE_REASON_TARGET_LANE_NOT_ACCESSIBLE = 4
LANE_CHANGE_REASON_SPEED_RANGE = 5
LANE_CHANGE_REASON_SENSOR_BLOCKED = 6
LANE_CHANGE_REASON_SYSTEM_FAILURE = 7
LANE_CHANGE_REASON_STEERING_NOT_ACTIVE = 8
LANE_CHANGE_REASON_DRIVER_NOT_ATTENTIVE = 9
LANE_CHANGE_REASON_DRIVER_OVERRIDE = 10
LANE_CHANGE_REASON_ROAD_TYPE = 11
LANE_CHANGE_REASON_ROAD_TYPE_NOT_DETERMINED = 12
LANE_CHANGE_REASON_UNKNOWN = 13
LANE_CHANGE_POSSIBLE_DIRECTION_NONE = 0
LANE_CHANGE_POSSIBLE_DIRECTION_LEFT = 1
LANE_CHANGE_POSSIBLE_DIRECTION_RIGHT = 2
LANE_CHANGE_POSSIBLE_DIRECTION_BOTH = 3
LANE_CHANGE_STATUS_OFF = 0
LANE_CHANGE_STATUS_STANDBY = 1
LANE_CHANGE_STATUS_REQUESTED = 2
LANE_CHANGE_STATUS_LATERAL_MANEUVER_STARTED = 3
LANE_CHANGE_STATUS_IN_LATERAL_MANEUVER = 4
LANE_CHANGE_STATUS_FINISHED = 5
LANE_CHANGE_STATUS_REJECTED = 6
LANE_CHANGE_STATUS_ABORTING = 7
LANE_CHANGE_STATUS_HAND_OVER = 8
HANDS_OFF_WARNING_NO_WARNING = 0
HANDS_OFF_WARNING_WARNING_LEVEL_1 = 1
HANDS_OFF_WARNING_WARNING_LEVEL_2 = 2



_CANCELREASONACC = _descriptor.Descriptor(
  name='CancelReasonAcc',
  full_name='Zenuity.Crusing.CancelReasonAcc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='no_lead_vehicle', full_name='Zenuity.Crusing.CancelReasonAcc.no_lead_vehicle', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_brake_only', full_name='Zenuity.Crusing.CancelReasonAcc.end_brake_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\001\212\265\030\002\010\036\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=172,
)


_ACCELERATIONREQUEST = _descriptor.Descriptor(
  name='AccelerationRequest',
  full_name='Zenuity.Crusing.AccelerationRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='request_active', full_name='Zenuity.Crusing.AccelerationRequest.request_active', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='nominal_acceleration', full_name='Zenuity.Crusing.AccelerationRequest.nominal_acceleration', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\007\"\005m/s\302\262\222\265\030\0062\0040.01\222\265\030\036*\034Current acceleration request\222\265\030\tI\000\000\000\000\000\000\024\300\222\265\030\tQ\000\000\000\000\000\000\024@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_jerk', full_name='Zenuity.Crusing.AccelerationRequest.min_jerk', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\007\"\005m/s\302\263\222\265\030\0062\0040.01\222\265\030X*VRequest from controller to use no less than this jerk to reach requested acceleration.\222\265\030\tI\000\000\000\000\000\000\024\300\222\265\030\tQ\000\000\000\000\000\000\024@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_jerk', full_name='Zenuity.Crusing.AccelerationRequest.max_jerk', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\007\"\005m/s\302\263\222\265\030\0062\0040.01\222\265\030X*VRequest from controller to use no more than this jerk to reach requested acceleration.\222\265\030\tI\000\000\000\000\000\000\024\300\222\265\030\tQ\000\000\000\000\000\000\024@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='standstill_request', full_name='Zenuity.Crusing.AccelerationRequest.standstill_request', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030>*<Request by ACC to stop vehicle and hold it still with brakes', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\001\212\265\030\002\010\037\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=795,
)


_SELECTEDTARGET = _descriptor.Descriptor(
  name='SelectedTarget',
  full_name='Zenuity.Crusing.SelectedTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_selected', full_name='Zenuity.Crusing.SelectedTarget.is_selected', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_controlled_towards', full_name='Zenuity.Crusing.SelectedTarget.is_controlled_towards', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lat_position', full_name='Zenuity.Crusing.SelectedTarget.lat_position', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\003\"\001m\222\265\030\0052\0030.1\222\265\030E*CLateral distance to selected target, ego vehicle coordinate system.\222\265\030\tI\000\000\000\000\000\0004\300\222\265\030\tQ\000\000\000\000\000\0004@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lon_position', full_name='Zenuity.Crusing.SelectedTarget.lon_position', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\003\"\001m\222\265\030\0052\0030.1\222\265\030J*HLongitudinal distance to selected target, ego vehicle coordinate system.\222\265\030\tI\000\000\000\000\000\000\000\000\222\265\030\tQ\000\000\000\000\000\000i@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='speed', full_name='Zenuity.Crusing.SelectedTarget.speed', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\005\"\003m/s\222\265\030\0052\0030.1\222\265\030\033*\031Speed of selected target.\222\265\030\tI\000\000\000\000\000\000\000\000\222\265\030\tQ\000\000\000\000\000\000N@', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=798,
  serialized_end=1261,
)


_TARGETSSELECTEDBYACC = _descriptor.Descriptor(
  name='TargetsSelectedByAcc',
  full_name='Zenuity.Crusing.TargetsSelectedByAcc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='closest_in_lane', full_name='Zenuity.Crusing.TargetsSelectedByAcc.closest_in_lane', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second_closest_in_lane', full_name='Zenuity.Crusing.TargetsSelectedByAcc.second_closest_in_lane', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cut_in', full_name='Zenuity.Crusing.TargetsSelectedByAcc.cut_in', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='closest_in_left_lane', full_name='Zenuity.Crusing.TargetsSelectedByAcc.closest_in_left_lane', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='closest_in_right_lane', full_name='Zenuity.Crusing.TargetsSelectedByAcc.closest_in_right_lane', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\001\212\265\030\002\010 \212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1264,
  serialized_end=1611,
)


_TRAFFICASSISTOUTPUT = _descriptor.Descriptor(
  name='TrafficAssistOutput',
  full_name='Zenuity.Crusing.TrafficAssistOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='turn_indicator_request', full_name='Zenuity.Crusing.TrafficAssistOutput.turn_indicator_request', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\001\212\265\030:\"8Collection of output signals for Traffic Assist function\212\265\030\003\010\232\005\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1614,
  serialized_end=1795,
)


_INFORMATIONTODRIVERFROMTRAFFICASSIST = _descriptor.Descriptor(
  name='InformationToDriverFromTrafficAssist',
  full_name='Zenuity.Crusing.InformationToDriverFromTrafficAssist',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='hands_off_warning', full_name='Zenuity.Crusing.InformationToDriverFromTrafficAssist.hands_off_warning', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_change_type', full_name='Zenuity.Crusing.InformationToDriverFromTrafficAssist.lane_change_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_change_reason', full_name='Zenuity.Crusing.InformationToDriverFromTrafficAssist.lane_change_reason', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_change_possible_direction', full_name='Zenuity.Crusing.InformationToDriverFromTrafficAssist.lane_change_possible_direction', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lane_change_status', full_name='Zenuity.Crusing.InformationToDriverFromTrafficAssist.lane_change_status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\001\212\265\0307\"5Collection of HMI signals for Traffic Assist function\212\265\030\003\010\233\005\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1798,
  serialized_end=2254,
)

_TARGETSSELECTEDBYACC.fields_by_name['closest_in_lane'].message_type = _SELECTEDTARGET
_TARGETSSELECTEDBYACC.fields_by_name['second_closest_in_lane'].message_type = _SELECTEDTARGET
_TARGETSSELECTEDBYACC.fields_by_name['cut_in'].message_type = _SELECTEDTARGET
_TARGETSSELECTEDBYACC.fields_by_name['closest_in_left_lane'].message_type = _SELECTEDTARGET
_TARGETSSELECTEDBYACC.fields_by_name['closest_in_right_lane'].message_type = _SELECTEDTARGET
_TRAFFICASSISTOUTPUT.fields_by_name['turn_indicator_request'].enum_type = _TURNINDICATORREQUEST
_INFORMATIONTODRIVERFROMTRAFFICASSIST.fields_by_name['hands_off_warning'].enum_type = _HANDSOFFWARNING
_INFORMATIONTODRIVERFROMTRAFFICASSIST.fields_by_name['lane_change_type'].enum_type = _LANECHANGETYPE
_INFORMATIONTODRIVERFROMTRAFFICASSIST.fields_by_name['lane_change_reason'].enum_type = _LANECHANGEREASON
_INFORMATIONTODRIVERFROMTRAFFICASSIST.fields_by_name['lane_change_possible_direction'].enum_type = _LANECHANGEPOSSIBLEDIRECTION
_INFORMATIONTODRIVERFROMTRAFFICASSIST.fields_by_name['lane_change_status'].enum_type = _LANECHANGESTATUS
DESCRIPTOR.message_types_by_name['CancelReasonAcc'] = _CANCELREASONACC
DESCRIPTOR.message_types_by_name['AccelerationRequest'] = _ACCELERATIONREQUEST
DESCRIPTOR.message_types_by_name['SelectedTarget'] = _SELECTEDTARGET
DESCRIPTOR.message_types_by_name['TargetsSelectedByAcc'] = _TARGETSSELECTEDBYACC
DESCRIPTOR.message_types_by_name['TrafficAssistOutput'] = _TRAFFICASSISTOUTPUT
DESCRIPTOR.message_types_by_name['InformationToDriverFromTrafficAssist'] = _INFORMATIONTODRIVERFROMTRAFFICASSIST
DESCRIPTOR.enum_types_by_name['TurnIndicatorRequest'] = _TURNINDICATORREQUEST
DESCRIPTOR.enum_types_by_name['LaneChangeType'] = _LANECHANGETYPE
DESCRIPTOR.enum_types_by_name['LaneChangeReason'] = _LANECHANGEREASON
DESCRIPTOR.enum_types_by_name['LaneChangePossibleDirection'] = _LANECHANGEPOSSIBLEDIRECTION
DESCRIPTOR.enum_types_by_name['LaneChangeStatus'] = _LANECHANGESTATUS
DESCRIPTOR.enum_types_by_name['HandsOffWarning'] = _HANDSOFFWARNING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CancelReasonAcc = _reflection.GeneratedProtocolMessageType('CancelReasonAcc', (_message.Message,), {
  'DESCRIPTOR' : _CANCELREASONACC,
  '__module__' : 'Zenuity.Cruising_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.Crusing.CancelReasonAcc)
  })
_sym_db.RegisterMessage(CancelReasonAcc)

AccelerationRequest = _reflection.GeneratedProtocolMessageType('AccelerationRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCELERATIONREQUEST,
  '__module__' : 'Zenuity.Cruising_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.Crusing.AccelerationRequest)
  })
_sym_db.RegisterMessage(AccelerationRequest)

SelectedTarget = _reflection.GeneratedProtocolMessageType('SelectedTarget', (_message.Message,), {
  'DESCRIPTOR' : _SELECTEDTARGET,
  '__module__' : 'Zenuity.Cruising_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.Crusing.SelectedTarget)
  })
_sym_db.RegisterMessage(SelectedTarget)

TargetsSelectedByAcc = _reflection.GeneratedProtocolMessageType('TargetsSelectedByAcc', (_message.Message,), {
  'DESCRIPTOR' : _TARGETSSELECTEDBYACC,
  '__module__' : 'Zenuity.Cruising_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.Crusing.TargetsSelectedByAcc)
  })
_sym_db.RegisterMessage(TargetsSelectedByAcc)

TrafficAssistOutput = _reflection.GeneratedProtocolMessageType('TrafficAssistOutput', (_message.Message,), {
  'DESCRIPTOR' : _TRAFFICASSISTOUTPUT,
  '__module__' : 'Zenuity.Cruising_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.Crusing.TrafficAssistOutput)
  })
_sym_db.RegisterMessage(TrafficAssistOutput)

InformationToDriverFromTrafficAssist = _reflection.GeneratedProtocolMessageType('InformationToDriverFromTrafficAssist', (_message.Message,), {
  'DESCRIPTOR' : _INFORMATIONTODRIVERFROMTRAFFICASSIST,
  '__module__' : 'Zenuity.Cruising_pb2'
  # @@protoc_insertion_point(class_scope:Zenuity.Crusing.InformationToDriverFromTrafficAssist)
  })
_sym_db.RegisterMessage(InformationToDriverFromTrafficAssist)


_CANCELREASONACC._options = None
_ACCELERATIONREQUEST.fields_by_name['nominal_acceleration']._options = None
_ACCELERATIONREQUEST.fields_by_name['min_jerk']._options = None
_ACCELERATIONREQUEST.fields_by_name['max_jerk']._options = None
_ACCELERATIONREQUEST.fields_by_name['standstill_request']._options = None
_ACCELERATIONREQUEST._options = None
_SELECTEDTARGET.fields_by_name['lat_position']._options = None
_SELECTEDTARGET.fields_by_name['lon_position']._options = None
_SELECTEDTARGET.fields_by_name['speed']._options = None
_TARGETSSELECTEDBYACC._options = None
_TRAFFICASSISTOUTPUT._options = None
_INFORMATIONTODRIVERFROMTRAFFICASSIST._options = None
# @@protoc_insertion_point(module_scope)