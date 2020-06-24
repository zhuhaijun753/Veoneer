/* Automatically generated qpb types header */
/* SPP version 2.0.0 */
/* Generated by Quick Protocol Buffers - 2 */

#ifndef SYSTEMCORE_FUNCTIONCALLS_FUNCTIONDEBUG_TYPES_INCLUDED
#define SYSTEMCORE_FUNCTIONCALLS_FUNCTIONDEBUG_TYPES_INCLUDED

#include "Tools/QuickProtobuf/qpb_types.h"

#include "Tools/Extension/DataSources_types.qpb.h"

#ifdef __cplusplus
extern "C" {
#endif

/* Struct definitions */
typedef struct _SystemCore_FunctionCalls_FunctionCallLink_Raw {
    /** Identifier
     * Identifier to link function call
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t identifier;
    /** FunctionCallName
     * Function call name, should be unique
     */
    char functionCallName[50];
} SystemCore_FunctionCalls_FunctionCallLink_Raw;

#define SystemCore_FunctionCalls_FunctionCallLink SystemCore_FunctionCalls_FunctionCallLink_Raw

typedef struct _SystemCore_FunctionCalls_InputData_Raw {
    /** DataSource */
    DataSource dataSource;
    /** DataIdentifier
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t dataIdentifier;
    /** FrameNumber
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t frameNumber;
    /** Timestamp
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t timestamp;
} SystemCore_FunctionCalls_InputData_Raw;

#define SystemCore_FunctionCalls_InputData SystemCore_FunctionCalls_InputData_Raw

typedef struct _SystemCore_FunctionCalls_FunctionCallLinks_Raw {
    qpb_size_t functionCallLinks_count;
    /** FunctionCallLinks
     * List of function calls e.g. AEB_run
     */
    SystemCore_FunctionCalls_FunctionCallLink_Raw functionCallLinks[20];
} SystemCore_FunctionCalls_FunctionCallLinks_Raw;

#define SystemCore_FunctionCalls_FunctionCallLinks SystemCore_FunctionCalls_FunctionCallLinks_Raw

typedef struct _SystemCore_FunctionCalls_FunctionExecution_Raw {
    /** FunctionCallIdentifier
     * Identifier linked to FunctionCallLink
     * Min: 0
     * Max: 4.29497e+09
     */
    uint32_t functionCallIdentifier;
    qpb_size_t inputData_count;
    /** InputData
     * List of input datatypes and their reference frame number/timestamp. Used to understand which data was input when to reproduce the behavior in for example SiL.
     */
    SystemCore_FunctionCalls_InputData_Raw inputData[30];
} SystemCore_FunctionCalls_FunctionExecution_Raw;

#define SystemCore_FunctionCalls_FunctionExecution SystemCore_FunctionCalls_FunctionExecution_Raw

#ifdef __cplusplus
} /* extern "C" */
#endif

#endif /* SYSTEMCORE_FUNCTIONCALLS_FUNCTIONDEBUG_TYPES_INCLUDED */
