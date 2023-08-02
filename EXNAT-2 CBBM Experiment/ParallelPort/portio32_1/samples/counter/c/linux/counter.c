/* Counter.c
* 	Winford Engineering
* 	www.winfordeng.com
* 	
* 	This a sample program for Winford Engineering's WECRD155B I/O Card.
*	This program uses Winford Engineering's PortIO32 Low-level library
*	Hardware setup:
*		This program assumes that you have eight LEDs connected
*		to port 1 (port A) of your I/O card.  It also assumes that you have
*		a bounceless pushbutton (or a low frequency clock source) 
*		connected between Bit 0 of port 2 (port B) and ground.
*	Operation:
*		This program keeps a count of how many times the pushbutton
*		has been pressed.  The count begins at 0 and is incremented
*		every time the button is pressed.  To monitor the state of the
*		pushbutton, the program configures Port 2 to be in the input state.
*		The current value is output onto Port 1; if you have LEDs connected
*		you will be able to see the value of the counter in binary form.
*		Notice that since Port 1 is configured for output operation, you 
*		should take care that you do not have any circuitry connected
*		to port 1 that could interfere with the port's outputs (See the
*		section in your manual about Data Contention).
*	Compiling Instructions:
*		This program is written for Winford Engineering's PortIO32.
*		To successfully compile this code, you must have the header file
*		for PortIO32 (portio32.h) and the library file (portio32.a in linux,
*		PortIO32.lib and PortIO32.dll in windows) See the PortIO32 documentation
*		for more details (Support section of www.winfordeng.com).
*/

#include <stdio.h>
#include "portio32.h"

#define BASE 384

int main()
{
	int result; //holds the error or success codes from calls to functions from PortIO32
	int value;  //holds the value read from Port B (Port 2)
	int count=0; //holds how many times the pushbutton has been pressed
	char choice;
	
	//First, we will output a notice and ask for user confirmation
	//this would not normally be done in an actual application.
	printf("Note: This program configures Port 1 as an output port.  Please be sure that you do not have interfering hardware connected to port 1 of your card.\n");
	printf("Also note that this program assumes your card's base address is %d. If that is incorrect, please edit the definition of BASE in the source code.\nContinue (Y/N)?", BASE);
	choice = getchar();
	if( (choice != 'y') && (choice != 'Y') )
		return(0);

	// Note that in this application, the error codes are checked on most function calls.
	// In a normal application, it would not be necessary to 
	// check for errors on all of the functions, but it is done here
	// to show that it is possible.
				  
	//configure the card. Port A (1) should be an output and Port B (2) and C (3) will be inputs
	result=OutByte(BASE + 3, 139); //139 is the proper control byte for this situation	
	if(result == -1)//error occurred
	{
		printf("An error occurred while writing a value to a port.\n");
		return(-1);
	}


	printf("Waiting for button to be pressed.  To exit, press Ctrl-C\n");
	fflush(stdout);//fflush would not normally be used, but it is in this case because of the continuous loop
	
	while(1)//loop to monitor the state of the pushbutton
	{		//Note that this loop has no delays, so it uses up
			//all of the CPU time that it can.  This is done to
			//keep the sample code simple. In a real program,
			//it is recommended that you implement some kind
			//of sleep or timer mechanism.
		result = InByte(BASE + 1, &value);//read a value from Port B
		if(result == -1)
		{
			printf("An error occurred while reading a value from a port.\n");
			return(-1);
		}
		
		//in this sample, we will assume that when the button is pressed,
		//it results in Bit 0 being low (0)
		if( !(value & 1) )//test whether bit 0 (which has a binary weight of 1) is off
		{//the code below will execute if bit 0 was off (button pressed)
			count++;//increment counter
			printf("Count: %d\n", count);
			fflush(stdout);

			//output the new count to the LEDs on port A
			result=OutByte(BASE, count);
			if(result == -1)//function failed
			{
				printf("An error occurred while writing a value.\n");
				return(-1);
			}
			//Now we will wait until bit 0 goes back to being on (wait til the pushbutton is released)
			//so, we will loop while bit 0 is off
			while( !(value & 1) )
			{
				InByte(BASE + 1, &value); //note that this could be (note the R) value=InByteR(BASE + 1); 
			}//end of inner while loop
		}//end of if (test for button pressed)
	}//end of while loop
	return(0);
}//end of main function
