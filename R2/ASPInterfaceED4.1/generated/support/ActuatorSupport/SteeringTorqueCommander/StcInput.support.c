/* Automatically generated Extension Support code */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#include "Tools/CSupport/ConversionSupport.h"
#include "ActuatorSupport/SteeringTorqueCommander/StcInput.support.h"

/* Defines */
#define F_0_01               0.01f

/* Conversion functions */
float ActuatorSupport_SteeringTorqueCommander_StcInput_pinionAngleRequestToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToPinionAngleRequest(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float ActuatorSupport_SteeringTorqueCommander_StcInput_pinionAngleFeedbackToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToPinionAngleFeedback(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float ActuatorSupport_SteeringTorqueCommander_StcInput_steeringWheelTorqueFeedbackToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToSteeringWheelTorqueFeedback(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float ActuatorSupport_SteeringTorqueCommander_StcInput_longitudinalSpeedToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToLongitudinalSpeed(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
