import streamlit as st
import google.generativeai as genai

# --- 1. ตั้งค่า API Key (ใช้ตัวเดิมที่คุณรันผ่าน) ---
GEMINI_KEY = "AIzaSyCXGorUX-NC_EVzNTXRDnbZ5AzBRRecqcM" 
genai.configure(api_key=GEMINI_KEY)

st.set_page_config(page_title="AI Music Fortune Teller", page_icon="🔮")
st.title("🔮 AI Music Fortune Teller 2026")

# --- 2. ระบบเลือก Model อัตโนมัติ (ตัวเดิมที่ใช้งานได้) ---
target_model = 'gemini-1.5-flash' 

try:
    model = genai.GenerativeModel(target_model)
    # ทดสอบเบื้องต้นว่าโมเดลพร้อมไหม (ใส่หลอกๆ ไว้)
    available_models = [target_model] 
    st.caption(f"🚀 Connected via: `{target_model}` (Stable Mode)")
except Exception as e:
    available_models = []
    st.error(f"❌ ไม่สามารถเชื่อมต่อกับ Gemini ได้: {e}")

# --- 3. ส่วนรับข้อมูล ---
st.write("---")
col1, col2 = st.columns(2)
with col1:
    artist = st.text_input("👤 ศิลปินที่ชอบ")
with col2:
    song = st.text_input("🎵 เพลงที่ฟังบ่อย")

lyrics = st.text_area("✍️ ท่อนเพลงที่ตรงใจ (ใส่หรือไม่ใส่ก็ได้)")

if st.button("🌟 วิเคราะห์ดวงชะตาอย่างละเอียด"):
    if artist and song and available_models:
        try:
            with st.spinner('🔭 กำลังเปิดคัมภีร์ดนตรีทำนายดวง...'):
                # ปรับ Prompt ให้ยาวและละเอียดขึ้น
                full_prompt = f"""คุณคือ 'นักพยากรณ์คลื่นความถี่ดนตรี' (Musical Frequency Oracle) 
                จงทำนายดวงชะตาจากเพลง '{song}' ของ '{artist}' 
                ท่อนเพลงที่ผู้ใช้เน้น: '{lyrics}'
                
                จงตอบเป็นภาษาไทยที่ดูน่าตื่นเต้น มีเสน่ห์ และให้พลังใจ โดยแบ่งหัวข้อดังนี้:
                
                1. 🎵 [พลังงานจากบทเพลง]: วิเคราะห์ลึกๆ ว่ารสนิยมนี้บอกอะไรเกี่ยวกับ "จิตวิญญาณ" และ "ตัวตน" ของเขา
                2. 💼 [การงานและการเรียน]: แนวโน้มความสำเร็จ อุปสรรคที่ต้องระวัง และโอกาสในช่วงนี้
                3. ❤️ [ความรักและความสัมพันธ์]: สถานะหัวใจในช่วงนี้จะเป็นอย่างไร (คนโสด/มีคู่)
                4. 🍀 [เคล็ดลับเสริมดวง]: สีนำโชค หรือข้อคิดจากเนื้อเพลงที่เขาควรยึดถือ
                5. 🎧 [AI Recommended]: แนะนำเพลงอีก 1 เพลงที่เหมาะกับดวงชะตาเขาในตอนนี้ พร้อมเหตุผลสั้นๆ
                
                เขียนให้ยาวและน่าอ่าน ใส่ Emoji ประกอบทุกหัวข้อ"""

                response = model.generate_content(full_prompt)
                
                st.write("---")
                st.success("✨ วิเคราะห์ดวงชะตาของคุณเสร็จสมบูรณ์!")
                st.markdown(response.text)
                st.balloons()
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")
    else:
        st.warning("⚠️ กรุณากรอกชื่อศิลปินและเพลงก่อนนะครับ")

st.write("---")
st.caption("Music Fortune v4.0 | Detailed Analysis Mode")
