/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef SYSTEMCORE_CRUISING_CRUISINGINPUT_INCLUDED
#define SYSTEMCORE_CRUISING_CRUISINGINPUT_INCLUDED

#include "SystemCore/Cruising/CruisingInput_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define SystemCore_Cruising_DriverAlertControlInput_size                                 (2)
#define SystemCore_Cruising_LaneChangeAssistInput_size                                   (9)
#define SystemCore_Cruising_RiskMitigationSupportInput_size                              (2)
#define SystemCore_Cruising_TrafficAssistInput_size                                      (8)

/* Message IDs (where set with "identifier" option) */
#define SystemCore_Cruising_TrafficAssistInput_source                                    3U
#define SystemCore_Cruising_TrafficAssistInput_identifier                                777U
#define SystemCore_Cruising_TrafficAssistInput_majorVersion                              1U
#define SystemCore_Cruising_TrafficAssistInput_minorVersion                              0U
#define SystemCore_Cruising_LaneChangeAssistInput_source                                 3U
#define SystemCore_Cruising_LaneChangeAssistInput_identifier                             778U
#define SystemCore_Cruising_LaneChangeAssistInput_majorVersion                           1U
#define SystemCore_Cruising_LaneChangeAssistInput_minorVersion                           0U
#define SystemCore_Cruising_RiskMitigationSupportInput_source                            3U
#define SystemCore_Cruising_RiskMitigationSupportInput_identifier                        779U
#define SystemCore_Cruising_RiskMitigationSupportInput_majorVersion                      1U
#define SystemCore_Cruising_RiskMitigationSupportInput_minorVersion                      0U
#define SystemCore_Cruising_DriverAlertControlInput_source                               3U
#define SystemCore_Cruising_DriverAlertControlInput_identifier                           780U
#define SystemCore_Cruising_DriverAlertControlInput_majorVersion                         1U
#define SystemCore_Cruising_DriverAlertControlInput_minorVersion                         0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_SystemCore_Cruising_DriverAlertControlInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_DriverAlertControlInput_Raw *const data);
bool decode_SystemCore_Cruising_DriverAlertControlInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_DriverAlertControlInput_Raw *const data);
#define encode_SystemCore_Cruising_DriverAlertControlInput encode_SystemCore_Cruising_DriverAlertControlInput_Raw
#define decode_SystemCore_Cruising_DriverAlertControlInput decode_SystemCore_Cruising_DriverAlertControlInput_Raw

bool encode_SystemCore_Cruising_LaneChangeAssistInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_LaneChangeAssistInput_Raw *const data);
bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_LaneChangeAssistInput_Raw *const data);
#define encode_SystemCore_Cruising_LaneChangeAssistInput encode_SystemCore_Cruising_LaneChangeAssistInput_Raw
#define decode_SystemCore_Cruising_LaneChangeAssistInput decode_SystemCore_Cruising_LaneChangeAssistInput_Raw

bool encode_SystemCore_Cruising_RiskMitigationSupportInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_RiskMitigationSupportInput_Raw *const data);
bool decode_SystemCore_Cruising_RiskMitigationSupportInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_RiskMitigationSupportInput_Raw *const data);
#define encode_SystemCore_Cruising_RiskMitigationSupportInput encode_SystemCore_Cruising_RiskMitigationSupportInput_Raw
#define decode_SystemCore_Cruising_RiskMitigationSupportInput decode_SystemCore_Cruising_RiskMitigationSupportInput_Raw

bool encode_SystemCore_Cruising_TrafficAssistInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_TrafficAssistInput_Raw *const data);
bool decode_SystemCore_Cruising_TrafficAssistInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_TrafficAssistInput_Raw *const data);
#define encode_SystemCore_Cruising_TrafficAssistInput encode_SystemCore_Cruising_TrafficAssistInput_Raw
#define decode_SystemCore_Cruising_TrafficAssistInput decode_SystemCore_Cruising_TrafficAssistInput_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_CRUISING_CRUISINGINPUT_INCLUDED */