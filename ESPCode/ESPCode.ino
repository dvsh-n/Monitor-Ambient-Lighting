#define MAX_BUFF_LEN 255
#define onboard_led 2
#define LEDS 66

char c;
char led_color[LEDS][3];
uint8_t led_idx = 0;
uint8_t channel_idx = 0;
bool full = false;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(921600);
  pinMode(onboard_led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()){
    c = Serial.read();

    if (full) {
      memset(led_color, 0, sizeof(led_color));
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

    led_color[led_idx][channel_idx] = +c;
    channel_idx++;

    Serial.println(c);
  }
  if (led_color[1][2] == 225) digitalWrite(onboard_led, HIGH);
}
// Whenever gets new data, updates
// Clears the array when new data comes