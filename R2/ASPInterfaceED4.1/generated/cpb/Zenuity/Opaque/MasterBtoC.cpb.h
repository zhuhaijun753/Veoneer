/* Automatically generated pb header */
/* Generated by Protocol Buffers - 1 */

#ifndef ZENUITY_OPAQUE_MASTERBTOC_INCLUDED
#define ZENUITY_OPAQUE_MASTERBTOC_INCLUDED
#include "Tools/CProtobuf/pb.h"
#include "Tools/CProtobuf/pb_decode.h"
#include "Tools/CProtobuf/pb_encode.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define Zenuity_Opaque_MasterBtoC_size                                                   (183)

/* Message IDs (where set with "identifier" option) */
#define Zenuity_Opaque_MasterBtoC_source                                                 1U
#define Zenuity_Opaque_MasterBtoC_identifier                                             51U
#define Zenuity_Opaque_MasterBtoC_majorVersion                                           1U
#define Zenuity_Opaque_MasterBtoC_minorVersion                                           0U

/* Struct definitions */
typedef PB_BYTES_ARRAY_T(180) Zenuity_Opaque_MasterBtoC_data_t;
typedef struct _Zenuity_Opaque_MasterBtoC {
    /** Data */
    Zenuity_Opaque_MasterBtoC_data_t data;
} Zenuity_Opaque_MasterBtoC;

/* Struct field encoding specification for pb */
extern const pb_field_t Zenuity_Opaque_MasterBtoC_fields[2];
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_OPAQUE_MASTERBTOC_INCLUDED */