/* Automatically generated qpb header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCOUTPUT_INCLUDED
#define ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCOUTPUT_INCLUDED

#include "ActuatorSupport/SteeringTorqueCommander/StcOutput_types.qpb.h"


#include "Tools/QuickProtobuf/qpb.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#ifdef __cplusplus
extern "C" {
#endif

/* Maximum encoded size of messages (where known) */
#define ActuatorSupport_SteeringTorqueCommander_StcOutput_size                           (14)

/* Message IDs (where set with "identifier" option) */
#define ActuatorSupport_SteeringTorqueCommander_StcOutput_source                         5U
#define ActuatorSupport_SteeringTorqueCommander_StcOutput_identifier                     11U
#define ActuatorSupport_SteeringTorqueCommander_StcOutput_majorVersion                   1U
#define ActuatorSupport_SteeringTorqueCommander_StcOutput_minorVersion                   0U

/* Encoding / decoding functions
 * Returns true on success, false on any failure.
 * Notes on Decode:
 * User is expected to provide a struct with wanted/default values (all zeroes).
 * A case where default values are not wanted is if you want to merge two messages
 * i.e. update only the fields that exist in the new message.
 * Note: These functions supports NULL termination of messages which most other
 *       protobuf implementations do not just so you know
 */
bool encode_ActuatorSupport_SteeringTorqueCommander_StcOutput_Raw(qpb_ostream_t *const stream, const ActuatorSupport_SteeringTorqueCommander_StcOutput_Raw *const data);
bool decode_ActuatorSupport_SteeringTorqueCommander_StcOutput_Raw(qpb_istream_t *const stream, ActuatorSupport_SteeringTorqueCommander_StcOutput_Raw *const data);
bool encode_ActuatorSupport_SteeringTorqueCommander_StcOutput(qpb_ostream_t *const stream, const ActuatorSupport_SteeringTorqueCommander_StcOutput *const data);
bool decode_ActuatorSupport_SteeringTorqueCommander_StcOutput(qpb_istream_t *const stream, ActuatorSupport_SteeringTorqueCommander_StcOutput *const data);

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* ACTUATORSUPPORT_STEERINGTORQUECOMMANDER_STCOUTPUT_INCLUDED */
