/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "VisionCore/Road/RoadBoundary.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t VisionCore_Road_RoadBoundaryClothoid_fields[5] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, VisionCore_Road_RoadBoundaryClothoid, lateralDistance, lateralDistance, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryClothoid, heading, lateralDistance, 0),
    PB_FIELD(  3, 24   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryClothoid, curvature, heading, 0),
    PB_FIELD(  4, 32   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryClothoid, curvatureRate, curvature, 0),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_RoadBoundaryClothoidVariance_fields[5] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, VisionCore_Road_RoadBoundaryClothoidVariance, lateralDistanceVariance, lateralDistanceVariance, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryClothoidVariance, headingVariance, lateralDistanceVariance, 0),
    PB_FIELD(  3, 24   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryClothoidVariance, curvatureVariance, headingVariance, 0),
    PB_FIELD(  4, 32   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryClothoidVariance, curvatureRateVariance, curvatureVariance, 0),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_RoadBoundaryTrack_fields[10] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, VisionCore_Road_RoadBoundaryTrack, valid, valid, 0),
    PB_FIELD(  2, 16   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, id, valid, 0),
    PB_FIELD(  3, 24   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, detectionDistance, id, 0),
    PB_FIELD(  4, 32   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, trackingStatus, detectionDistance, 0),
    PB_FIELD(  5, 40   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, modelError, trackingStatus, 0),
    PB_FIELD(  6, 48   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, measurementQuality, modelError, 0),
    PB_FIELD(  7, 58   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, clothoid, measurementQuality, &VisionCore_Road_RoadBoundaryClothoid_fields),
    PB_FIELD(  8, 64   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, isSafe, clothoid, 0),
    PB_FIELD(  9, 74   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundaryTrack, clothoidVariance, isSafe, &VisionCore_Road_RoadBoundaryClothoidVariance_fields),
    PB_LAST_FIELD
};

const pb_field_t VisionCore_Road_RoadBoundary_fields[5] = {
    PB_FIELD(  1, 10   , 1    , MESSAGE , OPTIONAL, STATIC  , FIRST, VisionCore_Road_RoadBoundary, leftTraversableRoadBoundary, leftTraversableRoadBoundary, &VisionCore_Road_RoadBoundaryTrack_fields),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundary, rightTraversableRoadBoundary, leftTraversableRoadBoundary, &VisionCore_Road_RoadBoundaryTrack_fields),
    PB_FIELD(  3, 26   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundary, leftNonTraversableRoadBoundary, rightTraversableRoadBoundary, &VisionCore_Road_RoadBoundaryTrack_fields),
    PB_FIELD(  4, 34   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, VisionCore_Road_RoadBoundary, rightNonTraversableRoadBoundary, leftNonTraversableRoadBoundary, &VisionCore_Road_RoadBoundaryTrack_fields),
    PB_LAST_FIELD
};
