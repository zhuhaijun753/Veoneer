/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef VISIONCORE_ROAD_SCENECLASSIFICATION_TYPES_INCLUDED
#define VISIONCORE_ROAD_SCENECLASSIFICATION_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _VisionCore_Road_RoadClassificationResult_Raw {
    /** IsDetected
     * Describes if the scene includes the class or not
     */
    bool isDetected;
    /** Confidence
     * Classification confidence for the current frame
     * Unit: %
     * Min: 0
     * Max: 100
     */
    uint8_t confidence;
} VisionCore_Road_RoadClassificationResult_Raw;

#define VisionCore_Road_RoadClassificationResult VisionCore_Road_RoadClassificationResult_Raw

typedef struct _VisionCore_Road_RoadCover_Raw {
    /** Snow
     * Snow covered road
     */
    VisionCore_Road_RoadClassificationResult_Raw snow;
    /** Gravel
     * Gravel road
     */
    VisionCore_Road_RoadClassificationResult_Raw gravel;
    /** Wet
     * Wet road
     */
    VisionCore_Road_RoadClassificationResult_Raw wet;
} VisionCore_Road_RoadCover_Raw;

#define VisionCore_Road_RoadCover VisionCore_Road_RoadCover_Raw

typedef struct _VisionCore_Road_SceneClassification_Raw {
    /** RoadCover
     * Road cover classification result
     */
    VisionCore_Road_RoadCover_Raw roadCover;
    /** Tunnel
     * Tunnel classification result
     */
    VisionCore_Road_RoadClassificationResult_Raw tunnel;
    /** Fog
     * Fog classification result
     */
    VisionCore_Road_RoadClassificationResult_Raw fog;
} VisionCore_Road_SceneClassification_Raw;

#define VisionCore_Road_SceneClassification VisionCore_Road_SceneClassification_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* VISIONCORE_ROAD_SCENECLASSIFICATION_TYPES_INCLUDED */
