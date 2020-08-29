#ifndef LedStrip_H_
#define LedStrip_H_

  #include <Arduino.h>
  #include <FastLED.h>

  // number of all LEDs in the SmartStorageUnit
  #define LedStrip_NUM_LEDS 240

  // number of LEDs in every small part storage
  #define LedStrip_NUM_LEDS_SPS1 30
  #define LedStrip_NUM_LEDS_SPS2 30
  #define LedStrip_NUM_LEDS_SPS3 60
  #define LedStrip_NUM_LEDS_SPS4 60
  #define LedStrip_NUM_LEDS_SPS5 60

  // data pin for every small part storage
  #define LedStrip_DATA_PIN_SPS1 3
  #define LedStrip_DATA_PIN_SPS2 4
  #define LedStrip_DATA_PIN_SPS3 5
  #define LedStrip_DATA_PIN_SPS4 6
  #define LedStrip_DATA_PIN_SPS5 7

  // defines for better clearness and meaning of the bits
  #define LedStrip_LED_ACTIVATED 7
  #define LedStrip_LED_STATE 6
  #define LedStrip_LED_SPEED2 2
  #define LedStrip_LED_SPEED1 1
  #define LedStrip_LED_SPEED0 0

  // structures for better clearness in the program
  typedef struct Color_{
    byte R, G, B;
  } Color;

  typedef struct LED_{
    Color color;
    byte state;
  } LED;

  // definition of the single LED-strips and LED array
  #ifdef LedStrip_C_
    CRGB LedStrip_SPS1[LedStrip_NUM_LEDS_SPS1];
    CRGB LedStrip_SPS2[LedStrip_NUM_LEDS_SPS2];
    CRGB LedStrip_SPS3[LedStrip_NUM_LEDS_SPS3];
    CRGB LedStrip_SPS4[LedStrip_NUM_LEDS_SPS4];
    CRGB LedStrip_SPS5[LedStrip_NUM_LEDS_SPS5];
    LED LedStrips[LedStrip_NUM_LEDS];
  #else 
    extern CRGB LedStrip_SPS1[LedStrip_NUM_LEDS_SPS1];
    extern CRGB LedStrip_SPS2[LedStrip_NUM_LEDS_SPS2];
    extern CRGB LedStrip_SPS3[LedStrip_NUM_LEDS_SPS3];
    extern CRGB LedStrip_SPS4[LedStrip_NUM_LEDS_SPS4];
    extern CRGB LedStrip_SPS5[LedStrip_NUM_LEDS_SPS5];
    extern LED LedStrips[LedStrip_NUM_LEDS];
  #endif

  // functions
  void LedStrip_Init();
  void LedStrip_SetLED(LED led, int Index);

#endif
