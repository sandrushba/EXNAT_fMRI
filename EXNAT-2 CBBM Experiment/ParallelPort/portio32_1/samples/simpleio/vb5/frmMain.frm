VERSION 5.00
Begin VB.Form frmMain 
   Caption         =   "Simple I/O  -- PortIO32 Demo"
   ClientHeight    =   2775
   ClientLeft      =   60
   ClientTop       =   345
   ClientWidth     =   3915
   LinkTopic       =   "Form1"
   ScaleHeight     =   2775
   ScaleWidth      =   3915
   StartUpPosition =   3  'Windows Default
   Begin VB.Frame Frame2 
      Caption         =   " Input: "
      Height          =   1215
      Left            =   270
      TabIndex        =   6
      Top             =   1440
      Width           =   3375
      Begin VB.CommandButton btnRead 
         Caption         =   "Read"
         Height          =   375
         Left            =   2280
         TabIndex        =   4
         Top             =   480
         Width           =   975
      End
      Begin VB.TextBox txtInAddress 
         Height          =   300
         Left            =   960
         TabIndex        =   3
         Top             =   360
         Width           =   1095
      End
      Begin VB.Label lblInValue 
         BorderStyle     =   1  'Fixed Single
         Height          =   300
         Left            =   960
         TabIndex        =   11
         Top             =   720
         Width           =   1095
      End
      Begin VB.Label Label4 
         Alignment       =   1  'Right Justify
         Caption         =   "Value:"
         Height          =   255
         Left            =   140
         TabIndex        =   10
         Top             =   765
         Width           =   735
      End
      Begin VB.Label Label3 
         Alignment       =   1  'Right Justify
         Caption         =   "Address:"
         Height          =   255
         Left            =   140
         TabIndex        =   9
         Top             =   405
         Width           =   735
      End
   End
   Begin VB.Frame Frame1 
      Caption         =   " Output: "
      Height          =   1215
      Left            =   270
      TabIndex        =   5
      Top             =   120
      Width           =   3375
      Begin VB.CommandButton btnWrite 
         Caption         =   "Write"
         Height          =   375
         Left            =   2280
         TabIndex        =   2
         Top             =   480
         Width           =   975
      End
      Begin VB.TextBox txtOutValue 
         Height          =   300
         Left            =   960
         TabIndex        =   1
         Top             =   720
         Width           =   1095
      End
      Begin VB.TextBox txtOutAddress 
         Height          =   300
         Left            =   960
         TabIndex        =   0
         Top             =   360
         Width           =   1095
      End
      Begin VB.Label Label2 
         Alignment       =   1  'Right Justify
         Caption         =   "Value:"
         Height          =   255
         Left            =   140
         TabIndex        =   8
         Top             =   765
         Width           =   735
      End
      Begin VB.Label Label1 
         Alignment       =   1  'Right Justify
         Caption         =   "Address:"
         Height          =   255
         Left            =   140
         TabIndex        =   7
         Top             =   400
         Width           =   735
      End
   End
End
Attribute VB_Name = "frmMain"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Private Sub btnRead_Click()
  'Dimension variables
   Dim Address As Integer       'Holds the address of the input port
   Dim Value As Long            'Holds the value read in from the input port

  'Extract input port address from the text box
   Address = Val([txtInAddress])
  
  'Read the input port
   If InByte(Address, Value) Then
      MsgBox "Error reading value with InByte.  Please ensure the PortIO32 driver and library are installed."
   End If
  
  'Display the data from the input port
   lblInValue = Value

End Sub

Private Sub btnWrite_Click()
  'Dimension variables
   Dim Address As Integer       'Holds the address of the output port
   Dim Value As Long            'Holds the value to write to the output port

  'Extract the output port address from the text box
   Address = Val([txtOutAddress])

  'Extract the value to write to the output port
   Value = Val([txtOutValue])

  'Write the value to the output port
   If OutByte(Address, Value) Then
      MsgBox "Error writing value with OutByte.  Please ensure the PortIO32 driver and library are installed."
   End If


End Sub
