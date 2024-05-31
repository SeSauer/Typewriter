#include <Arduino.h>



void setup(){
  Serial.begin(9600);
  for (int i = 2; i<= A3; i++){
    pinMode(i, OUTPUT);
  }
}

void resetPins(){
  for (int i = 2; i<=A3; i++){
    digitalWrite(i, LOW);
  }
}

void setPins(uint16_t bits){
  for (int i = 2; i <= A3; i++){
    uint8_t state = (bits >> (18-(i+1))) & 1;
    digitalWrite(i, state);
  }
}

void loop(){
  byte inputBuffer[2] = {};
  //wait for signal
  while (Serial.peek() == -1) {
    //byte i = 0;
    analogWrite(A5, 250);
    delay(100);
  }
  analogWrite(A5, 0);
  delay(100);

  //interpret Signal
  Serial.readBytes(inputBuffer, 2);
  uint16_t bits = inputBuffer[0];
  bits = bits << 8;
  bits += inputBuffer[1];
  setPins(bits);
  delay(100);              //may need adjustment
  resetPins();
  //send answer
  Serial.write((byte)1);
}
