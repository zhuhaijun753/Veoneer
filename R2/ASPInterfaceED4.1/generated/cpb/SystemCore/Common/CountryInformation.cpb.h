/* Automatically generated pb header */
/* Generated by Protocol Buffers - 1 */

#ifndef SYSTEMCORE_COMMON_COUNTRYINFORMATION_INCLUDED
#define SYSTEMCORE_COMMON_COUNTRYINFORMATION_INCLUDED
#include "Tools/CProtobuf/pb.h"
#include "Tools/CProtobuf/pb_decode.h"
#include "Tools/CProtobuf/pb_encode.h"

#include "Common/CountryCodes.cpb.h"
#include "Common/Environment.cpb.h"
#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define SystemCore_Common_CountryInformation_size                                        (5)

/* Message IDs (where set with "identifier" option) */
#define SystemCore_Common_CountryInformation_source                                      3U
#define SystemCore_Common_CountryInformation_identifier                                  50U
#define SystemCore_Common_CountryInformation_majorVersion                                1U
#define SystemCore_Common_CountryInformation_minorVersion                                0U

/* Struct definitions */
typedef struct _SystemCore_Common_CountryInformation {
    /** CountryCode
     * Current country
     */
    Common_CountryCode countryCode;
    /** TrafficStyle
     * Current traffic style
     */
    Common_TrafficStyle trafficStyle;
} SystemCore_Common_CountryInformation;

/* Struct field encoding specification for pb */
extern const pb_field_t SystemCore_Common_CountryInformation_fields[3];
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_COMMON_COUNTRYINFORMATION_INCLUDED */
