/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "SystemCore/Headers/InterfaceHeader.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t SystemCore_Headers_InterfaceHeader_fields[6] = {
    PB_FIELD(  1, 8    , 1    , UINT32  , OPTIONAL, STATIC  , FIRST, SystemCore_Headers_InterfaceHeader, formatVersion, formatVersion, 0),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, SystemCore_Headers_InterfaceHeader, dataHeader, formatVersion, &SystemCore_Headers_DataHeader_fields),
    PB_FIELD(  3, 26   , 1    , BYTES   , OPTIONAL, POINTER , OTHER, SystemCore_Headers_InterfaceHeader, data, dataHeader, 0),
    PB_FIELD(  5, 40   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, SystemCore_Headers_InterfaceHeader, timestamp, data, 0),
    PB_FIELD(  6, 48   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, SystemCore_Headers_InterfaceHeader, frameNumber, timestamp, 0),
    PB_LAST_FIELD
};

