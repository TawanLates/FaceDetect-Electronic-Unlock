#include <ESP8266WiFi.h>

const char* ssid = "Tawan_Titie";         // Replace with your network SSID
const char* password = "620523371"; // Replace with your network password

WiFiServer server(80);  // Create a server that listens on port 80

const int relayPin = D1;  // ใช้ GPIO D1 สำหรับควบคุม Relay

void setup() {
  Serial.begin(115200);
  delay(10);

  // ตั้งค่า Relay Pin เป็น OUTPUT
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, LOW);  // เริ่มต้นให้ Relay ปิดอยู่

  // ตั้งค่า Built-in LED เป็น OUTPUT
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);  // เริ่มต้นให้ LED ปิดอยู่

  // เชื่อมต่อ Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("Connected to Wi-Fi");
  server.begin();  // เริ่มต้น server
}

void loop() {
  WiFiClient client = server.available(); // เช็คว่ามีการเชื่อมต่อจาก client หรือไม่
  if (client) {
    String request = client.readStringUntil('\r');
    client.flush();

    // ตรวจสอบคำสั่งเปิด relay
    if (request.indexOf("/turnOn") != -1) {
      digitalWrite(LED_BUILTIN, HIGH); // เปิด LED บนบอร์ด
      digitalWrite(relayPin, HIGH);    // เปิด Relay
      Serial.println("Relay turned ON");  // Log ข้อความ
    }

    // ตรวจสอบคำสั่งปิด relay
    if (request.indexOf("/turnOff") != -1) {
      digitalWrite(LED_BUILTIN, LOW);  // ปิด LED บนบอร์ด
      digitalWrite(relayPin, LOW);     // ปิด Relay
      Serial.println("Relay turned OFF");  // Log ข้อความ
    }

    // ส่ง Response กลับไปยัง Client
    client.println("HTTP/1.1 200 OK");
    client.println("Content-type:text/html");
    client.println();
    client.println("<html><body><h1>ESP8266 Relay Control</h1></body></html>");
    client.stop();  // ปิดการเชื่อมต่อ
  }
}
