#include <FastLED.h>

#define DATA_PIN 4
#define onboard_led 2
#define LEDS 66

uint8_t c;
uint8_t led_idx = 0;
uint8_t channel_idx = 0;
bool full = false;

CRGB leds[LEDS];

uint8_t leds2[LEDS][3] = {0};

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, LEDS);  // GRB ordering is typical
}

void loop() {

  while (Serial.available()){
    c = Serial.read();

    if (full) {
      full = false;
      led_idx = -1; // -1 because the next if statement makes it 0
    }
    if (channel_idx == 3){
      channel_idx = 0;
      led_idx++;
    }
    if (channel_idx == 2 && led_idx == LEDS-1){
      full = true;
    }

    leds[led_idx][channel_idx] = c;
    leds2[led_idx][channel_idx] = +c;
    channel_idx++;

    Serial.println(+c);

    if (leds2[0][0] == 60){
      digitalWrite(LED_BUILTIN, HIGH);
    }

    FastLED.show();
  }


}
// + operater is the unary operator
// void loop() { 
//   // Turn the LED on, then pause
//   leds[0].red = 18;
//   leds[0].green = 200;
//   leds[0].blue = 150;
//   FastLED.show();
//   delay(500);
//   // Now turn the LED off, then pause
//   leds[0] = CRGB::Black;
//   FastLED.show();
//   delay(500);
// }
// Whenever gets new data, updates
// Clears the array when new data comes
// 150 LEDS