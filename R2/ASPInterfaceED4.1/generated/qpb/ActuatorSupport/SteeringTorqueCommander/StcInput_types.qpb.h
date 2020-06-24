/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCINPUT_TYPES_INCLUDED
#define ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCINPUT_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _ActuatorSupport_SteeringTorqueCommander_DrivingMode {
    ActuatorSupport_SteeringTorqueCommander_DrivingMode_Unknown = 0,
    ActuatorSupport_SteeringTorqueCommander_DrivingMode_Standard = 1,
    ActuatorSupport_SteeringTorqueCommander_DrivingMode_Comfort = 2,
    ActuatorSupport_SteeringTorqueCommander_DrivingMode_Sport = 3
} ActuatorSupport_SteeringTorqueCommander_DrivingMode;
#define ActuatorSupport_SteeringTorqueCommander_DrivingMode_MIN ActuatorSupport_SteeringTorqueCommander_DrivingMode_Unknown
#define ActuatorSupport_SteeringTorqueCommander_DrivingMode_MAX ActuatorSupport_SteeringTorqueCommander_DrivingMode_Sport
#define ActuatorSupport_SteeringTorqueCommander_DrivingMode_ARRAYSIZE ((ActuatorSupport_SteeringTorqueCommander_DrivingMode)(ActuatorSupport_SteeringTorqueCommander_DrivingMode_Sport+1))

/* Struct definitions */
typedef struct _ActuatorSupport_SteeringTorqueCommander_StcInput_Raw {
    /** PinionAngleRequest
     * Steering Angle command input to the STC
     * Unit: rad
     * Scale: 0.01
     * Min: -15
     * Max: 15
     */
    int16_t pinionAngleRequest;
    /** PinionAngleFeedback
     * Steering Angle feedback input measurement from the vehicle
     * Unit: rad
     * Scale: 0.01
     * Min: -15
     * Max: 15
     */
    int16_t pinionAngleFeedback;
    /** SteeringWheelTorqueFeedback
     * Steering Torque feedback input measurement from the vehicle
     * Unit: Nm
     * Scale: 0.01
     * Min: -20
     * Max: 20
     */
    int16_t steeringWheelTorqueFeedback;
    /** LongitudinalSpeed
     * Vehicle Longitudinal speed input measurement from the vehicle
     * Unit: m/s
     * Scale: 0.01
     * Min: -30
     * Max: 120
     */
    int16_t longitudinalSpeed;
    /** SteeringControlEnabled
     * Flag input indicating if Overlay Steering Torque control is requested by the vehicle
     */
    bool steeringControlEnabled;
    /** DrivingMode
     * Driving mode input from vehicle
     */
    ActuatorSupport_SteeringTorqueCommander_DrivingMode drivingMode;
    /** SystemFault
     * Flag indicating if a system fault has been detected
     */
    bool systemFault;
} ActuatorSupport_SteeringTorqueCommander_StcInput_Raw;

typedef struct _ActuatorSupport_SteeringTorqueCommander_StcInput {
    /** PinionAngleRequest
     * Steering Angle command input to the STC
     * Unit: rad
     * Resolution: 0.01
     * Min: -15
     * Max: 15
     */
    float pinionAngleRequest;
    /** PinionAngleFeedback
     * Steering Angle feedback input measurement from the vehicle
     * Unit: rad
     * Resolution: 0.01
     * Min: -15
     * Max: 15
     */
    float pinionAngleFeedback;
    /** SteeringWheelTorqueFeedback
     * Steering Torque feedback input measurement from the vehicle
     * Unit: Nm
     * Resolution: 0.01
     * Min: -20
     * Max: 20
     */
    float steeringWheelTorqueFeedback;
    /** LongitudinalSpeed
     * Vehicle Longitudinal speed input measurement from the vehicle
     * Unit: m/s
     * Resolution: 0.01
     * Min: -30
     * Max: 120
     */
    float longitudinalSpeed;
    /** SteeringControlEnabled
     * Flag input indicating if Overlay Steering Torque control is requested by the vehicle
     */
    bool steeringControlEnabled;
    /** DrivingMode
     * Driving mode input from vehicle
     */
    ActuatorSupport_SteeringTorqueCommander_DrivingMode drivingMode;
    /** SystemFault
     * Flag indicating if a system fault has been detected
     */
    bool systemFault;
} ActuatorSupport_SteeringTorqueCommander_StcInput;

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCINPUT_TYPES_INCLUDED */
