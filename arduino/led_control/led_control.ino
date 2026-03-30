#include <Servo.h>

const int greenLED = 13;
const int redLED = 12;
Servo myServo;

bool servoAttached = false;

void setup() {
  pinMode(greenLED, OUTPUT);
  pinMode(redLED, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      // Known face
      digitalWrite(greenLED, HIGH);
      digitalWrite(redLED, LOW);

      if (!servoAttached) {
        myServo.attach(9);  // Attach only when needed
        servoAttached = true;
      }
      myServo.write(90); // Rotate to 90°
    }  
    else {
      // Unknown face or no face
      digitalWrite(greenLED, LOW);
      digitalWrite(redLED, command == '2' ? HIGH : LOW);

      if (servoAttached) {
        myServo.detach();  // Detach to stop holding torque
        servoAttached = false;
      }
    }
  }
}


