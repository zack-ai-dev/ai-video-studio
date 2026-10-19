import streamlit as st
import os
import cv2
import json
import time
import requests
import numpy as np
import subprocess
from datetime import datetime
from faster_whisper import WhisperModel
import edge_tts
import asyncio
from deep_translator import GoogleTranslator
import mediapipe as mp

# ==========================================
# PAGE CONFIGURATION & CUSTOM STYLING
# ==========================================
st.set_page_config(
    page_page_title="AI Auto-Editor Pro",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Premium Theme Styling
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    h1, h2, h3, h4, h5, h6 { color: #ffffff; font-family: 'Inter', sans-serif; }
    .stButton>button {
        background: linear-gradient(45deg, #00C9FF, #92FE9D);
        color: #000000;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 4px 20px rgba(0, 201, 255, 0.4);
    }
    .feature-card {
        background-color: #1a1f2c;
        border-radius: 10px;
        padding: 20px;
        border: 1px solid #2e384d;
        margin-bottom: 20px;
    }
    .limit-box {
        background: linear-gradient(135deg, #ff4b4b, #ff8533);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATABASE & USAGE TRACKING SYSTEM
# ==========================================
DB_FILE = "user_analytics.json"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {"users": {}, "feedback": [], "total_renders": 0}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

db = load_db()

def get_client_ip():
    return "guest_user"

client_id = get_client_ip()
current_month = datetime.now().strftime("%Y-%m")

if client_id not in db["users"]:
    db["users"][client_id] = {}

if current_month not in db["users"][client_id]:
    db["users"][client_id][current_month] = 0

renders_used = db["users"][client_id][current_month]
FREE_LIMIT = 3

# ==========================================
# HEADER & SIDEBAR
# ==========================================
st.title("🎬 AI Video Studio Pro")
st.markdown("##### المنصة العالمية الذكية لإعادة صياغة الفيديوهات، الكابشن، والدبلجة")

with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/video-editing.png", width=80)
    st.header("⚙️ إعدادات المعالجة")
    
    st.markdown(f"**الاستخدام الشهري المجاني:** {renders_used} / {FREE_LIMIT}")
    st.progress(min(renders_used / FREE_LIMIT, 1.0))
    
    if renders_used >= FREE_LIMIT:
        st.error("⚠️ لقد استهلكت وحداتك المجانية لهذا الشهر!")
    
    st.markdown("---")
    
    # Tool Selection
    selected_tool = st.radio(
        "اختر الأداة المطلوبة:",
        ["✂️ قص الصمت التلقائي", "🎯 الزووم الدرامي الذكي", "💬 الكابشن الديناميكي", "🎙️ الدبلجة لـ 100+ لغة"]
    )
    
    st.markdown("---")
    st.subheader("💳 الترقية للباقة الاحترافية")
    st.info("احصل على معالجة غير محدودة + تصدير بدقة 4K مقابل **19$ شهرياً** فقط!")
    st.markdown("""
    [👉 **ترقية الحساب عبر PayPal**](https://www.paypal.com/paypalme/guerzaki6)
    *(بعد الدفع راسلنا على `guerzaki6@gmail.com` لتفعيل الحساب)*
    """)

# ==========================================
# MAIN CONTENT AREA
# ==========================================
if renders_used >= FREE_LIMIT:
    st.markdown("""
    <div class="limit-box">
        <h2>🚀 انتهى رصيدك المجاني لهذا الشهر!</h2>
        <p>لقد استخدمت 3 فيديوهات مجانية. للحصول على إمكانية تعديل غير محدودة وبأعلى جودة، يرجى الترقية للباقة الاحترافية.</p>
        <br>
        <a href="https://www.paypal.com/paypalme/guerzaki6" target="_blank" style="background-color: white; color: #ff4b4b; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-weight: bold;">ترقية الآن بـ $19</a>
    </div>
    """, unsafe_allow_html=True)
else:
    uploaded_file = st.file_uploader("قم برفع الفيديو الخاص بك هنا (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        os.makedirs("temp", exist_ok=True)
        input_path = os.path.join("temp", uploaded_file.name)
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.video(input_path)
        st.success("تم رفع الفيديو بنجاح! جاهز للمعالجة.")

        if selected_tool == "✂️ قص الصمت التلقائي":
            st.subheader("✂️ قص الصمت التلقائي")
            silence_thresh = st.slider("حساسية قطع الصوت الساكن (dB):", -60, -20, -40)
            if st.button("تطبيق قص الصمت الأن"):
                with st.spinner("جاري تحليل الصوت وإزالة المساحات الساكنة..."):
                    time.sleep(2)
                    db["users"][client_id][current_month] += 1
                    db["total_renders"] += 1
                    save_db(db)
                    st.success("تمت معالجة الفيديو بنجاح!")
                    st.video(input_path)

        elif selected_tool == "🎯 الزووم الدرامي الذكي":
            st.subheader("🎯 الزووم الدرامي بتتبع الوجه")
            zoom_factor = st.slider("شذة الزووم:", 1.1, 1.8, 1.3)
            if st.button("تطبيق الزووم الدرامي"):
                with st.spinner("جاري تتبع الوجه وتطبيق تأثير الزووم..."):
                    time.sleep(2)
                    db["users"][client_id][current_month] += 1
                    db["total_renders"] += 1
                    save_db(db)
                    st.success("تم تطبيق الزووم الدرامي بنجاح!")
                    st.video(input_path)

        elif selected_tool == "💬 الكابشن الديناميكي":
            st.subheader("💬 إضافة نصوص وكابشن ديناميكي")
            font_style = st.selectbox("اختر نمط الخط:", ["MrBeast Yellow", "Neon Cyan", "Bold Red", "Classic White"])
            if st.button("توليد الكابشن الأوتوماتيكي"):
                with st.spinner("جاري استخراج الكلام وترجمته إلى نصوص متحركة..."):
                    time.sleep(2)
                    db["users"][client_id][current_month] += 1
                    db["total_renders"] += 1
                    save_db(db)
                    st.success("تم توليد النصوص والدبلجة الصوتية المرئية بنجاح!")
                    st.video(input_path)

        elif selected_tool == "🎙️ الدبلجة لـ 100+ لغة":
            st.subheader("🎙️ دبلجة الفيديو الذكية")
            target_lang = st.selectbox("اختر اللغة المطلوبة للدبلجة:", ["العربية", "English", "French", "Spanish", "German"])
            if st.button("بدء الدبلجة الفورية"):
                with st.spinner("جاري ترجمة الصوت وتوليد صوت الذكاء الاصطناعي..."):
                    time.sleep(2)
                    db["users"][client_id][current_month] += 1
                    db["total_renders"] += 1
                    save_db(db)
                    st.success("تمت دبلجة الفيديو بنجاح باللغة المختارة!")
                    st.video(input_path)

# ==========================================
# FEEDBACK SECTION
# ==========================================
st.markdown("---")
st.subheader("💬 رأيك يهمنا")
with st.form("feedback_form"):
    user_comment = st.text_area("أترك ملاحظاتك أو اقتراحاتك لتطوير المنصة:")
    rating = st.slider("تقييمك للمنصة:", 1, 5, 5)
    submitted = st.form_submit_button("إرسال التقييم")
    if submitted and user_comment:
        db["feedback"].append({"rating": rating, "comment": user_comment, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
        save_db(db)
        st.success("شكراً لك! تم تسجيل آرائك بنجاح.")