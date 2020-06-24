"""
Brief: This file contains classes for HTML documentation generation
       based on protobuf definitions extended with SystemOptions.

Copyright (c) 2019 Veoneer Sweden AB

Author: Ludwig Ring

All rights reserved. Property of Veoneer Sweden AB.
Restricted rights to use, duplicate or disclose this code are granted through contract.
"""

from optparse import OptionParser
import sys

import Tools.Extension.spp_support as Support
from Tools.Extension.spp_support import EncodedSize

from Tools.Extension.spp_prototypes import (
    ArrayProtoType,
    BoolProtoType,
    EnumProtoType,
    MessageProtoType,
)
from Tools.Extension.spp_base import (
    EnumDefinition,
    EnumValue,
    Field,
    Generator,
    GeneratorResult,
    Message,
    ProtoFile,
    Version,
)

from Tools.Extension.spp_base import run_generator

Support.verify_imports()

# Availability checked by verify_imports
import google.protobuf.descriptor_pb2 as descriptor

import Tools.Extension.DataSources_pb2 as ds


class HtmlEnum(EnumDefinition):
    def __init__(
        self,
        name: str,
        descriptor: descriptor.EnumDescriptorProto,
        parent,
        enum_options: descriptor.EnumOptions,
    ):
        super().__init__(name, descriptor, parent, enum_options)

    def html(self):
        type_name = self.get_full_name().remove_from_beginning(self.get_package())
        result = '<h2 id="{full_name}">{type_name} ({full_name})</h2>\n'.format(
            full_name=self.get_full_name(), type_name=type_name,
        )
        result += f"Max Encoded Size (bytes): {self.encoded_size}"
        if self.description:
            result += f"{self.description}\n<br>\n"
        result += '<table class="enum-table">\n'
        result += "<tr><th>Name</th><th>Full name</th><th>Value</th></tr>\n"
        for enum_value in self.values:
            result += "<tr><td>{name}</td><td>{full_name}</td><td>{value}</td></tr>\n".format(
                name=enum_value.name,
                full_name=enum_value.get_full_name(),
                value=enum_value.number,
            )
        result += "</table>\n"
        return result


class HtmlField(Field):
    def __init__(self, parent, descriptor, field_options):
        super().__init__(parent, descriptor, field_options)

    @staticmethod
    def html_table_header():
        return "<tr><th>{}</th><th>{}</th><th>{}</th><th>{}</th><th>{}</th><th>{}</th><th>{}</th><th>{}</th><th>{}</th></tr>\n".format(
            "Field",
            "Type",
            "Min",
            "Max",
            "Resolution",
            "Unit",
            "Max Encoded Size (bytes) incl. tag & type [min/max considered]",
            "Tag & type size (bytes)",
            "Description",
        )

    @staticmethod
    def get_resolution_min_max(data_type):
        resolution = ""
        min_str = ""
        max_str = ""

        if isinstance(data_type, ArrayProtoType):
            return HtmlField.get_resolution_min_max(data_type.data_type)

        if (
            hasattr(data_type, "min")
            and hasattr(data_type, "max")
            and data_type.min != None
            and data_type.max != None
        ):
            min_str = Support.strip_float(f"{data_type.min:g}")
            max_str = Support.strip_float(f"{data_type.max:g}")

        # Exclude Bool and Enum since they inherit from Varint but we don't want to add resolution 1 to these
        if hasattr(data_type, "scale") and not (
            isinstance(data_type, BoolProtoType) or isinstance(data_type, EnumProtoType)
        ):
            resolution = data_type.scale if data_type.scale is not None else "1"

        return resolution, min_str, max_str

    def html_table_row(self, enc_size_str):
        resolution, min_str, max_str = HtmlField.get_resolution_min_max(self.data_type)

        if self.unit != "":
            min_str = f"{min_str} {self.unit}"
            max_str = f"{max_str} {self.unit}"

        type_with_link = self.data_type.get_name()
        data_type = self.data_type
        if isinstance(data_type, ArrayProtoType):
            type_with_link += f"[{self.data_type.max_count}]"
            data_type = self.data_type.data_type

        # TODO: Think about adding link for external dependencies
        if isinstance(data_type, MessageProtoType) or isinstance(
            data_type, EnumProtoType
        ):
            type_with_link = '<a href="#{name}">{type_name}</a>'.format(
                name=self.data_type.get_name(), type_name=type_with_link
            )

        return "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>\n".format(
            self.name,
            type_with_link,
            min_str,
            max_str,
            resolution,
            self.unit,
            enc_size_str,
            Support.varint_max_size(self.id << 3),
            self.description,
        )

    @staticmethod
    def html_table_summary(total_enc_size_str, total_tag_sizes):
        return "<tr><th></th><th></th><th></th><th></th><th></th><th></th><th>{}</th><th>{}</th><th></th></tr>\n".format(
            total_enc_size_str, total_tag_sizes
        )


