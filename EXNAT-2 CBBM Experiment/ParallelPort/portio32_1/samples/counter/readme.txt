Winford Engineering
www.winfordeng.com


**********  GENERAL INFORMATION  **********

   This simple program demonstrates how to access the CRD155B card using Winford       
   Engineering's PortIO32 library, which provides low-level I/O port access.


**********  PROGRAM FUNCTION  **********

   This is a simple counter program.  A bit of the input port acts as the clock (Port 2, 
   bit 0).  We assume that a bounceless pushbutton or some low-frequency clock source is 
   connected to this bit of the input port.  The program counts the number of times the 
   pushbutton is pressed and outputs the count to the screen as well as to the output 
   port (Port 1).

   While this is a simplistic program, it provides a framework to guide the programmer 
   in using the API.


**********  HARDWARE SETUP  **********

   This program assumes that your CRD155B card is set for base address 384 decimal.  It    
   automatically configures Port 1 as an OUTPUT port and Port 2 as an INPUT port.  Port 3   
   will not be used, but it will also be configured as an INPUT port.  To prevent data    
   conflicts, be sure that Port 1 is not connected to the outputs of any devices, as this   
   port will become an output port when this program runs. 

   You can connect 8 LEDs to Port 1 to view the current count, or you can just watch it on  
   the screen.

   To increment the count, you will need to either connect a pushbutton with a pull-up 
   resistor or a low frequency clock source to Port 2, Bit 0.



**********  DRIVER AND LIBRARY REQUIRED  *********

   This program requires that the PortIO32 driver and library be installed
   on the system.  Please see the installation instructions in the PortIO32
   documentation.

   For the Visual Basic 5 executable, you must also have the Visual Basic 5 
   runtime (MSVBVM50.dll) on your system.  This can be downloaded from Winford 
   Engineering's web site if you do not have it on your system.

   For the Visual Basic .NET executable, you will need the .NET Framework 
   installed on your computer.  This can be downloaded from Microsoft's 
   web site if you do not have it on your system.


