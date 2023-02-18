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
    c = Serial.read();

    if (channel_idx == 3){
      channel_idx = 0;
      led_idx++;
    }
    if (led_idx == LEDS) break;

    led_color[led_idx][channel_idx] = +c;
    channel_idx++;

    Serial.println(c);
  }
  if (led_color[1][2] == 57) digitalWrite(onboard_led, HIGH);
}
