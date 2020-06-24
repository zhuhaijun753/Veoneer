# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VisionCore/Road/RoadBoundary.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Tools.Extension import SystemOptions_pb2 as Tools_dot_Extension_dot_SystemOptions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='VisionCore/Road/RoadBoundary.proto',
  package='VisionCore.Road',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"VisionCore/Road/RoadBoundary.proto\x12\x0fVisionCore.Road\x1a#Tools/Extension/SystemOptions.proto\"\xdb\x04\n\x14RoadBoundaryClothoid\x12\x91\x01\n\x10lateral_distance\x18\x01 \x01(\x11\x42w\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x03\"\x01m\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00I\xc0\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00I@\x92\xb5\x18\x42*@Lateral distance to the inside of the road boundary (default: 0)\x12g\n\x07heading\x18\x02 \x01(\x11\x42V\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\n2\x08\x30.000025\x92\xb5\x18\x0b\"\tatan(rad)\x92\xb5\x18/*-The heading coefficient of the clothoid model\x12o\n\tcurvature\x18\x03 \x01(\x11\x42\\\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x0b\x32\t0.0000025\x92\xb5\x18\x05\"\x03\x31/m\x92\xb5\x18:*8Horizontal curvature for the start of the first clothoid\x12m\n\x0e\x63urvature_rate\x18\x04 \x01(\x11\x42U\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\n2\x08\x30.000001\x92\xb5\x18\x07\"\x05\x31/m\xc2\xb2\x92\xb5\x18\x32*0Horizontal curvature rate for the first clothoid:f\x8a\xb5\x18\x62\"`Cartesian coordinates in Autosar Front Axis Coordinate system projected on ground plane (AFAC-G)\"\x99\x03\n\x1cRoadBoundaryClothoidVariance\x12\x61\n\x19lateral_distance_variance\x18\x01 \x01(\x11\x42>\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x07\"\x05\x31/m\xc2\xb2\x92\xb5\x18\x1f*\x1dVariance for lateral distance\x12Y\n\x10heading_variance\x18\x02 \x01(\x11\x42?\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\n2\x08\x30.000025\x92\xb5\x18\r\"\x0b\x61tan(rad)\xc2\xb2\x92\xb5\x18\x16*\x14Variance for heading\x12X\n\x12\x63urvature_variance\x18\x03 \x01(\x11\x42<\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\x0b\x32\t0.0000025\x92\xb5\x18\x07\"\x05\x31/m\xc2\xb2\x92\xb5\x18\x18*\x16Variance for curvature\x12\x61\n\x17\x63urvature_rate_variance\x18\x04 \x01(\x11\x42@\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\n2\x08\x30.000001\x92\xb5\x18\x07\"\x05\x31/m^4\x92\xb5\x18\x1d*\x1bVariance for curvature rate\"\xf6\x07\n\x11RoadBoundaryTrack\x12V\n\x05valid\x18\x01 \x01(\x08\x42G\x92\xb5\x18\x43*ATrue means that RoadBoundaryTrack describes a valid road boundary\x12G\n\x02id\x18\x02 \x01(\rB;\x92\xb5\x18\x02\x08\x08\x92\xb5\x18\x31*/ID nr (default: 255 = SNA, propose change to 0)\x12\x82\x01\n\x12\x64\x65tection_distance\x18\x03 \x01(\rBf\x92\xb5\x18\x02\x08\x10\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\xc0\x62@\x92\xb5\x18\x05\x32\x03\x30.1\x92\xb5\x18\x03\"\x01m\x92\xb5\x18?*=Longitudinal distance for which the Road Boundary is detected\x12\x66\n\x0ftracking_status\x18\x04 \x01(\x0e\x32+.VisionCore.Road.RoadBoundaryTrackingStatusB \x92\xb5\x18\x1c*\x1a\x44\x65scribes detection status\x12\xc7\x01\n\x0bmodel_error\x18\x05 \x01(\rB\xb1\x01\x92\xb5\x18\x02\x08\x08\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x00\x00\x92\xb5\x18\tQffffff\x04@\x92\xb5\x18\x06\x32\x04\x30.01\x92\xb5\x18\x03\"\x01m\x92\xb5\x18|*zDescribes how well the measurements are adapted to the model. Mean square deviation between measurements and model points.\x12l\n\x13measurement_quality\x18\x06 \x01(\rBO\x92\xb5\x18\x02\x08\x08\x92\xb5\x18\tI\x00\x00\x00\x00\x00\x00\x00\x00\x92\xb5\x18\tQ\x00\x00\x00\x00\x00\x00Y@\x92\xb5\x18\x03\"\x01%\x92\xb5\x18$*\"Describes quality of the detection\x12_\n\x08\x63lothoid\x18\x07 \x01(\x0b\x32%.VisionCore.Road.RoadBoundaryClothoidB&\x92\xb5\x18\"* Describes road boundary clothoid\x12?\n\x07is_safe\x18\x08 \x01(\x08\x42.\x92\xb5\x18**(True means that the track is safe to use\x12y\n\x11\x63lothoid_variance\x18\t \x01(\x0b\x32-.VisionCore.Road.RoadBoundaryClothoidVarianceB/\x92\xb5\x18+*)Describes road boundary clothoid variance\"\xd3\x04\n\x0cRoadBoundary\x12t\n\x1eleft_traversable_road_boundary\x18\x01 \x01(\x0b\x32\".VisionCore.Road.RoadBoundaryTrackB(\x92\xb5\x18$*\"The left traversable road boundary\x12v\n\x1fright_traversable_road_boundary\x18\x02 \x01(\x0b\x32\".VisionCore.Road.RoadBoundaryTrackB)\x92\xb5\x18%*#The right traversable road boundary\x12{\n\"left_non_traversable_road_boundary\x18\x03 \x01(\x0b\x32\".VisionCore.Road.RoadBoundaryTrackB+\x92\xb5\x18\'*%The left nontraversable road boundary\x12}\n#right_non_traversable_road_boundary\x18\x04 \x01(\x0b\x32\".VisionCore.Road.RoadBoundaryTrackB,\x92\xb5\x18(*&The right nontraversable road boundary:Y\x8a\xb5\x18\x02(\x02\x8a\xb5\x18<\":Output describing the road boundaries ahead of the vehicle\x8a\xb5\x18\x03\x08\xcb\x01\x8a\xb5\x18\x02\x10\x01\x8a\xb5\x18\x02\x18\x00*\xc1\x02\n\x1aRoadBoundaryTrackingStatus\x12.\n*ROAD_BOUNDARY_TRACKING_STATUS_NOT_DETECTED\x10\x00\x12;\n7ROAD_BOUNDARY_TRACKING_STATUS_TRACKED_DETECTED_BOUNDARY\x10\x01\x12@\n<ROAD_BOUNDARY_TRACKING_STATUS_CLOSE_RANGE_PREDICTED_BOUNDARY\x10\x02\x12>\n:ROAD_BOUNDARY_TRACKING_STATUS_FAR_RANGE_PREDICTED_BOUNDARY\x10\x03\x12\x34\n0ROAD_BOUNDARY_TRACKING_STATUS_PREDICTED_BOUNDARY\x10\x04\x62\x06proto3'
  ,
  dependencies=[Tools_dot_Extension_dot_SystemOptions__pb2.DESCRIPTOR,])

