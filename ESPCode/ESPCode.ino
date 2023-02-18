#define MAX_BUFF_LEN 255
#define onboard_led 2
#define LEDS 66

char c;
char led_color[LEDS][3];
uint8_t led_idx = 0;
uint8_t channel_idx = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(921600);
  pinMode(onboard_led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()){
    for (led_idx = 0; led_idx<LEDS ;led_idx++){
      for (channel_idx = 0; channel_idx<3; channel_idx++){
        c = Serial.read();
        led_color[led_idx][channel_idx] = +c;
      }
  }
    }

  }
}
