/* Automatically generated Extension Support code */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#include "Tools/CSupport/ConversionSupport.h"
#include "VisionCore/Common/EgoMotion.support.h"

/* Defines */
#define F_0_0001             0.0001f
#define F_0_01               0.01f

/* Conversion functions */
float VisionCore_Common_EgoMotionOutput_longitudinalVelocityToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t VisionCore_Common_EgoMotionOutput_floatToLongitudinalVelocity(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float VisionCore_Common_EgoMotionOutput_longitudinalAccelerationToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t VisionCore_Common_EgoMotionOutput_floatToLongitudinalAcceleration(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float VisionCore_Common_EgoMotionOutput_lateralVelocityToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t VisionCore_Common_EgoMotionOutput_floatToLateralVelocity(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float VisionCore_Common_EgoMotionOutput_lateralAccelerationToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t VisionCore_Common_EgoMotionOutput_floatToLateralAcceleration(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float VisionCore_Common_EgoMotionOutput_yawRateToFloat(const int16_t value)
{
   return value * F_0_0001;
}

int16_t VisionCore_Common_EgoMotionOutput_floatToYawRate(const float value)
{
   return (int16_t)convertToInt32(value, F_0_0001, INT16_MIN, INT16_MAX);
}