_ROADBOUNDARYTRACKINGSTATUS = _descriptor.EnumDescriptor(
  name='RoadBoundaryTrackingStatus',
  full_name='VisionCore.Road.RoadBoundaryTrackingStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROAD_BOUNDARY_TRACKING_STATUS_NOT_DETECTED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROAD_BOUNDARY_TRACKING_STATUS_TRACKED_DETECTED_BOUNDARY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROAD_BOUNDARY_TRACKING_STATUS_CLOSE_RANGE_PREDICTED_BOUNDARY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROAD_BOUNDARY_TRACKING_STATUS_FAR_RANGE_PREDICTED_BOUNDARY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROAD_BOUNDARY_TRACKING_STATUS_PREDICTED_BOUNDARY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2726,
  serialized_end=3047,
)
_sym_db.RegisterEnumDescriptor(_ROADBOUNDARYTRACKINGSTATUS)

RoadBoundaryTrackingStatus = enum_type_wrapper.EnumTypeWrapper(_ROADBOUNDARYTRACKINGSTATUS)
ROAD_BOUNDARY_TRACKING_STATUS_NOT_DETECTED = 0
ROAD_BOUNDARY_TRACKING_STATUS_TRACKED_DETECTED_BOUNDARY = 1
ROAD_BOUNDARY_TRACKING_STATUS_CLOSE_RANGE_PREDICTED_BOUNDARY = 2
ROAD_BOUNDARY_TRACKING_STATUS_FAR_RANGE_PREDICTED_BOUNDARY = 3
ROAD_BOUNDARY_TRACKING_STATUS_PREDICTED_BOUNDARY = 4



