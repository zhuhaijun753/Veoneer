/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef VISIONCORE_COMMON_EGOMOTION_INCLUDED
#define VISIONCORE_COMMON_EGOMOTION_INCLUDED

#include "VisionCore/Common/EgoMotion_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define VisionCore_Common_EgoMotionOutput_size                                           (34)

/* Message IDs (where set with "identifier" option) */
#define VisionCore_Common_EgoMotionOutput_source                                         2U
#define VisionCore_Common_EgoMotionOutput_identifier                                     460U
#define VisionCore_Common_EgoMotionOutput_majorVersion                                   1U
#define VisionCore_Common_EgoMotionOutput_minorVersion                                   0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_VisionCore_Common_EgoMotionOutput_Raw(qpb_ostream_t *const stream, const VisionCore_Common_EgoMotionOutput_Raw *const data);
bool decode_VisionCore_Common_EgoMotionOutput_Raw(qpb_istream_t *const stream, VisionCore_Common_EgoMotionOutput_Raw *const data);
bool encode_VisionCore_Common_EgoMotionOutput(qpb_ostream_t *const stream, const VisionCore_Common_EgoMotionOutput *const data);
bool decode_VisionCore_Common_EgoMotionOutput(qpb_istream_t *const stream, VisionCore_Common_EgoMotionOutput *const data);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* VISIONCORE_COMMON_EGOMOTION_INCLUDED */