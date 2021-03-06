/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef SYSTEMCORE_COMMON_EGOMOTIONMCU_INCLUDED
#define SYSTEMCORE_COMMON_EGOMOTIONMCU_INCLUDED

#include "SystemCore/Common/EgoMotionMcu_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define SystemCore_Common_EgoMotionMcuOutput_size                                        (26)

/* Message IDs (where set with "identifier" option) */
#define SystemCore_Common_EgoMotionMcuOutput_source                                      3U
#define SystemCore_Common_EgoMotionMcuOutput_identifier                                  460U
#define SystemCore_Common_EgoMotionMcuOutput_majorVersion                                2U
#define SystemCore_Common_EgoMotionMcuOutput_minorVersion                                0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_SystemCore_Common_EgoMotionMcuOutput_Raw(qpb_ostream_t *const stream, const SystemCore_Common_EgoMotionMcuOutput_Raw *const data);
bool decode_SystemCore_Common_EgoMotionMcuOutput_Raw(qpb_istream_t *const stream, SystemCore_Common_EgoMotionMcuOutput_Raw *const data);
bool encode_SystemCore_Common_EgoMotionMcuOutput(qpb_ostream_t *const stream, const SystemCore_Common_EgoMotionMcuOutput *const data);
bool decode_SystemCore_Common_EgoMotionMcuOutput(qpb_istream_t *const stream, SystemCore_Common_EgoMotionMcuOutput *const data);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_COMMON_EGOMOTIONMCU_INCLUDED */