_ROADBOUNDARYCLOTHOID = _descriptor.Descriptor(
  name='RoadBoundaryClothoid',
  full_name='VisionCore.Road.RoadBoundaryClothoid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lateral_distance', full_name='VisionCore.Road.RoadBoundaryClothoid.lateral_distance', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0062\0040.01\222\265\030\003\"\001m\222\265\030\tI\000\000\000\000\000\000I\300\222\265\030\tQ\000\000\000\000\000\000I@\222\265\030B*@Lateral distance to the inside of the road boundary (default: 0)', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading', full_name='VisionCore.Road.RoadBoundaryClothoid.heading', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\n2\0100.000025\222\265\030\013\"\tatan(rad)\222\265\030/*-The heading coefficient of the clothoid model', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curvature', full_name='VisionCore.Road.RoadBoundaryClothoid.curvature', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0132\t0.0000025\222\265\030\005\"\0031/m\222\265\030:*8Horizontal curvature for the start of the first clothoid', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curvature_rate', full_name='VisionCore.Road.RoadBoundaryClothoid.curvature_rate', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\n2\0100.000001\222\265\030\007\"\0051/m\302\262\222\265\0302*0Horizontal curvature rate for the first clothoid', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030b\"`Cartesian coordinates in Autosar Front Axis Coordinate system projected on ground plane (AFAC-G)',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=696,
)


_ROADBOUNDARYCLOTHOIDVARIANCE = _descriptor.Descriptor(
  name='RoadBoundaryClothoidVariance',
  full_name='VisionCore.Road.RoadBoundaryClothoidVariance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lateral_distance_variance', full_name='VisionCore.Road.RoadBoundaryClothoidVariance.lateral_distance_variance', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0062\0040.01\222\265\030\007\"\0051/m\302\262\222\265\030\037*\035Variance for lateral distance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='heading_variance', full_name='VisionCore.Road.RoadBoundaryClothoidVariance.heading_variance', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\n2\0100.000025\222\265\030\r\"\013atan(rad)\302\262\222\265\030\026*\024Variance for heading', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curvature_variance', full_name='VisionCore.Road.RoadBoundaryClothoidVariance.curvature_variance', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\0132\t0.0000025\222\265\030\007\"\0051/m\302\262\222\265\030\030*\026Variance for curvature', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='curvature_rate_variance', full_name='VisionCore.Road.RoadBoundaryClothoidVariance.curvature_rate_variance', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\n2\0100.000001\222\265\030\007\"\0051/m^4\222\265\030\035*\033Variance for curvature rate', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=699,
  serialized_end=1108,
)


