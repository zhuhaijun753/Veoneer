/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_CALONG_AEBOUTPUT_INCLUDED
#define ZENUITY_CALONG_AEBOUTPUT_INCLUDED

#include "Zenuity/CaLong_AebOutput_types.qpb.h"

#include "VisionCore/Common/Coords.qpb.h"

#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define Zenuity_CaLong_AebRequest_size                                                   (5)
#define Zenuity_CaLong_CollisionForwardWarningControl_size                               ((25 + VisionCore_Common_Coord2_m_0_01_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define Zenuity_CaLong_CollisionMitigationBrakeRequest_size                              (7)
#define Zenuity_CaLong_StaticDistanceWarningOutput_size                                  (8)
#define Zenuity_CaLong_TimeToThreat_size                                                 (8)
#define Zenuity_CaLong_VruAebOutput_size                                                 (5)
#define Zenuity_CaLong_CollisionMitigationThreatInformation_size                         ((17 + Zenuity_CaLong_TimeToThreat_size + Zenuity_CaLong_AebRequest_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define Zenuity_CaLong_CollisionMitigationSystem_size                                    ((4 + Zenuity_CaLong_CollisionForwardWarningControl_size + Zenuity_CaLong_CollisionMitigationThreatInformation_size) + QPB_VARINT_MAX_ENCODED_SIZE)

/* Message IDs (where set with "identifier" option) */
#define Zenuity_CaLong_CollisionMitigationBrakeRequest_source                            1U
#define Zenuity_CaLong_CollisionMitigationBrakeRequest_identifier                        4U
#define Zenuity_CaLong_CollisionMitigationBrakeRequest_majorVersion                      1U
#define Zenuity_CaLong_CollisionMitigationBrakeRequest_minorVersion                      0U
#define Zenuity_CaLong_CollisionMitigationSystem_source                                  1U
#define Zenuity_CaLong_CollisionMitigationSystem_identifier                              1U
#define Zenuity_CaLong_CollisionMitigationSystem_majorVersion                            2U
#define Zenuity_CaLong_CollisionMitigationSystem_minorVersion                            3U
#define Zenuity_CaLong_VruAebOutput_source                                               1U
#define Zenuity_CaLong_VruAebOutput_identifier                                           2U
#define Zenuity_CaLong_VruAebOutput_majorVersion                                         1U
#define Zenuity_CaLong_VruAebOutput_minorVersion                                         0U
#define Zenuity_CaLong_StaticDistanceWarningOutput_source                                1U
#define Zenuity_CaLong_StaticDistanceWarningOutput_identifier                            3U
#define Zenuity_CaLong_StaticDistanceWarningOutput_majorVersion                          1U
#define Zenuity_CaLong_StaticDistanceWarningOutput_minorVersion                          0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_Zenuity_CaLong_AebRequest_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_AebRequest_Raw *const data);
bool decode_Zenuity_CaLong_AebRequest_Raw(qpb_istream_t *const stream, Zenuity_CaLong_AebRequest_Raw *const data);
bool encode_Zenuity_CaLong_AebRequest(qpb_ostream_t *const stream, const Zenuity_CaLong_AebRequest *const data);
bool decode_Zenuity_CaLong_AebRequest(qpb_istream_t *const stream, Zenuity_CaLong_AebRequest *const data);

bool encode_Zenuity_CaLong_CollisionForwardWarningControl_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionForwardWarningControl_Raw *const data);
bool decode_Zenuity_CaLong_CollisionForwardWarningControl_Raw(qpb_istream_t *const stream, Zenuity_CaLong_CollisionForwardWarningControl_Raw *const data);
bool encode_Zenuity_CaLong_CollisionForwardWarningControl(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionForwardWarningControl *const data);
bool decode_Zenuity_CaLong_CollisionForwardWarningControl(qpb_istream_t *const stream, Zenuity_CaLong_CollisionForwardWarningControl *const data);

