/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef VISIONCORE_ROAD_ROADBOUNDARY_TYPES_INCLUDED
#define VISIONCORE_ROAD_ROADBOUNDARY_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _VisionCore_Road_RoadBoundaryTrackingStatus {
    VisionCore_Road_RoadBoundaryTrackingStatus_NotDetected = 0,
    VisionCore_Road_RoadBoundaryTrackingStatus_TrackedDetectedBoundary = 1,
    VisionCore_Road_RoadBoundaryTrackingStatus_CloseRangePredictedBoundary = 2,
    VisionCore_Road_RoadBoundaryTrackingStatus_FarRangePredictedBoundary = 3,
    VisionCore_Road_RoadBoundaryTrackingStatus_PredictedBoundary = 4
} VisionCore_Road_RoadBoundaryTrackingStatus;
#define VisionCore_Road_RoadBoundaryTrackingStatus_MIN VisionCore_Road_RoadBoundaryTrackingStatus_NotDetected
#define VisionCore_Road_RoadBoundaryTrackingStatus_MAX VisionCore_Road_RoadBoundaryTrackingStatus_PredictedBoundary
#define VisionCore_Road_RoadBoundaryTrackingStatus_ARRAYSIZE ((VisionCore_Road_RoadBoundaryTrackingStatus)(VisionCore_Road_RoadBoundaryTrackingStatus_PredictedBoundary+1))

/* Struct definitions */
typedef struct _VisionCore_Road_RoadBoundaryClothoid_Raw {
    /** LateralDistance
     * Lateral distance to the inside of the road boundary (default: 0)
     * Unit: m
     * Scale: 0.01
     * Min: -50
     * Max: 50
     */
    int16_t lateralDistance;
    /** Heading
     * The heading coefficient of the clothoid model
     * Unit: atan(rad)
     * Scale: 0.000025
     * Min: -0.8192
     * Max: 0.819175
     */
    int16_t heading;
    /** Curvature
     * Horizontal curvature for the start of the first clothoid
     * Unit: 1/m
     * Scale: 0.0000025
     * Min: -0.08192
     * Max: 0.0819175
     */
    int16_t curvature;
    /** CurvatureRate
     * Horizontal curvature rate for the first clothoid
     * Unit: 1/m²
     * Scale: 0.000001
     * Min: -0.032768
     * Max: 0.032767
     */
    int16_t curvatureRate;
} VisionCore_Road_RoadBoundaryClothoid_Raw;

typedef struct _VisionCore_Road_RoadBoundaryClothoid {
    /** LateralDistance
     * Lateral distance to the inside of the road boundary (default: 0)
     * Unit: m
     * Resolution: 0.01
     * Min: -50
     * Max: 50
     */
    float lateralDistance;
    /** Heading
     * The heading coefficient of the clothoid model
     * Unit: atan(rad)
     * Resolution: 0.000025
     * Min: -0.8192
     * Max: 0.819175
     */
    float heading;
    /** Curvature
     * Horizontal curvature for the start of the first clothoid
     * Unit: 1/m
     * Resolution: 0.0000025
     * Min: -0.08192
     * Max: 0.0819175
     */
    float curvature;
    /** CurvatureRate
     * Horizontal curvature rate for the first clothoid
     * Unit: 1/m²
     * Resolution: 0.000001
     * Min: -0.032768
     * Max: 0.032767
     */
    float curvatureRate;
} VisionCore_Road_RoadBoundaryClothoid;

typedef struct _VisionCore_Road_RoadBoundaryClothoidVariance_Raw {
    /** LateralDistanceVariance
     * Variance for lateral distance
     * Unit: 1/m²
     * Scale: 0.01
     * Min: -327.68
     * Max: 327.67
     */
    int16_t lateralDistanceVariance;
    /** HeadingVariance
     * Variance for heading
     * Unit: atan(rad)²
     * Scale: 0.000025
     * Min: -0.8192
     * Max: 0.819175
     */
    int16_t headingVariance;
    /** CurvatureVariance
     * Variance for curvature
     * Unit: 1/m²
     * Scale: 0.0000025
     * Min: -0.08192
     * Max: 0.0819175
     */
    int16_t curvatureVariance;
    /** CurvatureRateVariance
     * Variance for curvature rate
     * Unit: 1/m^4
     * Scale: 0.000001
     * Min: -0.032768
     * Max: 0.032767
     */
    int16_t curvatureRateVariance;
} VisionCore_Road_RoadBoundaryClothoidVariance_Raw;

