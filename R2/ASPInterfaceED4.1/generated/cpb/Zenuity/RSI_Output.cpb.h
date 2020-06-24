/* Automatically generated pb header */
/* Generated by Protocol Buffers - 1 */

#ifndef ZENUITY_RSI_OUTPUT_INCLUDED
#define ZENUITY_RSI_OUTPUT_INCLUDED
#include "Tools/CProtobuf/pb.h"
#include "Tools/CProtobuf/pb_decode.h"
#include "Tools/CProtobuf/pb_encode.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define Zenuity_RSI_RoadSignWarnings_size                                                (9)
#define Zenuity_RSI_RsiDebug_size                                                        (8)
#define Zenuity_RSI_SpeedLimit_size                                                      (14)
#define Zenuity_RSI_RsiOutput_size                                                       ((14 + Zenuity_RSI_SpeedLimit_size + Zenuity_RSI_RoadSignWarnings_size + Zenuity_RSI_RsiDebug_size) + PB_VARINT_MAX_ENCODED_SIZE)

/* Message IDs (where set with "identifier" option) */
#define Zenuity_RSI_RsiOutput_source                                                     1U
#define Zenuity_RSI_RsiOutput_identifier                                                 40U
#define Zenuity_RSI_RsiOutput_majorVersion                                               1U
#define Zenuity_RSI_RsiOutput_minorVersion                                               0U

/* Enum definitions */
typedef enum _Zenuity_RSI_RoadSignInformationAvailability {
    Zenuity_RSI_RoadSignInformationAvailability_NotAvailable = 0,
    Zenuity_RSI_RoadSignInformationAvailability_Vision = 1,
    Zenuity_RSI_RoadSignInformationAvailability_ElectronicHorizon = 2,
    Zenuity_RSI_RoadSignInformationAvailability_VisionAndElectronicHorizon = 3
} Zenuity_RSI_RoadSignInformationAvailability;
#define Zenuity_RSI_RoadSignInformationAvailability_MIN Zenuity_RSI_RoadSignInformationAvailability_NotAvailable
#define Zenuity_RSI_RoadSignInformationAvailability_MAX Zenuity_RSI_RoadSignInformationAvailability_VisionAndElectronicHorizon
#define Zenuity_RSI_RoadSignInformationAvailability_ARRAYSIZE ((Zenuity_RSI_RoadSignInformationAvailability)(Zenuity_RSI_RoadSignInformationAvailability_VisionAndElectronicHorizon+1))

typedef enum _Zenuity_RSI_FunctionStatus {
    Zenuity_RSI_FunctionStatus_Unknown = 0,
    Zenuity_RSI_FunctionStatus_Off = 1,
    Zenuity_RSI_FunctionStatus_Disabled = 2,
    Zenuity_RSI_FunctionStatus_On = 3
} Zenuity_RSI_FunctionStatus;
#define Zenuity_RSI_FunctionStatus_MIN Zenuity_RSI_FunctionStatus_Unknown
#define Zenuity_RSI_FunctionStatus_MAX Zenuity_RSI_FunctionStatus_On
#define Zenuity_RSI_FunctionStatus_ARRAYSIZE ((Zenuity_RSI_FunctionStatus)(Zenuity_RSI_FunctionStatus_On+1))

typedef enum _Zenuity_RSI_SpeedUnit {
    Zenuity_RSI_SpeedUnit_Unknown = 0,
    Zenuity_RSI_SpeedUnit_KilometersPerHour = 1,
    Zenuity_RSI_SpeedUnit_MilesPerHour = 2
} Zenuity_RSI_SpeedUnit;
#define Zenuity_RSI_SpeedUnit_MIN Zenuity_RSI_SpeedUnit_Unknown
#define Zenuity_RSI_SpeedUnit_MAX Zenuity_RSI_SpeedUnit_MilesPerHour
#define Zenuity_RSI_SpeedUnit_ARRAYSIZE ((Zenuity_RSI_SpeedUnit)(Zenuity_RSI_SpeedUnit_MilesPerHour+1))

