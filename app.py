import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Music Fortune Teller", page_icon="🔮")
st.title("🔮 AI Music Fortune Teller 2026")

# --- 1. ดึง API Key จาก Secrets อย่างปลอดภัย ---
try:
    GEMINI_KEY = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=GEMINI_KEY)
except Exception as e:
    st.error("⚠️ ไม่พบ API Key กรุณาตรวจสอบ Streamlit Secrets")
    st.stop()

# --- 2. ระบบค้นหาและเลือก Model อัตโนมัติ (แก้ 404 ถาวร) ---
try:
    # สั่งให้ระบบลิสต์รายชื่อโมเดลทั้งหมดที่คีย์นี้มีสิทธิ์ใช้
    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    # ถ้าหารายชื่อเจอ ให้ดึง 'ชื่อแรก' มาใช้ (กันปัญหา Error list/string)
    if available_models:
        model_name = available_models
    else:
        # ถ้าระบบ Cloud เอ๋อ หาลิสต์ไม่เจอ ให้บังคับใช้รุ่นพื้นฐานที่สุดที่ทุก Server ต้องมี
        model_name = 'models/gemini-pro'
        
    model = genai.GenerativeModel(model_name)
    st.caption(f"🚀 System Online | Auto-Selected Model: `{model_name}`")
    
except Exception as e:
    st.error(f"การเชื่อมต่อ Model มีปัญหา: {e}")
    st.stop()

# --- 3. ส่วนรับข้อมูล ---
st.write("---")
col1, col2 = st.columns(2)
with col1:
    artist = st.text_input("👤 ศิลปินที่ชอบ")
with col2:
    song = st.text_input("🎵 เพลงที่ฟังบ่อย")

lyrics = st.text_area("✍️ ท่อนเพลงที่ตรงใจ (ใส่หรือไม่ใส่ก็ได้)")

if st.button("🌟 วิเคราะห์ดวงชะตาอย่างละเอียด"):
    if artist and song:
        with st.spinner('🔭 กำลังเปิดคัมภีร์ดนตรีทำนายดวง...'):
            try:
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

                response = model.generate_content(full_prompt)
                
                st.write("---")
                st.success("✨ วิเคราะห์ดวงชะตาของคุณเสร็จสมบูรณ์!")
                st.markdown(response.text)
                st.balloons()
            except Exception as e:
                st.error(f"เกิดข้อผิดพลาดในการทำนาย: {e}")
    else:
        st.warning("⚠️ กรุณากรอกชื่อศิลปินและเพลงก่อนนะครับ")

st.write("---")
st.caption("Music Fortune v7.0 | Ultimate Auto-Fix Mode")
