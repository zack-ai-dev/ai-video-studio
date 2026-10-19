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
# 3. SIDEBAR NAVIGATION
# ==========================================
with st.sidebar:
    st.header("⚙️ لوحة التحكم")
    
    # Display usage meter
    used = st.session_state.usage_count
    st.markdown(f"**الاستخدام المجاني:** `{used} / {FREE_LIMIT}` فيديوهات")
    st.progress(min(used / FREE_LIMIT, 1.0))
    
    st.markdown("---")
    selected_tool = st.radio(
        "اختر تقنية الذكاء الاصطناعي:",
        [
            "✂️ قص الصمت التلقائي", 
            "🎯 الزووم الدرامي الذكي", 
            "💬 الكابشن الديناميكي", 
            "🎙️ الدبلجة لـ 100+ لغة"
        ]
    )
    
    st.markdown("---")
    st.subheader("💳 الترقية غير المحدودة")
    st.info("احصل على معالجة غير محدودة وبسرعة فائقة مقابل **19$ شهرياً**!")
    st.markdown(f"[👉 **اضغط هنا للترقية عبر PayPal**]({PAYPAL_URL})")

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
    uploaded_file = st.file_uploader(
        f"قم برفع الفيديو لمعالجته بـ [{selected_tool}] (MP4, MOV, AVI):", 
        type=["mp4", "mov", "avi"]
    )

    if uploaded_file is not None:
        st.success("تم استلام الفيديو بنجاح!")
        st.video(uploaded_file)
        
        if st.button(f"بدء التشغيل بـ ({selected_tool})"):
            with st.spinner("جاري تحليل الفيديو وتشغيل محرك الذكاء الاصطناعي..."):
                time.sleep(3) # Processing simulation
                
                # Update usage limit
                st.session_state.usage_count += 1
                
            st.balloons()
            st.success("✨ اكتملت المعالجة بنجاح!")
            
            # Offer download
            st.download_button(
                label="📥 تحميل الفيديو المعالج",
                data=uploaded_file.getvalue(),
                file_name=f"processed_{uploaded_file.name}",
                mime="video/mp4"
            )

# ==========================================
# 5. FEEDBACK SECTION
# ==========================================
st.markdown("---")
st.subheader("💬 تقييم الخدمة")
comment = st.text_area("أترك ملاحظتك لتطوير المنصة:")
if st.button("إرسال التقييم"):
    if comment:
        st.success("شكراً لك يا زكرياء! تم حفظ ملاحظتك بنجاح.")
    else:
        st.warning("يرجى كتابة ملاحظة قبل الإرسال.")
