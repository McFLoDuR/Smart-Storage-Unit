#ifndef LightHandler_H_
#define LightHandler_H_

  #include <Arduino.h>
  #include <FastLED.h>
  #include "LedStrip.h"

  // atleast time (in ms) to wait until the next LED upate happens
  #define LightHandler_WAIT_TIME 125

  // time to wait, until the next LED command can be sended
  #define LightHandler_LEDSTRIP_COMMAND_TIMEOUT 50

  // enumeration for better clearness
  enum TimerSet {
    Speed1s,
    Speed750ms,
    Speed500ms,
    Speed250ms,
    SpeedNone
  };

  //functions
  void LightHandler_UpdateAllLEDStrips();
  void LightHandler_UpdateSingleLED(CRGB ledStrip[], int index, LED *led);
  void LightHandler_SetLEDInformations(LED led);
  
#endif
