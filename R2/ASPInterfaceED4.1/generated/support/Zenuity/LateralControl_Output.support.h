/* Automatically generated Extension Support header */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#ifndef SUPPORT_ZENUITY_LATERALCONTROL_OUTPUT_INCLUDED
#define SUPPORT_ZENUITY_LATERALCONTROL_OUTPUT_INCLUDED

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Conversion functions */
float Zenuity_LateralControl_FrontWheelRequest_angleToFloat(const int32_t value);
int32_t Zenuity_LateralControl_FrontWheelRequest_floatToAngle(const float value);
float Zenuity_LateralControl_FrontWheelRequest_angleRateLimitToFloat(const int32_t value);
int32_t Zenuity_LateralControl_FrontWheelRequest_floatToAngleRateLimit(const float value);
float Zenuity_LateralControl_FrontWheelRequest_lowerTorqueLimitToFloat(const int32_t value);
int32_t Zenuity_LateralControl_FrontWheelRequest_floatToLowerTorqueLimit(const float value);
float Zenuity_LateralControl_FrontWheelRequest_upperLorqueLimitToFloat(const int32_t value);
int32_t Zenuity_LateralControl_FrontWheelRequest_floatToUpperLorqueLimit(const float value);
float Zenuity_LateralControl_FrontWheelRequest_additionalTorqueToFloat(const int32_t value);
int32_t Zenuity_LateralControl_FrontWheelRequest_floatToAdditionalTorque(const float value);
float Zenuity_LateralControl_FrontWheelRequest_bandwidthScalingToFloat(const uint32_t value);
uint32_t Zenuity_LateralControl_FrontWheelRequest_floatToBandwidthScaling(const float value);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SUPPORT_ZENUITY_LATERALCONTROL_OUTPUT_INCLUDED */
