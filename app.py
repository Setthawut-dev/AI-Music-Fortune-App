import streamlit as st
import google.generativeai as genai
import os

# --- 1. ตั้งค่า API Key ---
# วิธีนี้จะดึงจาก Secrets ของ Streamlit (ถ้ามี) หรือดึงจากโค้ดตรงๆ
# เพื่อความง่ายในการส่งอาจารย์ ผมจะทำระบบ Check ให้ครับ
if "GEMINI_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_KEY"]
else:
    # วางคีย์ใหม่ของคุณที่นี่ (แต่ตอนอัปขึ้น GitHub แนะนำให้ลบออกหรือใช้ Secrets แทน)
    api_key = "AIzaSyBpm407vYBE8_6QMwP4Ube5pN6ALIJMebk" 

genai.configure(api_key=api_key)

st.set_page_config(page_title="AI Music Fortune Teller", page_icon="🔮")
st.title("🔮 AI Music Fortune Teller 2026")

# --- 2. เลือกโมเดลแบบเจาะจง (Fix ปัญหา 404) ---
# ระบุรุ่นที่เสถียรที่สุดไปเลย ไม่ต้อง List หาแล้วครับ
model_name = 'gemini-1.5-flash'
model = genai.GenerativeModel(model_name)
st.caption(f"🚀 System Ready | Model: `{model_name}`")

# --- 3. ส่วนรับข้อมูล (คงเดิม) ---
st.write("---")
col1, col2 = st.columns(2)
with col1:
    artist = st.text_input("👤 ศิลปินที่ชอบ")
with col2:
    song = st.text_input("🎵 เพลงที่ฟังบ่อย")

lyrics = st.text_area("✍️ ท่อนเพลงที่ตรงใจ")

if st.button("🌟 วิเคราะห์ดวงชะตาอย่างละเอียด"):
    if artist and song and api_key:
        try:
            with st.spinner('🔭 กำลังทำนายดวง...'):
                prompt = f"ทำนายดวงจากเพลง {song} ของ {artist} แยกหมวดหมู่ การงาน ความรัก ตัวตน และแนะนำเพลงภาษาไทย"
                response = model.generate_content(prompt)
                st.write("---")
                st.markdown(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
            st.info("💡 หากขึ้น 404/403 อาจเป็นเพราะ API Key ถูกระงับเนื่องจากหลุดไปใน GitHub")
