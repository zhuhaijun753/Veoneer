/* Automatically generated Extension Support code */
/* SPP version 2.0.0 */
/* Generated by C Conversion Support - 1 */

#include "Tools/CSupport/ConversionSupport.h"
#include "SystemCore/CollisionAvoidance/SettingsInput.support.h"

/* Defines */
#define F_0_01               0.01f
#define F_0_05               0.05f
#define F_0_1                0.1f

/* Conversion functions */
float SystemCore_CollisionAvoidance_ThreatThresholdLookupTable_valuesToFloat(const int16_t value)
{
   return value * F_0_1;
}

int16_t SystemCore_CollisionAvoidance_ThreatThresholdLookupTable_floatToValues(const float value)
{
   return (int16_t)convertToInt32(value, F_0_1, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_ThreatThresholdLookupTable_breakpointsToFloat(const uint16_t value)
{
   return value * F_0_1;
}

uint16_t SystemCore_CollisionAvoidance_ThreatThresholdLookupTable_floatToBreakpoints(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_1, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_FullBrakeParameters_negativeAccelerationMaximumToFloat(const int8_t value)
{
   return value * F_0_1;
}

int8_t SystemCore_CollisionAvoidance_FullBrakeParameters_floatToNegativeAccelerationMaximum(const float value)
{
   return (int8_t)convertToInt32(value, F_0_1, INT8_MIN, INT8_MAX);
}
float SystemCore_CollisionAvoidance_FullBrakeParameters_nominalAccelerationFactorToFloat(const int8_t value)
{
   return value * F_0_01;
}

int8_t SystemCore_CollisionAvoidance_FullBrakeParameters_floatToNominalAccelerationFactor(const float value)
{
   return (int8_t)convertToInt32(value, F_0_01, INT8_MIN, INT8_MAX);
}
float SystemCore_CollisionAvoidance_FullBrakeParameters_previousAccelerationRequestFactorToFloat(const int8_t value)
{
   return value * F_0_01;
}

int8_t SystemCore_CollisionAvoidance_FullBrakeParameters_floatToPreviousAccelerationRequestFactor(const float value)
{
   return (int8_t)convertToInt32(value, F_0_01, INT8_MIN, INT8_MAX);
}
float SystemCore_CollisionAvoidance_FullBrakeParameters_previousNominalRequestFactorToFloat(const int8_t value)
{
   return value * F_0_01;
}

int8_t SystemCore_CollisionAvoidance_FullBrakeParameters_floatToPreviousNominalRequestFactor(const float value)
{
   return (int8_t)convertToInt32(value, F_0_01, INT8_MIN, INT8_MAX);
}
float SystemCore_CollisionAvoidance_PreBrakeParameters_negativeAccelerationMaximumToFloat(const int8_t value)
{
   return value * F_0_1;
}

int8_t SystemCore_CollisionAvoidance_PreBrakeParameters_floatToNegativeAccelerationMaximum(const float value)
{
   return (int8_t)convertToInt32(value, F_0_1, INT8_MIN, INT8_MAX);
}
float SystemCore_CollisionAvoidance_PreBrakeParameters_nominalRequestFactorToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_PreBrakeParameters_floatToNominalRequestFactor(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_PreBrakeParameters_negativeJerkMinimumToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t SystemCore_CollisionAvoidance_PreBrakeParameters_floatToNegativeJerkMinimum(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_AebTimingParameters_beltActivationDelayToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_AebTimingParameters_floatToBeltActivationDelay(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_AebTimingParameters_postEventMessageActivationDelayToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_AebTimingParameters_floatToPostEventMessageActivationDelay(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_AebTimingParameters_standstillRequestHoldTimeToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_AebTimingParameters_floatToStandstillRequestHoldTime(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_AebDeactivationParameters_timeWithHighTtcToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_AebDeactivationParameters_floatToTimeWithHighTtc(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_AebDeactivationParameters_standstillTimeToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_AebDeactivationParameters_floatToStandstillTime(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_EmaParameters_lateralJerkActivationThresholdToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_EmaParameters_floatToLateralJerkActivationThreshold(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LongitudinalTaTunableParameters_brakeDelayEstimateToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_LongitudinalTaTunableParameters_floatToBrakeDelayEstimate(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_LongitudinalTaTunableParameters_longitudinalMarginWhenAebActiveToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_LongitudinalTaTunableParameters_floatToLongitudinalMarginWhenAebActive(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_TimeToCollisionOffsetAndCorrection_offsetToFloat(const int16_t value)
{
   return value * F_0_1;
}

int16_t SystemCore_CollisionAvoidance_TimeToCollisionOffsetAndCorrection_floatToOffset(const float value)
{
   return (int16_t)convertToInt32(value, F_0_1, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_TimeToCollisionOffsetAndCorrection_correctionToFloat(const int16_t value)
{
   return value * F_0_1;
}

int16_t SystemCore_CollisionAvoidance_TimeToCollisionOffsetAndCorrection_floatToCorrection(const float value)
{
   return (int16_t)convertToInt32(value, F_0_1, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_LateralMarginOffsetAndCorrection_offsetToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t SystemCore_CollisionAvoidance_LateralMarginOffsetAndCorrection_floatToOffset(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_LateralMarginOffsetAndCorrection_correctionToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t SystemCore_CollisionAvoidance_LateralMarginOffsetAndCorrection_floatToCorrection(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_TimeToCollisionCalibrationTable_minToFloat(const int16_t value)
{
   return value * F_0_1;
}

int16_t SystemCore_CollisionAvoidance_TimeToCollisionCalibrationTable_floatToMin(const float value)
{
   return (int16_t)convertToInt32(value, F_0_1, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_TimeToCollisionCalibrationTable_maxToFloat(const int16_t value)
{
   return value * F_0_1;
}

int16_t SystemCore_CollisionAvoidance_TimeToCollisionCalibrationTable_floatToMax(const float value)
{
   return (int16_t)convertToInt32(value, F_0_1, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_TimeToCollisionCalibrationTable_baselineToFloat(const int16_t value)
{
   return value * F_0_1;
}

int16_t SystemCore_CollisionAvoidance_TimeToCollisionCalibrationTable_floatToBaseline(const float value)
{
   return (int16_t)convertToInt32(value, F_0_1, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_LateralMarginCalibrationTable_minToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t SystemCore_CollisionAvoidance_LateralMarginCalibrationTable_floatToMin(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_LateralMarginCalibrationTable_maxToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t SystemCore_CollisionAvoidance_LateralMarginCalibrationTable_floatToMax(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_LateralMarginCalibrationTable_baselineToFloat(const int16_t value)
{
   return value * F_0_01;
}

int16_t SystemCore_CollisionAvoidance_LateralMarginCalibrationTable_floatToBaseline(const float value)
{
   return (int16_t)convertToInt32(value, F_0_01, INT16_MIN, INT16_MAX);
}
float SystemCore_CollisionAvoidance_VruZoneCalibrationTableParameters_speedNodesToFloat(const uint16_t value)
{
   return value * F_0_1;
}

uint16_t SystemCore_CollisionAvoidance_VruZoneCalibrationTableParameters_floatToSpeedNodes(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_1, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_VruDecelerationRequestParameters_avoidanceDecelerationLagToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_VruDecelerationRequestParameters_floatToAvoidanceDecelerationLag(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_VruDecelerationRequestParameters_avoidanceDistanceToFloat(const uint8_t value)
{
   return value * F_0_1;
}

uint8_t SystemCore_CollisionAvoidance_VruDecelerationRequestParameters_floatToAvoidanceDistance(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_1, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lkaMaxTimeNeededToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLkaMaxTimeNeeded(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_elkaRoadEdgeMaxTimeNeededToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToElkaRoadEdgeMaxTimeNeeded(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lkaLaneWidthEnableMarginToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLkaLaneWidthEnableMargin(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssOncomingObjectSuppressionTimeToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssOncomingObjectSuppressionTime(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssOvertakeObjectSuppressionTimeToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssOvertakeObjectSuppressionTime(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssAccelerationExtrapolationTimeForObjectSuppressionToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssAccelerationExtrapolationTimeForObjectSuppression(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssOncomingObjectSuppressionTimeToReachLimitToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssOncomingObjectSuppressionTimeToReachLimit(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssOvertakeObjectSuppressionTimeToReachLimitToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssOvertakeObjectSuppressionTimeToReachLimit(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssOvertakeObjectSuppressionLateralPositionLimitToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssOvertakeObjectSuppressionLateralPositionLimit(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssOncomingObjectSuppressionLateralGapLimitToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssOncomingObjectSuppressionLateralGapLimit(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_LSSTunableParameters_lssObjectSuppressionNarrowRoadLimitToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_LSSTunableParameters_floatToLssObjectSuppressionNarrowRoadLimit(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_PredictedDecelerationSensitivityLookupTable_valuesToFloat(const int8_t value)
{
   return value * F_0_1;
}

int8_t SystemCore_CollisionAvoidance_PredictedDecelerationSensitivityLookupTable_floatToValues(const float value)
{
   return (int8_t)convertToInt32(value, F_0_1, INT8_MIN, INT8_MAX);
}
float SystemCore_CollisionAvoidance_PredictedDecelerationSensitivityLookupTable_breakpointsToFloat(const uint16_t value)
{
   return value * F_0_1;
}

uint16_t SystemCore_CollisionAvoidance_PredictedDecelerationSensitivityLookupTable_floatToBreakpoints(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_1, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_ReactionTimeLookupTable_valuesToFloat(const uint8_t value)
{
   return value * F_0_01;
}

uint8_t SystemCore_CollisionAvoidance_ReactionTimeLookupTable_floatToValues(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_01, 0, UINT8_MAX);
}
float SystemCore_CollisionAvoidance_ReactionTimeLookupTable_breakpointsToFloat(const uint16_t value)
{
   return value * F_0_1;
}

uint16_t SystemCore_CollisionAvoidance_ReactionTimeLookupTable_floatToBreakpoints(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_1, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_TargetSelectionParameters_funnelBreakpointsToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_TargetSelectionParameters_floatToFunnelBreakpoints(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_TargetSelectionParameters_innerFunnelWidthsToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_TargetSelectionParameters_floatToInnerFunnelWidths(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_TargetSelectionParameters_outerFunnelWidthsToFloat(const uint16_t value)
{
   return value * F_0_01;
}

uint16_t SystemCore_CollisionAvoidance_TargetSelectionParameters_floatToOuterFunnelWidths(const float value)
{
   return (uint16_t)convertToUint32(value, F_0_01, 0, UINT16_MAX);
}
float SystemCore_CollisionAvoidance_TargetSelectionParameters_cutInTimeThresholdToFloat(const uint8_t value)
{
   return value * F_0_05;
}

uint8_t SystemCore_CollisionAvoidance_TargetSelectionParameters_floatToCutInTimeThreshold(const float value)
{
   return (uint8_t)convertToUint32(value, F_0_05, 0, UINT8_MAX);
}
