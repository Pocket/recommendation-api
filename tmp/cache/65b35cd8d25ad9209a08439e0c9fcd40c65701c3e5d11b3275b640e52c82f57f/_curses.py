# encoding: utf-8
# module _curses
# from /usr/local/lib/python3.8/lib-dynload/_curses.cpython-38-aarch64-linux-gnu.so
# by generator 1.147
# no doc
# no imports

# Variables with simple values

ALL_MOUSE_EVENTS = 268435455

A_ALTCHARSET = 4194304
A_ATTRIBUTES = 4294967040
A_BLINK = 524288
A_BOLD = 2097152
A_CHARTEXT = 255
A_COLOR = 65280
A_DIM = 1048576
A_HORIZONTAL = 33554432
A_INVIS = 8388608
A_ITALIC = 2147483648
A_LEFT = 67108864
A_LOW = 134217728
A_NORMAL = 0
A_PROTECT = 16777216
A_REVERSE = 262144
A_RIGHT = 268435456
A_STANDOUT = 65536
A_TOP = 536870912
A_UNDERLINE = 131072
A_VERTICAL = 1073741824

BUTTON1_CLICKED = 4

BUTTON1_DOUBLE_CLICKED = 8

BUTTON1_PRESSED = 2
BUTTON1_RELEASED = 1

BUTTON1_TRIPLE_CLICKED = 16

BUTTON2_CLICKED = 128

BUTTON2_DOUBLE_CLICKED = 256

BUTTON2_PRESSED = 64
BUTTON2_RELEASED = 32

BUTTON2_TRIPLE_CLICKED = 512

BUTTON3_CLICKED = 4096

BUTTON3_DOUBLE_CLICKED = 8192

BUTTON3_PRESSED = 2048
BUTTON3_RELEASED = 1024

BUTTON3_TRIPLE_CLICKED = 16384

BUTTON4_CLICKED = 131072

BUTTON4_DOUBLE_CLICKED = 262144

BUTTON4_PRESSED = 65536
BUTTON4_RELEASED = 32768

BUTTON4_TRIPLE_CLICKED = 524288

BUTTON_ALT = 134217728
BUTTON_CTRL = 33554432
BUTTON_SHIFT = 67108864

COLOR_BLACK = 0
COLOR_BLUE = 4
COLOR_CYAN = 6
COLOR_GREEN = 2
COLOR_MAGENTA = 5
COLOR_RED = 1
COLOR_WHITE = 7
COLOR_YELLOW = 3

ERR = -1

KEY_A1 = 348
KEY_A3 = 349
KEY_B2 = 350
KEY_BACKSPACE = 263
KEY_BEG = 354
KEY_BREAK = 257
KEY_BTAB = 353
KEY_C1 = 351
KEY_C3 = 352
KEY_CANCEL = 355
KEY_CATAB = 342
KEY_CLEAR = 333
KEY_CLOSE = 356
KEY_COMMAND = 357
KEY_COPY = 358
KEY_CREATE = 359
KEY_CTAB = 341
KEY_DC = 330
KEY_DL = 328
KEY_DOWN = 258
KEY_EIC = 332
KEY_END = 360
KEY_ENTER = 343
KEY_EOL = 335
KEY_EOS = 334
KEY_EXIT = 361
KEY_F0 = 264
KEY_F1 = 265
KEY_F10 = 274
KEY_F11 = 275
KEY_F12 = 276
KEY_F13 = 277
KEY_F14 = 278
KEY_F15 = 279
KEY_F16 = 280
KEY_F17 = 281
KEY_F18 = 282
KEY_F19 = 283
KEY_F2 = 266
KEY_F20 = 284
KEY_F21 = 285
KEY_F22 = 286
KEY_F23 = 287
KEY_F24 = 288
KEY_F25 = 289
KEY_F26 = 290
KEY_F27 = 291
KEY_F28 = 292
KEY_F29 = 293
KEY_F3 = 267
KEY_F30 = 294
KEY_F31 = 295
KEY_F32 = 296
KEY_F33 = 297
KEY_F34 = 298
KEY_F35 = 299
KEY_F36 = 300
KEY_F37 = 301
KEY_F38 = 302
KEY_F39 = 303
KEY_F4 = 268
KEY_F40 = 304
KEY_F41 = 305
KEY_F42 = 306
KEY_F43 = 307
KEY_F44 = 308
KEY_F45 = 309
KEY_F46 = 310
KEY_F47 = 311
KEY_F48 = 312
KEY_F49 = 313
KEY_F5 = 269
KEY_F50 = 314
KEY_F51 = 315
KEY_F52 = 316
KEY_F53 = 317
KEY_F54 = 318
KEY_F55 = 319
KEY_F56 = 320
KEY_F57 = 321
KEY_F58 = 322
KEY_F59 = 323
KEY_F6 = 270
KEY_F60 = 324
KEY_F61 = 325
KEY_F62 = 326
KEY_F63 = 327
KEY_F7 = 271
KEY_F8 = 272
KEY_F9 = 273
KEY_FIND = 362
KEY_HELP = 363
KEY_HOME = 262
KEY_IC = 331
KEY_IL = 329
KEY_LEFT = 260
KEY_LL = 347
KEY_MARK = 364
KEY_MAX = 511
KEY_MESSAGE = 365
KEY_MIN = 257
KEY_MOUSE = 409
KEY_MOVE = 366
KEY_NEXT = 367
KEY_NPAGE = 338
KEY_OPEN = 368
KEY_OPTIONS = 369
KEY_PPAGE = 339
KEY_PREVIOUS = 370
KEY_PRINT = 346
KEY_REDO = 371
KEY_REFERENCE = 372
KEY_REFRESH = 373
KEY_REPLACE = 374
KEY_RESET = 345
KEY_RESIZE = 410
KEY_RESTART = 375
KEY_RESUME = 376
KEY_RIGHT = 261
KEY_SAVE = 377
KEY_SBEG = 378
KEY_SCANCEL = 379
KEY_SCOMMAND = 380
KEY_SCOPY = 381
KEY_SCREATE = 382
KEY_SDC = 383
KEY_SDL = 384
KEY_SELECT = 385
KEY_SEND = 386
KEY_SEOL = 387
KEY_SEXIT = 388
KEY_SF = 336
KEY_SFIND = 389
KEY_SHELP = 390
KEY_SHOME = 391
KEY_SIC = 392
KEY_SLEFT = 393
KEY_SMESSAGE = 394
KEY_SMOVE = 395
KEY_SNEXT = 396
KEY_SOPTIONS = 397
KEY_SPREVIOUS = 398
KEY_SPRINT = 399
KEY_SR = 337
KEY_SREDO = 400
KEY_SREPLACE = 401
KEY_SRESET = 344
KEY_SRIGHT = 402
KEY_SRSUME = 403
KEY_SSAVE = 404
KEY_SSUSPEND = 405
KEY_STAB = 340
KEY_SUNDO = 406
KEY_SUSPEND = 407
KEY_UNDO = 408
KEY_UP = 259

