#ifndef I2C_H_
#define I2C_H_

  #include <Arduino.h>
  #include <Wire.h>
  #include "LedStrip.h"

  // set the address of the Arduino
  #define I2C_ADDRESS 0x51

  //functions
  void I2C_Init();
  void I2C_ReceiveData();
  void I2C_parseReceivedCommand();

#endif
