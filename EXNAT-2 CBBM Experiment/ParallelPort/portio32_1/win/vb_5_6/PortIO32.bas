Attribute VB_Name = "PortIO32"
'************** PortIO32.dll Function declarations *******************************
'************** Winford Engineering                *******************************
'DLL Functions are declared in a module, then they are accessible
'throughout the entire Visual Basic Project.
Public Declare Function OutByte Lib "PortIO32.dll" (ByVal Port As Integer, ByVal Data As Long) As Long
Public Declare Function OutWord Lib "PortIO32.dll" (ByVal Port As Integer, ByVal Data As Long) As Long
Public Declare Function InByte Lib "PortIO32.dll" (ByVal Port As Integer, Data as Long) As Long
Public Declare Function InWord Lib "PortIO32.dll" (ByVal Port As Integer, Data as Long) As Long
Public Declare Function InByteR Lib "PortIO32.dll" (ByVal Port As Integer) As Long
Public Declare Function InWordR Lib "PortIO32.dll" (ByVal Port As Integer) As Long

'*********************************************************************************
