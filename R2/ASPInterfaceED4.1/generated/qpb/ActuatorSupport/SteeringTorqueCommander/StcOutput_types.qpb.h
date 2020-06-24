/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCOUTPUT_TYPES_INCLUDED
#define ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCOUTPUT_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited {
    ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_NoLimit = 0,
    ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_MagnitudeLimitActivated = 1,
    ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_RateLimitActivated = 2,
    ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_MagnitudeAndRateLimitActivated = 3
} ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited;
#define ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_MIN ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_NoLimit
#define ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_MAX ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_MagnitudeAndRateLimitActivated
#define ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_ARRAYSIZE ((ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited)(ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited_MagnitudeAndRateLimitActivated+1))

typedef enum _ActuatorSupport_SteeringTorqueCommander_ControlState {
    ActuatorSupport_SteeringTorqueCommander_ControlState_Disabled = 0,
    ActuatorSupport_SteeringTorqueCommander_ControlState_Active = 1,
    ActuatorSupport_SteeringTorqueCommander_ControlState_Inactive = 2,
    ActuatorSupport_SteeringTorqueCommander_ControlState_Ramping = 3
} ActuatorSupport_SteeringTorqueCommander_ControlState;
#define ActuatorSupport_SteeringTorqueCommander_ControlState_MIN ActuatorSupport_SteeringTorqueCommander_ControlState_Disabled
#define ActuatorSupport_SteeringTorqueCommander_ControlState_MAX ActuatorSupport_SteeringTorqueCommander_ControlState_Ramping
#define ActuatorSupport_SteeringTorqueCommander_ControlState_ARRAYSIZE ((ActuatorSupport_SteeringTorqueCommander_ControlState)(ActuatorSupport_SteeringTorqueCommander_ControlState_Ramping+1))

/* Struct definitions */
typedef struct _ActuatorSupport_SteeringTorqueCommander_StcOutput_Raw {
    /** SteeringWheelTorqueRequest
     * Magnitude of Overlay Steering torque commanded to vehicle for lateral control
     * Unit: Nm
     * Scale: 0.01
     * Min: -20
     * Max: 20
     */
    int16_t steeringWheelTorqueRequest;
    /** SteeringWheelTorqueActive
     * Flag indicating if the Overlay Steering Torque Control is Active and that the torque request can be used for actuation
     */
    bool steeringWheelTorqueActive;
    /** SteeringWheelControlLimited
     * Signal indicating if Overlay Steering Torque command is limited by magnitude and/or rate
     */
    ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited steeringWheelControlLimited;
    /** SteeringWheelTorqueRatio
     * Ratio of Overlay Steering torque to total torque observed by the vehicle steering system
     * Scale: 0.005
     * Min: 0
     * Max: 1
     */
    uint16_t steeringWheelTorqueRatio;
    /** SteeringWheelTorqueControlState
     * Signal indicating operating state of the Steering Torque Controller
     */
    ActuatorSupport_SteeringTorqueCommander_ControlState steeringWheelTorqueControlState;
} ActuatorSupport_SteeringTorqueCommander_StcOutput_Raw;

typedef struct _ActuatorSupport_SteeringTorqueCommander_StcOutput {
    /** SteeringWheelTorqueRequest
     * Magnitude of Overlay Steering torque commanded to vehicle for lateral control
     * Unit: Nm
     * Resolution: 0.01
     * Min: -20
     * Max: 20
     */
    float steeringWheelTorqueRequest;
    /** SteeringWheelTorqueActive
     * Flag indicating if the Overlay Steering Torque Control is Active and that the torque request can be used for actuation
     */
    bool steeringWheelTorqueActive;
    /** SteeringWheelControlLimited
     * Signal indicating if Overlay Steering Torque command is limited by magnitude and/or rate
     */
    ActuatorSupport_SteeringTorqueCommander_SteeringWheelTorqueLimited steeringWheelControlLimited;
    /** SteeringWheelTorqueRatio
     * Ratio of Overlay Steering torque to total torque observed by the vehicle steering system
     * Resolution: 0.005
     * Min: 0
     * Max: 1
     */
    float steeringWheelTorqueRatio;
    /** SteeringWheelTorqueControlState
     * Signal indicating operating state of the Steering Torque Controller
     */
    ActuatorSupport_SteeringTorqueCommander_ControlState steeringWheelTorqueControlState;
} ActuatorSupport_SteeringTorqueCommander_StcOutput;

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCOUTPUT_TYPES_INCLUDED */