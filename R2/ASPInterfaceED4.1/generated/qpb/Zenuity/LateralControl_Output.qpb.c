/* Automatically generated qpb constant definitions */
/* Generated by Quick Protocol Buffers - 2 */

#include "Zenuity/LateralControl_Output.qpb.h"
#include "Tools/QuickProtobuf/qpb_decode.h"
#include "Tools/QuickProtobuf/qpb_encode.h"
#include "Tools/CSupport/ConversionSupport.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

#define F_0_0001             0.0001f
#define F_0_01               0.01f

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angle(qpb_ostream_t *const stream, const int32_t *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_angle(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angleRateLimit(qpb_ostream_t *const stream, const int32_t *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_angleRateLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_lowerTorqueLimit(qpb_ostream_t *const stream, const int32_t *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_lowerTorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_upperLorqueLimit(qpb_ostream_t *const stream, const int32_t *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_upperLorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_additionalTorque(qpb_ostream_t *const stream, const int32_t *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_additionalTorque(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_bandwidthScaling(qpb_ostream_t *const stream, const uint32_t *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_bandwidthScaling(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_angle(qpb_ostream_t *const stream, const float *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_angle(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_angleRateLimit(qpb_ostream_t *const stream, const float *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_angleRateLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_lowerTorqueLimit(qpb_ostream_t *const stream, const float *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_lowerTorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_upperLorqueLimit(qpb_ostream_t *const stream, const float *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_upperLorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_additionalTorque(qpb_ostream_t *const stream, const float *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_additionalTorque(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_FrontWheelRequest_bandwidthScaling(qpb_ostream_t *const stream, const float *const data);
static bool decode_Zenuity_LateralControl_FrontWheelRequest_bandwidthScaling(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_LateralControlOutput_Raw_mode(qpb_ostream_t *const stream, const Zenuity_LateralControl_LateralControlMode *const data);
static bool decode_Zenuity_LateralControl_LateralControlOutput_Raw_mode(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_LateralControlOutput_Raw_frontWheelRequest(qpb_ostream_t *const stream, const Zenuity_LateralControl_FrontWheelRequest_Raw *const data);
static bool decode_Zenuity_LateralControl_LateralControlOutput_Raw_frontWheelRequest(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_LateralControlOutput_mode(qpb_ostream_t *const stream, const Zenuity_LateralControl_LateralControlMode *const data);
static bool decode_Zenuity_LateralControl_LateralControlOutput_mode(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_Zenuity_LateralControl_LateralControlOutput_frontWheelRequest(qpb_ostream_t *const stream, const Zenuity_LateralControl_FrontWheelRequest *const data);
static bool decode_Zenuity_LateralControl_LateralControlOutput_frontWheelRequest(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);

#define Zenuity_LateralControl_FrontWheelRequest_Raw_DECODERS_COUNT 7
const qpb_decoder_entry_t Zenuity_LateralControl_FrontWheelRequest_Raw_decoders[Zenuity_LateralControl_FrontWheelRequest_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_Zenuity_LateralControl_FrontWheelRequest_Raw_angle },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_Raw_angleRateLimit },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_Raw_lowerTorqueLimit },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_Raw_upperLorqueLimit },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_Raw_additionalTorque },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_Raw_bandwidthScaling }
};

#define Zenuity_LateralControl_FrontWheelRequest_DECODERS_COUNT 7
const qpb_decoder_entry_t Zenuity_LateralControl_FrontWheelRequest_decoders[Zenuity_LateralControl_FrontWheelRequest_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_Zenuity_LateralControl_FrontWheelRequest_angle },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_angleRateLimit },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_lowerTorqueLimit },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_upperLorqueLimit },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_additionalTorque },
   { &decode_Zenuity_LateralControl_FrontWheelRequest_bandwidthScaling }
};

#define Zenuity_LateralControl_LateralControlOutput_Raw_DECODERS_COUNT 3
const qpb_decoder_entry_t Zenuity_LateralControl_LateralControlOutput_Raw_decoders[Zenuity_LateralControl_LateralControlOutput_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_Zenuity_LateralControl_LateralControlOutput_Raw_mode },
   { &decode_Zenuity_LateralControl_LateralControlOutput_Raw_frontWheelRequest }
};

#define Zenuity_LateralControl_LateralControlOutput_DECODERS_COUNT 3
const qpb_decoder_entry_t Zenuity_LateralControl_LateralControlOutput_decoders[Zenuity_LateralControl_LateralControlOutput_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_Zenuity_LateralControl_LateralControlOutput_mode },
   { &decode_Zenuity_LateralControl_LateralControlOutput_frontWheelRequest }
};

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angle(qpb_ostream_t *const stream, const int32_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_svarint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_angle(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_svarint(stream, (void*)&((Zenuity_LateralControl_FrontWheelRequest_Raw*)data)->angle, sizeof(int32_t));
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angleRateLimit(qpb_ostream_t *const stream, const int32_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 16;
      ++stream->buffer;
      qpb_encode_svarint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_angleRateLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_svarint(stream, (void*)&((Zenuity_LateralControl_FrontWheelRequest_Raw*)data)->angleRateLimit, sizeof(int32_t));
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_lowerTorqueLimit(qpb_ostream_t *const stream, const int32_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 24;
      ++stream->buffer;
      qpb_encode_svarint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_lowerTorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_svarint(stream, (void*)&((Zenuity_LateralControl_FrontWheelRequest_Raw*)data)->lowerTorqueLimit, sizeof(int32_t));
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_upperLorqueLimit(qpb_ostream_t *const stream, const int32_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 32;
      ++stream->buffer;
      qpb_encode_svarint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_upperLorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_svarint(stream, (void*)&((Zenuity_LateralControl_FrontWheelRequest_Raw*)data)->upperLorqueLimit, sizeof(int32_t));
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_additionalTorque(qpb_ostream_t *const stream, const int32_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 40;
      ++stream->buffer;
      qpb_encode_svarint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_additionalTorque(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_svarint(stream, (void*)&((Zenuity_LateralControl_FrontWheelRequest_Raw*)data)->additionalTorque, sizeof(int32_t));
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_Raw_bandwidthScaling(qpb_ostream_t *const stream, const uint32_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 48;
      ++stream->buffer;
      qpb_encode_uvarint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw_bandwidthScaling(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_uvarint(stream, (void*)&((Zenuity_LateralControl_FrontWheelRequest_Raw*)data)->bandwidthScaling, sizeof(uint32_t));
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_angle(qpb_ostream_t *const stream, const float *const data)
{
   int32_t value = (int32_t)convertToInt32(*data, F_0_0001, INT32_MIN, INT32_MAX);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angle(stream, &value);
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_angle(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   int32_t value;
   bool result = qpb_decode_svarint(stream, (void*)&value, sizeof(int32_t));
   ((Zenuity_LateralControl_FrontWheelRequest*)data)->angle = value * F_0_0001;
   return result;
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_angleRateLimit(qpb_ostream_t *const stream, const float *const data)
{
   int32_t value = (int32_t)convertToInt32(*data, F_0_0001, INT32_MIN, INT32_MAX);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angleRateLimit(stream, &value);
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_angleRateLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   int32_t value;
   bool result = qpb_decode_svarint(stream, (void*)&value, sizeof(int32_t));
   ((Zenuity_LateralControl_FrontWheelRequest*)data)->angleRateLimit = value * F_0_0001;
   return result;
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_lowerTorqueLimit(qpb_ostream_t *const stream, const float *const data)
{
   int32_t value = (int32_t)convertToInt32(*data, F_0_01, INT32_MIN, INT32_MAX);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_lowerTorqueLimit(stream, &value);
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_lowerTorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   int32_t value;
   bool result = qpb_decode_svarint(stream, (void*)&value, sizeof(int32_t));
   ((Zenuity_LateralControl_FrontWheelRequest*)data)->lowerTorqueLimit = value * F_0_01;
   return result;
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_upperLorqueLimit(qpb_ostream_t *const stream, const float *const data)
{
   int32_t value = (int32_t)convertToInt32(*data, F_0_01, INT32_MIN, INT32_MAX);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_upperLorqueLimit(stream, &value);
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_upperLorqueLimit(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   int32_t value;
   bool result = qpb_decode_svarint(stream, (void*)&value, sizeof(int32_t));
   ((Zenuity_LateralControl_FrontWheelRequest*)data)->upperLorqueLimit = value * F_0_01;
   return result;
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_additionalTorque(qpb_ostream_t *const stream, const float *const data)
{
   int32_t value = (int32_t)convertToInt32(*data, F_0_01, INT32_MIN, INT32_MAX);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_additionalTorque(stream, &value);
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_additionalTorque(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   int32_t value;
   bool result = qpb_decode_svarint(stream, (void*)&value, sizeof(int32_t));
   ((Zenuity_LateralControl_FrontWheelRequest*)data)->additionalTorque = value * F_0_01;
   return result;
}

static inline void encode_Zenuity_LateralControl_FrontWheelRequest_bandwidthScaling(qpb_ostream_t *const stream, const float *const data)
{
   uint32_t value = (uint32_t)convertToUint32(*data, F_0_01, 0, UINT32_MAX);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_bandwidthScaling(stream, &value);
}

static bool decode_Zenuity_LateralControl_FrontWheelRequest_bandwidthScaling(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   uint32_t value;
   bool result = qpb_decode_uvarint(stream, (void*)&value, sizeof(uint32_t));
   ((Zenuity_LateralControl_FrontWheelRequest*)data)->bandwidthScaling = value * F_0_01;
   return result;
}

static inline void encode_Zenuity_LateralControl_LateralControlOutput_Raw_mode(qpb_ostream_t *const stream, const Zenuity_LateralControl_LateralControlMode *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_LateralControlOutput_Raw_mode(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((Zenuity_LateralControl_LateralControlOutput_Raw*)data)->mode, qpb_membersize(Zenuity_LateralControl_LateralControlOutput_Raw, mode));
}

static inline void encode_Zenuity_LateralControl_LateralControlOutput_Raw_frontWheelRequest(qpb_ostream_t *const stream, const Zenuity_LateralControl_FrontWheelRequest_Raw *const data)
{
   qpb_byte_t* start;
   qpb_byte_t* dataPtr;
   qpb_size_t size;
   qpb_byte_t dataToClear;
   *stream->buffer = 18;
   ++stream->buffer;
   start = stream->buffer;
   stream->buffer += QPB_VARINT_MAX_ENCODED_SIZE;
   dataPtr = stream->buffer;
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw(stream, data);
   if (stream->buffer > dataPtr)
   {
      /* Check size of encoded message and write size at the appropriate offset */
      size = (stream->buffer - dataPtr);
      stream->buffer = start;
      qpb_encode_varint(stream, (qpb_uint64_t)size);
      dataToClear = QPB_VARINT_MAX_ENCODED_SIZE - (stream->buffer - start);
      /* Shift buffer back to end of varint */
      memmove(stream->buffer, dataPtr, size);
      stream->buffer += size;
      memset(stream->buffer, 0, dataToClear);
   }
   else /* No data written shift buffer back */
   {
      stream->buffer = start - 1;
      memset(stream->buffer, 0, 1);
   }
}

static bool decode_Zenuity_LateralControl_LateralControlOutput_Raw_frontWheelRequest(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   qpb_size_t size;
   qpb_istream_t substream;
   bool result = qpb_decode_uvarint(stream, &size, sizeof(qpb_size_t));
   if (!result)
   {
      return false;
   }
   substream = qpb_istream_from_buffer(stream->buffer, size);
   result = decode_Zenuity_LateralControl_FrontWheelRequest_Raw(&substream, &((Zenuity_LateralControl_LateralControlOutput_Raw*)data)->frontWheelRequest);
   if (!result)
   {
      QPB_RETURN_ERROR(stream, QPB_GET_ERROR(&substream));
   }
   stream->buffer += size;
   return result;
}

static inline void encode_Zenuity_LateralControl_LateralControlOutput_mode(qpb_ostream_t *const stream, const Zenuity_LateralControl_LateralControlMode *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_Zenuity_LateralControl_LateralControlOutput_mode(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((Zenuity_LateralControl_LateralControlOutput*)data)->mode, qpb_membersize(Zenuity_LateralControl_LateralControlOutput, mode));
}

static inline void encode_Zenuity_LateralControl_LateralControlOutput_frontWheelRequest(qpb_ostream_t *const stream, const Zenuity_LateralControl_FrontWheelRequest *const data)
{
   qpb_byte_t* start;
   qpb_byte_t* dataPtr;
   qpb_size_t size;
   qpb_byte_t dataToClear;
   *stream->buffer = 18;
   ++stream->buffer;
   start = stream->buffer;
   stream->buffer += QPB_VARINT_MAX_ENCODED_SIZE;
   dataPtr = stream->buffer;
   encode_Zenuity_LateralControl_FrontWheelRequest(stream, data);
   if (stream->buffer > dataPtr)
   {
      /* Check size of encoded message and write size at the appropriate offset */
      size = (stream->buffer - dataPtr);
      stream->buffer = start;
      qpb_encode_varint(stream, (qpb_uint64_t)size);
      dataToClear = QPB_VARINT_MAX_ENCODED_SIZE - (stream->buffer - start);
      /* Shift buffer back to end of varint */
      memmove(stream->buffer, dataPtr, size);
      stream->buffer += size;
      memset(stream->buffer, 0, dataToClear);
   }
   else /* No data written shift buffer back */
   {
      stream->buffer = start - 1;
      memset(stream->buffer, 0, 1);
   }
}

static bool decode_Zenuity_LateralControl_LateralControlOutput_frontWheelRequest(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   qpb_size_t size;
   qpb_istream_t substream;
   bool result = qpb_decode_uvarint(stream, &size, sizeof(qpb_size_t));
   if (!result)
   {
      return false;
   }
   substream = qpb_istream_from_buffer(stream->buffer, size);
   result = decode_Zenuity_LateralControl_FrontWheelRequest(&substream, &((Zenuity_LateralControl_LateralControlOutput*)data)->frontWheelRequest);
   if (!result)
   {
      QPB_RETURN_ERROR(stream, QPB_GET_ERROR(&substream));
   }
   stream->buffer += size;
   return result;
}

/* Encoding / decoding functions */
bool encode_Zenuity_LateralControl_FrontWheelRequest_Raw(qpb_ostream_t *const stream, const Zenuity_LateralControl_FrontWheelRequest_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < Zenuity_LateralControl_FrontWheelRequest_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angle(stream, &data->angle);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_angleRateLimit(stream, &data->angleRateLimit);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_lowerTorqueLimit(stream, &data->lowerTorqueLimit);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_upperLorqueLimit(stream, &data->upperLorqueLimit);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_additionalTorque(stream, &data->additionalTorque);
   encode_Zenuity_LateralControl_FrontWheelRequest_Raw_bandwidthScaling(stream, &data->bandwidthScaling);
   return true;
}

bool decode_Zenuity_LateralControl_FrontWheelRequest_Raw(qpb_istream_t *const stream, Zenuity_LateralControl_FrontWheelRequest_Raw *const data)
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
      if (id < Zenuity_LateralControl_FrontWheelRequest_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = Zenuity_LateralControl_FrontWheelRequest_Raw_decoders[id].func;
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

bool encode_Zenuity_LateralControl_FrontWheelRequest(qpb_ostream_t *const stream, const Zenuity_LateralControl_FrontWheelRequest *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < Zenuity_LateralControl_FrontWheelRequest_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_Zenuity_LateralControl_FrontWheelRequest_angle(stream, &data->angle);
   encode_Zenuity_LateralControl_FrontWheelRequest_angleRateLimit(stream, &data->angleRateLimit);
   encode_Zenuity_LateralControl_FrontWheelRequest_lowerTorqueLimit(stream, &data->lowerTorqueLimit);
   encode_Zenuity_LateralControl_FrontWheelRequest_upperLorqueLimit(stream, &data->upperLorqueLimit);
   encode_Zenuity_LateralControl_FrontWheelRequest_additionalTorque(stream, &data->additionalTorque);
   encode_Zenuity_LateralControl_FrontWheelRequest_bandwidthScaling(stream, &data->bandwidthScaling);
   return true;
}

bool decode_Zenuity_LateralControl_FrontWheelRequest(qpb_istream_t *const stream, Zenuity_LateralControl_FrontWheelRequest *const data)
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
      if (id < Zenuity_LateralControl_FrontWheelRequest_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = Zenuity_LateralControl_FrontWheelRequest_decoders[id].func;
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

bool encode_Zenuity_LateralControl_LateralControlOutput_Raw(qpb_ostream_t *const stream, const Zenuity_LateralControl_LateralControlOutput_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < Zenuity_LateralControl_LateralControlOutput_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_Zenuity_LateralControl_LateralControlOutput_Raw_mode(stream, &data->mode);
   encode_Zenuity_LateralControl_LateralControlOutput_Raw_frontWheelRequest(stream, &data->frontWheelRequest);
   return true;
}

bool decode_Zenuity_LateralControl_LateralControlOutput_Raw(qpb_istream_t *const stream, Zenuity_LateralControl_LateralControlOutput_Raw *const data)
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
      if (id < Zenuity_LateralControl_LateralControlOutput_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = Zenuity_LateralControl_LateralControlOutput_Raw_decoders[id].func;
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

bool encode_Zenuity_LateralControl_LateralControlOutput(qpb_ostream_t *const stream, const Zenuity_LateralControl_LateralControlOutput *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < Zenuity_LateralControl_LateralControlOutput_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_Zenuity_LateralControl_LateralControlOutput_Raw_mode(stream, &data->mode);
   encode_Zenuity_LateralControl_LateralControlOutput_frontWheelRequest(stream, &data->frontWheelRequest);
   return true;
}

bool decode_Zenuity_LateralControl_LateralControlOutput(qpb_istream_t *const stream, Zenuity_LateralControl_LateralControlOutput *const data)
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
      if (id < Zenuity_LateralControl_LateralControlOutput_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = Zenuity_LateralControl_LateralControlOutput_decoders[id].func;
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