OK = 0

REPORT_MOUSE_POSITION = 268435456

version = b'2.2'

__version__ = b'2.2'

# functions

def baudrate(*args, **kwargs): # real signature unknown
    """ Return the output speed of the terminal in bits per second. """
    pass

def beep(*args, **kwargs): # real signature unknown
    """ Emit a short attention sound. """
    pass

def can_change_color(*args, **kwargs): # real signature unknown
    """ Return True if the programmer can change the colors displayed by the terminal. """
    pass

def cbreak(): # real signature unknown; restored from __doc__
    """
    Enter cbreak mode.
    
      flag
        If false, the effect is the same as calling nocbreak().
    
    In cbreak mode (sometimes called "rare" mode) normal tty line buffering is
    turned off and characters are available to be read one by one.  However,
    unlike raw mode, special characters (interrupt, quit, suspend, and flow
    control) retain their effects on the tty driver and calling program.
    Calling first raw() then cbreak() leaves the terminal in cbreak mode.
    """
    pass

def color_content(*args, **kwargs): # real signature unknown
    """
    Return the red, green, and blue (RGB) components of the specified color.
    
      color_number
        The number of the color (0 - (COLORS-1)).
    
    A 3-tuple is returned, containing the R, G, B values for the given color,
    which will be between 0 (no component) and 1000 (maximum amount of component).
    """
    pass

def color_pair(*args, **kwargs): # real signature unknown
    """
    Return the attribute value for displaying text in the specified color.
    
      pair_number
        The number of the color pair.
    
    This attribute value can be combined with A_STANDOUT, A_REVERSE, and the
    other A_* attributes.  pair_number() is the counterpart to this function.
    """
    pass

def curs_set(*args, **kwargs): # real signature unknown
    """
    Set the cursor state.
    
      visibility
        0 for invisible, 1 for normal visible, or 2 for very visible.
    
    If the terminal supports the visibility requested, the previous cursor
    state is returned; otherwise, an exception is raised.  On many terminals,
    the "visible" mode is an underline cursor and the "very visible" mode is
    a block cursor.
    """
    pass

def def_prog_mode(*args, **kwargs): # real signature unknown
    """
    Save the current terminal mode as the "program" mode.
    
    The "program" mode is the mode when the running program is using curses.
    
    Subsequent calls to reset_prog_mode() will restore this mode.
    """
    pass

def def_shell_mode(*args, **kwargs): # real signature unknown
    """
    Save the current terminal mode as the "shell" mode.
    
    The "shell" mode is the mode when the running program is not using curses.
    
    Subsequent calls to reset_shell_mode() will restore this mode.
    """
    pass

def delay_output(*args, **kwargs): # real signature unknown
    """
    Insert a pause in output.
    
      ms
        Duration in milliseconds.
    """
    pass

def doupdate(*args, **kwargs): # real signature unknown
    """ Update the physical screen to match the virtual screen. """
    pass