_ROADBOUNDARYTRACK = _descriptor.Descriptor(
  name='RoadBoundaryTrack',
  full_name='VisionCore.Road.RoadBoundaryTrack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='VisionCore.Road.RoadBoundaryTrack.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030C*ATrue means that RoadBoundaryTrack describes a valid road boundary', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='VisionCore.Road.RoadBoundaryTrack.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\010\222\265\0301*/ID nr (default: 255 = SNA, propose change to 0)', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='detection_distance', full_name='VisionCore.Road.RoadBoundaryTrack.detection_distance', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\020\222\265\030\tQ\000\000\000\000\000\300b@\222\265\030\0052\0030.1\222\265\030\003\"\001m\222\265\030?*=Longitudinal distance for which the Road Boundary is detected', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tracking_status', full_name='VisionCore.Road.RoadBoundaryTrack.tracking_status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\034*\032Describes detection status', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='model_error', full_name='VisionCore.Road.RoadBoundaryTrack.model_error', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\010\222\265\030\tI\000\000\000\000\000\000\000\000\222\265\030\tQffffff\004@\222\265\030\0062\0040.01\222\265\030\003\"\001m\222\265\030|*zDescribes how well the measurements are adapted to the model. Mean square deviation between measurements and model points.', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='measurement_quality', full_name='VisionCore.Road.RoadBoundaryTrack.measurement_quality', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\002\010\010\222\265\030\tI\000\000\000\000\000\000\000\000\222\265\030\tQ\000\000\000\000\000\000Y@\222\265\030\003\"\001%\222\265\030$*\"Describes quality of the detection', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clothoid', full_name='VisionCore.Road.RoadBoundaryTrack.clothoid', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\"* Describes road boundary clothoid', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_safe', full_name='VisionCore.Road.RoadBoundaryTrack.is_safe', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030**(True means that the track is safe to use', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='clothoid_variance', full_name='VisionCore.Road.RoadBoundaryTrack.clothoid_variance', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030+*)Describes road boundary clothoid variance', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1111,
  serialized_end=2125,
)


_ROADBOUNDARY = _descriptor.Descriptor(
  name='RoadBoundary',
  full_name='VisionCore.Road.RoadBoundary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='left_traversable_road_boundary', full_name='VisionCore.Road.RoadBoundary.left_traversable_road_boundary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030$*\"The left traversable road boundary', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_traversable_road_boundary', full_name='VisionCore.Road.RoadBoundary.right_traversable_road_boundary', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030%*#The right traversable road boundary', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='left_non_traversable_road_boundary', full_name='VisionCore.Road.RoadBoundary.left_non_traversable_road_boundary', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030\'*%The left nontraversable road boundary', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='right_non_traversable_road_boundary', full_name='VisionCore.Road.RoadBoundary.right_non_traversable_road_boundary', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\222\265\030(*&The right nontraversable road boundary', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\212\265\030\002(\002\212\265\030<\":Output describing the road boundaries ahead of the vehicle\212\265\030\003\010\313\001\212\265\030\002\020\001\212\265\030\002\030\000',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2128,
  serialized_end=2723,
)

_ROADBOUNDARYTRACK.fields_by_name['tracking_status'].enum_type = _ROADBOUNDARYTRACKINGSTATUS
_ROADBOUNDARYTRACK.fields_by_name['clothoid'].message_type = _ROADBOUNDARYCLOTHOID
_ROADBOUNDARYTRACK.fields_by_name['clothoid_variance'].message_type = _ROADBOUNDARYCLOTHOIDVARIANCE
_ROADBOUNDARY.fields_by_name['left_traversable_road_boundary'].message_type = _ROADBOUNDARYTRACK
_ROADBOUNDARY.fields_by_name['right_traversable_road_boundary'].message_type = _ROADBOUNDARYTRACK
_ROADBOUNDARY.fields_by_name['left_non_traversable_road_boundary'].message_type = _ROADBOUNDARYTRACK
_ROADBOUNDARY.fields_by_name['right_non_traversable_road_boundary'].message_type = _ROADBOUNDARYTRACK
DESCRIPTOR.message_types_by_name['RoadBoundaryClothoid'] = _ROADBOUNDARYCLOTHOID
DESCRIPTOR.message_types_by_name['RoadBoundaryClothoidVariance'] = _ROADBOUNDARYCLOTHOIDVARIANCE
DESCRIPTOR.message_types_by_name['RoadBoundaryTrack'] = _ROADBOUNDARYTRACK
DESCRIPTOR.message_types_by_name['RoadBoundary'] = _ROADBOUNDARY
DESCRIPTOR.enum_types_by_name['RoadBoundaryTrackingStatus'] = _ROADBOUNDARYTRACKINGSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoadBoundaryClothoid = _reflection.GeneratedProtocolMessageType('RoadBoundaryClothoid', (_message.Message,), {
  'DESCRIPTOR' : _ROADBOUNDARYCLOTHOID,
  '__module__' : 'VisionCore.Road.RoadBoundary_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Road.RoadBoundaryClothoid)
  })
