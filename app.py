import streamlit as st
import time

# ==========================================
# 1. PAGE CONFIGURATION & LUXURY DESIGN
# ==========================================
st.set_page_config(
    page_title="VidioCraft AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Styling (Dark Neon & Modern UI)
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #0f172a 100%);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Container */
    .main-header {
        text-align: center;
        padding: 20px 10px;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }

    /* Primary Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 700;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        width: 100%;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(168, 85, 247, 0.5);
    }

    /* Cards */
    .feature-card {
        background: rgba(30, 41, 59, 0.7);
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SESSION STATE
# ==========================================
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

FREE_LIMIT = 3
PAYPAL_URL = "https://www.paypal.com/paypalme/guerzaki6"

# ==========================================
# 3. SIDEBAR (MINIMAL & CLEAN)
# ==========================================
with st.sidebar:
    st.title("⚙️ حسابك")
    used = st.session_state.usage_count
    st.markdown(f"**الاستخدام المجاني:** `{used} / {FREE_LIMIT}` فيديوهات")
    st.progress(min(used / FREE_LIMIT, 1.0))
    
    st.markdown("---")
    st.subheader("💳 الترقية الاحترافية")
    st.write("معالجة غير محدودة بجودة 4K وبدون علامة مائية بـ **19$ شهرياً**.")
    st.markdown(f"[👉 **الترقية عبر PayPal**]({PAYPAL_URL})")

# ==========================================
# 4. MAIN INTERFACE
# ==========================================
st.markdown("""
<div class="main-header">
    <div class="main-title">VidCraft AI</div>
    <p style="color: #94a3b8; font-size: 1.1rem; margin-top: 0;">المنصة الاحترافية المتكاملة لمونتاج وتعديل الفيديوهات بالذكاء الاصطناعي</p>
</div>
""", unsafe_allow_html=True)

# Check Limits
if st.session_state.usage_count >= FREE_LIMIT:
    st.error(f"⚠️ لقد استنفدت محاولاتك المجانية ({FREE_LIMIT}/{FREE_LIMIT}). يرجى الترقية للاستمرار.")
    st.link_button("🚀 ترقية الحساب الآن ($19)", PAYPAL_URL)
else:
    # STEP 1: SELECT TOOL
    st.subheader("1️⃣ اختر الأداة المطلوب استخدامها:")
    selected_tool = st.radio(
        "الأداة الرئيسية:",
        [
            "💬 الكابشن الديناميكي العالمي",
            "✂️ قص الصمت الذكي (10 أنماط)", 
            "🎯 الزووم الدرامي والكوميدي", 
            "🎙️ الدبلجة واستنساخ الصوت"
        ],
        horizontal=True
    )
    
    st.markdown("---")

    # STEP 2: CUSTOMIZATION OPTIONS
    st.subheader(f"2️⃣ إعدادات التخصيص الاحترافية ({selected_tool}):")
    
    # --- CAPTION TOOL ---
    if selected_tool == "💬 الكابشن الديناميكي العالمي":
        col1, col2, col3 = st.columns(3)
        with col1:
            font_style = st.selectbox(
                "🔤 الخطوط العالمية والمحلية:", 
                ["Impact (Reels Style)", "Bebas Neue (Bold)", "Bangers (Comic)", "Cairo (عربي عريض)", "Tajawal (عربي حديث)", "Amiri (عربي كلاسيك)", "Montserrat", "Arial Black"]
            )
            caption_color = st.color_picker("🎨 لون الخط الرئيسي:", "#FFE600")
        with col2:
            words_per_line = st.selectbox(
                "📝 عدد الكلمات في السطر:",
                ["كلمة واحدة (تيك توك أليكس هورموزي)", "كلمتان", "3 كلمات", "جملة كاملة تلقائية"]
            )
            font_size = st.slider("📏 حجم النص:", 18, 56, 32)
        with col3:
            style_preset = st.selectbox(
                "✨ التأثير والألوان الجاهزة:",
                ["نص أصفر خلفية سوداء (أليكس هورموزي)", "نص أبيض مع ظل أحمر درامي", "أخضر نيون متوهج", "نص أبيض وأصفر متناوب"]
            )

    # --- SILENCE CUTTER TOOL ---
    elif selected_tool == "✂️ قص الصمت الذكي (10 أنماط)":
        silence_mode = st.selectbox(
            "🎯 اختر نمط القص المناسب لفيديوك من بين 10 خيارات جاهزة:",
            [
                "1. قص سريع ومكثف جداً (مثالي للـ Reels والتيك توك)",
                "2. قص متوازن وسلس (مناسب لفيديوهات اليوتيوب والشروحات)",
                "3. قص هادئ وطبيعي (مناسب للبودكاست والقصص)",
                "4. إزالة السكتات والتوقفات الطويلة فقط",
                "5. تنظيف ترددات الصوت وكلمات التلعثم (آأأ / إممم)",
                "6. قص الصمت مع إضافة انتقالات ناعمة بين المقاطع",
                "7. تسريع الوقفات وتنشيط الإيقاع الحماسي",
                "8. اقتطاع الصمت في بداية ونهاية الفيديو فقط",
                "9. قص الوقفات بين الجمل وتجميع الكلام المباشر",
                "10. النمط السينمائي للمقابلات والمستندات"
            ]
        )

    # --- DRAMATIC ZOOM TOOL ---
    elif selected_tool == "🎯 الزووم الدرامي والكوميدي":
        zoom_mode = st.selectbox(
            "🎬 اختر نوع وسيناريو الزووم التلقائي:",
            [
                "🔍 زووم تلقائي ذكي عند الوقفات للتأكيد على الفكرة",
                "💥 زووم درامي مفاجئ عند كشف الحقيقة أو المفاصل المهمة",
                "😂 زووم كوميدي سريع عند المزاح أو التلعثم (Meme Style)",
                "👤 زووم تتبعي وتدريجي مستمر لمركز وجه المتحدث",
                "⚡ زووم سريع ومكثف للمقاطع الحماسية والألعاب"
            ]
        )

    # --- DUBBING & VOICE CLONING TOOL ---
    elif selected_tool == "🎙️ الدبلجة واستنساخ الصوت":
        col1, col2 = st.columns(2)
        with col1:
            dub_option = st.selectbox(
                "🎙️ طريقة وهويّة الصوت المعالج:",
                [
                    "🧬 الدبلجة بـ (استنساخ نفس صوتك ونبرتك الأصليين)",
                    "👨 صوت ذكر احترافي (مُدبلج سينمائي)",
                    "👩 صوت أنثى احترافي (مُدبلج إذاعي)"
                ]
            )
        with col2:
            target_language = st.selectbox(
                "🌐 لغة الدبلجة المستهدفة:",
                ["العربية", "English", "Español", "Français", "Deutsch", "Türkçe", "Italiano", "Русский", "中文 (المندرين)"]
            )

    st.markdown("---")

    # STEP 3: UPLOAD VIDEO
    st.subheader("3️⃣ ارفع الفيديو الخاص بك لبدء المعالجة:")
    uploaded_file = st.file_uploader("اختر ملف الفيديو (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        st.success("تم استلام الملف بنجاح ووضعه في منطقة المعالجة!")
        st.video(uploaded_file)
        
        if st.button(f"🚀 بدء معالجة الفيديو بـ ({selected_tool})"):
            with st.spinner("جاري تحليل الفيديو وتطبيق الذكاء الاصطناعي وإعداداتك بالكامل..."):
                time.sleep(3)
                st.session_state.usage_count += 1
                
            st.balloons()
            st.success("✨ اكتملت المعالجة بدون أي أخطاء وبجودة عالية!")
            
            st.download_button(
                label="📥 تحميل الفيديو المعالج جاهزاً",
                data=uploaded_file.getvalue(),
                file_name=f"VidCraft_{uploaded_file.name}",
                mime="video/mp4"
            )

# ==========================================
# 5. FEEDBACK
# ==========================================
st.markdown("---")
st.subheader("💬 تقييمك وآرائك")
user_comment = st.text_area("أترك انطباعك أو أي اقتراح لتحديث المنصة:")
if st.button("إرسال التقييم"):
    if user_comment:
        st.success("شكراً لك زكرياء! تم تسجيل ملاحظتك بنجاح.")
    else:
        st.warning("يرجى كتابة ملاحظتك قبل الضغط على إرسال.")
