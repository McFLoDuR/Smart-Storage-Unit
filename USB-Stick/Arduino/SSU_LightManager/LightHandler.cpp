#include "LightHandler.h"

unsigned long TimeCounter = (millis() + LightHandler_WAIT_TIME);
unsigned long CurrentTime = millis();

unsigned long Timer1s = (millis() + 1000);
unsigned long Timer750ms = (millis() + 750);
unsigned long Timer500ms = (millis() + 500);
unsigned long Timer250ms = (millis() + 250);

bool LEDactivated = false;
bool LEDon = false;
TimerSet LEDspeed;

// updates all LED-strips in the smart storage unit
void LightHandler_UpdateAllLEDStrips(){
  if(TimeCounter < millis()){
    FastLED.clear();
    
    for(int i = 0; i < (LedStrip_NUM_LEDS - 1); i++){
      if(i >= 180){
        LightHandler_UpdateSingleLED(LedStrip_SPS5, (i - 180), &LedStrips[i]);
      } else if (i >= 120){
        LightHandler_UpdateSingleLED(LedStrip_SPS4, (i - 120), &LedStrips[i]);
      } else if (i >= 60){
        LightHandler_UpdateSingleLED(LedStrip_SPS3, (i - 60), &LedStrips[i]);
      } else if (i >= 30){
        LightHandler_UpdateSingleLED(LedStrip_SPS2, (i - 30), &LedStrips[i]);
      } else {
        LightHandler_UpdateSingleLED(LedStrip_SPS1, i, &LedStrips[i]);
      }

      delayMicroseconds(LightHandler_LEDSTRIP_COMMAND_TIMEOUT);
    }

    FastLED.show();

    if(Timer250ms < CurrentTime)
      Timer250ms = (millis() + 250);
    if(Timer500ms <CurrentTime)
      Timer500ms = (millis() + 500);
    if(Timer750ms < CurrentTime)
      Timer750ms = (millis() + 750);
    if(Timer1s < CurrentTime)
      Timer1s = (millis() + 1000);
    
    TimeCounter = (millis() + LightHandler_WAIT_TIME);
  }
}

// updates one special LED in a LED strip
void LightHandler_UpdateSingleLED(CRGB ledStrip[], int index, LED *led){
  LightHandler_SetLEDInformations(*led);
  
  CurrentTime = millis();
  
  if(LEDactivated){
    if(LEDspeed != SpeedNone){ 
      if(((LEDspeed == Speed1s) && (Timer1s < CurrentTime)) || ((LEDspeed == Speed750ms) && (Timer750ms < CurrentTime)) || 
        ((LEDspeed == Speed500ms) && (Timer500ms < CurrentTime)) || ((LEDspeed == Speed250ms) && (Timer250ms < CurrentTime)))
      {
        if(!LEDon){
          ledStrip[index] = CRGB(led->color.R, led->color.G, led->color.B);
          led->state |= (1 << LedStrip_LED_STATE);
        } else {
          ledStrip[index] = CRGB::Black;
          led->state &= ~(1 << LedStrip_LED_STATE);
        }
      } else {
        if(LEDon)
          ledStrip[index] = CRGB(led->color.R, led->color.G, led->color.B);
        else
          ledStrip[index] = CRGB::Black;
      }
    } else {
      ledStrip[index] = CRGB(led->color.R, led->color.G, led->color.B);
    }
  } else {
    ledStrip[index] = CRGB::Black;
  }
}

// set LED informations
void LightHandler_SetLEDInformations(LED led){
  LEDon = false;
  LEDactivated = false;
  LEDspeed = SpeedNone;
  
  if(led.state & (1 << LedStrip_LED_ACTIVATED)){
    LEDactivated = true;
    
    if(led.state & (1 << LedStrip_LED_STATE))
      LEDon = true;

    if((led.state & (1 << LedStrip_LED_SPEED2)) && !(led.state & (1 << LedStrip_LED_SPEED1)) && !(led.state & (1 << LedStrip_LED_SPEED0))){
      LEDspeed = Speed1s;
    } else if (!(led.state & (1 << LedStrip_LED_SPEED2)) && (led.state & (1 << LedStrip_LED_SPEED1)) && (led.state & (1 << LedStrip_LED_SPEED0))) {
      LEDspeed = Speed750ms;
    } else if (!(led.state & (1 << LedStrip_LED_SPEED2)) && (led.state & (1 << LedStrip_LED_SPEED1)) && !(led.state & (1 << LedStrip_LED_SPEED0))) {
      LEDspeed = Speed500ms;
    } else if (!(led.state & (1 << LedStrip_LED_SPEED2)) && !(led.state & (1 << LedStrip_LED_SPEED1)) && (led.state & (1 << LedStrip_LED_SPEED0))) {
      LEDspeed = Speed250ms;
    }    
  }
}
