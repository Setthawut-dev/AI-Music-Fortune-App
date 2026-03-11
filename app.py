import streamlit as st
import google.generativeai as genai

# --- 1. ตั้งค่าหน้าเว็บ ---
st.set_page_config(page_title="AI Music Fortune Teller", page_icon="🔮")
st.title("🔮 AI Music Fortune Teller 2026")

# --- 2. ตั้งค่า API Key ---
GEMINI_KEY = "AIzaSyDzrTUBKTz_CZT4M5Ne-1hbELPjyWmUijA" 
genai.configure(api_key=GEMINI_KEY)

# --- 3. ระบบเลือก Model (แก้ไขปัญหาสตริงกับลิสต์เรียบร้อยแล้ว) ---
try:
    # ดึงรายชื่อโมเดลทั้งหมดมาเก็บในตัวแปร all_models (ซึ่งจะได้มาเป็น List)
    all_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    
    if all_models:
        # [จุดที่แก้ไข] เติม เพื่อดึงเฉพาะ "ชื่อแรก" ออกมาให้เป็นตัวอักษร (String) ตัวเดียว
        model_name = all_models 
    else:
        model_name = 'models/gemini-1.5-flash'
        
    model = genai.GenerativeModel(model_name)
    st.caption(f"🚀 System Online | Model: `{model_name}`")
    
except Exception as e:
    st.error(f"การเชื่อมต่อมีปัญหา: {e}")
    # บังคับใช้ชื่อมาตรฐานหากเกิดข้อผิดพลาดในการดึงชื่อ
    model_name = 'gemini-1.5-flash'
    model = genai.GenerativeModel(model_name)

# --- 4. ส่วนรับข้อมูล ---
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
                # ปรับ Prompt ให้คมชัดและเป็นระบบ
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
st.caption("Music Fortune v4.2 | Stable Version")
