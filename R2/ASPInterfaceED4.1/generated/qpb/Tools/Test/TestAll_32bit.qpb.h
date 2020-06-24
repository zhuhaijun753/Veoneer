/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef TOOLS_TEST_TESTALL_32BIT_INCLUDED
#define TOOLS_TEST_TESTALL_32BIT_INCLUDED

#include "Tools/Test/TestAll_32bit_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
/* InterfacesTest_TestAllTypesPointers32Bit_static_size depends on runtime parameters */
#define InterfacesTest_TestAllTypesPointers32Bit_static_size                             12
#define InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_size (2)
#define InterfacesTest_SubSubMessage32Bit_size                                           (6)
#define InterfacesTest_TestAllTypes32Bit_size                                            (119)
#define InterfacesTest_TestAllTypesArray32Bit_size                                       (565)
#define InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_size                 ((8 + InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define InterfacesTest_SubMessage32Bit_size                                              ((24 + InterfacesTest_SubSubMessage32Bit_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define InterfacesTest_DeepSubMessage32Bit_size                                          ((269 + InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_size) + QPB_VARINT_MAX_ENCODED_SIZE)
#define InterfacesTest_MainMessage32Bit_size                                             ((5 + InterfacesTest_SubMessage32Bit_size + InterfacesTest_DeepSubMessage32Bit_size) + QPB_VARINT_MAX_ENCODED_SIZE)

/* Message IDs (where set with "identifier" option) */
#define InterfacesTest_TestAllTypes32Bit_source                                          2U
#define InterfacesTest_TestAllTypes32Bit_identifier                                      1234U
#define InterfacesTest_TestAllTypes32Bit_majorVersion                                    5U
#define InterfacesTest_TestAllTypes32Bit_minorVersion                                    2U
#define InterfacesTest_TestAllTypesArray32Bit_source                                     2U
#define InterfacesTest_TestAllTypesArray32Bit_identifier                                 12345U
#define InterfacesTest_TestAllTypesArray32Bit_majorVersion                               5U
#define InterfacesTest_TestAllTypesArray32Bit_minorVersion                               2U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_InterfacesTest_TestAllTypesPointers32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_TestAllTypesPointers32Bit_Raw *const data);
bool decode_InterfacesTest_TestAllTypesPointers32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_TestAllTypesPointers32Bit_Raw *const data);
#define encode_InterfacesTest_TestAllTypesPointers32Bit encode_InterfacesTest_TestAllTypesPointers32Bit_Raw
#define decode_InterfacesTest_TestAllTypesPointers32Bit decode_InterfacesTest_TestAllTypesPointers32Bit_Raw

bool encode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_Raw *const data);
bool decode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_Raw *const data);
#define encode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit encode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_Raw
#define decode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit decode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_SubMessageInSubMessage32Bit_Raw

bool encode_InterfacesTest_SubSubMessage32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_SubSubMessage32Bit_Raw *const data);
bool decode_InterfacesTest_SubSubMessage32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_SubSubMessage32Bit_Raw *const data);
#define encode_InterfacesTest_SubSubMessage32Bit encode_InterfacesTest_SubSubMessage32Bit_Raw
#define decode_InterfacesTest_SubSubMessage32Bit decode_InterfacesTest_SubSubMessage32Bit_Raw

bool encode_InterfacesTest_TestAllTypes32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_TestAllTypes32Bit_Raw *const data);
bool decode_InterfacesTest_TestAllTypes32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_TestAllTypes32Bit_Raw *const data);
bool encode_InterfacesTest_TestAllTypes32Bit(qpb_ostream_t *const stream, const InterfacesTest_TestAllTypes32Bit *const data);
bool decode_InterfacesTest_TestAllTypes32Bit(qpb_istream_t *const stream, InterfacesTest_TestAllTypes32Bit *const data);

bool encode_InterfacesTest_TestAllTypesArray32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_TestAllTypesArray32Bit_Raw *const data);
bool decode_InterfacesTest_TestAllTypesArray32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_TestAllTypesArray32Bit_Raw *const data);
bool encode_InterfacesTest_TestAllTypesArray32Bit(qpb_ostream_t *const stream, const InterfacesTest_TestAllTypesArray32Bit *const data);
bool decode_InterfacesTest_TestAllTypesArray32Bit(qpb_istream_t *const stream, InterfacesTest_TestAllTypesArray32Bit *const data);

bool encode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_Raw *const data);
bool decode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_Raw *const data);
#define encode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit encode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_Raw
#define decode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit decode_InterfacesTest_DeepSubMessage32Bit_MessageInSubMessage32Bit_Raw

bool encode_InterfacesTest_SubMessage32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_SubMessage32Bit_Raw *const data);
bool decode_InterfacesTest_SubMessage32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_SubMessage32Bit_Raw *const data);
#define encode_InterfacesTest_SubMessage32Bit encode_InterfacesTest_SubMessage32Bit_Raw
#define decode_InterfacesTest_SubMessage32Bit decode_InterfacesTest_SubMessage32Bit_Raw

bool encode_InterfacesTest_DeepSubMessage32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_DeepSubMessage32Bit_Raw *const data);
bool decode_InterfacesTest_DeepSubMessage32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_DeepSubMessage32Bit_Raw *const data);
#define encode_InterfacesTest_DeepSubMessage32Bit encode_InterfacesTest_DeepSubMessage32Bit_Raw
#define decode_InterfacesTest_DeepSubMessage32Bit decode_InterfacesTest_DeepSubMessage32Bit_Raw

bool encode_InterfacesTest_MainMessage32Bit_Raw(qpb_ostream_t *const stream, const InterfacesTest_MainMessage32Bit_Raw *const data);
bool decode_InterfacesTest_MainMessage32Bit_Raw(qpb_istream_t *const stream, InterfacesTest_MainMessage32Bit_Raw *const data);
#define encode_InterfacesTest_MainMessage32Bit encode_InterfacesTest_MainMessage32Bit_Raw
#define decode_InterfacesTest_MainMessage32Bit decode_InterfacesTest_MainMessage32Bit_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* TOOLS_TEST_TESTALL_32BIT_INCLUDED */
