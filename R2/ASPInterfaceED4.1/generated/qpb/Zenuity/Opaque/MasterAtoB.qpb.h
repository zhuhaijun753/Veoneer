/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_OPAQUE_MASTERATOB_INCLUDED
#define ZENUITY_OPAQUE_MASTERATOB_INCLUDED

#include "Zenuity/Opaque/MasterAtoB_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define Zenuity_Opaque_MasterAtoB_size                                                   (20484)

/* Message IDs (where set with "identifier" option) */
#define Zenuity_Opaque_MasterAtoB_source                                                 1U
#define Zenuity_Opaque_MasterAtoB_identifier                                             50U
#define Zenuity_Opaque_MasterAtoB_majorVersion                                           1U
#define Zenuity_Opaque_MasterAtoB_minorVersion                                           0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_Zenuity_Opaque_MasterAtoB_Raw(qpb_ostream_t *const stream, const Zenuity_Opaque_MasterAtoB_Raw *const data);
bool decode_Zenuity_Opaque_MasterAtoB_Raw(qpb_istream_t *const stream, Zenuity_Opaque_MasterAtoB_Raw *const data);
#define encode_Zenuity_Opaque_MasterAtoB encode_Zenuity_Opaque_MasterAtoB_Raw
#define decode_Zenuity_Opaque_MasterAtoB decode_Zenuity_Opaque_MasterAtoB_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_OPAQUE_MASTERATOB_INCLUDED */
