/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_CRUISING_TYPES_INCLUDED
#define ZENUITY_CRUISING_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _Zenuity_Crusing_TurnIndicatorRequest {
    Zenuity_Crusing_TurnIndicatorRequest_None = 0,
    Zenuity_Crusing_TurnIndicatorRequest_Left = 1,
    Zenuity_Crusing_TurnIndicatorRequest_Right = 2,
    Zenuity_Crusing_TurnIndicatorRequest_HazardLight = 3
} Zenuity_Crusing_TurnIndicatorRequest;
#define Zenuity_Crusing_TurnIndicatorRequest_MIN Zenuity_Crusing_TurnIndicatorRequest_None
#define Zenuity_Crusing_TurnIndicatorRequest_MAX Zenuity_Crusing_TurnIndicatorRequest_HazardLight
#define Zenuity_Crusing_TurnIndicatorRequest_ARRAYSIZE ((Zenuity_Crusing_TurnIndicatorRequest)(Zenuity_Crusing_TurnIndicatorRequest_HazardLight+1))

typedef enum _Zenuity_Crusing_LaneChangeType {
    Zenuity_Crusing_LaneChangeType_NoIntent = 0,
    Zenuity_Crusing_LaneChangeType_Left = 1,
    Zenuity_Crusing_LaneChangeType_Right = 2
} Zenuity_Crusing_LaneChangeType;
#define Zenuity_Crusing_LaneChangeType_MIN Zenuity_Crusing_LaneChangeType_NoIntent
#define Zenuity_Crusing_LaneChangeType_MAX Zenuity_Crusing_LaneChangeType_Right
#define Zenuity_Crusing_LaneChangeType_ARRAYSIZE ((Zenuity_Crusing_LaneChangeType)(Zenuity_Crusing_LaneChangeType_Right+1))

typedef enum _Zenuity_Crusing_LaneChangeReason {
    Zenuity_Crusing_LaneChangeReason_NoReason = 0,
    Zenuity_Crusing_LaneChangeReason_DeniedByDriver = 1,
    Zenuity_Crusing_LaneChangeReason_LaneOccupied = 2,
    Zenuity_Crusing_LaneChangeReason_NoTargetLane = 3,
    Zenuity_Crusing_LaneChangeReason_TargetLaneNotAccessible = 4,
    Zenuity_Crusing_LaneChangeReason_SpeedRange = 5,
    Zenuity_Crusing_LaneChangeReason_SensorBlocked = 6,
    Zenuity_Crusing_LaneChangeReason_SystemFailure = 7,
    Zenuity_Crusing_LaneChangeReason_SteeringNotActive = 8,
    Zenuity_Crusing_LaneChangeReason_DriverNotAttentive = 9,
    Zenuity_Crusing_LaneChangeReason_DriverOverride = 10,
    Zenuity_Crusing_LaneChangeReason_RoadType = 11,
    Zenuity_Crusing_LaneChangeReason_RoadTypeNotDetermined = 12,
    Zenuity_Crusing_LaneChangeReason_Unknown = 13
} Zenuity_Crusing_LaneChangeReason;
#define Zenuity_Crusing_LaneChangeReason_MIN Zenuity_Crusing_LaneChangeReason_NoReason
#define Zenuity_Crusing_LaneChangeReason_MAX Zenuity_Crusing_LaneChangeReason_Unknown
#define Zenuity_Crusing_LaneChangeReason_ARRAYSIZE ((Zenuity_Crusing_LaneChangeReason)(Zenuity_Crusing_LaneChangeReason_Unknown+1))

typedef enum _Zenuity_Crusing_LaneChangePossibleDirection {
    Zenuity_Crusing_LaneChangePossibleDirection_None = 0,
    Zenuity_Crusing_LaneChangePossibleDirection_Left = 1,
    Zenuity_Crusing_LaneChangePossibleDirection_Right = 2,
    Zenuity_Crusing_LaneChangePossibleDirection_Both = 3
} Zenuity_Crusing_LaneChangePossibleDirection;
#define Zenuity_Crusing_LaneChangePossibleDirection_MIN Zenuity_Crusing_LaneChangePossibleDirection_None
#define Zenuity_Crusing_LaneChangePossibleDirection_MAX Zenuity_Crusing_LaneChangePossibleDirection_Both
#define Zenuity_Crusing_LaneChangePossibleDirection_ARRAYSIZE ((Zenuity_Crusing_LaneChangePossibleDirection)(Zenuity_Crusing_LaneChangePossibleDirection_Both+1))

