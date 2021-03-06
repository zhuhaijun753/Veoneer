/* Automatically generated Extension Support header */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#ifndef SUPPORT_ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCINPUT_INCLUDED
#define SUPPORT_ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCINPUT_INCLUDED

#include <stdint.h>

#ifdef __cplusplus
extern "C" {
#endif

/* Conversion functions */
float ActuatorSupport_SteeringTorqueCommander_StcInput_pinionAngleRequestToFloat(const int16_t value);
int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToPinionAngleRequest(const float value);
float ActuatorSupport_SteeringTorqueCommander_StcInput_pinionAngleFeedbackToFloat(const int16_t value);
int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToPinionAngleFeedback(const float value);
float ActuatorSupport_SteeringTorqueCommander_StcInput_steeringWheelTorqueFeedbackToFloat(const int16_t value);
int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToSteeringWheelTorqueFeedback(const float value);
float ActuatorSupport_SteeringTorqueCommander_StcInput_longitudinalSpeedToFloat(const int16_t value);
int16_t ActuatorSupport_SteeringTorqueCommander_StcInput_floatToLongitudinalSpeed(const float value);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SUPPORT_ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCINPUT_INCLUDED */
