/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef SYSTEMCORE_HEADERS_INTERFACEHEADER_INCLUDED
#define SYSTEMCORE_HEADERS_INTERFACEHEADER_INCLUDED

#include "SystemCore/Headers/InterfaceHeader_types.qpb.h"

#include "SystemCore/Headers/DataHeader.qpb.h"

#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
/* SystemCore_Headers_InterfaceHeader_static_size depends on runtime parameters */
#define SystemCore_Headers_InterfaceHeader_static_size                                   41

/* Message IDs (where set with "identifier" option) */
#define SystemCore_Headers_InterfaceHeader_majorVersion                                  2U
#define SystemCore_Headers_InterfaceHeader_minorVersion                                  0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_SystemCore_Headers_InterfaceHeader_Raw(qpb_ostream_t *const stream, const SystemCore_Headers_InterfaceHeader_Raw *const data);
bool decode_SystemCore_Headers_InterfaceHeader_Raw(qpb_istream_t *const stream, SystemCore_Headers_InterfaceHeader_Raw *const data);
#define encode_SystemCore_Headers_InterfaceHeader encode_SystemCore_Headers_InterfaceHeader_Raw
#define decode_SystemCore_Headers_InterfaceHeader decode_SystemCore_Headers_InterfaceHeader_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_HEADERS_INTERFACEHEADER_INCLUDED */
