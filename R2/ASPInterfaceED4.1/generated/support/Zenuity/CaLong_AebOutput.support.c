/* Automatically generated Extension Support code */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#include "Tools/CSupport/ConversionSupport.h"
#include "Zenuity/CaLong_AebOutput.support.h"

/* Defines */
#define F_0_01               0.01f
#define F_0_1                0.1f

/* Conversion functions */
float Zenuity_CaLong_TimeToThreat_brakeThreatToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t Zenuity_CaLong_TimeToThreat_floatToBrakeThreat(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float Zenuity_CaLong_TimeToThreat_steeringThreatToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t Zenuity_CaLong_TimeToThreat_floatToSteeringThreat(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float Zenuity_CaLong_AebRequest_avoidanceDecelerationToFloat(const uint8_t value)
{
   return value * F_0_1;
}

uint8_t Zenuity_CaLong_AebRequest_floatToAvoidanceDeceleration(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_1, 0, UINT8_MAX);
}
float Zenuity_CaLong_CollisionMitigationThreatInformation_timeToCollisionToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t Zenuity_CaLong_CollisionMitigationThreatInformation_floatToTimeToCollision(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float Zenuity_CaLong_CollisionForwardWarningControl_brakeGainRequestToFloat(const uint8_t value)
{
   return value * F_0_1;
}

uint8_t Zenuity_CaLong_CollisionForwardWarningControl_floatToBrakeGainRequest(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_1, 0, UINT8_MAX);
}
float Zenuity_CaLong_CollisionForwardWarningControl_brakeGainMaxDecelerationToFloat(const uint8_t value)
{
   return value * F_0_1;
}

uint8_t Zenuity_CaLong_CollisionForwardWarningControl_floatToBrakeGainMaxDeceleration(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_1, 0, UINT8_MAX);
}
float Zenuity_CaLong_CollisionForwardWarningControl_timeToCollisionToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t Zenuity_CaLong_CollisionForwardWarningControl_floatToTimeToCollision(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float Zenuity_CaLong_CollisionMitigationBrakeRequest_decelerationRequestToFloat(const uint8_t value)
{
   return value * F_0_1;
}

uint8_t Zenuity_CaLong_CollisionMitigationBrakeRequest_floatToDecelerationRequest(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_1, 0, UINT8_MAX);
}
float Zenuity_CaLong_VruAebOutput_avoidanceDecelerationToFloat(const uint8_t value)
{
   return value * F_0_1;
}

uint8_t Zenuity_CaLong_VruAebOutput_floatToAvoidanceDeceleration(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_1, 0, UINT8_MAX);
}
float Zenuity_CaLong_StaticDistanceWarningOutput_timeGapToFloat(const uint8_t value)
{
   return value * F_0_1;
}

uint8_t Zenuity_CaLong_StaticDistanceWarningOutput_floatToTimeGap(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_1, 0, UINT8_MAX);
}