typedef struct _VisionCore_Road_RoadBoundaryClothoidVariance {
    /** LateralDistanceVariance
     * Variance for lateral distance
     * Unit: 1/m²
     * Resolution: 0.01
     * Min: -327.68
     * Max: 327.67
     */
    float lateralDistanceVariance;
    /** HeadingVariance
     * Variance for heading
     * Unit: atan(rad)²
     * Resolution: 0.000025
     * Min: -0.8192
     * Max: 0.819175
     */
    float headingVariance;
    /** CurvatureVariance
     * Variance for curvature
     * Unit: 1/m²
     * Resolution: 0.0000025
     * Min: -0.08192
     * Max: 0.0819175
     */
    float curvatureVariance;
    /** CurvatureRateVariance
     * Variance for curvature rate
     * Unit: 1/m^4
     * Resolution: 0.000001
     * Min: -0.032768
     * Max: 0.032767
     */
    float curvatureRateVariance;
} VisionCore_Road_RoadBoundaryClothoidVariance;

typedef struct _VisionCore_Road_RoadBoundaryTrack_Raw {
    /** Valid
     * True means that RoadBoundaryTrack describes a valid road boundary
     */
    bool valid;
    /** Id
     * ID nr (default: 255 = SNA, propose change to 0)
     * Min: 0
     * Max: 255
     */
    uint8_t id;
    /** DetectionDistance
     * Longitudinal distance for which the Road Boundary is detected
     * Unit: m
     * Scale: 0.1
     * Min: 0
     * Max: 150
     */
    uint16_t detectionDistance;
    /** TrackingStatus
     * Describes detection status
     */
    VisionCore_Road_RoadBoundaryTrackingStatus trackingStatus;
    /** ModelError
     * Describes how well the measurements are adapted to the model. Mean square deviation between measurements and model points.
     * Unit: m
     * Scale: 0.01
     * Min: 0
     * Max: 2.55
     */
    uint8_t modelError;
    /** MeasurementQuality
     * Describes quality of the detection
     * Unit: %
     * Min: 0
     * Max: 100
     */
    uint8_t measurementQuality;
    /** Clothoid
     * Describes road boundary clothoid
     */
    VisionCore_Road_RoadBoundaryClothoid_Raw clothoid;
    /** IsSafe
     * True means that the track is safe to use
     */
    bool isSafe;
    /** ClothoidVariance
     * Describes road boundary clothoid variance
     */
    VisionCore_Road_RoadBoundaryClothoidVariance_Raw clothoidVariance;
} VisionCore_Road_RoadBoundaryTrack_Raw;

typedef struct _VisionCore_Road_RoadBoundaryTrack {
    /** Valid
     * True means that RoadBoundaryTrack describes a valid road boundary
     */
    bool valid;
    /** Id
     * ID nr (default: 255 = SNA, propose change to 0)
     * Min: 0
     * Max: 255
     */
    uint8_t id;
    /** DetectionDistance
     * Longitudinal distance for which the Road Boundary is detected
     * Unit: m
     * Resolution: 0.1
     * Min: 0
     * Max: 150
     */
    float detectionDistance;
    /** TrackingStatus
     * Describes detection status
     */
    VisionCore_Road_RoadBoundaryTrackingStatus trackingStatus;
    /** ModelError
     * Describes how well the measurements are adapted to the model. Mean square deviation between measurements and model points.
     * Unit: m
     * Resolution: 0.01
     * Min: 0
     * Max: 2.55
     */
    float modelError;
    /** MeasurementQuality
     * Describes quality of the detection
     * Unit: %
     * Min: 0
     * Max: 100
     */
    uint8_t measurementQuality;
    /** Clothoid
     * Describes road boundary clothoid
     */
    VisionCore_Road_RoadBoundaryClothoid clothoid;
    /** IsSafe
     * True means that the track is safe to use
     */
    bool isSafe;
    /** ClothoidVariance
     * Describes road boundary clothoid variance
     */
    VisionCore_Road_RoadBoundaryClothoidVariance clothoidVariance;
} VisionCore_Road_RoadBoundaryTrack;

typedef struct _VisionCore_Road_RoadBoundary_Raw {
    /** LeftTraversableRoadBoundary
     * The left traversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack_Raw leftTraversableRoadBoundary;
    /** RightTraversableRoadBoundary
     * The right traversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack_Raw rightTraversableRoadBoundary;
    /** LeftNonTraversableRoadBoundary
     * The left nontraversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack_Raw leftNonTraversableRoadBoundary;
    /** RightNonTraversableRoadBoundary
     * The right nontraversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack_Raw rightNonTraversableRoadBoundary;
} VisionCore_Road_RoadBoundary_Raw;

typedef struct _VisionCore_Road_RoadBoundary {
    /** LeftTraversableRoadBoundary
     * The left traversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack leftTraversableRoadBoundary;
    /** RightTraversableRoadBoundary
     * The right traversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack rightTraversableRoadBoundary;
    /** LeftNonTraversableRoadBoundary
     * The left nontraversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack leftNonTraversableRoadBoundary;
    /** RightNonTraversableRoadBoundary
     * The right nontraversable road boundary
     */
    VisionCore_Road_RoadBoundaryTrack rightNonTraversableRoadBoundary;
} VisionCore_Road_RoadBoundary;

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* VISIONCORE_ROAD_ROADBOUNDARY_TYPES_INCLUDED */
