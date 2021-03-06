/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "VisionCore/Road/LaneOutput.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t VisionCore_Road_LaneEvent_fields[6] = {
    PB_FIELD(  1, 8    , 1    , UINT32  , OPTIONAL, STATIC  , FIRST, VisionCore_Road_LaneEvent, id, id, 0),
    PB_FIELD(  2, 16   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneEvent, laneTrackId, id, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneEvent, distance, laneTrackId, 0),
    PB_FIELD(  4, 32   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneEvent, eventType, distance, 0),
    PB_FIELD(  5, 40   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneEvent, side, eventType, 0),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_Clothoid_fields[8] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, VisionCore_Road_Clothoid, lateralDistance, lateralDistance, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_Clothoid, heading, lateralDistance, 0),
    PB_FIELD(  3, 24   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_Clothoid, curvature, heading, 0),
    PB_FIELD(  4, 32   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_Clothoid, curvatureRate, curvature, 0),
    PB_FIELD(  5, 40   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_Clothoid, transitionDistance, curvatureRate, 0),
    PB_FIELD(  6, 48   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_Clothoid, curvatureRateSecondClothoid, transitionDistance, 0),
    PB_FIELD(  7, 56   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_Clothoid, secondClothoidActive, curvatureRateSecondClothoid, 0),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_ClothoidVariance_fields[6] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, VisionCore_Road_ClothoidVariance, lateralDistanceVariance, lateralDistanceVariance, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_ClothoidVariance, headingVariance, lateralDistanceVariance, 0),
    PB_FIELD(  3, 24   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_ClothoidVariance, curvatureVariance, headingVariance, 0),
    PB_FIELD(  4, 32   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_ClothoidVariance, curvatureRateVariance, curvatureVariance, 0),
    PB_FIELD(  5, 40   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_ClothoidVariance, curvatureRateSecondClothoidVariance, curvatureRateVariance, 0),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_LaneTrack_fields[21] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, VisionCore_Road_LaneTrack, valid, valid, 0),
    PB_FIELD(  2, 16   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, id, valid, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, detectionDistance, id, 0),
    PB_FIELD(  4, 32   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, markingType, detectionDistance, 0),
    PB_FIELD(  5, 40   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, markingLength, markingType, 0),
    PB_FIELD(  6, 48   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, gapLength, markingLength, 0),
    PB_FIELD(  7, 56   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, secondMarkingType, gapLength, 0),
    PB_FIELD(  8, 64   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, markingStructure, secondMarkingType, 0),
    PB_FIELD(  9, 72   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, trackingStatus, markingStructure, 0),
    PB_FIELD( 10, 80   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, markingWidth, trackingStatus, 0),
    PB_FIELD( 11, 88   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, totalMarkingWidth, markingWidth, 0),
    PB_FIELD( 12, 96   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, color, totalMarkingWidth, 0),
    PB_FIELD( 13, 104  , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, modelError, color, 0),
    PB_FIELD( 14, 112  , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, measurementQuality, modelError, 0),
    PB_FIELD( 15, 120  , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, selectionConfidence, measurementQuality, 0),
    PB_FIELD( 16, 128  , 2    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, distanceFirstToSecondMarking, selectionConfidence, 0),
    PB_FIELD( 17, 138  , 2    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, clothoid, distanceFirstToSecondMarking, &VisionCore_Road_Clothoid_fields),
    PB_FIELD( 18, 144  , 2    , BOOL    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, isSafe, clothoid, 0),
    PB_FIELD( 19, 152  , 2    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, unsafeReason, isSafe, 0),
    PB_FIELD( 20, 162  , 2    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneTrack, clothoidVariance, unsafeReason, &VisionCore_Road_ClothoidVariance_fields),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_TemporaryMarkings_fields[3] = {
    PB_FIELD(  1, 8    , 1    , ENUM    , OPTIONAL, STATIC  , FIRST, VisionCore_Road_TemporaryMarkings, type, type, 0),
    PB_FIELD(  2, 16   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_TemporaryMarkings, longitudinalDistance, type, 0),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_EgoLane_fields[4] = {
    PB_FIELD(  1, 10   , 1    , MESSAGE , OPTIONAL, STATIC  , FIRST, VisionCore_Road_EgoLane, left, left, &VisionCore_Road_LaneTrack_fields),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_EgoLane, right, left, &VisionCore_Road_LaneTrack_fields),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_EgoLane, parallelDistance, right, 0),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_LaneOutput_fields[14] = {
    PB_FIELD(  1, 10   , 1    , MESSAGE , OPTIONAL, STATIC  , FIRST, VisionCore_Road_LaneOutput, egoLane, egoLane, &VisionCore_Road_EgoLane_fields),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, coupledEgoLane, egoLane, &VisionCore_Road_EgoLane_fields),
    PB_FIELD(  3, 26   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, neighborLeft, coupledEgoLane, &VisionCore_Road_LaneTrack_fields),
    PB_FIELD(  4, 34   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, neighborRight, neighborLeft, &VisionCore_Road_LaneTrack_fields),
    PB_FIELD(  5, 42   , 1    , MESSAGE , REPEATED, STATIC  , OTHER, VisionCore_Road_LaneOutput, events, neighborRight, 0),
    PB_FIELD(  6, 50   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, temporaryMarkings, events, &VisionCore_Road_TemporaryMarkings_fields),
    PB_FIELD(  7, 56   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, sideSuggestion, temporaryMarkings, 0),
    PB_FIELD(  8, 64   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, laneChange, sideSuggestion, 0),
    PB_FIELD(  9, 72   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, frameDrop, laneChange, 0),
    PB_FIELD( 10, 80   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, blockageDuration, frameDrop, 0),
    PB_FIELD( 11, 88   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, selfAssessmentFailed, blockageDuration, 0),
    PB_FIELD( 12, 96   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, attentionMarkers, selfAssessmentFailed, 0),
    PB_FIELD( 13, 104  , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_LaneOutput, operationMode, attentionMarkers, 0),
    PB_LAST_FIELD
};

