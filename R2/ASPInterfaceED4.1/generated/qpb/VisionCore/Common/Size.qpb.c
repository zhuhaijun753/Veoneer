/* Automatically generated qpb constant definitions */
/* Generated by Quick Protocol Buffers - 2 */

#include "VisionCore/Common/Size.qpb.h"
#include "Tools/QuickProtobuf/qpb_decode.h"
#include "Tools/QuickProtobuf/qpb_encode.h"
#include "Tools/CSupport/ConversionSupport.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#define F_0_01               0.01f

static inline void encode_VisionCore_Common_Size2_m_0_01_Raw_width(qpb_ostream_t *const stream, const uint16_t *const data);
static bool decode_VisionCore_Common_Size2_m_0_01_Raw_width(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_VisionCore_Common_Size2_m_0_01_Raw_height(qpb_ostream_t *const stream, const uint16_t *const data);
static bool decode_VisionCore_Common_Size2_m_0_01_Raw_height(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_VisionCore_Common_Size2_m_0_01_width(qpb_ostream_t *const stream, const float *const data);
static bool decode_VisionCore_Common_Size2_m_0_01_width(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_VisionCore_Common_Size2_m_0_01_height(qpb_ostream_t *const stream, const float *const data);
static bool decode_VisionCore_Common_Size2_m_0_01_height(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);

#define VisionCore_Common_Size2_m_0_01_Raw_DECODERS_COUNT 3
const qpb_decoder_entry_t VisionCore_Common_Size2_m_0_01_Raw_decoders[VisionCore_Common_Size2_m_0_01_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_VisionCore_Common_Size2_m_0_01_Raw_width },
   { &decode_VisionCore_Common_Size2_m_0_01_Raw_height }
};

#define VisionCore_Common_Size2_m_0_01_DECODERS_COUNT 3
const qpb_decoder_entry_t VisionCore_Common_Size2_m_0_01_decoders[VisionCore_Common_Size2_m_0_01_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_VisionCore_Common_Size2_m_0_01_width },
   { &decode_VisionCore_Common_Size2_m_0_01_height }
};

static inline void encode_VisionCore_Common_Size2_m_0_01_Raw_width(qpb_ostream_t *const stream, const uint16_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_uvarint(stream, *data);
   }
}

static bool decode_VisionCore_Common_Size2_m_0_01_Raw_width(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_uvarint(stream, (void*)&((VisionCore_Common_Size2_m_0_01_Raw*)data)->width, sizeof(uint16_t));
}

static inline void encode_VisionCore_Common_Size2_m_0_01_Raw_height(qpb_ostream_t *const stream, const uint16_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 16;
      ++stream->buffer;
      qpb_encode_uvarint(stream, *data);
   }
}

static bool decode_VisionCore_Common_Size2_m_0_01_Raw_height(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_uvarint(stream, (void*)&((VisionCore_Common_Size2_m_0_01_Raw*)data)->height, sizeof(uint16_t));
}

static inline void encode_VisionCore_Common_Size2_m_0_01_width(qpb_ostream_t *const stream, const float *const data)
{
   uint16_t value = (uint16_t)convertToUint32(*data, F_0_01, 0, UINT16_MAX);
   encode_VisionCore_Common_Size2_m_0_01_Raw_width(stream, &value);
}

static bool decode_VisionCore_Common_Size2_m_0_01_width(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   uint16_t value;
   bool result = qpb_decode_uvarint(stream, (void*)&value, sizeof(uint16_t));
   ((VisionCore_Common_Size2_m_0_01*)data)->width = value * F_0_01;
   return result;
}

static inline void encode_VisionCore_Common_Size2_m_0_01_height(qpb_ostream_t *const stream, const float *const data)
{
   uint16_t value = (uint16_t)convertToUint32(*data, F_0_01, 0, UINT16_MAX);
   encode_VisionCore_Common_Size2_m_0_01_Raw_height(stream, &value);
}

static bool decode_VisionCore_Common_Size2_m_0_01_height(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   uint16_t value;
   bool result = qpb_decode_uvarint(stream, (void*)&value, sizeof(uint16_t));
   ((VisionCore_Common_Size2_m_0_01*)data)->height = value * F_0_01;
   return result;
}

/* Encoding / decoding functions */
bool encode_VisionCore_Common_Size2_m_0_01_Raw(qpb_ostream_t *const stream, const VisionCore_Common_Size2_m_0_01_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < VisionCore_Common_Size2_m_0_01_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_VisionCore_Common_Size2_m_0_01_Raw_width(stream, &data->width);
   encode_VisionCore_Common_Size2_m_0_01_Raw_height(stream, &data->height);
   return true;
}

bool decode_VisionCore_Common_Size2_m_0_01_Raw(qpb_istream_t *const stream, VisionCore_Common_Size2_m_0_01_Raw *const data)
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
      if (id < VisionCore_Common_Size2_m_0_01_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = VisionCore_Common_Size2_m_0_01_Raw_decoders[id].func;
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

bool encode_VisionCore_Common_Size2_m_0_01(qpb_ostream_t *const stream, const VisionCore_Common_Size2_m_0_01 *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < VisionCore_Common_Size2_m_0_01_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_VisionCore_Common_Size2_m_0_01_width(stream, &data->width);
   encode_VisionCore_Common_Size2_m_0_01_height(stream, &data->height);
   return true;
}

bool decode_VisionCore_Common_Size2_m_0_01(qpb_istream_t *const stream, VisionCore_Common_Size2_m_0_01 *const data)
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
      if (id < VisionCore_Common_Size2_m_0_01_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = VisionCore_Common_Size2_m_0_01_decoders[id].func;
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

