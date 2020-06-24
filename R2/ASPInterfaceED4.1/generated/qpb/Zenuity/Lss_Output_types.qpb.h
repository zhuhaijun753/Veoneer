/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_LSS_OUTPUT_TYPES_INCLUDED
#define ZENUITY_LSS_OUTPUT_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Enum definitions */
typedef enum _Zenuity_LaneSupportSystems_Side {
    Zenuity_LaneSupportSystems_Side_None = 0,
    Zenuity_LaneSupportSystems_Side_Left = 1,
    Zenuity_LaneSupportSystems_Side_Right = 2,
    Zenuity_LaneSupportSystems_Side_LeftAndRight = 3
} Zenuity_LaneSupportSystems_Side;
#define Zenuity_LaneSupportSystems_Side_MIN Zenuity_LaneSupportSystems_Side_None
#define Zenuity_LaneSupportSystems_Side_MAX Zenuity_LaneSupportSystems_Side_LeftAndRight
#define Zenuity_LaneSupportSystems_Side_ARRAYSIZE ((Zenuity_LaneSupportSystems_Side)(Zenuity_LaneSupportSystems_Side_LeftAndRight+1))

typedef enum _Zenuity_LaneSupportSystems_Status {
    Zenuity_LaneSupportSystems_Status_Disabled = 0,
    Zenuity_LaneSupportSystems_Status_Unavailable = 1,
    Zenuity_LaneSupportSystems_Status_Available = 2
} Zenuity_LaneSupportSystems_Status;
#define Zenuity_LaneSupportSystems_Status_MIN Zenuity_LaneSupportSystems_Status_Disabled
#define Zenuity_LaneSupportSystems_Status_MAX Zenuity_LaneSupportSystems_Status_Available
#define Zenuity_LaneSupportSystems_Status_ARRAYSIZE ((Zenuity_LaneSupportSystems_Status)(Zenuity_LaneSupportSystems_Status_Available+1))

/* Struct definitions */
typedef struct _Zenuity_LaneSupportSystems_SideAvailable_Raw {
    /** Left
     * Available left side
     */
    bool left;
    /** Right
     * Available right side
     */
    bool right;
} Zenuity_LaneSupportSystems_SideAvailable_Raw;

#define Zenuity_LaneSupportSystems_SideAvailable Zenuity_LaneSupportSystems_SideAvailable_Raw

typedef struct _Zenuity_LaneSupportSystems_FeatureOutput_Raw {
    /** Status
     * Information if feature is available
     */
    Zenuity_LaneSupportSystems_Status status;
    /** Available
     * Feature side dependent availability
     */
    Zenuity_LaneSupportSystems_SideAvailable_Raw available;
    /** WarningSide
     * Trigger warning for the feature
     */
    Zenuity_LaneSupportSystems_Side warningSide;
} Zenuity_LaneSupportSystems_FeatureOutput_Raw;

#define Zenuity_LaneSupportSystems_FeatureOutput Zenuity_LaneSupportSystems_FeatureOutput_Raw

typedef struct _Zenuity_LaneSupportSystems_LssOutput_Raw {
    /** Ldw
     * Feature output for LDW function
     */
    Zenuity_LaneSupportSystems_FeatureOutput_Raw ldw;
    /** Lka
     * Feature output for LKA function
     */
    Zenuity_LaneSupportSystems_FeatureOutput_Raw lka;
    /** ElkaRoadEdge
     * Feature output for eLKA Road Edge function
     */
    Zenuity_LaneSupportSystems_FeatureOutput_Raw elkaRoadEdge;
    /** ElkaFrontObjects
     * Feature output for eLKA Front Objects function (e.g. oncoming)
     */
    Zenuity_LaneSupportSystems_FeatureOutput_Raw elkaFrontObjects;
    /** ElkaRearObjects
     * Feature output for eLKA Rear Objects function (e.g. Blind Spot)
     */
    Zenuity_LaneSupportSystems_FeatureOutput_Raw elkaRearObjects;
    /** RequestPostEventMessage
     * Post event message request
     */
    bool requestPostEventMessage;
} Zenuity_LaneSupportSystems_LssOutput_Raw;

#define Zenuity_LaneSupportSystems_LssOutput Zenuity_LaneSupportSystems_LssOutput_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_LSS_OUTPUT_TYPES_INCLUDED */
