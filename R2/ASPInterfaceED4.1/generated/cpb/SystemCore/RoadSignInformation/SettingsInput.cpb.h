/* Automatically generated pb header */
/* Generated by Protocol Buffers - 1 */

#ifndef SYSTEMCORE_ROADSIGNINFORMATION_SETTINGSINPUT_INCLUDED
#define SYSTEMCORE_ROADSIGNINFORMATION_SETTINGSINPUT_INCLUDED
#include "Tools/CProtobuf/pb.h"
#include "Tools/CProtobuf/pb_decode.h"
#include "Tools/CProtobuf/pb_encode.h"

#include "Zenuity/RSI_Output.cpb.h"
#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define SystemCore_RoadSignInformation_RoadSignInformationSettings_size                  (11)

/* Message IDs (where set with "identifier" option) */
#define SystemCore_RoadSignInformation_RoadSignInformationSettings_source                3U
#define SystemCore_RoadSignInformation_RoadSignInformationSettings_identifier            40U
#define SystemCore_RoadSignInformation_RoadSignInformationSettings_majorVersion          1U
#define SystemCore_RoadSignInformation_RoadSignInformationSettings_minorVersion          0U

/* Struct definitions */
typedef struct _SystemCore_RoadSignInformation_RoadSignInformationSettings {
    /** RsiActivatedByDriver
     * On/Off for Road Sign Information
     */
    bool rsiActivatedByDriver;
    /** OverspeedWarningActivatedByDriver
     * On/Off for Overspeed Warning
     */
    bool overspeedWarningActivatedByDriver;
    /** OverspeedWarningOffset
     * Offset to speed limit when the driver shall get an overspeed warning. Unit km/h or mph depending on the setting in the car.
     * Min: -20
     * Max: 30
     */
    int8_t overspeedWarningOffset;
    /** SpeedUnit
     * Unit of the reported speed limit
     */
    Zenuity_RSI_SpeedUnit speedUnit;
    /** SpeedCameraWarningActivatedByDriver
     * On/Off for Speed Camera Warning
     */
    bool speedCameraWarningActivatedByDriver;
} SystemCore_RoadSignInformation_RoadSignInformationSettings;

/* Struct field encoding specification for pb */
extern const pb_field_t SystemCore_RoadSignInformation_RoadSignInformationSettings_fields[6];
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_ROADSIGNINFORMATION_SETTINGSINPUT_INCLUDED */