class HtmlMessage(Message):
    def __init__(self, names, descriptor, package, message_options, options):
        super().__init__(names, descriptor, package, message_options, options)

    def create_field(self, field, field_options):
        return HtmlField(self, field, field_options)

    def html(self, proto_file):
        type_name = self.get_full_name().remove_from_beginning(self.get_package())
        result = '<h2 id="{full_name}">{type_name} ({full_name})</h2>\n'.format(
            full_name=self.get_full_name(), type_name=type_name,
        )
        if self.source:
            result += "Source: {name} ({source})\n<br>\n".format(
                name=ds._DATASOURCE.values_by_number[self.source].name,
                source=self.source,
            )
        if self.identifier:
            result += f"Identifier: {self.identifier} ({self.identifier:0x})\n<br>\n"
        if self.version:
            result += f"Version: {self.version}\n<br>\n"
        if self.description:
            result += self.description + "\n<br>\n"
        result += '<table class="property-table">\n'
        result += HtmlField.html_table_header()
        total_enc_size = EncodedSize()
        total_tag_sizes = 0
        for field in self.fields:
            enc_size_str = ""
            encsize = field.get_encoded_size()
            if encsize is not None:
                if isinstance(encsize, EncodedSize):
                    enc_size_str = encsize.string_with_reduction()
                else:
                    raise Exception("TODO: Fix it")  # TODO: Remove
                total_enc_size += encsize
            total_tag_sizes += Support.varint_max_size(field.id << 3)
            default = field.html_table_row(enc_size_str)
            if default is not None:
                result += default
        total_enc_size_str = ""
        if total_enc_size is not None:
            if isinstance(total_enc_size, EncodedSize):
                total_enc_size_str = total_enc_size.string_with_reduction()
            else:
                total_enc_size_str = str(total_enc_size)
        result += HtmlField.html_table_summary(total_enc_size_str, total_tag_sizes)

        result += "</table>\n"
        return result


class HtmlProtoFile(ProtoFile):
    def create_enum(self, name, enum, parent, enum_options):
        return HtmlEnum(name, enum, parent, enum_options)

    def create_message(self, name, message, parent, message_options):
        return HtmlMessage(name, message, parent, message_options, self.options)

    def generate_html(self):
        """Generate content for a html file."""
        yield "<!DOCTYPE html>\n"
        yield "<html>\n"
        yield "<head>\n"
        yield f"   <title>{self.filename} Specification</title>\n"
        yield '   <style type="text/css">\n'
        yield "      body {\n"
        yield '         font-family: "lucida Sans Unicode", "Lucida Grande", "Segoe UI", vardana;\n'
        yield "      }\n"
        yield "\n"
        yield "      .property-table {\n"
        yield "         border-collapse: collapse;\n"
        yield "         text-align: left;\n"
        yield "      }\n"
        yield "\n"
        yield "      .property-table th,\n"
        yield "      .property-table td {\n"
        yield "         border: 1px solid black;\n"
        yield "         padding: 5px 10px;\n"
        yield "      }\n"
        yield "\n"
        yield "      .property-table tr:nth-child(odd) td {\n"
        yield "			background-color: #b5c5ea;\n"
        yield "		}\n"
        yield "\n"
        yield "		.property-table tr:nth-child(even) td {\n"
        yield "			background-color: #6f9aec;\n"
        yield "		}\n"
        yield "\n"
        yield "      .enum-table {\n"
        yield "         border-collapse: collapse;\n"
        yield "      }\n"
        yield "\n"
        yield "      .enum-table th,\n"
        yield "      .enum-table td {\n"
        yield "         padding: 1px 10px;\n"
        yield "         border: 1px solid black;\n"
        yield "      }\n"
        yield "\n"
        yield "      .enum-table tr:nth-child(odd) td {\n"
        yield "			background-color: #ebb4b4;\n"
        yield "		}\n"
        yield "\n"
        yield "		.enum-table tr:nth-child(even) td {\n"
        yield "			background-color: #dc7878;\n"
        yield "		}\n"
        yield "\n"
        yield "      a {\n"
        yield "         text-decoration: none;\n"
        yield "         color: black;\n"
        yield "      }\n"
        yield "   </style>\n"
        yield "</head>\n"
        yield "<body>\n"
        yield f"Spp version {self.spp_version}.<br>\n\n"

        if self.fdesc.package != "":
            yield f"<b>Package - {self.fdesc.package}</b>\n<br>\n"

        yield "<h1>Messages</h1>\n"
        for msg in self.messages:
            yield msg.html(self)

        if self.enums:
            yield "<h1>Enums</h1>\n"
            for enum in self.enums:
                yield enum.html()

        yield "</body>\n"
        yield "</html>\n"


class HtmlGenerator(Generator):
    def create_proto_file(self, fdesc: descriptor.FileDescriptorProto):
        return HtmlProtoFile(fdesc, self.options, self.spp_version)

    def generate_result(self):
        result = []
        filename = "{file}.html".format(file=self.proto_file.get_target_base())
        result.append(
            GeneratorResult(filename, "".join(self.proto_file.generate_html()))
        )

        return result


def main(plugin: bool = True):
    generator = HtmlGenerator()
    optparser = OptionParser()

    run_generator(generator, optparser, plugin)
