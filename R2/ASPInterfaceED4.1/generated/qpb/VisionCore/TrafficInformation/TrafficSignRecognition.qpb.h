/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef VISIONCORE_TRAFFICINFORMATION_TRAFFICSIGNRECOGNITION_INCLUDED
#define VISIONCORE_TRAFFICINFORMATION_TRAFFICSIGNRECOGNITION_INCLUDED

#include "VisionCore/TrafficInformation/TrafficSignRecognition_types.qpb.h"

#include "VisionCore/Common/Coords.qpb.h"
#include "VisionCore/Common/Size.qpb.h"

#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define VisionCore_TrafficInformation_AddOnSign_size                                     (5)
#define VisionCore_TrafficInformation_Sign_size                                          (28)
#define VisionCore_TrafficInformation_StateInfo_size                                     (4)
#define VisionCore_TrafficInformation_ValidatedSign_size                                 ((30 + VisionCore_TrafficInformation_Sign_size + VisionCore_Common_Coord3_m_0_01_size + VisionCore_Common_Size2_m_0_01_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define VisionCore_TrafficInformation_ValidatedSignList_size                             ((1282 + VisionCore_TrafficInformation_StateInfo_size) + QPB_VARINT_MAX_ENCODED_SIZE)

/* Message IDs (where set with "identifier" option) */
#define VisionCore_TrafficInformation_ValidatedSignList_source                           2U
#define VisionCore_TrafficInformation_ValidatedSignList_identifier                       32U
#define VisionCore_TrafficInformation_ValidatedSignList_majorVersion                     1U
#define VisionCore_TrafficInformation_ValidatedSignList_minorVersion                     0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_VisionCore_TrafficInformation_AddOnSign_Raw(qpb_ostream_t *const stream, const VisionCore_TrafficInformation_AddOnSign_Raw *const data);
bool decode_VisionCore_TrafficInformation_AddOnSign_Raw(qpb_istream_t *const stream, VisionCore_TrafficInformation_AddOnSign_Raw *const data);
#define encode_VisionCore_TrafficInformation_AddOnSign encode_VisionCore_TrafficInformation_AddOnSign_Raw
#define decode_VisionCore_TrafficInformation_AddOnSign decode_VisionCore_TrafficInformation_AddOnSign_Raw

bool encode_VisionCore_TrafficInformation_Sign_Raw(qpb_ostream_t *const stream, const VisionCore_TrafficInformation_Sign_Raw *const data);
bool decode_VisionCore_TrafficInformation_Sign_Raw(qpb_istream_t *const stream, VisionCore_TrafficInformation_Sign_Raw *const data);
#define encode_VisionCore_TrafficInformation_Sign encode_VisionCore_TrafficInformation_Sign_Raw
#define decode_VisionCore_TrafficInformation_Sign decode_VisionCore_TrafficInformation_Sign_Raw

bool encode_VisionCore_TrafficInformation_StateInfo_Raw(qpb_ostream_t *const stream, const VisionCore_TrafficInformation_StateInfo_Raw *const data);
bool decode_VisionCore_TrafficInformation_StateInfo_Raw(qpb_istream_t *const stream, VisionCore_TrafficInformation_StateInfo_Raw *const data);
#define encode_VisionCore_TrafficInformation_StateInfo encode_VisionCore_TrafficInformation_StateInfo_Raw
#define decode_VisionCore_TrafficInformation_StateInfo decode_VisionCore_TrafficInformation_StateInfo_Raw

bool encode_VisionCore_TrafficInformation_ValidatedSign_Raw(qpb_ostream_t *const stream, const VisionCore_TrafficInformation_ValidatedSign_Raw *const data);
bool decode_VisionCore_TrafficInformation_ValidatedSign_Raw(qpb_istream_t *const stream, VisionCore_TrafficInformation_ValidatedSign_Raw *const data);
bool encode_VisionCore_TrafficInformation_ValidatedSign(qpb_ostream_t *const stream, const VisionCore_TrafficInformation_ValidatedSign *const data);
bool decode_VisionCore_TrafficInformation_ValidatedSign(qpb_istream_t *const stream, VisionCore_TrafficInformation_ValidatedSign *const data);

bool encode_VisionCore_TrafficInformation_ValidatedSignList_Raw(qpb_ostream_t *const stream, const VisionCore_TrafficInformation_ValidatedSignList_Raw *const data);
bool decode_VisionCore_TrafficInformation_ValidatedSignList_Raw(qpb_istream_t *const stream, VisionCore_TrafficInformation_ValidatedSignList_Raw *const data);
bool encode_VisionCore_TrafficInformation_ValidatedSignList(qpb_ostream_t *const stream, const VisionCore_TrafficInformation_ValidatedSignList *const data);
bool decode_VisionCore_TrafficInformation_ValidatedSignList(qpb_istream_t *const stream, VisionCore_TrafficInformation_ValidatedSignList *const data);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* VISIONCORE_TRAFFICINFORMATION_TRAFFICSIGNRECOGNITION_INCLUDED */