typedef enum _Zenuity_Crusing_LaneChangeStatus {
    Zenuity_Crusing_LaneChangeStatus_Off = 0,
    Zenuity_Crusing_LaneChangeStatus_Standby = 1,
    Zenuity_Crusing_LaneChangeStatus_Requested = 2,
    Zenuity_Crusing_LaneChangeStatus_LateralManeuverStarted = 3,
    Zenuity_Crusing_LaneChangeStatus_InLateralManeuver = 4,
    Zenuity_Crusing_LaneChangeStatus_Finished = 5,
    Zenuity_Crusing_LaneChangeStatus_Rejected = 6,
    Zenuity_Crusing_LaneChangeStatus_Aborting = 7,
    Zenuity_Crusing_LaneChangeStatus_HandOver = 8
} Zenuity_Crusing_LaneChangeStatus;
#define Zenuity_Crusing_LaneChangeStatus_MIN Zenuity_Crusing_LaneChangeStatus_Off
#define Zenuity_Crusing_LaneChangeStatus_MAX Zenuity_Crusing_LaneChangeStatus_HandOver
#define Zenuity_Crusing_LaneChangeStatus_ARRAYSIZE ((Zenuity_Crusing_LaneChangeStatus)(Zenuity_Crusing_LaneChangeStatus_HandOver+1))

typedef enum _Zenuity_Crusing_HandsOffWarning {
    Zenuity_Crusing_HandsOffWarning_NoWarning = 0,
    Zenuity_Crusing_HandsOffWarning_WarningLevel1 = 1,
    Zenuity_Crusing_HandsOffWarning_WarningLevel2 = 2
} Zenuity_Crusing_HandsOffWarning;
#define Zenuity_Crusing_HandsOffWarning_MIN Zenuity_Crusing_HandsOffWarning_NoWarning
#define Zenuity_Crusing_HandsOffWarning_MAX Zenuity_Crusing_HandsOffWarning_WarningLevel2
#define Zenuity_Crusing_HandsOffWarning_ARRAYSIZE ((Zenuity_Crusing_HandsOffWarning)(Zenuity_Crusing_HandsOffWarning_WarningLevel2+1))

/* Struct definitions */
typedef struct _Zenuity_Crusing_AccelerationRequest_Raw {
    /** RequestActive */
    bool requestActive;
    /** NominalAcceleration
     * Current acceleration request
     * Unit: m/s²
     * Scale: 0.01
     * Min: -5
     * Max: 5
     */
    int16_t nominalAcceleration;
    /** MinJerk
     * Request from controller to use no less than this jerk to reach requested acceleration.
     * Unit: m/s³
     * Scale: 0.01
     * Min: -5
     * Max: 5
     */
    int16_t minJerk;
    /** MaxJerk
     * Request from controller to use no more than this jerk to reach requested acceleration.
     * Unit: m/s³
     * Scale: 0.01
     * Min: -5
     * Max: 5
     */
    int16_t maxJerk;
    /** StandstillRequest
     * Request by ACC to stop vehicle and hold it still with brakes
     */
    bool standstillRequest;
} Zenuity_Crusing_AccelerationRequest_Raw;

typedef struct _Zenuity_Crusing_AccelerationRequest {
    /** RequestActive */
    bool requestActive;
    /** NominalAcceleration
     * Current acceleration request
     * Unit: m/s²
     * Resolution: 0.01
     * Min: -5
     * Max: 5
     */
    float nominalAcceleration;
    /** MinJerk
     * Request from controller to use no less than this jerk to reach requested acceleration.
     * Unit: m/s³
     * Resolution: 0.01
     * Min: -5
     * Max: 5
     */
    float minJerk;
    /** MaxJerk
     * Request from controller to use no more than this jerk to reach requested acceleration.
     * Unit: m/s³
     * Resolution: 0.01
     * Min: -5
     * Max: 5
     */
    float maxJerk;
    /** StandstillRequest
     * Request by ACC to stop vehicle and hold it still with brakes
     */
    bool standstillRequest;
} Zenuity_Crusing_AccelerationRequest;

typedef struct _Zenuity_Crusing_CancelReasonAcc_Raw {
    /** NoLeadVehicle */
    bool noLeadVehicle;
    /** EndBrakeOnly */
    bool endBrakeOnly;
} Zenuity_Crusing_CancelReasonAcc_Raw;

#define Zenuity_Crusing_CancelReasonAcc Zenuity_Crusing_CancelReasonAcc_Raw

