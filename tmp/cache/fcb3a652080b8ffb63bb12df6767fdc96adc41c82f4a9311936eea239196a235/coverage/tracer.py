# encoding: utf-8
# module coverage.tracer
# from /.venv/lib/python3.8/site-packages/coverage/tracer.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
""" Fast coverage tracer. """
# no imports

# no functions
# classes

class CFileDisposition(object):
    """ CFileDisposition objects """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    canonical_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    file_tracer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    has_dynamic_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    original_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    reason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CTracer(object):
    """ CTracer objects """
    def activity(self, *args, **kwargs): # real signature unknown
        """ Has there been any activity? """
        pass

    def get_stats(self, *args, **kwargs): # real signature unknown
        """ Get statistics about the tracing """
        pass

    def reset_activity(self, *args, **kwargs): # real signature unknown
        """ Reset the activity flag """
        pass

    def start(self, *args, **kwargs): # real signature unknown
        """ Start the tracer """
        pass

    def stop(self, *args, **kwargs): # real signature unknown
        """ Stop the tracer """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    check_include = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function indicating whether to include a file."""

    concur_id_func = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for determining concurrency context"""

    data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The raw dictionary of trace data."""

    disable_plugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for disabling a plugin."""

    file_tracers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Mapping from file name to plugin name."""

    should_start_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for starting contexts."""

    should_trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function indicating whether to trace a file."""

    should_trace_cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dictionary caching should_trace results."""

    switch_context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for switching to a new context."""

    trace_arcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Should we trace arcs, or just lines?"""

    warn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function for issuing warnings."""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac873340>'

__spec__ = None # (!) real value is "ModuleSpec(name='coverage.tracer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac873340>, origin='/.venv/lib/python3.8/site-packages/coverage/tracer.cpython-38-aarch64-linux-gnu.so')"