def echo(): # real signature unknown; restored from __doc__
    """
    Enter echo mode.
    
      flag
        If false, the effect is the same as calling noecho().
    
    In echo mode, each character input is echoed to the screen as it is entered.
    """
    pass

def endwin(*args, **kwargs): # real signature unknown
    """ De-initialize the library, and return terminal to normal status. """
    pass

def erasechar(*args, **kwargs): # real signature unknown
    """ Return the user's current erase character. """
    pass

def filter(*args, **kwargs): # real signature unknown
    pass

def flash(*args, **kwargs): # real signature unknown
    """
    Flash the screen.
    
    That is, change it to reverse-video and then change it back in a short interval.
    """
    pass

def flushinp(*args, **kwargs): # real signature unknown
    """
    Flush all input buffers.
    
    This throws away any typeahead that has been typed by the user and has not
    yet been processed by the program.
    """
    pass

def getmouse(*args, **kwargs): # real signature unknown
    """
    Retrieve the queued mouse event.
    
    After getch() returns KEY_MOUSE to signal a mouse event, this function
    returns a 5-tuple (id, x, y, z, bstate).
    """
    pass

def getsyx(*args, **kwargs): # real signature unknown
    """
    Return the current coordinates of the virtual screen cursor.
    
    Return a (y, x) tuple.  If leaveok is currently true, return (-1, -1).
    """
    pass

def getwin(*args, **kwargs): # real signature unknown
    """
    Read window related data stored in the file by an earlier putwin() call.
    
    The routine then creates and initializes a new window using that data,
    returning the new window object.
    """
    pass

def halfdelay(*args, **kwargs): # real signature unknown
    """
    Enter half-delay mode.
    
      tenths
        Maximal blocking delay in tenths of seconds (1 - 255).
    
    Use nocbreak() to leave half-delay mode.
    """
    pass

def has_colors(*args, **kwargs): # real signature unknown
    """ Return True if the terminal can display colors; otherwise, return False. """
    pass

def has_ic(*args, **kwargs): # real signature unknown
    """ Return True if the terminal has insert- and delete-character capabilities. """
    pass

def has_il(*args, **kwargs): # real signature unknown
    """ Return True if the terminal has insert- and delete-line capabilities. """
    pass

def has_key(*args, **kwargs): # real signature unknown
    """
    Return True if the current terminal type recognizes a key with that value.
    
      key
        Key number.
    """
    pass

def initscr(*args, **kwargs): # real signature unknown
    """
    Initialize the library.
    
    Return a WindowObject which represents the whole screen.
    """
    pass

def init_color(): # real signature unknown; restored from __doc__
    """
    Change the definition of a color.
    
      color_number
        The number of the color to be changed (0 - (COLORS-1)).
      r
        Red component (0 - 1000).
      g
        Green component (0 - 1000).
      b
        Blue component (0 - 1000).
    
    When init_color() is used, all occurrences of that color on the screen
    immediately change to the new definition.  This function is a no-op on
    most terminals; it is active only if can_change_color() returns true.
    """
    pass

def init_pair(*args, **kwargs): # real signature unknown
    """
    Change the definition of a color-pair.
    
      pair_number
        The number of the color-pair to be changed (1 - (COLOR_PAIRS-1)).
      fg
        Foreground color number (-1 - (COLORS-1)).
      bg
        Background color number (-1 - (COLORS-1)).
    
    If the color-pair was previously initialized, the screen is refreshed and
    all occurrences of that color-pair are changed to the new definition.
    """
    pass

def intrflush(*args, **kwargs): # real signature unknown
    pass

def isendwin(*args, **kwargs): # real signature unknown
    """ Return True if endwin() has been called. """
    pass

def is_term_resized(*args, **kwargs): # real signature unknown
    """
    Return True if resize_term() would modify the window structure, False otherwise.
    
      nlines
        Height.
      ncols
        Width.
    """
    pass

def keyname(*args, **kwargs): # real signature unknown
    """
    Return the name of specified key.
    
      key
        Key number.
    """
    pass

def killchar(*args, **kwargs): # real signature unknown
    """ Return the user's current line kill character. """
    pass

def longname(*args, **kwargs): # real signature unknown
    """
    Return the terminfo long name field describing the current terminal.
    
    The maximum length of a verbose description is 128 characters.  It is defined
    only after the call to initscr().
    """
    pass

def meta(*args, **kwargs): # real signature unknown
    """
    Enable/disable meta keys.
    
    If yes is True, allow 8-bit characters to be input.  If yes is False,
    allow only 7-bit characters.
    """
    pass

def mouseinterval(*args, **kwargs): # real signature unknown
    """
    Set and retrieve the maximum time between press and release in a click.
    
      interval
        Time in milliseconds.
    
    Set the maximum time that can elapse between press and release events in
    order for them to be recognized as a click, and return the previous interval
    value.
    """
    pass

