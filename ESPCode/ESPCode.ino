#define MAX_BUFF_LEN 255
#define onboard_led 2

char c;
char str[MAX_BUFF_LEN];
uint8_t idx = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(onboard_led, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available()){
    c = Serial.read();
    Serial.println("start");
    Serial.println(c);
    Serial.println("end");
  }
}
