import streamlit as st
from google import genai # ใช้ระบบใหม่ล่าสุดตาม requirements.txt

st.set_page_config(page_title="AI Music Fortune Teller", page_icon="🔮")
st.title("🔮 AI Music Fortune Teller 2026")

# --- 1. เชื่อมต่อ API Key (New SDK) ---
try:
    GEMINI_KEY = st.secrets["GEMINI_KEY"]
    client = genai.Client(api_key=GEMINI_KEY)
    st.success("🚀 System Ready | API Key Connected (New SDK)")
except Exception as e:
    st.error("⚠️ ไม่พบ API Key กรุณาตรวจสอบ Streamlit Secrets")
    st.stop()

# --- 2. ส่วนรับข้อมูล ---
st.write("---")
col1, col2 = st.columns(2)
with col1:
    artist = st.text_input("👤 ศิลปินที่ชอบ")
with col2:
    song = st.text_input("🎵 เพลงที่ฟังบ่อย")

lyrics = st.text_area("✍️ ท่อนเพลงที่ตรงใจ (ใส่หรือไม่ใส่ก็ได้)")

if st.button("🌟 วิเคราะห์ดวงชะตาอย่างละเอียด"):
    if artist and song:
        with st.spinner('🔭 กำลังเปิดคัมภีร์ดนตรีทำนายดวง และค้นหาโมเดลที่ทำงานได้...'):
            
            # 💡 รายชื่อโมเดลสำรอง (สำหรับ New SDK)
            fallback_models = [
                "gemini-1.5-flash",
                "gemini-1.5-flash-latest",
                "gemini-1.5-pro",
                "gemini-pro"
            ]
            
            success = False
            
            full_prompt = f"""คุณคือ 'นักพยากรณ์คลื่นความถี่ดนตรี' (Musical Frequency Oracle) 
            จงทำนายดวงชะตาจากเพลง '{song}' ของ '{artist}' 
            ท่อนเพลงที่ผู้ใช้เน้น: '{lyrics}'
            
            จงตอบเป็นภาษาไทยโดยแบ่งหัวข้อดังนี้:
            1. 🎵 [พลังงานจากบทเพลง]: วิเคราะห์จิตวิญญาณและตัวตน
            2. 💼 [การงานและการเรียน]: แนวโน้มความสำเร็จและสิ่งที่ต้องระวัง
            3. ❤️ [ความรักและความสัมพันธ์]: สถานะหัวใจในช่วงนี้
            4. 🍀 [เคล็ดลับเสริมดวง]: สีนำโชคหรือข้อคิดจากเพลง
            5. 🎧 [AI Recommended]: แนะนำอีก 1 เพลงที่เหมาะกับดวงเขาตอนนี้
            
            เขียนให้ยาวและน่าอ่าน ใส่ Emoji ประกอบทุกหัวข้อ"""

            # ลองเรียกใช้ทีละโมเดล
            for m_name in fallback_models:
                try:
                    response = client.models.generate_content(
                        model=m_name,
                        contents=full_prompt
                    )
                    
                    st.write("---")
                    st.success(f"✨ วิเคราะห์ดวงชะตาของคุณเสร็จสมบูรณ์! (พยากรณ์โดย AI รุ่น: {m_name})")
                    st.markdown(response.text)
                    st.balloons()
                    success = True
                    break # ถ้าสำเร็จให้หยุดทำงานเลย
                except Exception as e:
                    continue # ถ้า Error 404 อีก ให้ลองข้ามไปตัวต่อไป
            
            if not success:
                st.error("เกิดข้อผิดพลาด: Google ปฏิเสธการเข้าถึงโมเดลทั้งหมด (อาจต้องลองสร้าง API Key ใหม่ที่ Google AI Studio ครับ)")

    else:
        st.warning("⚠️ กรุณากรอกชื่อศิลปินและเพลงก่อนนะครับ")

st.write("---")
st.caption("Music Fortune v11.0 | New SDK + Fallback Mode")