def mousemask(*args, **kwargs): # real signature unknown
    """
    Set the mouse events to be reported, and return a tuple (availmask, oldmask).
    
    Return a tuple (availmask, oldmask).  availmask indicates which of the
    specified mouse events can be reported; on complete failure it returns 0.
    oldmask is the previous value of the given window's mouse event mask.
    If this function is never called, no mouse events are ever reported.
    """
    pass

def napms(*args, **kwargs): # real signature unknown
    """
    Sleep for specified time.
    
      ms
        Duration in milliseconds.
    """
    pass

def newpad(*args, **kwargs): # real signature unknown
    """
    Create and return a pointer to a new pad data structure.
    
      nlines
        Height.
      ncols
        Width.
    """
    pass

def newwin(nlines, ncols, begin_y=0, begin_x=0): # real signature unknown; restored from __doc__
    """
    newwin(nlines, ncols, [begin_y=0, begin_x=0])
    Return a new window.
    
      nlines
        Height.
      ncols
        Width.
      begin_y
        Top side y-coordinate.
      begin_x
        Left side x-coordinate.
    
    By default, the window will extend from the specified position to the lower
    right corner of the screen.
    """
    pass

def nl(): # real signature unknown; restored from __doc__
    """
    Enter newline mode.
    
      flag
        If false, the effect is the same as calling nonl().
    
    This mode translates the return key into newline on input, and translates
    newline into return and line-feed on output.  Newline mode is initially on.
    """
    pass

def nocbreak(*args, **kwargs): # real signature unknown
    """
    Leave cbreak mode.
    
    Return to normal "cooked" mode with line buffering.
    """
    pass

def noecho(*args, **kwargs): # real signature unknown
    """
    Leave echo mode.
    
    Echoing of input characters is turned off.
    """
    pass

def nonl(*args, **kwargs): # real signature unknown
    """
    Leave newline mode.
    
    Disable translation of return into newline on input, and disable low-level
    translation of newline into newline/return on output.
    """
    pass

def noqiflush(*args, **kwargs): # real signature unknown
    """
    Disable queue flushing.
    
    When queue flushing is disabled, normal flush of input and output queues
    associated with the INTR, QUIT and SUSP characters will not be done.
    """
    pass

def noraw(*args, **kwargs): # real signature unknown
    """
    Leave raw mode.
    
    Return to normal "cooked" mode with line buffering.
    """
    pass

def pair_content(*args, **kwargs): # real signature unknown
    """
    Return a tuple (fg, bg) containing the colors for the requested color pair.
    
      pair_number
        The number of the color pair (1 - (COLOR_PAIRS-1)).
    """
    pass

def pair_number(*args, **kwargs): # real signature unknown
    """
    Return the number of the color-pair set by the specified attribute value.
    
    color_pair() is the counterpart to this function.
    """
    pass

def putp(): # real signature unknown; restored from __doc__
    """
    Emit the value of a specified terminfo capability for the current terminal.
    
    Note that the output of putp() always goes to standard output.
    """
    pass

def qiflush(): # real signature unknown; restored from __doc__
    """
    Enable queue flushing.
    
      flag
        If false, the effect is the same as calling noqiflush().
    
    If queue flushing is enabled, all output in the display driver queue
    will be flushed when the INTR, QUIT and SUSP characters are read.
    """
    pass

def raw(): # real signature unknown; restored from __doc__
    """
    Enter raw mode.
    
      flag
        If false, the effect is the same as calling noraw().
    
    In raw mode, normal line buffering and processing of interrupt, quit,
    suspend, and flow control keys are turned off; characters are presented to
    curses input functions one by one.
    """
    pass

def resetty(*args, **kwargs): # real signature unknown
    """ Restore terminal mode. """
    pass

def reset_prog_mode(*args, **kwargs): # real signature unknown
    """ Restore the terminal to "program" mode, as previously saved by def_prog_mode(). """
    pass

def reset_shell_mode(*args, **kwargs): # real signature unknown
    """ Restore the terminal to "shell" mode, as previously saved by def_shell_mode(). """
    pass

def resizeterm(*args, **kwargs): # real signature unknown
    """
    Resize the standard and current windows to the specified dimensions.
    
      nlines
        Height.
      ncols
        Width.
    
    Adjusts other bookkeeping data used by the curses library that record the
    window dimensions (in particular the SIGWINCH handler).
    """
    pass

def resize_term(): # real signature unknown; restored from __doc__
    """
    Backend function used by resizeterm(), performing most of the work.
    
      nlines
        Height.
      ncols
        Width.
    
    When resizing the windows, resize_term() blank-fills the areas that are
    extended.  The calling application should fill in these areas with appropriate
    data.  The resize_term() function attempts to resize all windows.  However,
    due to the calling convention of pads, it is not possible to resize these
    without additional interaction with the application.
    """
    pass

def savetty(*args, **kwargs): # real signature unknown
    """ Save terminal mode. """
    pass

