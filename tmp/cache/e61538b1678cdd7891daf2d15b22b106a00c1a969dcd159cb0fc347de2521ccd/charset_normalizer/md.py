# encoding: utf-8
# module charset_normalizer.md
# from /.venv/lib/python3.8/site-packages/charset_normalizer/md.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

TRACE = 5

# functions

def getLogger(name=None): # reliably restored by inspect
    """
    Return a logger with the specified name, creating it if necessary.
    
        If no name is specified, return the root logger.
    """
    pass

def is_accentuated(*args, **kwargs): # real signature unknown
    pass

def is_case_variable(*args, **kwargs): # real signature unknown
    pass

def is_cjk(*args, **kwargs): # real signature unknown
    pass

def is_emoticon(*args, **kwargs): # real signature unknown
    pass

def is_hangul(*args, **kwargs): # real signature unknown
    pass

def is_hiragana(*args, **kwargs): # real signature unknown
    pass

def is_katakana(*args, **kwargs): # real signature unknown
    pass

def is_latin(*args, **kwargs): # real signature unknown
    pass

def is_punctuation(*args, **kwargs): # real signature unknown
    pass

def is_separator(*args, **kwargs): # real signature unknown
    pass

def is_suspiciously_successive_range(*args, **kwargs): # real signature unknown
    pass

def is_symbol(*args, **kwargs): # real signature unknown
    pass

def is_thai(*args, **kwargs): # real signature unknown
    pass

def is_unprintable(*args, **kwargs): # real signature unknown
    pass

def List(*args, **kwargs): # real signature unknown
    """
    The central part of internal API.
    
        This represents a generic version of type 'origin' with type arguments 'params'.
        There are two kind of these aliases: user defined and special. The special ones
        are wrappers around builtin collections and ABCs in collections.abc. These must
        have 'name' always set. If 'inst' is False, then the alias can't be instantiated,
        this is used by e.g. typing.List and typing.Dict.
    """
    pass

def lru_cache(maxsize=128, typed=False): # reliably restored by inspect
    """
    Least-recently-used cache decorator.
    
        If *maxsize* is set to None, the LRU features are disabled and the cache
        can grow without bound.
    
        If *typed* is True, arguments of different types will be cached separately.
        For example, f(3.0) and f(3) will be treated as distinct calls with
        distinct results.
    
        Arguments to the cached function must be hashable.
    
        View the cache statistics named tuple (hits, misses, maxsize, currsize)
        with f.cache_info().  Clear the cache and statistics with f.cache_clear().
        Access the underlying function with f.__wrapped__.
    
        See:  http://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
    """
    pass

def mess_ratio(*args, **kwargs): # real signature unknown
    pass

def Optional(*args, **kwargs): # real signature unknown
    """
    Internal indicator of special typing constructs.
        See _doc instance attribute for specific docs.
    """
    pass

def remove_accent(*args, **kwargs): # real signature unknown
    pass

def unicode_range(*args, **kwargs): # real signature unknown
    """ Retrieve the Unicode range official name from a single character. """
    pass

# classes

class MessDetectorPlugin(object):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = ()


class ArchaicUpperLowerPlugin(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count_since_last_sep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _current_ascii_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_alpha_seen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _successive_upper_lower_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _successive_upper_lower_count_final = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_buf',
        '_character_count_since_last_sep',
        '_successive_upper_lower_count',
        '_successive_upper_lower_count_final',
        '_character_count',
        '_last_alpha_seen',
        '_current_ascii_only',
    )


class CjkInvalidStopPlugin(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _cjk_character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _wrong_stop_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_wrong_stop_count',
        '_cjk_character_count',
    )


class SuperWeirdWordPlugin(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _bad_character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _bad_word_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer_accent_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _foreign_long_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _foreign_long_watch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_current_word_bad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _word_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_word_count',
        '_bad_word_count',
        '_foreign_long_count',
        '_is_current_word_bad',
        '_foreign_long_watch',
        '_character_count',
        '_bad_character_count',
        '_buffer',
        '_buffer_accent_count',
    )


class SuspiciousDuplicateAccentPlugin(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_latin_character = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _successive_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_successive_count',
        '_character_count',
        '_last_latin_character',
    )


class SuspiciousRange(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_printable_seen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suspicious_successive_range_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_suspicious_successive_range_count',
        '_character_count',
        '_last_printable_seen',
    )


class TooManyAccentuatedPlugin(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _accentuated_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_character_count',
        '_accentuated_count',
    )


class TooManySymbolOrPunctuationPlugin(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _frenzy_symbol_in_word = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_printable_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _punctuation_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _symbol_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_punctuation_count',
        '_symbol_count',
        '_character_count',
        '_last_printable_char',
        '_frenzy_symbol_in_word',
    )


class UnprintablePlugin(MessDetectorPlugin):
    # no doc
    def eligible(self, *args, **kwargs): # real signature unknown
        pass

    def feed(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _unprintable_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_unprintable_count',
        '_character_count',
    )


# variables with complex values

COMMON_SAFE_ASCII_CHARACTERS = None # (!) real value is '{\'/\', \'&\', \'{\', \',\', \'>\', \'}\', \'[\', \'|\', \'-\', \']\', \'=\', \'"\', \';\', \'<\', \':\'}'

UNICODE_SECONDARY_RANGE_KEYWORD = [
    'Supplement',
    'Extended',
    'Extensions',
    'Modifier',
    'Marks',
    'Punctuation',
    'Symbols',
    'Forms',
    'Operators',
    'Miscellaneous',
    'Drawing',
    'Block',
    'Shapes',
    'Supplemental',
    'Tags',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffabebd820>'

__spec__ = None # (!) real value is "ModuleSpec(name='charset_normalizer.md', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffabebd820>, origin='/.venv/lib/python3.8/site-packages/charset_normalizer/md.cpython-38-aarch64-linux-gnu.so')"

