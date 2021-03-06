/* Automatically generated Extension Support header */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#ifndef SUPPORT_VISIONCORE_COMMON_EGOMOTION_INCLUDED
#define SUPPORT_VISIONCORE_COMMON_EGOMOTION_INCLUDED

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Conversion functions */
float VisionCore_Common_EgoMotionOutput_longitudinalVelocityToFloat(const int16_t value);
int16_t VisionCore_Common_EgoMotionOutput_floatToLongitudinalVelocity(const float value);
float VisionCore_Common_EgoMotionOutput_longitudinalAccelerationToFloat(const int16_t value);
int16_t VisionCore_Common_EgoMotionOutput_floatToLongitudinalAcceleration(const float value);
float VisionCore_Common_EgoMotionOutput_lateralVelocityToFloat(const int16_t value);
int16_t VisionCore_Common_EgoMotionOutput_floatToLateralVelocity(const float value);
float VisionCore_Common_EgoMotionOutput_lateralAccelerationToFloat(const int16_t value);
int16_t VisionCore_Common_EgoMotionOutput_floatToLateralAcceleration(const float value);
float VisionCore_Common_EgoMotionOutput_yawRateToFloat(const int16_t value);
int16_t VisionCore_Common_EgoMotionOutput_floatToYawRate(const float value);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SUPPORT_VISIONCORE_COMMON_EGOMOTION_INCLUDED */