_sym_db.RegisterMessage(RoadBoundaryClothoid)

RoadBoundaryClothoidVariance = _reflection.GeneratedProtocolMessageType('RoadBoundaryClothoidVariance', (_message.Message,), {
  'DESCRIPTOR' : _ROADBOUNDARYCLOTHOIDVARIANCE,
  '__module__' : 'VisionCore.Road.RoadBoundary_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Road.RoadBoundaryClothoidVariance)
  })
_sym_db.RegisterMessage(RoadBoundaryClothoidVariance)

RoadBoundaryTrack = _reflection.GeneratedProtocolMessageType('RoadBoundaryTrack', (_message.Message,), {
  'DESCRIPTOR' : _ROADBOUNDARYTRACK,
  '__module__' : 'VisionCore.Road.RoadBoundary_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Road.RoadBoundaryTrack)
  })
_sym_db.RegisterMessage(RoadBoundaryTrack)

RoadBoundary = _reflection.GeneratedProtocolMessageType('RoadBoundary', (_message.Message,), {
  'DESCRIPTOR' : _ROADBOUNDARY,
  '__module__' : 'VisionCore.Road.RoadBoundary_pb2'
  # @@protoc_insertion_point(class_scope:VisionCore.Road.RoadBoundary)
  })
_sym_db.RegisterMessage(RoadBoundary)


_ROADBOUNDARYCLOTHOID.fields_by_name['lateral_distance']._options = None
_ROADBOUNDARYCLOTHOID.fields_by_name['heading']._options = None
_ROADBOUNDARYCLOTHOID.fields_by_name['curvature']._options = None
_ROADBOUNDARYCLOTHOID.fields_by_name['curvature_rate']._options = None
_ROADBOUNDARYCLOTHOID._options = None
_ROADBOUNDARYCLOTHOIDVARIANCE.fields_by_name['lateral_distance_variance']._options = None
_ROADBOUNDARYCLOTHOIDVARIANCE.fields_by_name['heading_variance']._options = None
_ROADBOUNDARYCLOTHOIDVARIANCE.fields_by_name['curvature_variance']._options = None
_ROADBOUNDARYCLOTHOIDVARIANCE.fields_by_name['curvature_rate_variance']._options = None
_ROADBOUNDARYTRACK.fields_by_name['valid']._options = None
_ROADBOUNDARYTRACK.fields_by_name['id']._options = None
_ROADBOUNDARYTRACK.fields_by_name['detection_distance']._options = None
_ROADBOUNDARYTRACK.fields_by_name['tracking_status']._options = None
_ROADBOUNDARYTRACK.fields_by_name['model_error']._options = None
_ROADBOUNDARYTRACK.fields_by_name['measurement_quality']._options = None
_ROADBOUNDARYTRACK.fields_by_name['clothoid']._options = None
_ROADBOUNDARYTRACK.fields_by_name['is_safe']._options = None
_ROADBOUNDARYTRACK.fields_by_name['clothoid_variance']._options = None
_ROADBOUNDARY.fields_by_name['left_traversable_road_boundary']._options = None
_ROADBOUNDARY.fields_by_name['right_traversable_road_boundary']._options = None
_ROADBOUNDARY.fields_by_name['left_non_traversable_road_boundary']._options = None
_ROADBOUNDARY.fields_by_name['right_non_traversable_road_boundary']._options = None
_ROADBOUNDARY._options = None
# @@protoc_insertion_point(module_scope)
