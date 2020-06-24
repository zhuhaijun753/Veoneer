/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_DEBUG_LSS_DEBUG_TYPES_INCLUDED
#define ZENUITY_DEBUG_LSS_DEBUG_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"


#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _Zenuity_Debug_SideReason_Raw {
    /** Left
     * Bitfield for left side
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t left;
    /** Right
     * Bitfield for right side
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t right;
} Zenuity_Debug_SideReason_Raw;

#define Zenuity_Debug_SideReason Zenuity_Debug_SideReason_Raw

typedef struct _Zenuity_Debug_FeatureDebug_Raw {
    /** AvailableReason
     * Bitfields for available reason
     */
    Zenuity_Debug_SideReason_Raw availableReason;
    /** SuppressReason
     * Bitfields for suppress reason
     */
    Zenuity_Debug_SideReason_Raw suppressReason;
    /** AbortReason
     * Bitfield for abort reason
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t abortReason;
} Zenuity_Debug_FeatureDebug_Raw;

#define Zenuity_Debug_FeatureDebug Zenuity_Debug_FeatureDebug_Raw

typedef struct _Zenuity_Debug_LateralSupportSystemsDiagnostics_Raw {
    /** Ldw
     * Feature debug for LDW function
     */
    Zenuity_Debug_FeatureDebug_Raw ldw;
    /** Lka
     * Feature debug for LKA function
     */
    Zenuity_Debug_FeatureDebug_Raw lka;
    /** ElkaRoadEdge
     * Feature debug for eLKA Road Edge function
     */
    Zenuity_Debug_FeatureDebug_Raw elkaRoadEdge;
    /** ElkaFrontObjects
     * Feature debug for eLKA Front Objects function (e.g. oncoming)
     */
    Zenuity_Debug_FeatureDebug_Raw elkaFrontObjects;
    /** ElkaRearObjects
     * Feature debug for eLKA Rear Objects function (e.g. Blind Spot)
     */
    Zenuity_Debug_FeatureDebug_Raw elkaRearObjects;
} Zenuity_Debug_LateralSupportSystemsDiagnostics_Raw;

#define Zenuity_Debug_LateralSupportSystemsDiagnostics Zenuity_Debug_LateralSupportSystemsDiagnostics_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_DEBUG_LSS_DEBUG_TYPES_INCLUDED */