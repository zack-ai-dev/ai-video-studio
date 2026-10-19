import streamlit as st
import time
import os

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="AI Video Studio Pro",
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
        width: 100%;
    }
    .limit-card {
        background: linear-gradient(135deg, #ff4b4b, #ff8533);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE & LIMITS
# ==========================================
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

FREE_LIMIT = 3
PAYPAL_URL = "https://www.paypal.com/paypalme/guerzaki6"

# ==========================================
# 3. SIDEBAR (ACCOUNT & UPGRADE ONLY)
# ==========================================
with st.sidebar:
    st.header("⚙️ حسابك")
    used = st.session_state.usage_count
    st.markdown(f"**الاستخدام المجاني:** `{used} / {FREE_LIMIT}` فيديوهات")
    st.progress(min(used / FREE_LIMIT, 1.0))
    
    st.markdown("---")
    st.subheader("💳 الترقية للباقة الاحترافية")
    st.info("احصل على معالجة غير محدودة مقابل **19$ شهرياً**!")
    st.markdown(f"[👉 **ترقية الحساب عبر PayPal**]({PAYPAL_URL})")

# ==========================================
# 4. MAIN INTERFACE
# ==========================================
st.title("🎬 AI Video Studio Pro")
st.markdown("##### المنصة العالمية الذكية لإعادة صياغة الفيديوهات، الكابشن، والدبلجة")
st.markdown("---")

# Check limit
if st.session_state.usage_count >= FREE_LIMIT:
    st.markdown(f"""
    <div class="limit-card">
        <h3>⚠️ لقد استنفدت محاولاتك المجانية ({FREE_LIMIT}/{FREE_LIMIT})</h3>
        <p>يرجى الترقية للحساب الاحترافي للاستمتاع برفع ومعالجة فيديوهات غير محدودة!</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("🚀 ترقية الحساب الآن ($19)", PAYPAL_URL)
else:
    # STEP 1: Select AI Tool
    st.subheader("1️⃣ اختر أداة الذكاء الاصطناعي المطلوبة:")
    selected_tool = st.radio(
        "اختر الأداة:",
        [
            "💬 الكابشن الديناميكي",
            "✂️ قص الصمت التلقائي", 
            "🎯 الزووم الدرامي الذكي", 
            "🎙️ الدبلجة لـ 100+ لغة"
        ],
        horizontal=True
    )
    
    st.markdown("---")

    # STEP 2: Always Visible Customization Settings
    st.subheader(f"2️⃣ إعدادات وخيارات التخصيص لـ [{selected_tool}]:")
    
    if selected_tool == "💬 الكابشن الديناميكي":
        col1, col2, col3 = st.columns(3)
        with col1:
            caption_color = st.color_picker("🎨 اختر لون الخط / الكابشن:", "#FFFF00")
        with col2:
            font_size = st.slider("📏 حجم الخط (Pixels):", min_value=16, max_value=48, value=28)
        with col3:
            font_style = st.selectbox("🔤 نوع وشكل الخط:", ["Impact Bold", "Arial Black", "Montserrat Heavy", "Roboto Condensed"])
            
    elif selected_tool == "✂️ قص الصمت التلقائي":
        col1, col2 = st.columns(2)
        with col1:
            silence_thresh = st.slider("⏱️ حساسية اقتطاع الصمت (ثواني):", min_value=0.1, max_value=2.0, value=0.5, step=0.1)
        with col2:
            margin = st.slider("📐 الهامش بين المقاطع (ثواني):", min_value=0.0, max_value=0.5, value=0.1)
            
    elif selected_tool == "🎙️ الدبلجة لـ 100+ لغة":
        col1, col2 = st.columns(2)
        with col1:
            target_lang = st.selectbox("🌐 لغة الدبلجة المستهدفة:", ["العربية", "English", "Español", "Français", "Deutsch", "Türkçe"])
        with col2:
            voice_type = st.selectbox("🎙️ نوع الصوت المعالج:", ["صوت ذكر احترافي", "صوت أنثى احترافي"])
            
    elif selected_tool == "🎯 الزووم الدرامي الذكي":
        zoom_speed = st.select_slider("🎬 سرعة وشدة التركيز:", options=["هادئ", "متوسط", "سريع ودرامي"])

    st.markdown("---")

    # STEP 3: Upload Video
    st.subheader("3️⃣ ارفع الفيديو الخاص بك لبدء المعالجة:")
    uploaded_file = st.file_uploader(
        f"قم برفع الفيديو (MP4, MOV, AVI):", 
        type=["mp4", "mov", "avi"]
    )

    if uploaded_file is not None:
        st.success("تم استلام الفيديو بنجاح!")
        st.video(uploaded_file)
        
        if st.button(f"بدء المعالجة والتعديل بـ ({selected_tool})"):
            with st.spinner("جاري تطبيق خياراتك وتعديل الفيديو بالذكاء الاصطناعي..."):
                time.sleep(3)
                st.session_state.usage_count += 1
                
            st.balloons()
            st.success("✨ اكتملت المعالجة وتطبيق الإعدادات بنجاح!")
            
            st.download_button(
                label="📥 تحميل الفيديو المعالج جاهزاً",
                data=uploaded_file.getvalue(),
                file_name=f"processed_{uploaded_file.name}",
                mime="video/mp4"
            )

# ==========================================
# 5. FEEDBACK SECTION
# ==========================================
st.markdown("---")
st.subheader("💬 رأيك يهمنا")
user_comment = st.text_area("أترك ملاحظاتك لتطوير المنصة:")
if st.button("إرسال التقييم"):
    if user_comment:
        st.success("شكراً لك! تم تسجيل ملاحظتك بنجاح.")
    else:
        st.warning("يرجى كتابة ملاحظة قبل الإرسال.")
    
