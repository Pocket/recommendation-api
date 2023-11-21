# encoding: utf-8
# module pyexpat.errors
# from /usr/local/lib/python3.8/lib-dynload/pyexpat.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Constants used to describe error conditions. """
# no imports

# Variables with simple values

XML_ERROR_ABORTED = 'parsing aborted'

XML_ERROR_ASYNC_ENTITY = 'asynchronous entity'

XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF = 'reference to external entity in attribute'

XML_ERROR_BAD_CHAR_REF = 'reference to invalid character number'

XML_ERROR_BINARY_ENTITY_REF = 'reference to binary entity'

XML_ERROR_CANT_CHANGE_FEATURE_ONCE_PARSING = 'cannot change setting once parsing has begun'

XML_ERROR_DUPLICATE_ATTRIBUTE = 'duplicate attribute'

XML_ERROR_ENTITY_DECLARED_IN_PE = 'entity declared in parameter entity'

XML_ERROR_EXTERNAL_ENTITY_HANDLING = 'error in processing external entity reference'

XML_ERROR_FEATURE_REQUIRES_XML_DTD = 'requested feature requires XML_DTD support in Expat'

XML_ERROR_FINISHED = 'parsing finished'

XML_ERROR_INCOMPLETE_PE = 'incomplete markup in parameter entity'

XML_ERROR_INCORRECT_ENCODING = 'encoding specified in XML declaration is incorrect'

XML_ERROR_INVALID_TOKEN = 'not well-formed (invalid token)'

XML_ERROR_JUNK_AFTER_DOC_ELEMENT = 'junk after document element'

XML_ERROR_MISPLACED_XML_PI = 'XML or text declaration not at start of entity'

XML_ERROR_NOT_STANDALONE = 'document is not standalone'
XML_ERROR_NOT_SUSPENDED = 'parser not suspended'

XML_ERROR_NO_ELEMENTS = 'no element found'
XML_ERROR_NO_MEMORY = 'out of memory'

XML_ERROR_PARAM_ENTITY_REF = 'illegal parameter entity reference'

XML_ERROR_PARTIAL_CHAR = 'partial character'

XML_ERROR_PUBLICID = 'illegal character(s) in public id'

XML_ERROR_RECURSIVE_ENTITY_REF = 'recursive entity reference'

XML_ERROR_SUSPENDED = 'parser suspended'

XML_ERROR_SUSPEND_PE = 'cannot suspend in external parameter entity'

XML_ERROR_SYNTAX = 'syntax error'

XML_ERROR_TAG_MISMATCH = 'mismatched tag'

XML_ERROR_TEXT_DECL = 'text declaration not well-formed'

XML_ERROR_UNBOUND_PREFIX = 'unbound prefix'

XML_ERROR_UNCLOSED_CDATA_SECTION = 'unclosed CDATA section'

XML_ERROR_UNCLOSED_TOKEN = 'unclosed token'

XML_ERROR_UNDECLARING_PREFIX = 'must not undeclare prefix'

XML_ERROR_UNDEFINED_ENTITY = 'undefined entity'

XML_ERROR_UNEXPECTED_STATE = 'unexpected parser state - please send a bug report'

XML_ERROR_UNKNOWN_ENCODING = 'unknown encoding'

XML_ERROR_XML_DECL = 'XML declaration not well-formed'

__loader__ = None

__spec__ = None

# no functions
# no classes
# variables with complex values

codes = {
    'XML declaration not well-formed': 30,
    'XML or text declaration not at start of entity': 17,
    'asynchronous entity': 13,
    'cannot change setting once parsing has begun': 26,
    'cannot suspend in external parameter entity': 37,
    'document is not standalone': 22,
    'duplicate attribute': 8,
    'encoding specified in XML declaration is incorrect': 19,
    'entity declared in parameter entity': 24,
    'error in processing external entity reference': 21,
    'illegal character(s) in public id': 32,
    'illegal parameter entity reference': 10,
    'incomplete markup in parameter entity': 29,
    'junk after document element': 9,
    'mismatched tag': 7,
    'must not undeclare prefix': 28,
    'no element found': 3,
    'not well-formed (invalid token)': 4,
    'out of memory': 1,
    'parser not suspended': 34,
    'parser suspended': 33,
    'parsing aborted': 35,
    'parsing finished': 36,
    'partial character': 6,
    'recursive entity reference': 12,
    'reference to binary entity': 15,
    'reference to external entity in attribute': 16,
    'reference to invalid character number': 14,
    'requested feature requires XML_DTD support in Expat': 25,
    'syntax error': 2,
    'text declaration not well-formed': 31,
    'unbound prefix': 27,
    'unclosed CDATA section': 20,
    'unclosed token': 5,
    'undefined entity': 11,
    'unexpected parser state - please send a bug report': 23,
    'unknown encoding': 18,
}

messages = {
    1: 'out of memory',
    2: 'syntax error',
    3: 'no element found',
    4: 'not well-formed (invalid token)',
    5: 'unclosed token',
    6: 'partial character',
    7: 'mismatched tag',
    8: 'duplicate attribute',
    9: 'junk after document element',
    10: 'illegal parameter entity reference',
    11: 'undefined entity',
    12: 'recursive entity reference',
    13: 'asynchronous entity',
    14: 'reference to invalid character number',
    15: 'reference to binary entity',
    16: 'reference to external entity in attribute',
    17: 'XML or text declaration not at start of entity',
    18: 'unknown encoding',
    19: 'encoding specified in XML declaration is incorrect',
    20: 'unclosed CDATA section',
    21: 'error in processing external entity reference',
    22: 'document is not standalone',
    23: 'unexpected parser state - please send a bug report',
    24: 'entity declared in parameter entity',
    25: 'requested feature requires XML_DTD support in Expat',
    26: 'cannot change setting once parsing has begun',
    27: 'unbound prefix',
    28: 'must not undeclare prefix',
    29: 'incomplete markup in parameter entity',
    30: 'XML declaration not well-formed',
    31: 'text declaration not well-formed',
    32: 'illegal character(s) in public id',
    33: 'parser suspended',
    34: 'parser not suspended',
    35: 'parsing aborted',
    36: 'parsing finished',
    37: 'cannot suspend in external parameter entity',
}

