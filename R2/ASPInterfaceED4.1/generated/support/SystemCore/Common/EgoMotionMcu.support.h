/* Automatically generated Extension Support header */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#ifndef SUPPORT_SYSTEMCORE_COMMON_EGOMOTIONMCU_INCLUDED
#define SUPPORT_SYSTEMCORE_COMMON_EGOMOTIONMCU_INCLUDED

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Conversion functions */
float SystemCore_Common_EgoMotionMcuOutput_longitudinalVelocityToFloat(const int16_t value);
int16_t SystemCore_Common_EgoMotionMcuOutput_floatToLongitudinalVelocity(const float value);
float SystemCore_Common_EgoMotionMcuOutput_longitudinalAccelerationToFloat(const int16_t value);
int16_t SystemCore_Common_EgoMotionMcuOutput_floatToLongitudinalAcceleration(const float value);
float SystemCore_Common_EgoMotionMcuOutput_lateralVelocityToFloat(const int16_t value);
int16_t SystemCore_Common_EgoMotionMcuOutput_floatToLateralVelocity(const float value);
float SystemCore_Common_EgoMotionMcuOutput_lateralAccelerationToFloat(const int16_t value);
int16_t SystemCore_Common_EgoMotionMcuOutput_floatToLateralAcceleration(const float value);
float SystemCore_Common_EgoMotionMcuOutput_yawRateToFloat(const int16_t value);
int16_t SystemCore_Common_EgoMotionMcuOutput_floatToYawRate(const float value);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SUPPORT_SYSTEMCORE_COMMON_EGOMOTIONMCU_INCLUDED */
