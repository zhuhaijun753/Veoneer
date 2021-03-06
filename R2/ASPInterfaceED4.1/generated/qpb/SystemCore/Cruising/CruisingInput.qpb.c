/* Automatically generated qpb constant definitions */
/* Generated by Quick Protocol Buffers - 2 */

#include "SystemCore/Cruising/CruisingInput.qpb.h"
#include "Tools/QuickProtobuf/qpb_decode.h"
#include "Tools/QuickProtobuf/qpb_encode.h"

#if QPB_PROTO_HEADER_VERSION != 2
#error Regenerate this file with the current version of qpb generator.
#endif

static inline void encode_SystemCore_Cruising_DriverAlertControlInput_Raw_dacActivated(qpb_ostream_t *const stream, const bool *const data);
static bool decode_SystemCore_Cruising_DriverAlertControlInput_Raw_dacActivated(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_enable(qpb_ostream_t *const stream, const bool *const data);
static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_enable(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeRequestByDriver(qpb_ostream_t *const stream, const SystemCore_Cruising_LateralDirection *const data);
static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeRequestByDriver(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeAbortRequestByDriver(qpb_ostream_t *const stream, const bool *const data);
static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeAbortRequestByDriver(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_rearRadarDetectionRange(qpb_ostream_t *const stream, const uint8_t *const data);
static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_rearRadarDetectionRange(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_RiskMitigationSupportInput_Raw_rmsStatus(qpb_ostream_t *const stream, const SystemCore_Cruising_RmsStatus *const data);
static bool decode_SystemCore_Cruising_RiskMitigationSupportInput_Raw_rmsStatus(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_enable(qpb_ostream_t *const stream, const bool *const data);
static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_enable(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_steeringEnabled(qpb_ostream_t *const stream, const bool *const data);
static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_steeringEnabled(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_driverInTheLoopDetected(qpb_ostream_t *const stream, const bool *const data);
static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_driverInTheLoopDetected(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);
static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_trafficAssistIsSteering(qpb_ostream_t *const stream, const bool *const data);
static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_trafficAssistIsSteering(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype);

#define SystemCore_Cruising_DriverAlertControlInput_Raw_DECODERS_COUNT 2
const qpb_decoder_entry_t SystemCore_Cruising_DriverAlertControlInput_Raw_decoders[SystemCore_Cruising_DriverAlertControlInput_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_SystemCore_Cruising_DriverAlertControlInput_Raw_dacActivated }
};

#define SystemCore_Cruising_LaneChangeAssistInput_Raw_DECODERS_COUNT 5
const qpb_decoder_entry_t SystemCore_Cruising_LaneChangeAssistInput_Raw_decoders[SystemCore_Cruising_LaneChangeAssistInput_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_enable },
   { &decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeRequestByDriver },
   { &decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeAbortRequestByDriver },
   { &decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_rearRadarDetectionRange }
};

#define SystemCore_Cruising_RiskMitigationSupportInput_Raw_DECODERS_COUNT 2
const qpb_decoder_entry_t SystemCore_Cruising_RiskMitigationSupportInput_Raw_decoders[SystemCore_Cruising_RiskMitigationSupportInput_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_SystemCore_Cruising_RiskMitigationSupportInput_Raw_rmsStatus }
};

#define SystemCore_Cruising_TrafficAssistInput_Raw_DECODERS_COUNT 5
const qpb_decoder_entry_t SystemCore_Cruising_TrafficAssistInput_Raw_decoders[SystemCore_Cruising_TrafficAssistInput_Raw_DECODERS_COUNT] = {
   { &qpb_skip_field } /* Id 0 is not valid and this is skipped one level up */,
   { &decode_SystemCore_Cruising_TrafficAssistInput_Raw_enable },
   { &decode_SystemCore_Cruising_TrafficAssistInput_Raw_steeringEnabled },
   { &decode_SystemCore_Cruising_TrafficAssistInput_Raw_driverInTheLoopDetected },
   { &decode_SystemCore_Cruising_TrafficAssistInput_Raw_trafficAssistIsSteering }
};

static inline void encode_SystemCore_Cruising_DriverAlertControlInput_Raw_dacActivated(qpb_ostream_t *const stream, const bool *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_DriverAlertControlInput_Raw_dacActivated(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_DriverAlertControlInput_Raw*)data)->dacActivated, sizeof(bool));
}

static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_enable(qpb_ostream_t *const stream, const bool *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_enable(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_LaneChangeAssistInput_Raw*)data)->enable, sizeof(bool));
}

static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeRequestByDriver(qpb_ostream_t *const stream, const SystemCore_Cruising_LateralDirection *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 16;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeRequestByDriver(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_LaneChangeAssistInput_Raw*)data)->laneChangeRequestByDriver, qpb_membersize(SystemCore_Cruising_LaneChangeAssistInput_Raw, laneChangeRequestByDriver));
}

static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeAbortRequestByDriver(qpb_ostream_t *const stream, const bool *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 24;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeAbortRequestByDriver(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_LaneChangeAssistInput_Raw*)data)->laneChangeAbortRequestByDriver, sizeof(bool));
}

