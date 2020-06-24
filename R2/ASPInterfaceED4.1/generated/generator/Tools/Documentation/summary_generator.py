"""
Brief: This file contains classes for Interface Summary files (source, identifiers)
       based on protobuf definitions extended with SystemOptions.

Copyright (c) 2019 Veoneer Sweden AB

Author: Ludwig Ring

All rights reserved. Property of Veoneer Sweden AB.
Restricted rights to use, duplicate or disclose this code are granted through contract.
"""

from optparse import OptionParser
import sys

from Tools.Extension.spp_support import verify_imports

from Tools.Extension.spp_base import (
    Generator,
    GeneratorResult,
    ProtoFile,
)

from Tools.Extension.spp_base import run_generator

verify_imports()

# Availability checked by verify_imports
import google.protobuf.descriptor_pb2 as descriptor


class SummaryProtoFile(ProtoFile):
    def generate_summary(self):
        yield "Source.Identifier: Name\n"
        for msg in self.messages:
            if msg.source and msg.identifier:
                yield f"{msg.source}.{msg.identifier}: {msg.get_full_name()}\n"


class SummaryGenerator(Generator):
    def create_proto_file(self, fdesc: descriptor.FileDescriptorProto):
        return SummaryProtoFile(fdesc, self.options, self.spp_version)

    def generate_result(self):
        result = []
        interfaces = "".join(self.proto_file.generate_summary())
        if len(interfaces) > 0:
            filename = "{}{}.txt".format(
                self.proto_file.get_target_base(), self.options.extension,
            )
            result.append(GeneratorResult(filename, interfaces))

        return result


def main(plugin: bool = True):
    generator = SummaryGenerator()
    optparser = OptionParser()
    optparser.add_option(
        "-e",
        "--extension",
        dest="extension",
        metavar="EXTENSION",
        default=".summary",
        help="Set extension to use between filename and file extension for generated files. Example: file.summary.txt [default: %default]",
    )

    run_generator(generator, optparser, plugin)