def setsyx(*args, **kwargs): # real signature unknown
    """
    Set the virtual screen cursor.
    
      y
        Y-coordinate.
      x
        X-coordinate.
    
    If y and x are both -1, then leaveok is set.
    """
    pass

def setupterm(*args, **kwargs): # real signature unknown
    """
    Initialize the terminal.
    
      term
        Terminal name.
        If omitted, the value of the TERM environment variable will be used.
      fd
        File descriptor to which any initialization sequences will be sent.
        If not supplied, the file descriptor for sys.stdout will be used.
    """
    pass

def start_color(*args, **kwargs): # real signature unknown
    """
    Initializes eight basic colors and global variables COLORS and COLOR_PAIRS.
    
    Must be called if the programmer wants to use colors, and before any other
    color manipulation routine is called.  It is good practice to call this
    routine right after initscr().
    
    It also restores the colors on the terminal to the values they had when the
    terminal was just turned on.
    """
    pass

def termattrs(*args, **kwargs): # real signature unknown
    """ Return a logical OR of all video attributes supported by the terminal. """
    pass

def termname(*args, **kwargs): # real signature unknown
    """ Return the value of the environment variable TERM, truncated to 14 characters. """
    pass

def tigetflag(*args, **kwargs): # real signature unknown
    """
    Return the value of the Boolean capability.
    
      capname
        The terminfo capability name.
    
    The value -1 is returned if capname is not a Boolean capability, or 0 if
    it is canceled or absent from the terminal description.
    """
    pass

def tigetnum(*args, **kwargs): # real signature unknown
    """
    Return the value of the numeric capability.
    
      capname
        The terminfo capability name.
    
    The value -2 is returned if capname is not a numeric capability, or -1 if
    it is canceled or absent from the terminal description.
    """
    pass

def tigetstr(*args, **kwargs): # real signature unknown
    """
    Return the value of the string capability.
    
      capname
        The terminfo capability name.
    
    None is returned if capname is not a string capability, or is canceled or
    absent from the terminal description.
    """
    pass

def tparm(*args, **kwargs): # real signature unknown
    """
    Instantiate the specified byte string with the supplied parameters.
    
      str
        Parameterized byte string obtained from the terminfo database.
    """
    pass

def typeahead(*args, **kwargs): # real signature unknown
    """
    Specify that the file descriptor fd be used for typeahead checking.
    
      fd
        File descriptor.
    
    If fd is -1, then no typeahead checking is done.
    """
    pass

def unctrl(*args, **kwargs): # real signature unknown
    """
    Return a string which is a printable representation of the character ch.
    
    Control characters are displayed as a caret followed by the character,
    for example as ^C.  Printing characters are left as they are.
    """
    pass

def ungetch(*args, **kwargs): # real signature unknown
    """ Push ch so the next getch() will return it. """
    pass

def ungetmouse(*args, **kwargs): # real signature unknown
    """
    Push a KEY_MOUSE event onto the input queue.
    
    The following getmouse() will return the given state data.
    """
    pass

def unget_wch(*args, **kwargs): # real signature unknown
    """ Push ch so the next get_wch() will return it. """
    pass

def update_lines_cols(*args, **kwargs): # real signature unknown
    pass

def use_default_colors(*args, **kwargs): # real signature unknown
    """
    Allow use of default values for colors on terminals supporting this feature.
    
    Use this to support transparency in your application.  The default color
    is assigned to the color number -1.
    """
    pass

