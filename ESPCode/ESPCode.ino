#define MAX_BUFF_LEN 255

char c;
char str[MAX_BUFF_LEN];
uint8_t idx = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
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
}