static inline void encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_rearRadarDetectionRange(qpb_ostream_t *const stream, const uint8_t *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 32;
      ++stream->buffer;
      qpb_encode_uvarint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw_rearRadarDetectionRange(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_uvarint(stream, (void*)&((SystemCore_Cruising_LaneChangeAssistInput_Raw*)data)->rearRadarDetectionRange, sizeof(uint8_t));
}

static inline void encode_SystemCore_Cruising_RiskMitigationSupportInput_Raw_rmsStatus(qpb_ostream_t *const stream, const SystemCore_Cruising_RmsStatus *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_RiskMitigationSupportInput_Raw_rmsStatus(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_RiskMitigationSupportInput_Raw*)data)->rmsStatus, qpb_membersize(SystemCore_Cruising_RiskMitigationSupportInput_Raw, rmsStatus));
}

static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_enable(qpb_ostream_t *const stream, const bool *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 8;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_enable(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_TrafficAssistInput_Raw*)data)->enable, sizeof(bool));
}

static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_steeringEnabled(qpb_ostream_t *const stream, const bool *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 16;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_steeringEnabled(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_TrafficAssistInput_Raw*)data)->steeringEnabled, sizeof(bool));
}

static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_driverInTheLoopDetected(qpb_ostream_t *const stream, const bool *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 24;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_driverInTheLoopDetected(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_TrafficAssistInput_Raw*)data)->driverInTheLoopDetected, sizeof(bool));
}

static inline void encode_SystemCore_Cruising_TrafficAssistInput_Raw_trafficAssistIsSteering(qpb_ostream_t *const stream, const bool *const data)
{
   if (*data != 0)
   {
      *stream->buffer = 32;
      ++stream->buffer;
      qpb_encode_varint(stream, *data);
   }
}

static bool decode_SystemCore_Cruising_TrafficAssistInput_Raw_trafficAssistIsSteering(qpb_istream_t *const stream, void *const data, const qpb_wire_type_t wiretype)
{
   QPB_UNUSED(wiretype);
   return qpb_decode_varint(stream, (void*)&((SystemCore_Cruising_TrafficAssistInput_Raw*)data)->trafficAssistIsSteering, sizeof(bool));
}

/* Encoding / decoding functions */
bool encode_SystemCore_Cruising_DriverAlertControlInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_DriverAlertControlInput_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < SystemCore_Cruising_DriverAlertControlInput_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_SystemCore_Cruising_DriverAlertControlInput_Raw_dacActivated(stream, &data->dacActivated);
   return true;
}

bool decode_SystemCore_Cruising_DriverAlertControlInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_DriverAlertControlInput_Raw *const data)
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
      if (id < SystemCore_Cruising_DriverAlertControlInput_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = SystemCore_Cruising_DriverAlertControlInput_Raw_decoders[id].func;
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

bool encode_SystemCore_Cruising_LaneChangeAssistInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_LaneChangeAssistInput_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < SystemCore_Cruising_LaneChangeAssistInput_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_enable(stream, &data->enable);
   encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeRequestByDriver(stream, &data->laneChangeRequestByDriver);
   encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_laneChangeAbortRequestByDriver(stream, &data->laneChangeAbortRequestByDriver);
   encode_SystemCore_Cruising_LaneChangeAssistInput_Raw_rearRadarDetectionRange(stream, &data->rearRadarDetectionRange);
   return true;
}

bool decode_SystemCore_Cruising_LaneChangeAssistInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_LaneChangeAssistInput_Raw *const data)
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
      if (id < SystemCore_Cruising_LaneChangeAssistInput_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = SystemCore_Cruising_LaneChangeAssistInput_Raw_decoders[id].func;
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

bool encode_SystemCore_Cruising_RiskMitigationSupportInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_RiskMitigationSupportInput_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < SystemCore_Cruising_RiskMitigationSupportInput_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_SystemCore_Cruising_RiskMitigationSupportInput_Raw_rmsStatus(stream, &data->rmsStatus);
   return true;
}

bool decode_SystemCore_Cruising_RiskMitigationSupportInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_RiskMitigationSupportInput_Raw *const data)
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
      if (id < SystemCore_Cruising_RiskMitigationSupportInput_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = SystemCore_Cruising_RiskMitigationSupportInput_Raw_decoders[id].func;
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

bool encode_SystemCore_Cruising_TrafficAssistInput_Raw(qpb_ostream_t *const stream, const SystemCore_Cruising_TrafficAssistInput_Raw *const data)
{
   /* Optimize by checking that size is enough on top level? */
   if ((qpb_size_t)(stream->end - stream->buffer) < SystemCore_Cruising_TrafficAssistInput_size)
   {
      QPB_RETURN_ERROR(stream, "Buffer to small");
   }
   encode_SystemCore_Cruising_TrafficAssistInput_Raw_enable(stream, &data->enable);
   encode_SystemCore_Cruising_TrafficAssistInput_Raw_steeringEnabled(stream, &data->steeringEnabled);
   encode_SystemCore_Cruising_TrafficAssistInput_Raw_driverInTheLoopDetected(stream, &data->driverInTheLoopDetected);
   encode_SystemCore_Cruising_TrafficAssistInput_Raw_trafficAssistIsSteering(stream, &data->trafficAssistIsSteering);
   return true;
}

bool decode_SystemCore_Cruising_TrafficAssistInput_Raw(qpb_istream_t *const stream, SystemCore_Cruising_TrafficAssistInput_Raw *const data)
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
      if (id < SystemCore_Cruising_TrafficAssistInput_Raw_DECODERS_COUNT)
      {
         qpb_decoder_t decoder = SystemCore_Cruising_TrafficAssistInput_Raw_decoders[id].func;
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

