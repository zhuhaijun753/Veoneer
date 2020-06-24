/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef RADARCORE_TRACKS_REARCLUSTERTRACKS_INCLUDED
#define RADARCORE_TRACKS_REARCLUSTERTRACKS_INCLUDED

#include "RadarCore/Tracks/RearClusterTracks_types.qpb.h"

#include "RadarCore/Tracks/ClusterTracks.qpb.h"

#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define RadarCore_Tracks_RearClusterTrack_size                                           ((12 + RadarCore_Tracks_ClusterTrackPosition_size + RadarCore_Tracks_ClusterTrackModelBox_size + RadarCore_Tracks_ClusterTrackMovement_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define RadarCore_Tracks_RearClusterTrackList_size                                       (940)

/* Message IDs (where set with "identifier" option) */
#define RadarCore_Tracks_RearClusterTrackList_source                                     4U
#define RadarCore_Tracks_RearClusterTrackList_identifier                                 12U
#define RadarCore_Tracks_RearClusterTrackList_majorVersion                               1U
#define RadarCore_Tracks_RearClusterTrackList_minorVersion                               0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_RadarCore_Tracks_RearClusterTrack_Raw(qpb_ostream_t *const stream, const RadarCore_Tracks_RearClusterTrack_Raw *const data);
bool decode_RadarCore_Tracks_RearClusterTrack_Raw(qpb_istream_t *const stream, RadarCore_Tracks_RearClusterTrack_Raw *const data);
bool encode_RadarCore_Tracks_RearClusterTrack(qpb_ostream_t *const stream, const RadarCore_Tracks_RearClusterTrack *const data);
bool decode_RadarCore_Tracks_RearClusterTrack(qpb_istream_t *const stream, RadarCore_Tracks_RearClusterTrack *const data);

bool encode_RadarCore_Tracks_RearClusterTrackList_Raw(qpb_ostream_t *const stream, const RadarCore_Tracks_RearClusterTrackList_Raw *const data);
bool decode_RadarCore_Tracks_RearClusterTrackList_Raw(qpb_istream_t *const stream, RadarCore_Tracks_RearClusterTrackList_Raw *const data);
bool encode_RadarCore_Tracks_RearClusterTrackList(qpb_ostream_t *const stream, const RadarCore_Tracks_RearClusterTrackList *const data);
bool decode_RadarCore_Tracks_RearClusterTrackList(qpb_istream_t *const stream, RadarCore_Tracks_RearClusterTrackList *const data);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* RADARCORE_TRACKS_REARCLUSTERTRACKS_INCLUDED */
