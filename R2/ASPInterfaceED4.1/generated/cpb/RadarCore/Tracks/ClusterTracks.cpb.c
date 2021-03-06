/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "RadarCore/Tracks/ClusterTracks.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t RadarCore_Tracks_ClusterTrackPosition_fields[5] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, RadarCore_Tracks_ClusterTrackPosition, x, x, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackPosition, y, x, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackPosition, xStdDev, y, 0),
    PB_FIELD(  4, 32   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackPosition, yStdDev, xStdDev, 0),
    PB_LAST_FIELD
};

const pb_field_t RadarCore_Tracks_ClusterTrackModelBox_fields[6] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, RadarCore_Tracks_ClusterTrackModelBox, x, x, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackModelBox, y, x, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackModelBox, width, y, 0),
    PB_FIELD(  4, 32   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackModelBox, length, width, 0),
    PB_FIELD(  5, 40   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackModelBox, heading, length, 0),
    PB_LAST_FIELD
};

const pb_field_t RadarCore_Tracks_ClusterTrackMovement_fields[7] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, RadarCore_Tracks_ClusterTrackMovement, xVelocity, xVelocity, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackMovement, yVelocity, xVelocity, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackMovement, xVelocityStdDev, yVelocity, 0),
    PB_FIELD(  4, 32   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackMovement, yVelocityStdDev, xVelocityStdDev, 0),
    PB_FIELD(  5, 40   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackMovement, xAcceleration, yVelocityStdDev, 0),
    PB_FIELD(  6, 48   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrackMovement, yAcceleration, xAcceleration, 0),
    PB_LAST_FIELD
};

const pb_field_t RadarCore_Tracks_ClusterTrack_fields[16] = {
    PB_FIELD(  1, 8    , 1    , UINT32  , OPTIONAL, STATIC  , FIRST, RadarCore_Tracks_ClusterTrack, id, id, 0),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, closestPoint, id, &RadarCore_Tracks_ClusterTrackPosition_fields),
    PB_FIELD(  3, 26   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, boxModel, closestPoint, &RadarCore_Tracks_ClusterTrackModelBox_fields),
    PB_FIELD(  4, 34   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, movement, boxModel, &RadarCore_Tracks_ClusterTrackMovement_fields),
    PB_FIELD(  5, 40   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, lifetime, movement, 0),
    PB_FIELD(  6, 48   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, stationaryCounter, lifetime, 0),
    PB_FIELD(  7, 56   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, observationHistory, stationaryCounter, 0),
    PB_FIELD(  8, 64   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, motionClass, observationHistory, 0),
    PB_FIELD(  9, 72   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, type, motionClass, 0),
    PB_FIELD( 10, 80   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, confidence, type, 0),
    PB_FIELD( 11, 88   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, existanceProbability, confidence, 0),
    PB_FIELD( 12, 96   , 1    , UINT32  , REPEATED, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, objectClassConfidence, existanceProbability, 0),
    PB_FIELD( 13, 104  , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, elevation, objectClassConfidence, 0),
    PB_FIELD( 14, 112  , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, elevationConfidence, elevation, 0),
    PB_FIELD( 15, 120  , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, RadarCore_Tracks_ClusterTrack, qualityBits, elevationConfidence, 0),
    PB_LAST_FIELD
};

const pb_field_t RadarCore_Tracks_ClusterTrackList_fields[2] = {
    PB_FIELD(  1, 10   , 1    , MESSAGE , REPEATED, STATIC  , FIRST, RadarCore_Tracks_ClusterTrackList, tracks, tracks, 0),
    PB_LAST_FIELD
};

