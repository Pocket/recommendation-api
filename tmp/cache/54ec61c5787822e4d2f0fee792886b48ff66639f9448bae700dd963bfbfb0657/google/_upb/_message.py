# encoding: utf-8
# module google._upb._message
# from /.venv/lib/python3.8/site-packages/google/_upb/_message.abi3.so
# by generator 1.147
""" Protobuf Module """

# imports
import collections.abc as __collections_abc


# Variables with simple values

_IS_UPB = 1

# functions

def SetAllowOversizeProtos(*args, **kwargs): # real signature unknown
    """ Enable/disable oversize proto parsing. """
    pass

# classes

class Arena(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Descriptor(object):
    # no doc
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def EnumValueName(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    enum_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum sequence"""

    enum_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum types by name"""

    enum_values_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum values by name"""

    extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extensions Sequence"""

    extensions_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extensions by name"""

    extension_ranges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extension ranges"""

    fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields sequence"""

    fields_by_camelcase_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields by camelCase name"""

    fields_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields by name"""

    fields_by_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields by number"""

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    is_extendable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Last name"""

    nested_types = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nested types sequence"""

    nested_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Nested types by name"""

    oneofs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Oneofs Sequence"""

    oneofs_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Oneofs by name"""

    syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Syntax"""

    _concrete_class = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """concrete class"""



class DescriptorPool(object):
    # no doc
    def Add(self, *args, **kwargs): # real signature unknown
        """ Adds the FileDescriptorProto and its types to this pool. """
        pass

    def AddSerializedFile(self, *args, **kwargs): # real signature unknown
        """ Adds a serialized FileDescriptorProto to this pool. """
        pass

    def FindAllExtensions(self, *args, **kwargs): # real signature unknown
        """ Gets all known extensions of the given message descriptor. """
        pass

    def FindEnumTypeByName(self, *args, **kwargs): # real signature unknown
        """ Searches for enum type descriptor by full name. """
        pass

    def FindExtensionByName(self, *args, **kwargs): # real signature unknown
        """ Searches for extension descriptor by full name. """
        pass

    def FindExtensionByNumber(self, *args, **kwargs): # real signature unknown
        """ Gets the extension descriptor for the given number. """
        pass

    def FindFieldByName(self, *args, **kwargs): # real signature unknown
        """ Searches for a field descriptor by full name. """
        pass

    def FindFileByName(self, *args, **kwargs): # real signature unknown
        """ Searches for a file descriptor by its .proto name. """
        pass

    def FindFileContainingSymbol(self, *args, **kwargs): # real signature unknown
        """ Gets the FileDescriptor containing the specified symbol. """
        pass

    def FindMessageTypeByName(self, *args, **kwargs): # real signature unknown
        """ Searches for a message descriptor by full name. """
        pass

    def FindMethodByName(self, *args, **kwargs): # real signature unknown
        """ Searches for method descriptor by full name. """
        pass

    def FindOneofByName(self, *args, **kwargs): # real signature unknown
        """ Searches for oneof descriptor by full name. """
        pass

    def FindServiceByName(self, *args, **kwargs): # real signature unknown
        """ Searches for service descriptor by full name. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class EnumDescriptor(object):
    # no doc
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    is_closed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Checks if the enum is closed"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """last name"""

    values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """values"""

    values_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum values by name"""

    values_by_number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum values by number"""



class EnumValueDescriptor(object):
    # no doc
    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """index"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """number"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """index"""



class ExtensionDict(object):
    # no doc
    def _FindExtensionByName(self, *args, **kwargs): # real signature unknown
        """ Finds an extension by name. """
        pass

    def _FindExtensionByNumber(self, *args, **kwargs): # real signature unknown
        """ Finds an extension by number. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class ExtensionIterator(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


class FieldDescriptor(object):
    # no doc
    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    camelcase_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CamelCase name"""

    containing_oneof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing oneof"""

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    cpp_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """C++ Type"""

    default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default Value"""

    enum_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enum type"""

    extension_scope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extension scope"""

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File Descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_default_value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    has_presence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Presence"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    is_extension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ID"""

    json_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Json name"""

    label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Label"""

    message_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Message type"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Unqualified name"""

    number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type"""


    LABEL_OPTIONAL = 1
    LABEL_REPEATED = 3
    LABEL_REQUIRED = 2
    TYPE_BOOL = 8
    TYPE_BYTES = 12
    TYPE_DOUBLE = 1
    TYPE_ENUM = 14
    TYPE_FIXED32 = 7
    TYPE_FIXED64 = 6
    TYPE_FLOAT = 2
    TYPE_GROUP = 10
    TYPE_INT32 = 5
    TYPE_INT64 = 3
    TYPE_MESSAGE = 11
    TYPE_SFIXED32 = 15
    TYPE_SFIXED64 = 16
    TYPE_SINT32 = 17
    TYPE_SINT64 = 18
    TYPE_STRING = 9
    TYPE_UINT32 = 13
    TYPE_UINT64 = 4


class FileDescriptor(object):
    # no doc
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    dependencies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dependencies"""

    enum_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Enums by name"""

    extensions_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extensions by name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    message_types_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Messages by name"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name"""

    package = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """package"""

    pool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """pool"""

    public_dependencies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dependencies"""

    serialized_pb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    services_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Services by name"""

    syntax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Syntax"""



class MapIterator(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


class Message(object):
    """ A ProtocolMessage """
    def ByteSize(self, *args, **kwargs): # real signature unknown
        """ Returns the size of the message in bytes. """
        pass

    def Clear(self, *args, **kwargs): # real signature unknown
        """ Clears the message. """
        pass

    def ClearExtension(self, *args, **kwargs): # real signature unknown
        """ Clears a message field. """
        pass

    def ClearField(self, *args, **kwargs): # real signature unknown
        """ Clears a message field. """
        pass

    def DiscardUnknownFields(self, *args, **kwargs): # real signature unknown
        """ Discards the unknown fields. """
        pass

    def FindInitializationErrors(self, *args, **kwargs): # real signature unknown
        """ Finds unset required fields. """
        pass

    @classmethod
    def FromString(cls, *args, **kwargs): # real signature unknown
        """ Creates new method instance from given serialized data. """
        pass

    def HasExtension(self, *args, **kwargs): # real signature unknown
        """ Checks if a message field is set. """
        pass

    def HasField(self, *args, **kwargs): # real signature unknown
        """ Checks if a message field is set. """
        pass

    def IsInitialized(self, *args, **kwargs): # real signature unknown
        """ Checks if all required fields of a protocol message are set. """
        pass

    def ListFields(self, *args, **kwargs): # real signature unknown
        """ Lists all set fields of a message. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a protocol message into the current message. """
        pass

    def MergeFromString(self, *args, **kwargs): # real signature unknown
        """ Merges a serialized message into the current message. """
        pass

    def ParseFromString(self, *args, **kwargs): # real signature unknown
        """ Parses a serialized message into the current message. """
        pass

    def SerializePartialToString(self, *args, **kwargs): # real signature unknown
        """ Serializes the message to a string, even if it isn't initialized. """
        pass

    def SerializeToString(self, *args, **kwargs): # real signature unknown
        """ Serializes the message to a string, only for initialized messages. """
        pass

    def SetInParent(self, *args, **kwargs): # real signature unknown
        """ Sets the has bit of the given field in its parent message. """
        pass

    def UnknownFields(self, *args, **kwargs): # real signature unknown
        """ Parse unknown field set """
        pass

    def WhichOneof(self, *args, **kwargs): # real signature unknown
        """ Returns the name of the field set inside a oneof, or None if no field is set. """
        pass

    def _CheckCalledFromGeneratedFile(self, *args, **kwargs): # real signature unknown
        """ Raises TypeError if the caller is not in a _pb2.py file. """
        pass

    def _ListFieldsItemKey(self, *args, **kwargs): # real signature unknown
        """ Compares ListFields() list entries by field number """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __delattr__(self, *args, **kwargs): # real signature unknown
        """ Implement delattr(self, name). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setattr__(self, *args, **kwargs): # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    Extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extension dict"""


    __hash__ = None


class MessageMapContainer(__collections_abc.MutableMapping):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        """ Removes all elements from the map. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """ Gets the value for the given key if present, or otherwise a default """
        pass

    def GetEntryClass(self, *args, **kwargs): # real signature unknown
        """ Return the class used to build Entries of (key, value) pairs. """
        pass

    def get_or_create(self, *args, **kwargs): # real signature unknown
        """ Alias for getitem, useful to make explicit that the map is mutated. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a map into the current map. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Tests whether the map contains this element. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class MessageMeta(type):
    # no doc
    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class MethodDescriptor(object):
    # no doc
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    containing_service = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing service"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    input_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Input type"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name"""

    output_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Output type"""



class OneofDescriptor(object):
    # no doc
    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    containing_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Containing type"""

    fields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Fields"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    has_options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has Options"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name"""



class RepeatedCompositeContainer(object):
    # no doc
    def add(self, *args, **kwargs): # real signature unknown
        """ Adds an object to the repeated container. """
        pass

    def append(self, *args, **kwargs): # real signature unknown
        """ Appends a message to the end of the repeated container. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """ Adds objects to the repeated container. """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """ Inserts a message before the specified index. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Adds objects to the repeated container. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container and returns it. """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container. """
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverses elements order of the repeated container. """
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        """ Sorts the repeated container. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class RepeatedScalarContainer(object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        """ Appends an object to the repeated container. """
        pass

    def extend(self, *args, **kwargs): # real signature unknown
        """ Appends objects to the repeated container. """
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        """ Inserts an object at the specified position in the container. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a repeated container into the current container. """
        pass

    def pop(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container and returns it. """
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        """ Removes an object from the repeated container. """
        pass

    def reverse(self, *args, **kwargs): # real signature unknown
        """ Reverses elements order of the repeated container. """
        pass

    def sort(self, *args, **kwargs): # real signature unknown
        """ Sorts the repeated container. """
        pass

    def __deepcopy__(self, *args, **kwargs): # real signature unknown
        """ Makes a deep copy of the class. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Outputs picklable representation of the repeated field. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class ScalarMapContainer(__collections_abc.MutableMapping):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        """ Removes all elements from the map. """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """ Gets the value for the given key if present, or otherwise a default """
        pass

    def GetEntryClass(self, *args, **kwargs): # real signature unknown
        """ Return the class used to build Entries of (key, value) pairs. """
        pass

    def MergeFrom(self, *args, **kwargs): # real signature unknown
        """ Merges a map into the current map. """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Tests whether a key is a member of the map. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class ServiceDescriptor(object):
    # no doc
    def CopyToProto(self, *args, **kwargs): # real signature unknown
        pass

    def FindMethodByName(self, *args, **kwargs): # real signature unknown
        pass

    def GetOptions(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    file = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """File descriptor"""

    full_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Full name"""

    index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Index"""

    methods = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Methods"""

    methods_by_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Methods by name"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Name"""



class UnknownFieldSet(object):
    # no doc
    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __hash__ = None


class _ByNameIterator(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


class _ByNameMap(object):
    # no doc
    def get(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def values(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class _ByNumberIterator(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass


class _ByNumberMap(object):
    # no doc
    def get(self, *args, **kwargs): # real signature unknown
        pass

    def items(self, *args, **kwargs): # real signature unknown
        pass

    def keys(self, *args, **kwargs): # real signature unknown
        pass

    def values(self, *args, **kwargs): # real signature unknown
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return key in self. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    __hash__ = None


class _GenericSequence(object):
    # no doc
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def count(self, *args, **kwargs): # real signature unknown
        pass

    def index(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __hash__ = None


# variables with complex values

default_pool = None # (!) real value is '<google._upb._message.DescriptorPool object at 0xffffac924c70>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924a60>'

__spec__ = None # (!) real value is "ModuleSpec(name='google._upb._message', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924a60>, origin='/.venv/lib/python3.8/site-packages/google/_upb/_message.abi3.so')"

