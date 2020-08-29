#include "LedStrip.h"
#include "I2C.h"
#include "LightHandler.h"

void setup() {
  LedStrip_Init();
  I2C_Init();
/*
  Serial.begin(9600);
  LedStrips[0].state = ((1 << LedStrip_LED_ACTIVATED) | (1 << LedStrip_LED_SPEED2));
  LedStrips[0].color.R = 207;
  LedStrips[0].color.G = 0;
  LedStrips[0].color.B = 251;

  LedStrips[54].state = ((1 << LedStrip_LED_ACTIVATED) | (1 << LedStrip_LED_SPEED1) | (1 << LedStrip_LED_SPEED0));
  LedStrips[54].color.R = 0x00;
  LedStrips[54].color.G = 0xFF;
  LedStrips[54].color.B = 0x00;

  LedStrips[75].state = ((1 << LedStrip_LED_ACTIVATED) | (1 << LedStrip_LED_SPEED1));
  LedStrips[75].color.R = 0x00;
  LedStrips[75].color.G = 0x00;
  LedStrips[75].color.B = 0xFF;

  LedStrips[126].state = ((1 << LedStrip_LED_ACTIVATED) | (1 << LedStrip_LED_SPEED0));
  LedStrips[126].color.R = 0xFF;
  LedStrips[126].color.G = 0x00;
  LedStrips[126].color.B = 0xFF;

  LedStrips[187].state = (1 << LedStrip_LED_ACTIVATED);
  LedStrips[187].color.R = 0xFF;
  LedStrips[187].color.G = 0xFF;
  LedStrips[187].color.B = 0x00;
  */
}

void loop() {
  LightHandler_UpdateAllLEDStrips();
}
