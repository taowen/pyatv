"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.extension_dict
import google.protobuf.message
import pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GenericMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KEY_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    key: builtins.str
    value: builtins.bytes
    def __init__(
        self,
        *,
        key: builtins.str | None = ...,
        value: builtins.bytes | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

global___GenericMessage = GenericMessage

GENERICMESSAGE_FIELD_NUMBER: builtins.int
genericMessage: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[pyatv.protocols.mrp.protobuf.ProtocolMessage_pb2.ProtocolMessage, global___GenericMessage]
