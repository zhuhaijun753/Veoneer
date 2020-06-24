/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef SYSTEMCORE_CRUISING_CRUISINGINPUT_TYPES_INCLUDED
#define SYSTEMCORE_CRUISING_CRUISINGINPUT_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _SystemCore_Cruising_LateralDirection {
    SystemCore_Cruising_LateralDirection_None = 0,
    SystemCore_Cruising_LateralDirection_Left = 1,
    SystemCore_Cruising_LateralDirection_Right = 2
} SystemCore_Cruising_LateralDirection;
#define SystemCore_Cruising_LateralDirection_MIN SystemCore_Cruising_LateralDirection_None
#define SystemCore_Cruising_LateralDirection_MAX SystemCore_Cruising_LateralDirection_Right
#define SystemCore_Cruising_LateralDirection_ARRAYSIZE ((SystemCore_Cruising_LateralDirection)(SystemCore_Cruising_LateralDirection_Right+1))

typedef enum _SystemCore_Cruising_RmsStatus {
    SystemCore_Cruising_RmsStatus_Off = 0,
    SystemCore_Cruising_RmsStatus_Standby = 1,
    SystemCore_Cruising_RmsStatus_Level1 = 2,
    SystemCore_Cruising_RmsStatus_Level2 = 3,
    SystemCore_Cruising_RmsStatus_Level3 = 4,
    SystemCore_Cruising_RmsStatus_Level4 = 5,
    SystemCore_Cruising_RmsStatus_Level5 = 6,
    SystemCore_Cruising_RmsStatus_Level6 = 7,
    SystemCore_Cruising_RmsStatus_Level7 = 8,
    SystemCore_Cruising_RmsStatus_Level8 = 9
} SystemCore_Cruising_RmsStatus;
#define SystemCore_Cruising_RmsStatus_MIN SystemCore_Cruising_RmsStatus_Off
#define SystemCore_Cruising_RmsStatus_MAX SystemCore_Cruising_RmsStatus_Level8
#define SystemCore_Cruising_RmsStatus_ARRAYSIZE ((SystemCore_Cruising_RmsStatus)(SystemCore_Cruising_RmsStatus_Level8+1))

/* Struct definitions */
typedef struct _SystemCore_Cruising_DriverAlertControlInput_Raw {
    /** DacActivated
     * Indicates that Driver Alert Control is activated from HMI.
     */
    bool dacActivated;
} SystemCore_Cruising_DriverAlertControlInput_Raw;

#define SystemCore_Cruising_DriverAlertControlInput SystemCore_Cruising_DriverAlertControlInput_Raw

typedef struct _SystemCore_Cruising_LaneChangeAssistInput_Raw {
    /** Enable
     * Platform ok to enable Lane Change Assist.All criteria are met for Lane Change Assistto go from Off to Standby.
     */
    bool enable;
    /** LaneChangeRequestByDriver */
    SystemCore_Cruising_LateralDirection laneChangeRequestByDriver;
    /** LaneChangeAbortRequestByDriver
     * Lane change aborted by driver specified in R79
     */
    bool laneChangeAbortRequestByDriver;
    /** RearRadarDetectionRange
     * The current radial detection range of the rear radars
     * Unit: m
     * Min: 0
     * Max: 255
     */
    uint8_t rearRadarDetectionRange;
} SystemCore_Cruising_LaneChangeAssistInput_Raw;

#define SystemCore_Cruising_LaneChangeAssistInput SystemCore_Cruising_LaneChangeAssistInput_Raw

typedef struct _SystemCore_Cruising_RiskMitigationSupportInput_Raw {
    /** RmsStatus
     * Information if RMS is off, standby or requested intervention level
     */
    SystemCore_Cruising_RmsStatus rmsStatus;
} SystemCore_Cruising_RiskMitigationSupportInput_Raw;

#define SystemCore_Cruising_RiskMitigationSupportInput SystemCore_Cruising_RiskMitigationSupportInput_Raw

typedef struct _SystemCore_Cruising_TrafficAssistInput_Raw {
    /** Enable
     * Platform ok to enable Traffic Assist.All criteria are met for Traffic Assistto go from Off to Standby.
     */
    bool enable;
    /** SteeringEnabled
     * Request steering support from Traffic Assist.
     */
    bool steeringEnabled;
    /** DriverInTheLoopDetected
     * Driver confirmed to be in control of vehicle during Traffic Assist steering support. Detection might be done by DMC, steering wheel sensor or any other suitable method. driver_in_the_loop_detected has to be true often enough to not cause Hands Off warnings or maneuver aborts.
     */
    bool driverInTheLoopDetected;
    /** TrafficAssistIsSteering
     * TA steering confirmed by platform.
     */
    bool trafficAssistIsSteering;
} SystemCore_Cruising_TrafficAssistInput_Raw;

#define SystemCore_Cruising_TrafficAssistInput SystemCore_Cruising_TrafficAssistInput_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_CRUISING_CRUISINGINPUT_TYPES_INCLUDED */