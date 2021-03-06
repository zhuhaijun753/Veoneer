/* Automatically generated pb header */
/* Generated by Protocol Buffers - 1 */

#ifndef SYSTEMCORE_CRUISING_CRUISING_INCLUDED
#define SYSTEMCORE_CRUISING_CRUISING_INCLUDED
#include "Tools/CProtobuf/pb.h"
#include "Tools/CProtobuf/pb_decode.h"
#include "Tools/CProtobuf/pb_encode.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define SystemCore_Crusing_CruisingFeatureState_size                                     (6)
#define SystemCore_Crusing_DistanceControllerInput_size                                  (15)
#define SystemCore_Crusing_IndicatedSpeed_size                                           (5)
#define SystemCore_Crusing_SetSpeedControllerInput_size                                  (6)
#define SystemCore_Crusing_AccCommonInput_size                                           ((14 + SystemCore_Crusing_IndicatedSpeed_size) + PB_VARINT_MAX_ENCODED_SIZE)

/* Message IDs (where set with "identifier" option) */
#define SystemCore_Crusing_AccCommonInput_source                                         3U
#define SystemCore_Crusing_AccCommonInput_identifier                                     30U
#define SystemCore_Crusing_AccCommonInput_majorVersion                                   1U
#define SystemCore_Crusing_AccCommonInput_minorVersion                                   0U
#define SystemCore_Crusing_SetSpeedControllerInput_source                                3U
#define SystemCore_Crusing_SetSpeedControllerInput_identifier                            31U
#define SystemCore_Crusing_SetSpeedControllerInput_majorVersion                          1U
#define SystemCore_Crusing_SetSpeedControllerInput_minorVersion                          0U
#define SystemCore_Crusing_CruisingFeatureState_source                                   3U
#define SystemCore_Crusing_CruisingFeatureState_identifier                               32U
#define SystemCore_Crusing_CruisingFeatureState_majorVersion                             1U
#define SystemCore_Crusing_CruisingFeatureState_minorVersion                             0U
#define SystemCore_Crusing_DistanceControllerInput_source                                3U
#define SystemCore_Crusing_DistanceControllerInput_identifier                            33U
#define SystemCore_Crusing_DistanceControllerInput_majorVersion                          1U
#define SystemCore_Crusing_DistanceControllerInput_minorVersion                          0U

/* Enum definitions */
typedef enum _SystemCore_Crusing_SpeedUnit {
    SystemCore_Crusing_SpeedUnit_Kph = 0,
    SystemCore_Crusing_SpeedUnit_Mph = 1
} SystemCore_Crusing_SpeedUnit;
#define SystemCore_Crusing_SpeedUnit_MIN SystemCore_Crusing_SpeedUnit_Kph
#define SystemCore_Crusing_SpeedUnit_MAX SystemCore_Crusing_SpeedUnit_Mph
#define SystemCore_Crusing_SpeedUnit_ARRAYSIZE ((SystemCore_Crusing_SpeedUnit)(SystemCore_Crusing_SpeedUnit_Mph+1))

typedef enum _SystemCore_Crusing_AccDriveMode {
    SystemCore_Crusing_AccDriveMode_Invalid = 0,
    SystemCore_Crusing_AccDriveMode_Comfort = 1,
    SystemCore_Crusing_AccDriveMode_Dynamic = 2,
    SystemCore_Crusing_AccDriveMode_Eco = 3
} SystemCore_Crusing_AccDriveMode;
#define SystemCore_Crusing_AccDriveMode_MIN SystemCore_Crusing_AccDriveMode_Invalid
#define SystemCore_Crusing_AccDriveMode_MAX SystemCore_Crusing_AccDriveMode_Eco
#define SystemCore_Crusing_AccDriveMode_ARRAYSIZE ((SystemCore_Crusing_AccDriveMode)(SystemCore_Crusing_AccDriveMode_Eco+1))

typedef enum _SystemCore_Crusing_AccState {
    SystemCore_Crusing_AccState_Off = 0,
    SystemCore_Crusing_AccState_Standby = 1,
    SystemCore_Crusing_AccState_Active = 2,
    SystemCore_Crusing_AccState_Stop = 3,
    SystemCore_Crusing_AccState_BrakeOnly = 4
} SystemCore_Crusing_AccState;
#define SystemCore_Crusing_AccState_MIN SystemCore_Crusing_AccState_Off
#define SystemCore_Crusing_AccState_MAX SystemCore_Crusing_AccState_BrakeOnly
#define SystemCore_Crusing_AccState_ARRAYSIZE ((SystemCore_Crusing_AccState)(SystemCore_Crusing_AccState_BrakeOnly+1))

typedef enum _SystemCore_Crusing_StandstillStatus {
    SystemCore_Crusing_StandstillStatus_StationaryNotHeld = 0,
    SystemCore_Crusing_StandstillStatus_StationaryHeld = 1,
    SystemCore_Crusing_StandstillStatus_Moving = 2
} SystemCore_Crusing_StandstillStatus;
#define SystemCore_Crusing_StandstillStatus_MIN SystemCore_Crusing_StandstillStatus_StationaryNotHeld
#define SystemCore_Crusing_StandstillStatus_MAX SystemCore_Crusing_StandstillStatus_Moving
#define SystemCore_Crusing_StandstillStatus_ARRAYSIZE ((SystemCore_Crusing_StandstillStatus)(SystemCore_Crusing_StandstillStatus_Moving+1))

