/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "SystemCore/Cruising/CruisingInput.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t SystemCore_Cruising_TrafficAssistInput_fields[5] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, SystemCore_Cruising_TrafficAssistInput, enable, enable, 0),
    PB_FIELD(  2, 16   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, SystemCore_Cruising_TrafficAssistInput, steeringEnabled, enable, 0),
    PB_FIELD(  3, 24   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, SystemCore_Cruising_TrafficAssistInput, driverInTheLoopDetected, steeringEnabled, 0),
    PB_FIELD(  4, 32   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, SystemCore_Cruising_TrafficAssistInput, trafficAssistIsSteering, driverInTheLoopDetected, 0),
    PB_LAST_FIELD
};

const pb_field_t SystemCore_Cruising_LaneChangeAssistInput_fields[5] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, SystemCore_Cruising_LaneChangeAssistInput, enable, enable, 0),
    PB_FIELD(  2, 16   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, SystemCore_Cruising_LaneChangeAssistInput, laneChangeRequestByDriver, enable, 0),
    PB_FIELD(  3, 24   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, SystemCore_Cruising_LaneChangeAssistInput, laneChangeAbortRequestByDriver, laneChangeRequestByDriver, 0),
    PB_FIELD(  4, 32   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, SystemCore_Cruising_LaneChangeAssistInput, rearRadarDetectionRange, laneChangeAbortRequestByDriver, 0),
    PB_LAST_FIELD
};

const pb_field_t SystemCore_Cruising_RiskMitigationSupportInput_fields[2] = {
    PB_FIELD(  1, 8    , 1    , ENUM    , OPTIONAL, STATIC  , FIRST, SystemCore_Cruising_RiskMitigationSupportInput, rmsStatus, rmsStatus, 0),
    PB_LAST_FIELD
};

const pb_field_t SystemCore_Cruising_DriverAlertControlInput_fields[2] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, SystemCore_Cruising_DriverAlertControlInput, dacActivated, dacActivated, 0),
    PB_LAST_FIELD
};
