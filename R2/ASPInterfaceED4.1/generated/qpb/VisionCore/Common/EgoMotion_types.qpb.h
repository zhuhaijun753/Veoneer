/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef VISIONCORE_COMMON_EGOMOTION_TYPES_INCLUDED
#define VISIONCORE_COMMON_EGOMOTION_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _VisionCore_Common_EgoMotionGateKeeperStatus {
    VisionCore_Common_EgoMotionGateKeeperStatus_Unknown = 0,
    VisionCore_Common_EgoMotionGateKeeperStatus_SuccessfulVerification = 1,
    VisionCore_Common_EgoMotionGateKeeperStatus_VerificationFailed = 2
} VisionCore_Common_EgoMotionGateKeeperStatus;
#define VisionCore_Common_EgoMotionGateKeeperStatus_MIN VisionCore_Common_EgoMotionGateKeeperStatus_Unknown
#define VisionCore_Common_EgoMotionGateKeeperStatus_MAX VisionCore_Common_EgoMotionGateKeeperStatus_VerificationFailed
#define VisionCore_Common_EgoMotionGateKeeperStatus_ARRAYSIZE ((VisionCore_Common_EgoMotionGateKeeperStatus)(VisionCore_Common_EgoMotionGateKeeperStatus_VerificationFailed+1))

/* Struct definitions */
typedef struct _VisionCore_Common_EgoMotionOutput_Raw {
    /** LongitudinalVelocity
     * Longitudinal velocity i.e. speed along the X-axis in AFAC
     * Unit: m/s
     * Scale: 0.01
     * Min: -30
     * Max: 120
     */
    int16_t longitudinalVelocity;
    /** LongitudinalAcceleration
     * Longitudinal acceleration i.e. velocity change along the X-axis in AFAC
     * Unit: m/s²
     * Scale: 0.01
     * Min: -20
     * Max: 20
     */
    int16_t longitudinalAcceleration;
    /** LateralVelocity
     * Lateral velocity i.e. speed along the Y-axis in AFAC
     * Unit: m/s
     * Scale: 0.01
     * Min: -30
     * Max: 30
     */
    int16_t lateralVelocity;
    /** LateralAcceleration
     * Lateral acceleration i.e. velocity change along the Y-axis in AFAC
     * Unit: m/s²
     * Scale: 0.01
     * Min: -20
     * Max: 20
     */
    int16_t lateralAcceleration;
    /** YawRate
     * Rotational speed around the Z-axis in AFAC
     * Unit: rad/s
     * Scale: 0.0001
     * Min: -1.5
     * Max: 1.5
     */
    int16_t yawRate;
    /** IsAvailable
     * Is data contained in the message available or is it just dummy data
     */
    bool isAvailable;
    /** Timestamp
     * The time-stamp for the current frame
     * Unit: ?
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t timestamp;
    /** LongitudinalVelocityStatus
     * Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for longitudinal speed
     */
    VisionCore_Common_EgoMotionGateKeeperStatus longitudinalVelocityStatus;
    /** AccelerationStatus
     * Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for acceleration
     */
    VisionCore_Common_EgoMotionGateKeeperStatus accelerationStatus;
    /** YawRateStatus
     * Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for yaw rate
     */
    VisionCore_Common_EgoMotionGateKeeperStatus yawRateStatus;
} VisionCore_Common_EgoMotionOutput_Raw;

typedef struct _VisionCore_Common_EgoMotionOutput {
    /** LongitudinalVelocity
     * Longitudinal velocity i.e. speed along the X-axis in AFAC
     * Unit: m/s
     * Resolution: 0.01
     * Min: -30
     * Max: 120
     */
    float longitudinalVelocity;
    /** LongitudinalAcceleration
     * Longitudinal acceleration i.e. velocity change along the X-axis in AFAC
     * Unit: m/s²
     * Resolution: 0.01
     * Min: -20
     * Max: 20
     */
    float longitudinalAcceleration;
    /** LateralVelocity
     * Lateral velocity i.e. speed along the Y-axis in AFAC
     * Unit: m/s
     * Resolution: 0.01
     * Min: -30
     * Max: 30
     */
    float lateralVelocity;
    /** LateralAcceleration
     * Lateral acceleration i.e. velocity change along the Y-axis in AFAC
     * Unit: m/s²
     * Resolution: 0.01
     * Min: -20
     * Max: 20
     */
    float lateralAcceleration;
    /** YawRate
     * Rotational speed around the Z-axis in AFAC
     * Unit: rad/s
     * Resolution: 0.0001
     * Min: -1.5
     * Max: 1.5
     */
    float yawRate;
    /** IsAvailable
     * Is data contained in the message available or is it just dummy data
     */
    bool isAvailable;
    /** Timestamp
     * The time-stamp for the current frame
     * Unit: ?
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t timestamp;
    /** LongitudinalVelocityStatus
     * Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for longitudinal speed
     */
    VisionCore_Common_EgoMotionGateKeeperStatus longitudinalVelocityStatus;
    /** AccelerationStatus
     * Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for acceleration
     */
    VisionCore_Common_EgoMotionGateKeeperStatus accelerationStatus;
    /** YawRateStatus
     * Indication for if the QM and ASIL B estimations differ too much in the gatekeeper function within EM for yaw rate
     */
    VisionCore_Common_EgoMotionGateKeeperStatus yawRateStatus;
} VisionCore_Common_EgoMotionOutput;

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* VISIONCORE_COMMON_EGOMOTION_TYPES_INCLUDED */