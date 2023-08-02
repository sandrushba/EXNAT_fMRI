VERSION 5.00
Begin VB.Form frmMain 
   Caption         =   "Counter"
   ClientHeight    =   3195
   ClientLeft      =   60
   ClientTop       =   345
   ClientWidth     =   4680
   LinkTopic       =   "Form1"
   ScaleHeight     =   3195
   ScaleWidth      =   4680
   StartUpPosition =   3  'Windows Default
   Begin VB.Timer timercheck 
      Left            =   240
      Top             =   1320
   End
   Begin VB.CommandButton cmdStart 
      Caption         =   "Start "
      Height          =   735
      Left            =   960
      TabIndex        =   0
      Top             =   1080
      Width           =   2775
   End
   Begin VB.Label Label1 
      Caption         =   "Hit the 'Start' button to begin counting the pulses on Port 2, bit 0."
      Height          =   495
      Left            =   720
      TabIndex        =   3
      Top             =   480
      Width           =   3375
   End
   Begin VB.Label Label2 
      Alignment       =   1  'Right Justify
      Caption         =   "Count: "
      Height          =   255
      Left            =   1080
      TabIndex        =   2
      Top             =   2160
      Width           =   855
   End
   Begin VB.Label lblCount 
      BackColor       =   &H00E0E0E0&
      Height          =   255
      Left            =   2040
      TabIndex        =   1
      Top             =   2160
      Width           =   1215
   End
End
Attribute VB_Name = "frmMain"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
'   Winford Engineering
'   www.winfordeng.com
'
'   This a sample program for Winford Engineering's WECRD155B I/O Card.
'   This program uses Winford Engineering's PortIO32 Low-level library
'   Hardware setup:
'       This program assumes that you have eight LEDs connected
'       to port 1 (port A) of your I/O card.  It also assumes that you have
'       a bounceless pushbutton (or a low frequency clock source)
'       connected between Bit 0 of port 2 (port B) and ground.
'   Operation:
'       This program keeps a count of how many times the pushbutton
'       has been pressed.  The count begins at 0 and is incremented
'       every time the button is pressed.  To monitor the state of the
'       pushbutton, the program configures Port 2 to be in the input state.
'       The current value is output onto Port 1; if you have LEDs connected
'       you will be able to see the value of the counter in binary form.
'       Notice that since Port 1 is configured for output operation, you
'       should take care that you do not have any circuitry connected
'       to port 1 that could interfere with the port's outputs (See the
'       section in your manual about Data Contention).

Option Explicit
   
'Define form-level variables
Dim BaseAddress As Integer       'holds base address of CRD155B
    

Private Sub cmdStart_Click()
  timercheck.Interval = 1
  timercheck.Enabled = True

End Sub

Private Sub Form_Load()
   'Dimension variables
   Dim msg As String        'holds message to display to user
   Dim result As Long       'holds the error or success codes from calls to functions from PortIO32
   
   'Initialize variables
   BaseAddress = 384        'assume card is at base address 384 decimal
   
   '*********************************************
   'First,we will output a notice and ask for user confirmation.
   'This would not normally be done in an actual application.
   msg = "Note:  This program configures Port 1 as an output port. " & _
         "Please be sure that you do not have interfering hardware " & _
         "connected to Port 1 of your card." & vbCrLf & vbCrLf & _
         "Press Ok to continue or Cancel to exit the program."
   If MsgBox(msg, vbExclamation + vbOKCancel) = vbCancel Then
      'User hit Cancel --> End program
      End
   End If
       
   'Note that in this application, the error codes are checked on
   'most function calls.  In a normal application, it would not be
   'necessary to check for errors on all of the functions, but it
   'is done here to show that it is possible.
   
   '*********************************************
   'Configure the card.  Port A (1) should be an output and
   'Port B (2) and C (3) will be inputs.  The control byte
   'for this configuration is 139 decimal.
   result = OutByte(BaseAddress + 3, 139)
   If result = -1 Then      'error occurred
      'Display error message
      msg = "An error occurred while writing a value to a port."
      MsgBox msg
      'End Program
      End
   End If
   
   
End Sub

Private Sub timercheck_Timer()
    'Dimension variables
    'Static variables retain their value from one execution of this function
    ' to the next.
    Static count As Long      'counter of how many times the button has been pressed
    Static last_level As Boolean  ' Was the clock/switch line high or low last time? (True=high)
    Dim result As Long       'holds the error or success codes from calls to functions from PortIO32
    Dim value As Long        'holds the value read from Port B (Port 2)
    Dim level As Boolean    ' level (true=high, false=low) of just the one bit we're interested in
    
    result = InByte(BaseAddress + 1, value) 'read a value from Port B
    If result = -1 Then    'error occurred
       'Display error message
       MsgBox "An error occurred while reading a value from a port."
       'stop timer from firing
       timercheck.Enabled = False
    End If
    
    ' Look at only bit 0 by And-ing with 1
    level = (value And 1)

    'In this program, we will assume that when the input button is pressed,
    ' it results in Bit 0 going low (0).  When the input line goes low, we
    ' increment the counter
    
    ' We only take action on the falling edge of the signal, that is when the
    ' level of the signal last time was high and the level this time is low.
    If (last_level = True) And (level = False) Then
      ' last time the input was high
      ' If the bit has now gone low, it's time to increment our counter
      count = count + 1      'increment counter
      lblCount.Caption = count        'display current count value on the screen

      'Write current count value to the output port
      result = OutByte(BaseAddress, count)
      'Check for error during output operation
      If result = -1 Then    'Error occurred
        'Display error message
        MsgBox "An error occurred while writing a value"
        'stop timer from firing
        timercheck.Enabled = False
      End If
    End If
    
    ' Regardless of what level the signal was that we just read, we
    ' need to remember it for next time so we can compare to it.
    last_level = level
      
End Sub
