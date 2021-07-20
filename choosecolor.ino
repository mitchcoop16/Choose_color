#include <Adafruit_NeoPixel.h>

#define PIN 6
// setup neopixels
Adafruit_NeoPixel strip = Adafruit_NeoPixel (24, PIN, NEO_GRB + NEO_KHZ800);

void setup() {
  Serial.begin(9600);
  strip.begin();
  strip.setBrightness(25);
  strip.show();
}

void loop() {
  
  if (Serial.available()) {
    String color = Serial.readString();
    //convert string to long int
    long rgb = strtol(&color[1], NULL, 16);
    long r = rgb >> 16;
    long g = rgb >> 8 & 0xFF;
    long b = rgb & 0xFF;
    
    colorWipe(strip.Color(r, g, b),50);
    Serial.println(color);
  }
}

//will turn on one pixel at a time with the color selected
void colorWipe(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++){
    strip.setPixelColor(i, color);
    strip.show();
    delay(wait);}
  }
  
