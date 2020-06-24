/* Automatically generated qpb constant definitions */
/* Generated by Quick Protocol Buffers - 2 */

#include "SystemCore/LateralControl/LateralActuation.qpb.h"
#include "Tools/QuickProtobuf/qpb_decode.h"
#include "Tools/QuickProtobuf/qpb_encode.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

static inline void encode_SystemCore_LateralControl_LateralActuation_Raw_mode(qpb_ostream_t *const stream, const SystemCore_LateralControl_LateralControlMode *const data);
static bool decode_SystemCore_LateralControl_LateralActuation_Raw_mode(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);

#define SystemCore_LateralControl_LateralActuation_Raw_DECODERS_COUNT 2
const qpb_decoder_entry_t SystemCore_LateralControl_LateralActuation_Raw_decoders[SystemCore_LateralControl_LateralActuation_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_SystemCore_LateralControl_LateralActuation_Raw_mode }
};

static inline void encode_SystemCore_LateralControl_LateralActuation_Raw_mode(qpb_ostream_t *const stream, const SystemCore_LateralControl_LateralControlMode *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_LateralControl_LateralActuation_Raw_mode(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_LateralControl_LateralActuation_Raw*)data)->mode, qpb_membersize(SystemCore_LateralControl_LateralActuation_Raw, mode));
}

/* Encoding / decoding functions */
bool encode_SystemCore_LateralControl_LateralActuation_Raw(qpb_ostream_t *const stream, const SystemCore_LateralControl_LateralActuation_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < SystemCore_LateralControl_LateralActuation_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_SystemCore_LateralControl_LateralActuation_Raw_mode(stream, &data->mode);
   return true;
}

bool decode_SystemCore_LateralControl_LateralActuation_Raw(qpb_istream_t *const stream, SystemCore_LateralControl_LateralActuation_Raw *const data)
{
   qpb_uint64_t tag;
   qpb_uint64_t id;
   qpb_wire_type_t wireType;
   bool result = true;
   while (stream->end != stream->buffer)
   {
      result = qpb_decode_uvarint(stream, &tag, sizeof(qpb_uint64_t));
      if (!result)
      {
         return false;
      }
      /* Extended support for NULL termination */
      if (tag == 0)
      {
         return true;
      }
      id = qpb_id(tag);
      wireType = (qpb_wire_type_t)qpb_wireType(tag);
      if (id < SystemCore_LateralControl_LateralActuation_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = SystemCore_LateralControl_LateralActuation_Raw_decoders[id].func;
         result = decoder(stream, data, wireType);
      }
      else
      {
         result = qpb_skip_field(stream, NULL, wireType);
      }
      if (!result)
      {
         return false;
      }
   }
   return result;
}

