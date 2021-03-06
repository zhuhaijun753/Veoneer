/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_LONGITUDINALVEHICLECONTROLOUTPUT_TYPES_INCLUDED
#define ZENUITY_LONGITUDINALVEHICLECONTROLOUTPUT_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController {
    Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_ActuatorNotEnabledForControl = 0,
    Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_PropulsionActuatorEnabledForControl = 1,
    Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_BrakeActuatorEnabledForControl = 2
} Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController;
#define Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_MIN Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_ActuatorNotEnabledForControl
#define Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_MAX Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_BrakeActuatorEnabledForControl
#define Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_ARRAYSIZE ((Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController)(Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController_BrakeActuatorEnabledForControl+1))

/* Struct definitions */
typedef struct _Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw {
    /** DriverAwayReleaseRequestToBrake
     * Request for drive away, if true drive away is requested
     */
    bool driverAwayReleaseRequestToBrake;
    /** HoldRequestToBrake
     * Request to stand still, if true, stand still is requested
     */
    bool holdRequestToBrake;
    /** ParkRequestFromVehMtnControl
     * Request to park vehicle, if true, request is active
     */
    bool parkRequestFromVehMtnControl;
    /** BrakeAccelerationRequest
     * Acceleration request to brake
     * Unit: m/s²
     * Min: -5.12
     * Max: 5.11
     */
    int16_t brakeAccelerationRequest;
    /** LatestActiveAccelerationRequest
     * Informs which the intended acceleration of the actuators is at the moment, includes rate limitation, internal feedback
     * Unit: m/s²
     * Min: -5.12
     * Max: 5.11
     */
    int16_t latestActiveAccelerationRequest;
    /** ActutorActiveForLgtController
     * Informs which actuator that’s primarily active for speed control, none, powertrain or brake, internal feedback
     */
    Zenuity_LongitudinalVehicleControl_ActuatorActiveForLgtController actutorActiveForLgtController;
    /** PropulsionTorqueNegativeGradient
     * None rate limited torque request to Powertrain
     * Unit: Nm/s²
     * Min: -2.14748e+09
     * Max: 2.14748e+09
     */
    int32_t propulsionTorqueNegativeGradient;
    /** PropulstionTorquePositiveGradient
     * Negative rate limit to powertrain torque
     * Unit: Nm/s²
     * Min: -2.14748e+09
     * Max: 2.14748e+09
     */
    int32_t propulstionTorquePositiveGradient;
    /** PropulsionTorqueRequest
     * Positive rate limit to powertrain torque
     * Unit: Nm
     * Min: -2.14748e+09
     * Max: 2.14748e+09
     */
    int32_t propulsionTorqueRequest;
    /** LcpHealthStatus
     * FaultManagement event output from LCP for the HealthStatus reporting.  True if LCP Health Status is OK, otherwise false.
     */
    bool lcpHealthStatus;
} Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw;

#define Zenuity_LongitudinalVehicleControl_StopAndGoRequests Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_LONGITUDINALVEHICLECONTROLOUTPUT_TYPES_INCLUDED */
