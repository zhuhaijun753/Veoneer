/* Automatically generated pb header */
/* Generated by Protocol Buffers - 1 */

#ifndef ZENUITY_OPAQUE_MASTERCTOB_INCLUDED
#define ZENUITY_OPAQUE_MASTERCTOB_INCLUDED
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
#define Zenuity_Opaque_MasterCtoB_size                                                   (32)

/* Message IDs (where set with "identifier" option) */
#define Zenuity_Opaque_MasterCtoB_source                                                 1U
#define Zenuity_Opaque_MasterCtoB_identifier                                             52U
#define Zenuity_Opaque_MasterCtoB_majorVersion                                           1U
#define Zenuity_Opaque_MasterCtoB_minorVersion                                           0U

/* Struct definitions */
typedef PB_BYTES_ARRAY_T(30) Zenuity_Opaque_MasterCtoB_data_t;
typedef struct _Zenuity_Opaque_MasterCtoB {
    /** Data */
    Zenuity_Opaque_MasterCtoB_data_t data;
} Zenuity_Opaque_MasterCtoB;

/* Struct field encoding specification for pb */
extern const pb_field_t Zenuity_Opaque_MasterCtoB_fields[2];
#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_OPAQUE_MASTERCTOB_INCLUDED */