/* Struct definitions */
typedef struct _Zenuity_RSI_RoadSignWarnings {
    /** OverspeedWarning
     * Warn the driver about driving over the speed limit adjusted by a warning offset
     */
    bool overspeedWarning;
    /** SpeedCameraWarning
     * Warn the driver about an upcoming speed camera.
     */
    bool speedCameraWarning;
    /** DistanceToSpeedCamera
     * Distance to upcoming speed camera.
     * Unit: m
     * Scale: 10.0
     * Min: 0
     * Max: 2550
     */
    uint8_t distanceToSpeedCamera;
    /** NoEntryWarning
     * Warn driver about driving in the wrong direction.
     */
    bool noEntryWarning;
} Zenuity_RSI_RoadSignWarnings;

typedef struct _Zenuity_RSI_RsiDebug {
    /** VisionSpeedLimitAvailable
     * A speed limit derived from vision input is currently available.
     */
    bool visionSpeedLimitAvailable;
    /** ElectronicHorizonSpeedLimitAvailable
     * A speed limit derived from Electronic Horizon input is currently available.
     */
    bool electronicHorizonSpeedLimitAvailable;
    /** ElectronicHorizonAndVisionAvailableAndEqual
     * The speed limit derived from both sources, Electronic Horizon and vision, are both the same.
     */
    bool electronicHorizonAndVisionAvailableAndEqual;
    /** SpeedLimitSourceIsOnlyElectronicHorizon
     * The current speed limit is only based on Electronic Horizon as source.
     */
    bool speedLimitSourceIsOnlyElectronicHorizon;
} Zenuity_RSI_RsiDebug;

typedef struct _Zenuity_RSI_SpeedLimit {
    /** SpeedUnit
     * Unit of the reported speed limit
     */
    Zenuity_RSI_SpeedUnit speedUnit;
    /** CurrentSpeedLimit
     * Current valid speed limit. The field is unitless as the unit is provided by speed_unit.
     * Min: 0
     * Max: 255
     */
    uint8_t currentSpeedLimit;
    /** UpcomingSpeedLimit
     * Upcoming speed limit. The field is unitless as the unit is provided by speed_unit.
     * Min: 0
     * Max: 255
     */
    uint8_t upcomingSpeedLimit;
    /** DistanceToUpcomingSpeedLimit
     * Distance at which the upcoming speed limit becomes valid.
     * Unit: m
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t distanceToUpcomingSpeedLimit;
} Zenuity_RSI_SpeedLimit;

typedef struct _Zenuity_RSI_RsiOutput {
    /** Availability
     * Availability status of the Road Sign Information SWC.
     */
    Zenuity_RSI_RoadSignInformationAvailability availability;
    /** Status
     * Function status telling if the feature is on or off.
     */
    Zenuity_RSI_FunctionStatus status;
    /** SpeedLimit
     * Current and upcoming valid speed limit.
     */
    Zenuity_RSI_SpeedLimit speedLimit;
    /** Warnings
     * Road sign related warnings to the driver.
     */
    Zenuity_RSI_RoadSignWarnings warnings;
    /** ArbitratedCountry
     * The alpha-3 country codes with numeric code as specified by ISO 3166-1.
     * Min: 0
     * Max: 65535
     */
    uint16_t arbitratedCountry;
    /** Debug
     * Signals only used for debugging purpose of the Road Sign Information feature SWC.
     */
    Zenuity_RSI_RsiDebug debug;
} Zenuity_RSI_RsiOutput;

/* Struct field encoding specification for pb */
extern const pb_field_t Zenuity_RSI_SpeedLimit_fields[5];
extern const pb_field_t Zenuity_RSI_RoadSignWarnings_fields[5];
extern const pb_field_t Zenuity_RSI_RsiDebug_fields[5];
extern const pb_field_t Zenuity_RSI_RsiOutput_fields[7];
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_RSI_OUTPUT_INCLUDED */