# encoding: utf-8
# module _curses_panel
# from /usr/local/lib/python3.8/lib-dynload/_curses_panel.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

version = '2.1'

__version__ = '2.1'

# functions

def bottom_panel(*args, **kwargs): # real signature unknown
    """ Return the bottom panel in the panel stack. """
    pass

def new_panel(*args, **kwargs): # real signature unknown
    """ Return a panel object, associating it with the given window win. """
    pass

def top_panel(*args, **kwargs): # real signature unknown
    """ Return the top panel in the panel stack. """
    pass

def update_panels(*args, **kwargs): # real signature unknown
    """
    Updates the virtual screen after changes in the panel stack.
    
    This does not call curses.doupdate(), so you'll have to do this yourself.
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class panel(object):
    # no doc
    def above(self, *args, **kwargs): # real signature unknown
        """ Return the panel above the current panel. """
        pass

    def below(self, *args, **kwargs): # real signature unknown
        """ Return the panel below the current panel. """
        pass

    def bottom(self, *args, **kwargs): # real signature unknown
        """ Push the panel to the bottom of the stack. """
        pass

    def hidden(self, not_visible): # real signature unknown; restored from __doc__
        """ Return True if the panel is hidden (not visible), False otherwise. """
        pass

    def hide(self, *args, **kwargs): # real signature unknown
        """
        Hide the panel.
        
        This does not delete the object, it just makes the window on screen invisible.
        """
        pass

    def move(self, *args, **kwargs): # real signature unknown
        """ Move the panel to the screen coordinates (y, x). """
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Change the window associated with the panel to the window win. """
        pass

    def set_userptr(self, *args, **kwargs): # real signature unknown
        """ Set the panel's user pointer to obj. """
        pass

    def show(self, *args, **kwargs): # real signature unknown
        """ Display the panel (which might have been hidden). """
        pass

    def top(self, *args, **kwargs): # real signature unknown
        """ Push panel to the top of the stack. """
        pass

    def userptr(self, *args, **kwargs): # real signature unknown
        """ Return the user pointer for the panel. """
        pass

    def window(self, *args, **kwargs): # real signature unknown
        """ Return the window object associated with the panel. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_curses_panel', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_curses_panel.cpython-38-aarch64-linux-gnu.so')"

