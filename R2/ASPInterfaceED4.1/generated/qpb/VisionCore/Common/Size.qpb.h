/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef VISIONCORE_COMMON_SIZE_INCLUDED
#define VISIONCORE_COMMON_SIZE_INCLUDED

#include "VisionCore/Common/Size_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define VisionCore_Common_Size2_m_0_01_size                                              (8)

/* Message IDs (where set with "identifier" option) */

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_VisionCore_Common_Size2_m_0_01_Raw(qpb_ostream_t *const stream, const VisionCore_Common_Size2_m_0_01_Raw *const data);
bool decode_VisionCore_Common_Size2_m_0_01_Raw(qpb_istream_t *const stream, VisionCore_Common_Size2_m_0_01_Raw *const data);
bool encode_VisionCore_Common_Size2_m_0_01(qpb_ostream_t *const stream, const VisionCore_Common_Size2_m_0_01 *const data);
bool decode_VisionCore_Common_Size2_m_0_01(qpb_istream_t *const stream, VisionCore_Common_Size2_m_0_01 *const data);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* VISIONCORE_COMMON_SIZE_INCLUDED */