typedef struct _Zenuity_Crusing_InformationToDriverFromTrafficAssist_Raw {
    /** HandsOffWarning */
    Zenuity_Crusing_HandsOffWarning handsOffWarning;
    /** LaneChangeType */
    Zenuity_Crusing_LaneChangeType laneChangeType;
    /** LaneChangeReason */
    Zenuity_Crusing_LaneChangeReason laneChangeReason;
    /** LaneChangePossibleDirection */
    Zenuity_Crusing_LaneChangePossibleDirection laneChangePossibleDirection;
    /** LaneChangeStatus */
    Zenuity_Crusing_LaneChangeStatus laneChangeStatus;
} Zenuity_Crusing_InformationToDriverFromTrafficAssist_Raw;

#define Zenuity_Crusing_InformationToDriverFromTrafficAssist Zenuity_Crusing_InformationToDriverFromTrafficAssist_Raw

typedef struct _Zenuity_Crusing_SelectedTarget_Raw {
    /** IsSelected */
    bool isSelected;
    /** IsControlledTowards */
    bool isControlledTowards;
    /** LatPosition
     * Lateral distance to selected target, ego vehicle coordinate system.
     * Unit: m
     * Scale: 0.1
     * Min: -20
     * Max: 20
     */
    int16_t latPosition;
    /** LonPosition
     * Longitudinal distance to selected target, ego vehicle coordinate system.
     * Unit: m
     * Scale: 0.1
     * Min: -3276.8
     * Max: 200
     */
    int16_t lonPosition;
    /** Speed
     * Speed of selected target.
     * Unit: m/s
     * Scale: 0.1
     * Min: -3276.8
     * Max: 60
     */
    int16_t speed;
} Zenuity_Crusing_SelectedTarget_Raw;

typedef struct _Zenuity_Crusing_SelectedTarget {
    /** IsSelected */
    bool isSelected;
    /** IsControlledTowards */
    bool isControlledTowards;
    /** LatPosition
     * Lateral distance to selected target, ego vehicle coordinate system.
     * Unit: m
     * Resolution: 0.1
     * Min: -20
     * Max: 20
     */
    float latPosition;
    /** LonPosition
     * Longitudinal distance to selected target, ego vehicle coordinate system.
     * Unit: m
     * Resolution: 0.1
     * Min: -3276.8
     * Max: 200
     */
    float lonPosition;
    /** Speed
     * Speed of selected target.
     * Unit: m/s
     * Resolution: 0.1
     * Min: -3276.8
     * Max: 60
     */
    float speed;
} Zenuity_Crusing_SelectedTarget;

typedef struct _Zenuity_Crusing_TrafficAssistOutput_Raw {
    /** TurnIndicatorRequest */
    Zenuity_Crusing_TurnIndicatorRequest turnIndicatorRequest;
} Zenuity_Crusing_TrafficAssistOutput_Raw;

#define Zenuity_Crusing_TrafficAssistOutput Zenuity_Crusing_TrafficAssistOutput_Raw

typedef struct _Zenuity_Crusing_TargetsSelectedByAcc_Raw {
    /** ClosestInLane */
    Zenuity_Crusing_SelectedTarget_Raw closestInLane;
    /** SecondClosestInLane */
    Zenuity_Crusing_SelectedTarget_Raw secondClosestInLane;
    /** CutIn */
    Zenuity_Crusing_SelectedTarget_Raw cutIn;
    /** ClosestInLeftLane */
    Zenuity_Crusing_SelectedTarget_Raw closestInLeftLane;
    /** ClosestInRightLane */
    Zenuity_Crusing_SelectedTarget_Raw closestInRightLane;
} Zenuity_Crusing_TargetsSelectedByAcc_Raw;

typedef struct _Zenuity_Crusing_TargetsSelectedByAcc {
    /** ClosestInLane */
    Zenuity_Crusing_SelectedTarget closestInLane;
    /** SecondClosestInLane */
    Zenuity_Crusing_SelectedTarget secondClosestInLane;
    /** CutIn */
    Zenuity_Crusing_SelectedTarget cutIn;
    /** ClosestInLeftLane */
    Zenuity_Crusing_SelectedTarget closestInLeftLane;
    /** ClosestInRightLane */
    Zenuity_Crusing_SelectedTarget closestInRightLane;
} Zenuity_Crusing_TargetsSelectedByAcc;

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_CRUISING_TYPES_INCLUDED */
