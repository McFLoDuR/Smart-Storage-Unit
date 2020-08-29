#define I2C_C_
#include "I2C.h"

// define some buffer variables
LED CurrentLED;
int IndexLED = 0;
bool COMMAND_ERROR = false;

// initialization of the I2C connection
void I2C_Init(){
   Wire.begin(I2C_ADDRESS);
   Wire.onReceive(I2C_ReceiveData);
}

// receive event, it is called when the master sends data
void I2C_ReceiveData(){
  I2C_parseReceivedCommand();
  if(!COMMAND_ERROR)
    LedStrip_SetLED(CurrentLED, IndexLED);
}

// parse the data array from the master
void I2C_parseReceivedCommand(){
  COMMAND_ERROR = false;

  if(Wire.available() == 6){
    CurrentLED.state = Wire.read();
  
    // I2C Libary of the RPi sends always the Length of the data array on second position
    // because there is no use for this (in this application) it gets cleared from the buffer
    Wire.read();
  
    IndexLED = Wire.read();
    CurrentLED.color.R = Wire.read();
    CurrentLED.color.G = Wire.read();
    CurrentLED.color.B = Wire.read();
  } else {
    COMMAND_ERROR = true;
  }
}
