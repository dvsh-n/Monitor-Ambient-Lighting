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
  if (Serial.available()){
    c = Serial.read();
    
    if (c != '\n')
      str[idx++] = c;
    else{
      str[idx] = '\0';
      idx = 0;

      Serial.print("ESP: ");
      Serial.println(str);
    }
  }
  // if (str == "On\n")
  //   digitalWrite(onboard_led, HIGH);
  // else
  //   digitalWrite(onboard_led, LOW);
}
