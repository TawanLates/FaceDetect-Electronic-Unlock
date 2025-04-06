โปรเจคนี้ทำเพื่อพัฒนานวัตกรรมแห่งอนาคต (technological innovation) โดย Duangtawan Chuangchot

ชิ้นงาน : FaceDetect Unlock Electronic-Lock


โดยอุปกรณ์ และ การออกแบบมีดังนี้

1) แบตเตอรี่ 9V : จ่ายพลังงานให้กับระบบ

2) บอร์ดลอง (Breadboard) : ใช้สำหรับเชื่อมต่อระหว่างอุปกรณ์
   
3) ไมโครคอนโทรลเลอร์ ESP8266 : ใช้ควบคุมการทำงานและส่งสัญญาณให้รีเลย์เพื่อเปิดหรือปิดล็อค
   
4) โมดูลรีเลย์ : ทำหน้าที่เป็นสวิตช์เพื่อเปิดหรือปิดการจ่ายไฟไปยังล็อคไฟฟ้า
   
5) ล็อคไฟฟ้า : เป็นตัวล็อคที่จะทำงานเมื่อมีสัญญาณจากรีเลย์
   
6) กล้อง : เป็นตัวฉายภาพให้ระบบตรวจจับใบหน้า 


![image](https://github.com/user-attachments/assets/4eee0350-6fef-45fa-ad5a-824a3865531b)

การแสดงผล เมื่อตรวจสอบเจอใบหน้า สีฟ้าจะดับ สีแดงจะติด หากเซ็นเซอร์มีการตรวจจับใบหน้าได้ ระบบจะทำการปลดล็อคกลอน

![image](https://github.com/user-attachments/assets/d5930516-dd26-41b6-be8d-f17e64bc3e7a)
![image](https://github.com/user-attachments/assets/7aae1795-b1f4-4d55-bd05-68f83cecc299)

การแสดงผล เมื่อเอานิ้วมือปิดกล้อง Relays จะสับตัวจ่ายไฟ ไม่ให้จ่ายเข้าสู่กลอนไฟฟ้า ทำให้ตัวล็อคเด้งออกมา 
![image](https://github.com/user-attachments/assets/c6181789-cca7-4fa9-96b6-4e0eb1976d08)

การแสดงผล หากเอานิ้วมือออก และกล้องตรวจจับใบหน้าเจอ Relays จะสับกลับมาจ่ายไฟให้กลอนไฟฟ้า ทำให้ตัวล็อคหุบกลับไป

![image](https://github.com/user-attachments/assets/b485ec97-890b-4a6b-bfb9-4fb2c53a2891)
![image](https://github.com/user-attachments/assets/320105d1-c745-4448-9160-c63a24e5da7b)
