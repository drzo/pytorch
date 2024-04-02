"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

global___LegacyPadding = LegacyPadding
class _LegacyPadding(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LegacyPadding], type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
    NOTSET = LegacyPadding.V(0)
    VALID = LegacyPadding.V(1)
    SAME = LegacyPadding.V(2)
    CAFFE_LEGACY_POOLING = LegacyPadding.V(3)
class LegacyPadding(metaclass=_LegacyPadding):
    V = typing.NewType('V', int)
NOTSET = LegacyPadding.V(0)
VALID = LegacyPadding.V(1)
SAME = LegacyPadding.V(2)
CAFFE_LEGACY_POOLING = LegacyPadding.V(3)

class CaffeDatum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CHANNELS_FIELD_NUMBER: int
    HEIGHT_FIELD_NUMBER: int
    WIDTH_FIELD_NUMBER: int
    DATA_FIELD_NUMBER: int
    LABEL_FIELD_NUMBER: int
    FLOAT_DATA_FIELD_NUMBER: int
    ENCODED_FIELD_NUMBER: int
    channels: int = ...
    height: int = ...
    width: int = ...
    data: bytes = ...
    label: int = ...
    float_data: google.protobuf.internal.containers.RepeatedScalarFieldContainer[float] = ...
    encoded: bool = ...

    def __init__(self,
        *,
        channels : typing.Optional[int] = ...,
        height : typing.Optional[int] = ...,
        width : typing.Optional[int] = ...,
        data : typing.Optional[bytes] = ...,
        label : typing.Optional[int] = ...,
        float_data : typing.Optional[typing.Iterable[float]] = ...,
        encoded : typing.Optional[bool] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"channels",b"channels",u"data",b"data",u"encoded",b"encoded",u"height",b"height",u"label",b"label",u"width",b"width"]) -> bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"channels",b"channels",u"data",b"data",u"encoded",b"encoded",u"float_data",b"float_data",u"height",b"height",u"label",b"label",u"width",b"width"]) -> None: ...
global___CaffeDatum = CaffeDatum
