#include <SPI.h>
#include <SD.h>

const int ANALOG_IN_PIN = A1; // Input pin for measuring voltage
const int CURRENT_SENSOR_PIN = A2; // Input pin for measuring current
const float R1 = 30000.0;     // Resistance of R1 in ohms
const float R2 = 7500.0;      // Resistance of R2 in ohms
const float REF_VOLTAGE = 5.0; // Reference voltage of the Arduino
const float R_SHUNT = 220.0; // Resistance of your shunt resistor in ohms
const int LED_PIN = 8;
File dataFile;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  SD.begin(4); // Assuming the CS pin is 4
}

void loop() {
  static unsigned long previousMillis = 0;
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= 500) { // 2Hz sampling rate
    previousMillis = currentMillis;
    
    // Blink LED without blocking
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));

    // Read voltage and current
    float voltage = readVoltage(ANALOG_IN_PIN);
    float current = readCurrent(CURRENT_SENSOR_PIN); // Implement this based on your current sensor

    // Log to SD card
    logData(currentMillis, voltage, current);
  }
}

float readVoltage(int pin) {
  int svalue = analogRead(pin);
  float vout = (svalue * REF_VOLTAGE) / 1024.0;
  return vout / (R2 / (R1 + R2));
}


float readCurrent(int pin) {
  int svalue = analogRead(pin); // Read the analog value from the Arduino
  float vShunt = (svalue * REF_VOLTAGE) / 1024.0; // Convert that value to voltage
  float current = vShunt / R_SHUNT; // Calculate current (I = V/R)
  return current; // Return current in Amperes
}



void logData(unsigned long time, float voltage, float current) {
  // Open the data file on the SD card for writing
  dataFile = SD.open("lab4.txt", FILE_WRITE);
  if (dataFile) {
    // Construct the data string
    String dataString = String(time) + ", " + String(voltage, 3) + ", " + String(current, 7);
    
    // Write the data string to the SD card
    dataFile.println(dataString);
    dataFile.close(); // Make sure to close the file to save the data

    // Also print the data string to the Serial Monitor
    Serial.println(dataString);
  } else {
    // If the file didn't open, print an error to the Serial Monitor
    Serial.println("Error opening lab4.txt");
  }

}