typedef enum _SystemCore_Crusing_UsedActuator {
    SystemCore_Crusing_UsedActuator_None = 0,
    SystemCore_Crusing_UsedActuator_Engine = 1,
    SystemCore_Crusing_UsedActuator_Brake = 2
} SystemCore_Crusing_UsedActuator;
#define SystemCore_Crusing_UsedActuator_MIN SystemCore_Crusing_UsedActuator_None
#define SystemCore_Crusing_UsedActuator_MAX SystemCore_Crusing_UsedActuator_Brake
#define SystemCore_Crusing_UsedActuator_ARRAYSIZE ((SystemCore_Crusing_UsedActuator)(SystemCore_Crusing_UsedActuator_Brake+1))

typedef enum _SystemCore_Crusing_LateralDirection {
    SystemCore_Crusing_LateralDirection_None = 0,
    SystemCore_Crusing_LateralDirection_Left = 1,
    SystemCore_Crusing_LateralDirection_Right = 2
} SystemCore_Crusing_LateralDirection;
#define SystemCore_Crusing_LateralDirection_MIN SystemCore_Crusing_LateralDirection_None
#define SystemCore_Crusing_LateralDirection_MAX SystemCore_Crusing_LateralDirection_Right
#define SystemCore_Crusing_LateralDirection_ARRAYSIZE ((SystemCore_Crusing_LateralDirection)(SystemCore_Crusing_LateralDirection_Right+1))

typedef enum _SystemCore_Crusing_ChangedBy {
    SystemCore_Crusing_ChangedBy_System = 0,
    SystemCore_Crusing_ChangedBy_Driver = 1
} SystemCore_Crusing_ChangedBy;
#define SystemCore_Crusing_ChangedBy_MIN SystemCore_Crusing_ChangedBy_System
#define SystemCore_Crusing_ChangedBy_MAX SystemCore_Crusing_ChangedBy_Driver
#define SystemCore_Crusing_ChangedBy_ARRAYSIZE ((SystemCore_Crusing_ChangedBy)(SystemCore_Crusing_ChangedBy_Driver+1))

/* Struct definitions */
typedef struct _SystemCore_Crusing_CruisingFeatureState {
    /** CsaActive
     * If true: CSA will control against high curve speeds
     */
    bool csaActive;
    /** CcActive
     * If true: CC will control to reach setspeed
     */
    bool ccActive;
    /** AccState
     * State will affect ACC feature consiting of both distance(ACC) and setspeed(CC) controller
     */
    SystemCore_Crusing_AccState accState;
} SystemCore_Crusing_CruisingFeatureState;

typedef struct _SystemCore_Crusing_DistanceControllerInput {
    /** Timegap
     * Which of 5 timegaps that is requested
     * Min: 1
     * Max: 5
     */
    uint8_t timegap;
    /** CurrentAccelerationRequestedToActuators
     * Current acceleration requested to actuators, used for jerk limitation calculations within ACC
     * Unit: m/s²
     * Scale: 0.01
     * Min: -5
     * Max: 5
     */
    int16_t currentAccelerationRequestedToActuators;
    /** UsedActuator */
    SystemCore_Crusing_UsedActuator usedActuator;
    /** LaneChangeIndicatedByDriver */
    SystemCore_Crusing_LateralDirection laneChangeIndicatedByDriver;
    /** OvertakeBoostRequestedByDriver */
    bool overtakeBoostRequestedByDriver;
    /** HeavyRain
     * Used to lower acceleration request range from controller, previous OEMs used windshield wiper speed higher than threshold
     */
    bool heavyRain;
} SystemCore_Crusing_DistanceControllerInput;

typedef struct _SystemCore_Crusing_IndicatedSpeed {
    /** Speed
     * Indicated speed seen by driver, needed for no lead vehicle cancel condition in ACC
     * Unit: See enum unit
     * Min: 0
     * Max: 250
     */
    uint8_t speed;
    /** Unit */
    SystemCore_Crusing_SpeedUnit unit;
} SystemCore_Crusing_IndicatedSpeed;

typedef struct _SystemCore_Crusing_SetSpeedControllerInput {
    /** SetSpeed
     * Set speed for set speed controller to follow
     * Unit: m/s
     * Scale: 0.1
     * Min: 7
     * Max: 60
     */
    uint16_t setSpeed;
    /** SetSpeedChangedBy */
    SystemCore_Crusing_ChangedBy setSpeedChangedBy;
} SystemCore_Crusing_SetSpeedControllerInput;

typedef struct _SystemCore_Crusing_AccCommonInput {
    /** DriverOverride */
    bool driverOverride;
    /** DriveMode */
    SystemCore_Crusing_AccDriveMode driveMode;
    /** RoadInclination
     * Road inclination
     * Unit: radians
     * Scale: 0.005
     * Min: -1
     * Max: 1
     */
    int32_t roadInclination;
    /** StandstillStatus */
    SystemCore_Crusing_StandstillStatus standstillStatus;
    /** IndicatedSpeed */
    SystemCore_Crusing_IndicatedSpeed indicatedSpeed;
} SystemCore_Crusing_AccCommonInput;

/* Struct field encoding specification for pb */
extern const pb_field_t SystemCore_Crusing_IndicatedSpeed_fields[3];
extern const pb_field_t SystemCore_Crusing_AccCommonInput_fields[6];
extern const pb_field_t SystemCore_Crusing_SetSpeedControllerInput_fields[3];
extern const pb_field_t SystemCore_Crusing_CruisingFeatureState_fields[4];
extern const pb_field_t SystemCore_Crusing_DistanceControllerInput_fields[7];
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_CRUISING_CRUISING_INCLUDED */
