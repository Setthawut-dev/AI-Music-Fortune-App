import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Music Fortune Teller", page_icon="🔮")
st.title("🔮 AI Music Fortune Teller 2026")

# --- 1. เชื่อมต่อ API Key แบบปลอดภัย (ดึงจาก Secrets) ---
try:
    GEMINI_KEY = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=GEMINI_KEY)
except Exception as e:
    st.error("⚠️ ไม่พบ API Key กรุณาตั้งค่าใน Streamlit Secrets")
    st.stop()

# --- 2. ตั้งค่า Model แบบเจาะจง (ลบระบบ List ทิ้งเพื่อแก้ Error ถาวร) ---
try:
    # พิมพ์ชื่อตรงๆ เป็นตัวหนังสือ (ไม่มี List ไม่มีวงเล็บปีกกา)
    model_name = "gemini-1.5-flash" 
    model = genai.GenerativeModel(model_name)
    st.success(f"🚀 System Ready | Model: {model_name}")
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
st.caption("Music Fortune v8.0 | Final Fix Mode")
