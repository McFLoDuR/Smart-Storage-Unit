#define LedStrip_C_
#include "LedStrip.h"

// initialization of the LED-strip
void LedStrip_Init(){
  FastLED.addLeds<WS2813, LedStrip_DATA_PIN_SPS1, GRB>(LedStrip_SPS1, LedStrip_NUM_LEDS_SPS1);
  FastLED.addLeds<WS2813, LedStrip_DATA_PIN_SPS2, GRB>(LedStrip_SPS2, LedStrip_NUM_LEDS_SPS2);
  FastLED.addLeds<WS2813, LedStrip_DATA_PIN_SPS3, GRB>(LedStrip_SPS3, LedStrip_NUM_LEDS_SPS3);
  FastLED.addLeds<WS2813, LedStrip_DATA_PIN_SPS4, GRB>(LedStrip_SPS4, LedStrip_NUM_LEDS_SPS4);
  FastLED.addLeds<WS2813, LedStrip_DATA_PIN_SPS5, GRB>(LedStrip_SPS5, LedStrip_NUM_LEDS_SPS5);
  FastLED.clear();

  for(int i = 0; i < LedStrip_NUM_LEDS; i++){
    LedStrips[i].color.R = 0;
    LedStrips[i].color.G = 0;
    LedStrips[i].color.B = 0;
    LedStrips[i].state = 0;
  }
}

// set the configuration of a LED in the array
void LedStrip_SetLED(LED led, int Index){
   LedStrips[Index] = led;
}
