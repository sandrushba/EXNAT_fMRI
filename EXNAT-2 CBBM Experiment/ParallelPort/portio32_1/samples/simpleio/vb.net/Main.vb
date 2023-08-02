Public Class Main
    Inherits System.Windows.Forms.Form

#Region " Windows Form Designer generated code "

    Public Sub New()
        MyBase.New()

        'This call is required by the Windows Form Designer.
        InitializeComponent()

        'Add any initialization after the InitializeComponent() call

    End Sub

    'Form overrides dispose to clean up the component list.
    Protected Overloads Overrides Sub Dispose(ByVal disposing As Boolean)
        If disposing Then
            If Not (components Is Nothing) Then
                components.Dispose()
            End If
        End If
        MyBase.Dispose(disposing)
    End Sub

    'Required by the Windows Form Designer
    Private components As System.ComponentModel.IContainer

    'NOTE: The following procedure is required by the Windows Form Designer
    'It can be modified using the Windows Form Designer.  
    'Do not modify it using the code editor.
    Public WithEvents Frame2 As System.Windows.Forms.GroupBox
    Public WithEvents btnRead As System.Windows.Forms.Button
    Public WithEvents txtInAddress As System.Windows.Forms.TextBox
    Public WithEvents lblInValue As System.Windows.Forms.Label
    Public WithEvents Label4 As System.Windows.Forms.Label
    Public WithEvents Label3 As System.Windows.Forms.Label
    Public WithEvents Frame1 As System.Windows.Forms.GroupBox
    Public WithEvents btnWrite As System.Windows.Forms.Button
    Public WithEvents txtOutValue As System.Windows.Forms.TextBox
    Public WithEvents txtOutAddress As System.Windows.Forms.TextBox
    Public WithEvents Label2 As System.Windows.Forms.Label
    Public WithEvents Label1 As System.Windows.Forms.Label
    <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
        Me.Frame2 = New System.Windows.Forms.GroupBox()
        Me.btnRead = New System.Windows.Forms.Button()
        Me.txtInAddress = New System.Windows.Forms.TextBox()
        Me.lblInValue = New System.Windows.Forms.Label()
        Me.Label4 = New System.Windows.Forms.Label()
        Me.Label3 = New System.Windows.Forms.Label()
        Me.Frame1 = New System.Windows.Forms.GroupBox()
        Me.btnWrite = New System.Windows.Forms.Button()
        Me.txtOutValue = New System.Windows.Forms.TextBox()
        Me.txtOutAddress = New System.Windows.Forms.TextBox()
        Me.Label2 = New System.Windows.Forms.Label()
        Me.Label1 = New System.Windows.Forms.Label()
        Me.Frame2.SuspendLayout()
        Me.Frame1.SuspendLayout()
        Me.SuspendLayout()
        '
        'Frame2
        '
        Me.Frame2.BackColor = System.Drawing.SystemColors.Control
        Me.Frame2.Controls.AddRange(New System.Windows.Forms.Control() {Me.btnRead, Me.txtInAddress, Me.lblInValue, Me.Label4, Me.Label3})
        Me.Frame2.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Frame2.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Frame2.Location = New System.Drawing.Point(16, 96)
        Me.Frame2.Name = "Frame2"
        Me.Frame2.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Frame2.Size = New System.Drawing.Size(225, 81)
        Me.Frame2.TabIndex = 8
        Me.Frame2.TabStop = False
        Me.Frame2.Text = " Input: "
        '
        'btnRead
        '
        Me.btnRead.BackColor = System.Drawing.SystemColors.Control
        Me.btnRead.Cursor = System.Windows.Forms.Cursors.Default
        Me.btnRead.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.btnRead.ForeColor = System.Drawing.SystemColors.ControlText
        Me.btnRead.Location = New System.Drawing.Point(152, 32)
        Me.btnRead.Name = "btnRead"
        Me.btnRead.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.btnRead.Size = New System.Drawing.Size(65, 25)
        Me.btnRead.TabIndex = 4
        Me.btnRead.Text = "Read"
        '
        'txtInAddress
        '
        Me.txtInAddress.AcceptsReturn = True
        Me.txtInAddress.AutoSize = False
        Me.txtInAddress.BackColor = System.Drawing.SystemColors.Window
        Me.txtInAddress.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.txtInAddress.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.txtInAddress.ForeColor = System.Drawing.SystemColors.WindowText
        Me.txtInAddress.Location = New System.Drawing.Point(64, 24)
        Me.txtInAddress.MaxLength = 0
        Me.txtInAddress.Name = "txtInAddress"
        Me.txtInAddress.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.txtInAddress.Size = New System.Drawing.Size(73, 20)
        Me.txtInAddress.TabIndex = 3
        Me.txtInAddress.Text = ""
        '
        'lblInValue
        '
        Me.lblInValue.BackColor = System.Drawing.SystemColors.Control
        Me.lblInValue.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
        Me.lblInValue.Cursor = System.Windows.Forms.Cursors.Default
        Me.lblInValue.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.lblInValue.ForeColor = System.Drawing.SystemColors.ControlText
        Me.lblInValue.Location = New System.Drawing.Point(64, 48)
        Me.lblInValue.Name = "lblInValue"
        Me.lblInValue.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.lblInValue.Size = New System.Drawing.Size(73, 20)
        Me.lblInValue.TabIndex = 11
        '
        'Label4
        '
        Me.Label4.BackColor = System.Drawing.SystemColors.Control
        Me.Label4.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label4.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label4.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label4.Location = New System.Drawing.Point(10, 51)
        Me.Label4.Name = "Label4"
        Me.Label4.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label4.Size = New System.Drawing.Size(49, 17)
        Me.Label4.TabIndex = 10
        Me.Label4.Text = "Value:"
        Me.Label4.TextAlign = System.Drawing.ContentAlignment.TopRight
        '
        'Label3
        '
        Me.Label3.BackColor = System.Drawing.SystemColors.Control
        Me.Label3.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label3.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label3.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label3.Location = New System.Drawing.Point(10, 27)
        Me.Label3.Name = "Label3"
        Me.Label3.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label3.Size = New System.Drawing.Size(49, 17)
        Me.Label3.TabIndex = 9
        Me.Label3.Text = "Address:"
        Me.Label3.TextAlign = System.Drawing.ContentAlignment.TopRight
        '
        'Frame1
        '
        Me.Frame1.BackColor = System.Drawing.SystemColors.Control
        Me.Frame1.Controls.AddRange(New System.Windows.Forms.Control() {Me.btnWrite, Me.txtOutValue, Me.txtOutAddress, Me.Label2, Me.Label1})
        Me.Frame1.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Frame1.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Frame1.Location = New System.Drawing.Point(16, 8)
        Me.Frame1.Name = "Frame1"
        Me.Frame1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Frame1.Size = New System.Drawing.Size(225, 81)
        Me.Frame1.TabIndex = 7
        Me.Frame1.TabStop = False
        Me.Frame1.Text = " Output: "
        '
        'btnWrite
        '
        Me.btnWrite.BackColor = System.Drawing.SystemColors.Control
        Me.btnWrite.Cursor = System.Windows.Forms.Cursors.Default
        Me.btnWrite.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.btnWrite.ForeColor = System.Drawing.SystemColors.ControlText
        Me.btnWrite.Location = New System.Drawing.Point(152, 32)
        Me.btnWrite.Name = "btnWrite"
        Me.btnWrite.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.btnWrite.Size = New System.Drawing.Size(65, 25)
        Me.btnWrite.TabIndex = 2
        Me.btnWrite.Text = "Write"
        '
        'txtOutValue
        '
        Me.txtOutValue.AcceptsReturn = True
        Me.txtOutValue.AutoSize = False
        Me.txtOutValue.BackColor = System.Drawing.SystemColors.Window
        Me.txtOutValue.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.txtOutValue.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.txtOutValue.ForeColor = System.Drawing.SystemColors.WindowText
        Me.txtOutValue.Location = New System.Drawing.Point(64, 48)
        Me.txtOutValue.MaxLength = 0
        Me.txtOutValue.Name = "txtOutValue"
        Me.txtOutValue.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.txtOutValue.Size = New System.Drawing.Size(73, 20)
        Me.txtOutValue.TabIndex = 1
        Me.txtOutValue.Text = ""
        '
        'txtOutAddress
        '
        Me.txtOutAddress.AcceptsReturn = True
        Me.txtOutAddress.AutoSize = False
        Me.txtOutAddress.BackColor = System.Drawing.SystemColors.Window
        Me.txtOutAddress.Cursor = System.Windows.Forms.Cursors.IBeam
        Me.txtOutAddress.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.txtOutAddress.ForeColor = System.Drawing.SystemColors.WindowText
        Me.txtOutAddress.Location = New System.Drawing.Point(64, 24)
        Me.txtOutAddress.MaxLength = 0
        Me.txtOutAddress.Name = "txtOutAddress"
        Me.txtOutAddress.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.txtOutAddress.Size = New System.Drawing.Size(73, 20)
        Me.txtOutAddress.TabIndex = 0
        Me.txtOutAddress.Text = ""
        '
        'Label2
        '
        Me.Label2.BackColor = System.Drawing.SystemColors.Control
        Me.Label2.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label2.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label2.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label2.Location = New System.Drawing.Point(10, 51)
        Me.Label2.Name = "Label2"
        Me.Label2.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label2.Size = New System.Drawing.Size(49, 17)
        Me.Label2.TabIndex = 8
        Me.Label2.Text = "Value:"
        Me.Label2.TextAlign = System.Drawing.ContentAlignment.TopRight
        '
        'Label1
        '
        Me.Label1.BackColor = System.Drawing.SystemColors.Control
        Me.Label1.Cursor = System.Windows.Forms.Cursors.Default
        Me.Label1.Font = New System.Drawing.Font("Arial", 8.0!, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
        Me.Label1.ForeColor = System.Drawing.SystemColors.ControlText
        Me.Label1.Location = New System.Drawing.Point(10, 27)
        Me.Label1.Name = "Label1"
        Me.Label1.RightToLeft = System.Windows.Forms.RightToLeft.No
        Me.Label1.Size = New System.Drawing.Size(49, 17)
        Me.Label1.TabIndex = 7
        Me.Label1.Text = "Address:"
        Me.Label1.TextAlign = System.Drawing.ContentAlignment.TopRight
        '
        'Main
        '
        Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
        Me.ClientSize = New System.Drawing.Size(261, 185)
        Me.Controls.AddRange(New System.Windows.Forms.Control() {Me.Frame2, Me.Frame1})
        Me.Name = "Main"
        Me.Text = "Simple I/O  -- PortIO32 Demo"
        Me.Frame2.ResumeLayout(False)
        Me.Frame1.ResumeLayout(False)
        Me.ResumeLayout(False)

    End Sub

#End Region

    Private Sub btnRead_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles btnRead.Click
        'Dimension variables
        Dim Address As Short 'Holds the address of the input port
        Dim Value As Integer 'Holds the value read in from the input port

        'Extract input port address from the text box
        Address = Val([txtInAddress].Text)

        'Read the input port
        If InByte(Address, Value) Then
            MsgBox("Error reading value with InByte.  Please ensure the PortIO32 driver and library are installed.")
        End If

        'Display the data from the input port
        lblInValue.Text = CStr(Value)

    End Sub

    Private Sub btnWrite_Click(ByVal eventSender As System.Object, ByVal eventArgs As System.EventArgs) Handles btnWrite.Click
        'Dimension variables
        Dim Address As Short 'Holds the address of the output port
        Dim Value As Integer 'Holds the value to write to the output port

        'Extract the output port address from the text box
        Address = Val([txtOutAddress].Text)

        'Extract the value to write to the output port
        Value = Val([txtOutValue].Text)

        'Write the value to the output port
        If OutByte(Address, Value) Then
            MsgBox("Error writing value with OutByte.  Please ensure the PortIO32 driver and library are installed.")
        End If
    End Sub


End Class
