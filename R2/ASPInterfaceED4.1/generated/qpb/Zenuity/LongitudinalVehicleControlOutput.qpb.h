/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ZENUITY_LONGITUDINALVEHICLECONTROLOUTPUT_INCLUDED
#define ZENUITY_LONGITUDINALVEHICLECONTROLOUTPUT_INCLUDED

#include "Zenuity/LongitudinalVehicleControlOutput_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define Zenuity_LongitudinalVehicleControl_StopAndGoRequests_size                        (36)

/* Message IDs (where set with "identifier" option) */
#define Zenuity_LongitudinalVehicleControl_StopAndGoRequests_source                      1U
#define Zenuity_LongitudinalVehicleControl_StopAndGoRequests_identifier                  33U
#define Zenuity_LongitudinalVehicleControl_StopAndGoRequests_majorVersion                1U
#define Zenuity_LongitudinalVehicleControl_StopAndGoRequests_minorVersion                0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw(qpb_ostream_t *const stream, const Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw *const data);
bool decode_Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw(qpb_istream_t *const stream, Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw *const data);
#define encode_Zenuity_LongitudinalVehicleControl_StopAndGoRequests encode_Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw
#define decode_Zenuity_LongitudinalVehicleControl_StopAndGoRequests decode_Zenuity_LongitudinalVehicleControl_StopAndGoRequests_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ZENUITY_LONGITUDINALVEHICLECONTROLOUTPUT_INCLUDED */