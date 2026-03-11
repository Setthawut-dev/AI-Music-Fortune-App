import google.generativeai as genai

genai.configure(api_key="AIzaSyCXGorUX-NC_EVzNTXRDnbZ5AzBRRecqcM")

try:
    print("กำลังตรวจสอบโมเดลที่ API Key นี้เข้าถึงได้...")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"> {m.name}")
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")