bool encode_Zenuity_CaLong_CollisionMitigationBrakeRequest_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionMitigationBrakeRequest_Raw *const data);
bool decode_Zenuity_CaLong_CollisionMitigationBrakeRequest_Raw(qpb_istream_t *const stream, Zenuity_CaLong_CollisionMitigationBrakeRequest_Raw *const data);
bool encode_Zenuity_CaLong_CollisionMitigationBrakeRequest(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionMitigationBrakeRequest *const data);
bool decode_Zenuity_CaLong_CollisionMitigationBrakeRequest(qpb_istream_t *const stream, Zenuity_CaLong_CollisionMitigationBrakeRequest *const data);

bool encode_Zenuity_CaLong_StaticDistanceWarningOutput_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_StaticDistanceWarningOutput_Raw *const data);
bool decode_Zenuity_CaLong_StaticDistanceWarningOutput_Raw(qpb_istream_t *const stream, Zenuity_CaLong_StaticDistanceWarningOutput_Raw *const data);
bool encode_Zenuity_CaLong_StaticDistanceWarningOutput(qpb_ostream_t *const stream, const Zenuity_CaLong_StaticDistanceWarningOutput *const data);
bool decode_Zenuity_CaLong_StaticDistanceWarningOutput(qpb_istream_t *const stream, Zenuity_CaLong_StaticDistanceWarningOutput *const data);

bool encode_Zenuity_CaLong_TimeToThreat_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_TimeToThreat_Raw *const data);
bool decode_Zenuity_CaLong_TimeToThreat_Raw(qpb_istream_t *const stream, Zenuity_CaLong_TimeToThreat_Raw *const data);
bool encode_Zenuity_CaLong_TimeToThreat(qpb_ostream_t *const stream, const Zenuity_CaLong_TimeToThreat *const data);
bool decode_Zenuity_CaLong_TimeToThreat(qpb_istream_t *const stream, Zenuity_CaLong_TimeToThreat *const data);

bool encode_Zenuity_CaLong_VruAebOutput_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_VruAebOutput_Raw *const data);
bool decode_Zenuity_CaLong_VruAebOutput_Raw(qpb_istream_t *const stream, Zenuity_CaLong_VruAebOutput_Raw *const data);
bool encode_Zenuity_CaLong_VruAebOutput(qpb_ostream_t *const stream, const Zenuity_CaLong_VruAebOutput *const data);
bool decode_Zenuity_CaLong_VruAebOutput(qpb_istream_t *const stream, Zenuity_CaLong_VruAebOutput *const data);

bool encode_Zenuity_CaLong_CollisionMitigationThreatInformation_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionMitigationThreatInformation_Raw *const data);
bool decode_Zenuity_CaLong_CollisionMitigationThreatInformation_Raw(qpb_istream_t *const stream, Zenuity_CaLong_CollisionMitigationThreatInformation_Raw *const data);
bool encode_Zenuity_CaLong_CollisionMitigationThreatInformation(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionMitigationThreatInformation *const data);
bool decode_Zenuity_CaLong_CollisionMitigationThreatInformation(qpb_istream_t *const stream, Zenuity_CaLong_CollisionMitigationThreatInformation *const data);

bool encode_Zenuity_CaLong_CollisionMitigationSystem_Raw(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionMitigationSystem_Raw *const data);
bool decode_Zenuity_CaLong_CollisionMitigationSystem_Raw(qpb_istream_t *const stream, Zenuity_CaLong_CollisionMitigationSystem_Raw *const data);
bool encode_Zenuity_CaLong_CollisionMitigationSystem(qpb_ostream_t *const stream, const Zenuity_CaLong_CollisionMitigationSystem *const data);
bool decode_Zenuity_CaLong_CollisionMitigationSystem(qpb_istream_t *const stream, Zenuity_CaLong_CollisionMitigationSystem *const data);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_CALONG_AEBOUTPUT_INCLUDED */