def use_env(*args, **kwargs): # real signature unknown
    """
    Use environment variables LINES and COLUMNS.
    
    If used, this function should be called before initscr() or newterm() are
    called.
    
    When flag is False, the values of lines and columns specified in the terminfo
    database will be used, even if environment variables LINES and COLUMNS (used
    by default) are set, or if curses is running in a window (in which case
    default behavior would be to use the window size if LINES and COLUMNS are
    not set).
    """
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class window(object):
    # no doc
    def addch(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addch([y, x,] ch, [attr=_curses.A_NORMAL])
        Paint the character.
        
          y
            Y-coordinate.
          x
            X-coordinate.
          ch
            Character to add.
          attr
            Attributes for the character.
        
        Paint character ch at (y, x) with attributes attr,
        overwriting any character previously painted at that location.
        By default, the character position and attributes are the
        current settings for the window object.
        """
        pass

    def addnstr(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addnstr([y, x,] str, n, [attr])
        Paint at most n characters of the string.
        
          y
            Y-coordinate.
          x
            X-coordinate.
          str
            String to add.
          n
            Maximal number of characters.
          attr
            Attributes for characters.
        
        Paint at most n characters of the string str at (y, x) with
        attributes attr, overwriting anything previously on the display.
        By default, the character position and attributes are the
        current settings for the window object.
        """
        pass

    def addstr(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        addstr([y, x,] str, [attr])
        Paint the string.
        
          y
            Y-coordinate.
          x
            X-coordinate.
          str
            String to add.
          attr
            Attributes for characters.
        
        Paint the string str at (y, x) with attributes attr,
        overwriting anything previously on the display.
        By default, the character position and attributes are the
        current settings for the window object.
        """
        pass

    def attroff(self, *args, **kwargs): # real signature unknown
        """ Remove attribute attr from the "background" set. """
        pass

    def attron(self, *args, **kwargs): # real signature unknown
        """ Add attribute attr from the "background" set. """
        pass

    def attrset(self, *args, **kwargs): # real signature unknown
        """ Set the "background" set of attributes. """
        pass

    def bkgd(self, *args, **kwargs): # real signature unknown
        """
        Set the background property of the window.
        
          ch
            Background character.
          attr
            Background attributes.
        """
        pass

    def bkgdset(self, *args, **kwargs): # real signature unknown
        """
        Set the window's background.
        
          ch
            Background character.
          attr
            Background attributes.
        """
        pass

    def border(self, *args, **kwargs): # real signature unknown
        """
        Draw a border around the edges of the window.
        
          ls
            Left side.
          rs
            Right side.
          ts
            Top side.
          bs
            Bottom side.
          tl
            Upper-left corner.
          tr
            Upper-right corner.
          bl
            Bottom-left corner.
          br
            Bottom-right corner.
        
        Each parameter specifies the character to use for a specific part of the
        border.  The characters can be specified as integers or as one-character
        strings.  A 0 value for any parameter will cause the default character to be
        used for that parameter.
        """
        pass

    def box(self, verch=0, horch=0): # real signature unknown; restored from __doc__
        """
        box([verch=0, horch=0])
        Draw a border around the edges of the window.
        
          verch
            Left and right side.
          horch
            Top and bottom side.
        
        Similar to border(), but both ls and rs are verch and both ts and bs are
        horch.  The default corner characters are always used by this function.
        """
        pass

    def chgat(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def clearok(self, *args, **kwargs): # real signature unknown
        pass

    def clrtobot(self, *args, **kwargs): # real signature unknown
        pass

    def clrtoeol(self, *args, **kwargs): # real signature unknown
        pass

    def cursyncup(self, *args, **kwargs): # real signature unknown
        pass

    def delch(self, y=None, x=None): # real signature unknown; restored from __doc__
        """
        delch([y, x])
        Delete any character at (y, x).
        
          y
            Y-coordinate.
          x
            X-coordinate.
        """
        pass

    def deleteln(self, *args, **kwargs): # real signature unknown
        pass

    def derwin(self, nlines=0, ncols=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        derwin([nlines=0, ncols=0,] begin_y, begin_x)
        Create a sub-window (window-relative coordinates).
        
          nlines
            Height.
          ncols
            Width.
          begin_y
            Top side y-coordinate.
          begin_x
            Left side x-coordinate.
        
        derwin() is the same as calling subwin(), except that begin_y and begin_x
        are relative to the origin of the window, rather than relative to the entire
        screen.
        """
        pass

    def echochar(self, *args, **kwargs): # real signature unknown
        """
        Add character ch with attribute attr, and refresh.
        
          ch
            Character to add.
          attr
            Attributes for the character.
        """
        pass

    def enclose(self, *args, **kwargs): # real signature unknown
        """
        Return True if the screen-relative coordinates are enclosed by the window.
        
          y
            Y-coordinate.
          x
            X-coordinate.
        """
        pass

    def erase(self, *args, **kwargs): # real signature unknown
        pass

    def getbegyx(self, *args, **kwargs): # real signature unknown
        pass

    def getbkgd(self, *args, **kwargs): # real signature unknown
        """ Return the window's current background character/attribute pair. """
        pass

    def getch(self, y=None, x=None): # real signature unknown; restored from __doc__
        """
        getch([y, x])
        Get a character code from terminal keyboard.
        
          y
            Y-coordinate.
          x
            X-coordinate.
        
        The integer returned does not have to be in ASCII range: function keys,
        keypad keys and so on return numbers higher than 256.  In no-delay mode, -1
        is returned if there is no input, else getch() waits until a key is pressed.
        """
        pass

    def getkey(self, y=None, x=None): # real signature unknown; restored from __doc__
        """
        getkey([y, x])
        Get a character (string) from terminal keyboard.
        
          y
            Y-coordinate.
          x
            X-coordinate.
        
        Returning a string instead of an integer, as getch() does.  Function keys,
        keypad keys and other special keys return a multibyte string containing the
        key name.  In no-delay mode, an exception is raised if there is no input.
        """
        pass

    def getmaxyx(self, *args, **kwargs): # real signature unknown
        pass

    def getparyx(self, *args, **kwargs): # real signature unknown
        pass

    def getstr(self, *args, **kwargs): # real signature unknown
        pass

    def getyx(self, *args, **kwargs): # real signature unknown
        pass

    def get_wch(self, y=None, x=None): # real signature unknown; restored from __doc__
        """
        get_wch([y, x])
        Get a wide character from terminal keyboard.
        
          y
            Y-coordinate.
          x
            X-coordinate.
        
        Return a character for most keys, or an integer for function keys,
        keypad keys, and other special keys.
        """
        pass

    def hline(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        hline([y, x,] ch, n, [attr=_curses.A_NORMAL])
        Display a horizontal line.
        
          y
            Starting Y-coordinate.
          x
            Starting X-coordinate.
          ch
            Character to draw.
          n
            Line length.
          attr
            Attributes for the characters.
        """
        pass

    def idcok(self, *args, **kwargs): # real signature unknown
        pass

    def idlok(self, *args, **kwargs): # real signature unknown
        pass

    def immedok(self, *args, **kwargs): # real signature unknown
        pass

    def inch(self, y=None, x=None): # real signature unknown; restored from __doc__
        """
        inch([y, x])
        Return the character at the given position in the window.
        
          y
            Y-coordinate.
          x
            X-coordinate.
        
        The bottom 8 bits are the character proper, and upper bits are the attributes.
        """
        pass

    def insch(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        insch([y, x,] ch, [attr=_curses.A_NORMAL])
        Insert a character before the current or specified position.
        
          y
            Y-coordinate.
          x
            X-coordinate.
          ch
            Character to insert.
          attr
            Attributes for the character.
        
        All characters to the right of the cursor are shifted one position right, with
        the rightmost characters on the line being lost.
        """
        pass

    def insdelln(self, *args, **kwargs): # real signature unknown
        pass

    def insertln(self, *args, **kwargs): # real signature unknown
        pass

    def insnstr(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        insnstr([y, x,] str, n, [attr])
        Insert at most n characters of the string.
        
          y
            Y-coordinate.
          x
            X-coordinate.
          str
            String to insert.
          n
            Maximal number of characters.
          attr
            Attributes for characters.
        
        Insert a character string (as many characters as will fit on the line)
        before the character under the cursor, up to n characters.  If n is zero
        or negative, the entire string is inserted.  All characters to the right
        of the cursor are shifted right, with the rightmost characters on the line
        being lost.  The cursor position does not change (after moving to y, x, if
        specified).
        """
        pass

    def insstr(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        insstr([y, x,] str, [attr])
        Insert the string before the current or specified position.
        
          y
            Y-coordinate.
          x
            X-coordinate.
          str
            String to insert.
          attr
            Attributes for characters.
        
        Insert a character string (as many characters as will fit on the line)
        before the character under the cursor.  All characters to the right of
        the cursor are shifted right, with the rightmost characters on the line
        being lost.  The cursor position does not change (after moving to y, x,
        if specified).
        """
        pass

    def instr(self, *args, **kwargs): # real signature unknown
        pass

    def is_linetouched(self, *args, **kwargs): # real signature unknown
        """
        Return True if the specified line was modified, otherwise return False.
        
          line
            Line number.
        
        Raise a curses.error exception if line is not valid for the given window.
        """
        pass

    def is_wintouched(self, *args, **kwargs): # real signature unknown
        pass

    def keypad(self, *args, **kwargs): # real signature unknown
        pass

    def leaveok(self, *args, **kwargs): # real signature unknown
        pass

    def move(self, *args, **kwargs): # real signature unknown
        pass

    def mvderwin(self, *args, **kwargs): # real signature unknown
        pass

    def mvwin(self, *args, **kwargs): # real signature unknown
        pass

    def nodelay(self, *args, **kwargs): # real signature unknown
        pass

    def notimeout(self, *args, **kwargs): # real signature unknown
        pass

    def noutrefresh(self, pminrow=None, pmincol=None, sminrow=None, smincol=None, smaxrow=None, smaxcol=None): # real signature unknown; restored from __doc__
        """
        noutrefresh([pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol])
        Mark for refresh but wait.
        
        This function updates the data structure representing the desired state of the
        window, but does not force an update of the physical screen.  To accomplish
        that, call doupdate().
        """
        pass

    def overlay(self, destwin, sminrow=None, smincol=None, dminrow=None, dmincol=None, dmaxrow=None, dmaxcol=None): # real signature unknown; restored from __doc__
        """
        overlay(destwin, [sminrow, smincol, dminrow, dmincol, dmaxrow, dmaxcol])
        Overlay the window on top of destwin.
        
        The windows need not be the same size, only the overlapping region is copied.
        This copy is non-destructive, which means that the current background
        character does not overwrite the old contents of destwin.
        
        To get fine-grained control over the copied region, the second form of
        overlay() can be used.  sminrow and smincol are the upper-left coordinates
        of the source window, and the other variables mark a rectangle in the
        destination window.
        """
        pass

    def overwrite(self, destwin, sminrow=None, smincol=None, dminrow=None, dmincol=None, dmaxrow=None, dmaxcol=None): # real signature unknown; restored from __doc__
        """
        overwrite(destwin, [sminrow, smincol, dminrow, dmincol, dmaxrow,
                  dmaxcol])
        Overwrite the window on top of destwin.
        
        The windows need not be the same size, in which case only the overlapping
        region is copied.  This copy is destructive, which means that the current
        background character overwrites the old contents of destwin.
        
        To get fine-grained control over the copied region, the second form of
        overwrite() can be used. sminrow and smincol are the upper-left coordinates
        of the source window, the other variables mark a rectangle in the destination
        window.
        """
        pass

    def putwin(self, *args, **kwargs): # real signature unknown
        """
        Write all data associated with the window into the provided file object.
        
        This information can be later retrieved using the getwin() function.
        """
        pass

    def redrawln(self, *args, **kwargs): # real signature unknown
        """
        Mark the specified lines corrupted.
        
          beg
            Starting line number.
          num
            The number of lines.
        
        They should be completely redrawn on the next refresh() call.
        """
        pass

    def redrawwin(self, *args, **kwargs): # real signature unknown
        pass

    def refresh(self, pminrow=None, pmincol=None, sminrow=None, smincol=None, smaxrow=None, smaxcol=None): # real signature unknown; restored from __doc__
        """
        refresh([pminrow, pmincol, sminrow, smincol, smaxrow, smaxcol])
        Update the display immediately.
        
        Synchronize actual screen with previous drawing/deleting methods.
        The 6 optional arguments can only be specified when the window is a pad
        created with newpad().  The additional parameters are needed to indicate
        what part of the pad and screen are involved.  pminrow and pmincol specify
        the upper left-hand corner of the rectangle to be displayed in the pad.
        sminrow, smincol, smaxrow, and smaxcol specify the edges of the rectangle to
        be displayed on the screen.  The lower right-hand corner of the rectangle to
        be displayed in the pad is calculated from the screen coordinates, since the
        rectangles must be the same size.  Both rectangles must be entirely contained
        within their respective structures.  Negative values of pminrow, pmincol,
        sminrow, or smincol are treated as if they were zero.
        """
        pass

    def resize(self, *args, **kwargs): # real signature unknown
        pass

    def scroll(self, lines=1): # real signature unknown; restored from __doc__
        """
        scroll([lines=1])
        Scroll the screen or scrolling region.
        
          lines
            Number of lines to scroll.
        
        Scroll upward if the argument is positive and downward if it is negative.
        """
        pass

    def scrollok(self, *args, **kwargs): # real signature unknown
        pass

    def setscrreg(self, *args, **kwargs): # real signature unknown
        """
        Define a software scrolling region.
        
          top
            First line number.
          bottom
            Last line number.
        
        All scrolling actions will take place in this region.
        """
        pass

    def standend(self, *args, **kwargs): # real signature unknown
        pass

    def standout(self, *args, **kwargs): # real signature unknown
        pass

    def subpad(self, *args, **kwargs): # real signature unknown
        """
        subwin([nlines=0, ncols=0,] begin_y, begin_x)
        Create a sub-window (screen-relative coordinates).
        
          nlines
            Height.
          ncols
            Width.
          begin_y
            Top side y-coordinate.
          begin_x
            Left side x-coordinate.
        
        By default, the sub-window will extend from the specified position to the
        lower right corner of the window.
        """
        pass

    def subwin(self, nlines=0, ncols=0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        subwin([nlines=0, ncols=0,] begin_y, begin_x)
        Create a sub-window (screen-relative coordinates).
        
          nlines
            Height.
          ncols
            Width.
          begin_y
            Top side y-coordinate.
          begin_x
            Left side x-coordinate.
        
        By default, the sub-window will extend from the specified position to the
        lower right corner of the window.
        """
        pass

    def syncdown(self, *args, **kwargs): # real signature unknown
        pass

    def syncok(self, *args, **kwargs): # real signature unknown
        pass

    def syncup(self, *args, **kwargs): # real signature unknown
        pass

    def timeout(self, *args, **kwargs): # real signature unknown
        pass

    def touchline(self, start, count, changed=True): # real signature unknown; restored from __doc__
        """
        touchline(start, count, [changed=True])
        Pretend count lines have been changed, starting with line start.
        
        If changed is supplied, it specifies whether the affected lines are marked
        as having been changed (changed=True) or unchanged (changed=False).
        """
        pass

    def touchwin(self, *args, **kwargs): # real signature unknown
        pass

    def untouchwin(self, *args, **kwargs): # real signature unknown
        pass

    def vline(self, y=None, x=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        vline([y, x,] ch, n, [attr=_curses.A_NORMAL])
        Display a vertical line.
        
          y
            Starting Y-coordinate.
          x
            Starting X-coordinate.
          ch
            Character to draw.
          n
            Line length.
          attr
            Attributes for the character.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the typecode character used to create the array"""



# variables with complex values

ncurses_version = (
    6,
    4,
    20221231,
)

_C_API = None # (!) real value is '<capsule object "_curses._C_API" at 0xffffac924c60>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>'

__spec__ = None # (!) real value is "ModuleSpec(name='_curses', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0xffffac924ac0>, origin='/usr/local/lib/python3.8/lib-dynload/_curses.cpython-38-aarch64-linux-gnu.so')"

