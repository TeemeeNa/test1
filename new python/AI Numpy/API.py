import os
from google import genai  # เปลี่ยนจาก 'from genai import Client' เป็นแบบนี้
from dotenv import load_dotenv

# โหลดค่าจาก .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ไม่พบ API Key ในไฟล์ .env!")
    exit()

# สร้างตัวเชื่อมต่อ (Client)
# เราเรียกใช้ผ่าน genai.Client
client = genai.Client(api_key=api_key)

print("--- ระบบ AI พร้อมทำงานแล้ว (พิมพ์ exit เพื่อเลิก) ---")

while True:
    user_input = input("ถาม AI: ")
    if user_input.lower() in ['exit', 'quit', 'ออก']:
        break
    
    try:
        # ใช้รุ่น gemini-2.0-flash รุ่นใหม่ล่าสุด
        response = client.models.generate_content(
            model='gemini-2.0-flash', 
            contents=user_input
        )
        print(f"AI: {response.text}\n")
        
    except Exception as error:
        print(f"เกิดข้อผิดพลาด: {error}")