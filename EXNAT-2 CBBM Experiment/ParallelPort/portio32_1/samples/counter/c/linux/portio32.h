#ifndef PORTIO32_H
#define PORTIO32_H

#ifdef __cplusplus
#define PREFUNCTION extern "C"
#else
#define PREFUNCTION extern
#endif

// On Windows platforms, specify that all these functions should
// be called using the Standard Call calling convention.
#ifdef WIN32
#define MIDFUNCTION __stdcall
#else
// Otherwise, define MIDFUNCTION as being nothing
#define MIDFUNCTION 
#endif


PREFUNCTION int MIDFUNCTION OutByte(unsigned short Port, int Data);
PREFUNCTION int MIDFUNCTION OutWord(unsigned short Port, int Data);
PREFUNCTION int MIDFUNCTION InByte(unsigned short Port, int* Data);
PREFUNCTION int MIDFUNCTION InWord(unsigned short Port, int* Data);
PREFUNCTION int MIDFUNCTION InByteR(unsigned short Port);
PREFUNCTION int MIDFUNCTION InWordR(unsigned short Port);

#endif //PORTIO32_H