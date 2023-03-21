#include "BluetoothSerial.h"
#include <FastLED.h>

#define DATA_PIN 4
#define onboard_led 2
#define LEDS 4

CRGB leds[LEDS];
uint8_t leds2[LEDS][3] = {0};

uint8_t c;
uint8_t led_idx = 0;
uint8_t channel_idx = 0;
bool full = false;

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#if !defined(CONFIG_BT_SPP_ENABLED)
#error Serial Bluetooth not available or not enabled. It is only available for the ESP32 chip.
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); //Bluetooth device name
  Serial.println("The device started, now you can pair it with bluetooth!");
  FastLED.addLeds<WS2812B, DATA_PIN, GRB>(leds, LEDS);  // GRB ordering is typical
}

void loop() {
  if (SerialBT.available()){
    c = SerialBT.read();

    if (full) {
      full = false;
      led_idx = -1; // -1 because the next if statement makes it 0
      FastLED.clearData();
    }
    if (channel_idx == 3){
      channel_idx = 0;
      led_idx++;
    }
    if (channel_idx == 2 && led_idx == LEDS-1){
      full = true;
    }

    leds[led_idx][channel_idx] = c;
    leds2[led_idx][channel_idx] = c;
    Serial.print("led idx: "); Serial.print(led_idx); Serial.print(" ");
    Serial.print("channel idx: "); Serial.print(channel_idx); Serial.print(" ");
    Serial.println(leds2[led_idx][channel_idx]);
    channel_idx++;
  }
  if (Serial.available()){
    FastLED.show();
    delay(20);
  }

  // if (Serial.available()) {
  //   SerialBT.write(Serial.read());
  // }
  // if (SerialBT.available()) {
  //   Serial.write(SerialBT.read());
  // }
  // delay(20);
}

// void printArray(uint8_t arr[LEDS][3]){
//   for(int i = 0; i < 12; i++)
//     Serial.println(arr[i]);
// }









