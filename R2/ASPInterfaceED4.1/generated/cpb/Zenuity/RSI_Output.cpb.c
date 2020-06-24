/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "Zenuity/RSI_Output.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t Zenuity_RSI_SpeedLimit_fields[5] = {
    PB_FIELD(  1, 8    , 1    , ENUM    , OPTIONAL, STATIC  , FIRST, Zenuity_RSI_SpeedLimit, speedUnit, speedUnit, 0),
    PB_FIELD(  2, 16   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_SpeedLimit, currentSpeedLimit, speedUnit, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_SpeedLimit, upcomingSpeedLimit, currentSpeedLimit, 0),
    PB_FIELD(  4, 32   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_SpeedLimit, distanceToUpcomingSpeedLimit, upcomingSpeedLimit, 0),
    PB_LAST_FIELD
};

const pb_field_t Zenuity_RSI_RoadSignWarnings_fields[5] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, Zenuity_RSI_RoadSignWarnings, overspeedWarning, overspeedWarning, 0),
    PB_FIELD(  2, 16   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RoadSignWarnings, speedCameraWarning, overspeedWarning, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RoadSignWarnings, distanceToSpeedCamera, speedCameraWarning, 0),
    PB_FIELD(  4, 32   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RoadSignWarnings, noEntryWarning, distanceToSpeedCamera, 0),
    PB_LAST_FIELD
};

const pb_field_t Zenuity_RSI_RsiDebug_fields[5] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, Zenuity_RSI_RsiDebug, visionSpeedLimitAvailable, visionSpeedLimitAvailable, 0),
    PB_FIELD(  2, 16   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiDebug, electronicHorizonSpeedLimitAvailable, visionSpeedLimitAvailable, 0),
    PB_FIELD(  3, 24   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiDebug, electronicHorizonAndVisionAvailableAndEqual, electronicHorizonSpeedLimitAvailable, 0),
    PB_FIELD(  4, 32   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiDebug, speedLimitSourceIsOnlyElectronicHorizon, electronicHorizonAndVisionAvailableAndEqual, 0),
    PB_LAST_FIELD
};

const pb_field_t Zenuity_RSI_RsiOutput_fields[7] = {
    PB_FIELD(  1, 8    , 1    , ENUM    , OPTIONAL, STATIC  , FIRST, Zenuity_RSI_RsiOutput, availability, availability, 0),
    PB_FIELD(  2, 16   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiOutput, status, availability, 0),
    PB_FIELD(  3, 26   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiOutput, speedLimit, status, &Zenuity_RSI_SpeedLimit_fields),
    PB_FIELD(  4, 34   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiOutput, warnings, speedLimit, &Zenuity_RSI_RoadSignWarnings_fields),
    PB_FIELD(  5, 40   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiOutput, arbitratedCountry, warnings, 0),
    PB_FIELD(  6, 50   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, Zenuity_RSI_RsiOutput, debug, arbitratedCountry, &Zenuity_RSI_RsiDebug_fields),
    PB_LAST_FIELD
};

