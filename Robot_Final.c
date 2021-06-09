// Include the Servo library
#include <Servo.h>
// Declare the Servo pin
int servoPin = 3;
// Create a servo object
Servo Servo1;
int pin = 8;

bool o = true;

void setup(){
   // put your code here, to run once:
   pinMode(pin,OUTPUT);
   pinMode(LED_BUILTIN,OUTPUT);
  // We need to attach the servo to the used pin number
  Servo1.attach(servoPin); 

   
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(1000);
  if (o){
  digitalWrite(LED_BUILTIN,HIGH);
  digitalWrite(pin,HIGH);
  }
  delay(5000);
  if (o){
  digitalWrite(LED_BUILTIN,LOW);
  digitalWrite(pin,LOW);
  }
   //Make servo go to 90 degrees
  Servo1.write(90);
  delay(2000);
  if (o){
  digitalWrite(LED_BUILTIN,HIGH);
  digitalWrite(pin,HIGH);
  }
  delay(5000);
  if (o){
  digitalWrite(LED_BUILTIN,LOW);
  digitalWrite(pin,LOW);
  }
  Servo1.write(40);
  delay(1000);
  if (o){
  digitalWrite(LED_BUILTIN,HIGH);
  digitalWrite(pin,HIGH);
  }
  delay(3000);
  if (o){
  digitalWrite(LED_BUILTIN,LOW);
  digitalWrite(pin,LOW);
  }
  Servo1.write(140);
  delay(1000);
  if (o){
  digitalWrite(LED_BUILTIN,HIGH);
  digitalWrite(pin,HIGH);
  }
  delay(3000);
  if (o){
  digitalWrite(LED_BUILTIN,LOW);
  digitalWrite(pin,LOW);
  }
  digitalWrite(pin, HIGH);
  o = false;
}
