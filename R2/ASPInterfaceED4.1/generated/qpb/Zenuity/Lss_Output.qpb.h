/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_LSS_OUTPUT_INCLUDED
#define ZENUITY_LSS_OUTPUT_INCLUDED

#include "Zenuity/Lss_Output_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define Zenuity_LaneSupportSystems_SideAvailable_size                                    (4)
#define Zenuity_LaneSupportSystems_FeatureOutput_size                                    ((6 + Zenuity_LaneSupportSystems_SideAvailable_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define Zenuity_LaneSupportSystems_LssOutput_size                                        ((12 + Zenuity_LaneSupportSystems_FeatureOutput_size + Zenuity_LaneSupportSystems_FeatureOutput_size + Zenuity_LaneSupportSystems_FeatureOutput_size + Zenuity_LaneSupportSystems_FeatureOutput_size + Zenuity_LaneSupportSystems_FeatureOutput_size) + QPB_VARINT_MAX_ENCODED_SIZE)

/* Message IDs (where set with "identifier" option) */
#define Zenuity_LaneSupportSystems_LssOutput_source                                      1U
#define Zenuity_LaneSupportSystems_LssOutput_identifier                                  20U
#define Zenuity_LaneSupportSystems_LssOutput_majorVersion                                1U
#define Zenuity_LaneSupportSystems_LssOutput_minorVersion                                0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_Zenuity_LaneSupportSystems_SideAvailable_Raw(qpb_ostream_t *const stream, const Zenuity_LaneSupportSystems_SideAvailable_Raw *const data);
bool decode_Zenuity_LaneSupportSystems_SideAvailable_Raw(qpb_istream_t *const stream, Zenuity_LaneSupportSystems_SideAvailable_Raw *const data);
#define encode_Zenuity_LaneSupportSystems_SideAvailable encode_Zenuity_LaneSupportSystems_SideAvailable_Raw
#define decode_Zenuity_LaneSupportSystems_SideAvailable decode_Zenuity_LaneSupportSystems_SideAvailable_Raw

bool encode_Zenuity_LaneSupportSystems_FeatureOutput_Raw(qpb_ostream_t *const stream, const Zenuity_LaneSupportSystems_FeatureOutput_Raw *const data);
bool decode_Zenuity_LaneSupportSystems_FeatureOutput_Raw(qpb_istream_t *const stream, Zenuity_LaneSupportSystems_FeatureOutput_Raw *const data);
#define encode_Zenuity_LaneSupportSystems_FeatureOutput encode_Zenuity_LaneSupportSystems_FeatureOutput_Raw
#define decode_Zenuity_LaneSupportSystems_FeatureOutput decode_Zenuity_LaneSupportSystems_FeatureOutput_Raw

bool encode_Zenuity_LaneSupportSystems_LssOutput_Raw(qpb_ostream_t *const stream, const Zenuity_LaneSupportSystems_LssOutput_Raw *const data);
bool decode_Zenuity_LaneSupportSystems_LssOutput_Raw(qpb_istream_t *const stream, Zenuity_LaneSupportSystems_LssOutput_Raw *const data);
#define encode_Zenuity_LaneSupportSystems_LssOutput encode_Zenuity_LaneSupportSystems_LssOutput_Raw
#define decode_Zenuity_LaneSupportSystems_LssOutput decode_Zenuity_LaneSupportSystems_LssOutput_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_LSS_OUTPUT_INCLUDED */
