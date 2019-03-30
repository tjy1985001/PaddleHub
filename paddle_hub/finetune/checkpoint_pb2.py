# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: checkpoint.proto

import sys
_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
    name='checkpoint.proto',
    package='paddle_hub_finetune_checkpoint',
    syntax='proto3',
    serialized_pb=_b(
        '\n\x10\x63heckpoint.proto\x12\x1epaddle_hub_finetune_checkpoint\"K\n\nCheckPoint\x12\x12\n\nlast_epoch\x18\x01 \x01(\x03\x12\x11\n\tlast_step\x18\x02 \x01(\x03\x12\x16\n\x0elast_model_dir\x18\x03 \x01(\tB\x02H\x03\x62\x06proto3'
    ))
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_CHECKPOINT = _descriptor.Descriptor(
    name='CheckPoint',
    full_name='paddle_hub_finetune_checkpoint.CheckPoint',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='last_epoch',
            full_name='paddle_hub_finetune_checkpoint.CheckPoint.last_epoch',
            index=0,
            number=1,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='last_step',
            full_name='paddle_hub_finetune_checkpoint.CheckPoint.last_step',
            index=1,
            number=2,
            type=3,
            cpp_type=2,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
        _descriptor.FieldDescriptor(
            name='last_model_dir',
            full_name='paddle_hub_finetune_checkpoint.CheckPoint.last_model_dir',
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=52,
    serialized_end=127,
)

DESCRIPTOR.message_types_by_name['CheckPoint'] = _CHECKPOINT

CheckPoint = _reflection.GeneratedProtocolMessageType(
    'CheckPoint',
    (_message.Message, ),
    dict(
        DESCRIPTOR=_CHECKPOINT,
        __module__='checkpoint_pb2'
        # @@protoc_insertion_point(class_scope:paddle_hub_finetune_checkpoint.CheckPoint)
    ))
_sym_db.RegisterMessage(CheckPoint)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(),
                                                _b('H\003'))
# @@protoc_insertion_point(module_scope)