import ctypes


class POINT(ctypes.Structure):
    """A nice wrapper of the POINT structure.

    "The POINT structure defines the x- and y- coordinates of a point."

    The POINT structure is used by GetCursorPos(), WindowFromPhysicalPoint(),
    and other functions.

    Syntax:

    typedef struct tagPOINT {
      LONG x;
      LONG y;
    } POINT, *PPOINT;

    Microsoft Documentation:
    http://msdn.microsoft.com/en-us/library/windows/desktop/dd162805(v=vs.85).aspx
    """
    _fields_ = [('x', ctypes.c_long),
                ('y', ctypes.c_long)]

class RECT(ctypes.Structure):
    """A nice wrapper of the RECT structure.

    Syntax:
    typedef struct _RECT {
      LONG left;
      LONG top;
      LONG right;
      LONG bottom;
    } RECT, *PRECT;

    Microsoft Documentation:
    https://msdn.microsoft.com/en-us/library/windows/desktop/dd162897(v=vs.85).aspx
    """
    _fields_ = [('left', ctypes.c_long),
                ('top', ctypes.c_long),
                ('right', ctypes.c_long),
                ('bottom', ctypes.c_long)]


class WINDOWPLACEMENT(ctypes.Structure):
    """A nice wrapper of the WINDOWPLACEMENT structure.

    Syntax:
    typedef struct tagWINDOWPLACEMENT {
      UINT  length;
      UINT  flags;
      UINT  showCmd;
      POINT ptMinPosition;
      POINT ptMaxPosition;
      RECT  rcNormalPosition;
      RECT  rcDevice;
    } WINDOWPLACEMENT;

    Microsoft Documentation:
    https://docs.microsoft.com/en-us/windows/desktop/api/winuser/ns-winuser-tagwindowplacement
    """
    _fields_ = [('length', ctypes.c_uint),
                ('flags', ctypes.c_uint),
                ('showCmd', ctypes.c_uint),
                ('ptMinPosition', POINT),
                ('ptMaxPosition', POINT),
                ('rcNormalPosition', RECT),
                ('rcDevice', RECT)]


class WCRANGE(ctypes.Structure):
  """A nice wrapper of the WCRANGE structure.

  Syntax:
  typedef struct tagWCRANGE {
    WCHAR  wcLow;
    USHORT cGlyphs;
  } WCRANGE, *PWCRANGE, *LPWCRANGE;

  WCHAR docs:
  https://docs.microsoft.com/en-us/windows/desktop/extensible-storage-engine/wchar

  Microsoft Documentation:
  https://docs.microsoft.com/en-us/windows/desktop/api/wingdi/ns-wingdi-tagwcrange
  """
  _fields_ = [('wcLow', ctypes.c_ushort), # TODO - WCHAR has different definitions depending on the system. Is it okay to just use ushort for it?
              ('cGlyphs', ctypes.c_ushort),]


class GLYPHSET(ctypes.Structure):
  """A nice wrapper of the GLYPHSET structure.

  Syntax:
  typedef struct tagGLYPHSET {
    DWORD   cbThis;
    DWORD   flAccel;
    DWORD   cGlyphsSupported;
    DWORD   cRanges;
    WCRANGE ranges[1];
  } GLYPHSET, *PGLYPHSET, *LPGLYPHSET;

  Microsoft Documentation:
  https://docs.microsoft.com/en-us/windows/desktop/api/wingdi/ns-wingdi-tagglyphset
  """
  _fields_ = [('cbThis', ctypes.c_long),
              ('flAccel', ctypes.c_long),
              ('cGlyphsSupproted', ctypes.c_long),
              ('cRanges', ctypes.c_long),
              ('ranges', WCRANGE)] # TODO - not sure how to handle ranges[1] param. Is this a pointer?