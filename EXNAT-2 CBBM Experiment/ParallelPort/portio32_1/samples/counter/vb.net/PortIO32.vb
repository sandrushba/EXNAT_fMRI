Module PortIO32
    '   This file provides the function declarations, constants, and error
    '   codes for Winford Engineering's PortIO32 driver and library.
    '
    '    Winford Engineering
    '    www.winfordeng.com
    Public Declare Function OutByte Lib "PortIO32.dll" (ByVal Port As Short, ByVal Data As Integer) As Integer
    Public Declare Function OutWord Lib "PortIO32.dll" (ByVal Port As Short, ByVal Data As Integer) As Integer
    Public Declare Function InByte Lib "PortIO32.dll" (ByVal Port As Short, ByRef Data as Integer) As Integer
    Public Declare Function InWord Lib "PortIO32.dll" (ByVal Port As Short, ByRef Data as Integer) As Integer
    Public Declare Function InByteR Lib "PortIO32.dll" (ByVal Port As Short) As Integer
    Public Declare Function InWordR Lib "PortIO32.dll" (ByVal Port As Short) As Integer

End Module
