/* Automatically generated pb constant definitions */
/* Generated by Protocol Buffers - 1 */

#include "Tools/Test/TestAll.cpb.h"

#if PB_PROTO_HEADER_VERSION != 1
#error Regenerate this file with the current version of pb generator.
#endif

const pb_field_t InterfacesTest_TestAllTypes_fields[24] = {
    PB_FIELD(  1, 8    , 1    , SINT64  , OPTIONAL, STATIC  , FIRST, InterfacesTest_TestAllTypes, sint64Value, sint64Value, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, sint32Value, sint64Value, 0),
    PB_FIELD(  3, 24   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, sint32Value16, sint32Value, 0),
    PB_FIELD(  4, 32   , 1    , SINT32  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, sint32Value8, sint32Value16, 0),
    PB_FIELD(  5, 40   , 1    , INT64   , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, int64Value, sint32Value8, 0),
    PB_FIELD(  6, 48   , 1    , INT32   , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, int32Value, int64Value, 0),
    PB_FIELD(  7, 56   , 1    , INT32   , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, int32Value16, int32Value, 0),
    PB_FIELD(  8, 64   , 1    , INT32   , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, int32Value8, int32Value16, 0),
    PB_FIELD(  9, 72   , 1    , UINT64  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, uint64Value, int32Value8, 0),
    PB_FIELD( 10, 80   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, uint32Value, uint64Value, 0),
    PB_FIELD( 11, 88   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, uint32Value16, uint32Value, 0),
    PB_FIELD( 12, 96   , 1    , UINT32  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, uint32Value8, uint32Value16, 0),
    PB_FIELD( 13, 104  , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, boolValue, uint32Value8, 0),
    PB_FIELD( 14, 117  , 1    , FLOAT   , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, floatValue, boolValue, 0),
    PB_FIELD( 15, 121  , 1    , DOUBLE  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, doubleValue, floatValue, 0),
    PB_FIELD( 16, 130  , 2    , STRING  , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, stringValue, doubleValue, 0),
    PB_FIELD( 17, 138  , 2    , BYTES   , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, bytesValue, stringValue, 0),
    PB_FIELD( 18, 145  , 2    , FIXED64 , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, fixed64Value, bytesValue, 0),
    PB_FIELD( 19, 157  , 2    , FIXED32 , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, fixed32Value, fixed64Value, 0),
    PB_FIELD( 20, 161  , 2    , SFIXED64, OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, sfixed64Value, fixed32Value, 0),
    PB_FIELD( 21, 173  , 2    , SFIXED32, OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, sfixed32Value, sfixed64Value, 0),
    PB_FIELD( 22, 176  , 2    , ENUM    , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, enumValue, sfixed32Value, 0),
    PB_FIELD( 23, 184  , 2    , SENUM   , OPTIONAL, STATIC  , OTHER, InterfacesTest_TestAllTypes, negEnumValue, enumValue, 0),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_TestAllTypesPointers_fields[5] = {
    PB_FIELD(  1, 10   , 1    , STRING  , OPTIONAL, POINTER , FIRST, InterfacesTest_TestAllTypesPointers, stringPointerValue, stringPointerValue, 0),
    PB_FIELD(  2, 18   , 1    , BYTES   , OPTIONAL, POINTER , OTHER, InterfacesTest_TestAllTypesPointers, bytesPointerValue, stringPointerValue, 0),
    PB_FIELD(  3, 26   , 1    , STRING  , REPEATED, POINTER , OTHER, InterfacesTest_TestAllTypesPointers, stringPointerValueArray, bytesPointerValue, 0),
    PB_FIELD(  4, 34   , 1    , BYTES   , REPEATED, POINTER , OTHER, InterfacesTest_TestAllTypesPointers, bytesPointerValueArray, stringPointerValueArray, 0),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_TestAllTypesArray_fields[24] = {
    PB_FIELD(  1, 8    , 1    , SINT64  , REPEATED, STATIC  , FIRST, InterfacesTest_TestAllTypesArray, sint64Value, sint64Value, 0),
    PB_FIELD(  2, 16   , 1    , SINT32  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, sint32Value, sint64Value, 0),
    PB_FIELD(  3, 24   , 1    , SINT32  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, sint32Value16, sint32Value, 0),
    PB_FIELD(  4, 32   , 1    , SINT32  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, sint32Value8, sint32Value16, 0),
    PB_FIELD(  5, 40   , 1    , INT64   , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, int64Value, sint32Value8, 0),
    PB_FIELD(  6, 48   , 1    , INT32   , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, int32Value, int64Value, 0),
    PB_FIELD(  7, 56   , 1    , INT32   , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, int32Value16, int32Value, 0),
    PB_FIELD(  8, 64   , 1    , INT32   , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, int32Value8, int32Value16, 0),
    PB_FIELD(  9, 72   , 1    , UINT64  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, uint64Value, int32Value8, 0),
    PB_FIELD( 10, 80   , 1    , UINT32  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, uint32Value, uint64Value, 0),
    PB_FIELD( 11, 88   , 1    , UINT32  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, uint32Value16, uint32Value, 0),
    PB_FIELD( 12, 96   , 1    , UINT32  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, uint32Value8, uint32Value16, 0),
    PB_FIELD( 13, 104  , 1    , BOOL    , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, boolValue, uint32Value8, 0),
    PB_FIELD( 14, 117  , 1    , FLOAT   , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, floatValue, boolValue, 0),
    PB_FIELD( 15, 121  , 1    , DOUBLE  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, doubleValue, floatValue, 0),
    PB_FIELD( 16, 130  , 2    , STRING  , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, stringValue, doubleValue, 0),
    PB_FIELD( 17, 138  , 2    , BYTES   , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, bytesValue, stringValue, 0),
    PB_FIELD( 18, 145  , 2    , FIXED64 , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, fixed64Value, bytesValue, 0),
    PB_FIELD( 19, 157  , 2    , FIXED32 , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, fixed32Value, fixed64Value, 0),
    PB_FIELD( 20, 161  , 2    , SFIXED64, REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, sfixed64Value, fixed32Value, 0),
    PB_FIELD( 21, 173  , 2    , SFIXED32, REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, sfixed32Value, sfixed64Value, 0),
    PB_FIELD( 22, 176  , 2    , ENUM    , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, enumValue, sfixed32Value, 0),
    PB_FIELD( 23, 184  , 2    , SENUM   , REPEATED, STATIC  , OTHER, InterfacesTest_TestAllTypesArray, negEnumValue, enumValue, 0),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_SubSubMessage_fields[2] = {
    PB_FIELD(  1, 8    , 1    , UINT32  , OPTIONAL, STATIC  , FIRST, InterfacesTest_SubSubMessage, subSubUint32, subSubUint32, 0),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_SubMessage_fields[3] = {
    PB_FIELD(  1, 10   , 1    , STRING  , OPTIONAL, STATIC  , FIRST, InterfacesTest_SubMessage, subString, subString, 0),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, InterfacesTest_SubMessage, subSubMessage, subString, &InterfacesTest_SubSubMessage_fields),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_DeepSubMessage_fields[6] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, InterfacesTest_DeepSubMessage, subSint32Value, subSint32Value, 0),
    PB_FIELD(  2, 16   , 1    , BOOL    , OPTIONAL, STATIC  , OTHER, InterfacesTest_DeepSubMessage, subBoolValue, subSint32Value, 0),
    PB_FIELD(  5, 42   , 1    , MESSAGE , REPEATED, STATIC  , OTHER, InterfacesTest_DeepSubMessage, subMessage, subBoolValue, 0),
    PB_FIELD(  6, 50   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, InterfacesTest_DeepSubMessage, internalSubMessage, subMessage, &InterfacesTest_DeepSubMessage_MessageInSubMessage_fields),
    PB_FIELD(  7, 56   , 1    , ENUM    , OPTIONAL, STATIC  , OTHER, InterfacesTest_DeepSubMessage, enumInMessageValue, internalSubMessage, 0),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_DeepSubMessage_MessageInSubMessage_fields[3] = {
    PB_FIELD(  1, 8    , 1    , SINT32  , OPTIONAL, STATIC  , FIRST, InterfacesTest_DeepSubMessage_MessageInSubMessage, messageInMessageSint32, messageInMessageSint32, 0),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, InterfacesTest_DeepSubMessage_MessageInSubMessage, subMessageInMessageInMessage, messageInMessageSint32, &InterfacesTest_DeepSubMessage_MessageInSubMessage_SubMessageInSubMessage_fields),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_DeepSubMessage_MessageInSubMessage_SubMessageInSubMessage_fields[2] = {
    PB_FIELD(  1, 8    , 1    , BOOL    , OPTIONAL, STATIC  , FIRST, InterfacesTest_DeepSubMessage_MessageInSubMessage_SubMessageInSubMessage, subMessageInSubMessageBool, subMessageInSubMessageBool, 0),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_MainMessage_fields[3] = {
    PB_FIELD(  1, 10   , 1    , MESSAGE , OPTIONAL, STATIC  , FIRST, InterfacesTest_MainMessage, subMessage, subMessage, &InterfacesTest_SubMessage_fields),
    PB_FIELD(  2, 18   , 1    , MESSAGE , OPTIONAL, STATIC  , OTHER, InterfacesTest_MainMessage, deepSubMessage, subMessage, &InterfacesTest_DeepSubMessage_fields),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_ProcessedTypes_fields[7] = {
    PB_FIELD(  1, 8    , 1    , SINT64  , OPTIONAL, STATIC  , FIRST, InterfacesTest_ProcessedTypes, sint64ScaledValue, sint64ScaledValue, 0),
    PB_FIELD(  2, 16   , 1    , INT64   , OPTIONAL, STATIC  , OTHER, InterfacesTest_ProcessedTypes, int64ScaledValue, sint64ScaledValue, 0),
    PB_FIELD(  3, 24   , 1    , UINT64  , OPTIONAL, STATIC  , OTHER, InterfacesTest_ProcessedTypes, uint64ScaledValue, int64ScaledValue, 0),
    PB_FIELD(  4, 32   , 1    , SINT64  , REPEATED, STATIC  , OTHER, InterfacesTest_ProcessedTypes, sint64ArrayScaledValue, uint64ScaledValue, 0),
    PB_FIELD(  5, 40   , 1    , INT64   , REPEATED, STATIC  , OTHER, InterfacesTest_ProcessedTypes, int64ArrayScaledValue, sint64ArrayScaledValue, 0),
    PB_FIELD(  6, 48   , 1    , UINT64  , REPEATED, STATIC  , OTHER, InterfacesTest_ProcessedTypes, uint64ArrayScaledValue, int64ArrayScaledValue, 0),
    PB_LAST_FIELD
};

const pb_field_t InterfacesTest_ArrayOfProcessedTypes_fields[2] = {
    PB_FIELD(  1, 10   , 1    , MESSAGE , REPEATED, STATIC  , FIRST, InterfacesTest_ArrayOfProcessedTypes, processedTypesArray, processedTypesArray, 0),
    PB_LAST_FIELD
};

/* On some platforms (such as AVR), double is really float.
 * These are not directly supported by pb.
 * To get rid of this error, remove any double fields from your .proto.
 */
PB_STATIC_ASSERT(sizeof(double) == 8, DOUBLE_MUST_BE_8_BYTES)
