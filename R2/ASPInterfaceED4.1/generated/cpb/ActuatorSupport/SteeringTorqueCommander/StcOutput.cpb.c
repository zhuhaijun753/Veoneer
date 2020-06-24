/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "ActuatorSupport/SteeringTorqueCommander/StcOutput.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t ActuatorSupport_SteeringTorqueCommander_StcOutput_fields[6] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, ActuatorSupport_SteeringTorqueCommander_StcOutput, steeringWheelTorqueRequest, steeringWheelTorqueRequest, 0),
    PB_FIELD(  2, 16   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, ActuatorSupport_SteeringTorqueCommander_StcOutput, steeringWheelTorqueActive, steeringWheelTorqueRequest, 0),
    PB_FIELD(  3, 24   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, ActuatorSupport_SteeringTorqueCommander_StcOutput, steeringWheelControlLimited, steeringWheelTorqueActive, 0),
    PB_FIELD(  4, 32   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, ActuatorSupport_SteeringTorqueCommander_StcOutput, steeringWheelTorqueRatio, steeringWheelControlLimited, 0),
    PB_FIELD(  5, 40   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, ActuatorSupport_SteeringTorqueCommander_StcOutput, steeringWheelTorqueControlState, steeringWheelTorqueRatio, 0),
    PB_LAST_FIELD
};
