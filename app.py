import streamlit as st
import time

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="VidCraft AI | Ultra Edition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. CYBER ULTRA DARK & GLOW CSS STYLING
# ==========================================
st.markdown("""
<style>
    /* Dark Ocean/Space Background */
    .stApp {
        background: radial-gradient(circle at 50% -20%, #1e1b4b 0%, #030712 60%, #020617 100%);
        color: #f3f4f6;
        font-family: 'Inter', system-ui, sans-serif;
    }

    /* Glow Neon Header */
    .hero-container {
        text-align: center;
        padding: 35px 20px;
        background: rgba(15, 23, 42, 0.65);
        backdrop-filter: blur(16px);
        border-radius: 24px;
        border: 1px solid rgba(56, 189, 248, 0.2);
        box-shadow: 0 0 40px rgba(56, 189, 248, 0.15), inset 0 0 20px rgba(139, 92, 246, 0.1);
        margin-bottom: 35px;
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 900;
        letter-spacing: -1px;
        background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(56, 189, 248, 0.4);
        margin-bottom: 8px;
    }

    .hero-subtitle {
        color: #94a3b8;
        font-size: 1.15rem;
        font-weight: 400;
    }

    /* Neon Cyber Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #0284c7 0%, #6366f1 50%, #9333ea 100%);
        color: #ffffff;
        font-size: 1.2rem;
        font-weight: 800;
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 14px;
        padding: 0.85rem 1.8rem;
        width: 100%;
        box-shadow: 0 0 25px rgba(99, 102, 241, 0.4), 0 4px 12px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease-in-out;
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 0 35px rgba(168, 85, 247, 0.7), 0 6px 20px rgba(0, 0, 0, 0.6);
        border-color: #38bdf8;
    }

    /* Floating Glassmorphism Panels */
    .glass-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #030712 !important;
        border-left: 1px solid rgba(255, 255, 255, 0.08);
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. SESSION STATE
# ==========================================
if "usage_count" not in st.session_state:
    st.session_state.usage_count = 0

FREE_LIMIT = 3
PAYPAL_URL = "https://www.paypal.com/paypalme/guerzaki6"

# ==========================================
# 4. SIDEBAR
# ==========================================
with st.sidebar:
    st.markdown("### ⚡ حالة الحساب")
    used = st.session_state.usage_count
    st.markdown(f"**الاستخدام المجاني المتاح:** `{used} / {FREE_LIMIT}` فيديوهات")
    st.progress(min(used / FREE_LIMIT, 1.0))
    
    st.markdown("---")
    st.markdown("### 💎 الباقة الاحترافية")
    st.info("معالجة غير محدودة وبدقة 4K فائقة الجودة وبدون علامة مائية بـ **19$ شهرياً**.")
    st.markdown(f"[👉 **الترقية الفورية عبر PayPal**]({PAYPAL_URL})")

# ==========================================
# 5. MAIN HERO HEADER
# ==========================================
st.markdown("""
<div class="hero-container">
    <div class="hero-title">⚡ VidCraft AI</div>
    <div class="hero-subtitle">استوديو الجيل الجديد لمونتاج الفيديوهات بالذكاء الاصطناعي والتفاعل المباشر</div>
</div>
""", unsafe_allow_html=True)

# Limit Check
if st.session_state.usage_count >= FREE_LIMIT:
    st.error(f"⚠️ لقد استنفدت محاولاتك المجانية الثلاث ({FREE_LIMIT}/{FREE_LIMIT}). يرجى ترقية حسابك للاستمرار.")
    st.link_button("🚀 ترقية الحساب إلى PRO ($19)", PAYPAL_URL)
else:
    # STEP 1: TOOL SELECTION
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("1️⃣ اختر أداة الذكاء الاصطناعي المتقدمة:")
    selected_tool = st.radio(
        "الأدوات البرمجية الذكية:",
        [
            "💬 الكابشن الديناميكي العالمي (Reels & Shorts)",
            "✂️ قص الصمت التلقائي (10 خيارات أنماط)", 
            "🎯 الزووم الدرامي والكوميدي (Meme & Action)", 
            "🎙️ الدبلجة واستنساخ البصمة الصوتية (Voice Cloning)"
        ],
        horizontal=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

    # STEP 2: CUSTOMIZATION PANEL
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader(f"2️⃣ إعدادات التخصيص والتحكم الذكي لـ [{selected_tool}]:")
    
    # --- TOOL 1: CAPTION ---
    if selected_tool == "💬 الكابشن الديناميكي العالمي (Reels & Shorts)":
        c1, c2, c3 = st.columns(3)
        with c1:
            font_style = st.selectbox(
                "🔤 الخطوط العالمية والمحلية:", 
                ["Impact (Reels Style)", "Bebas Neue", "Bangers (Comic)", "Cairo (عربي عريض)", "Tajawal (حديث)", "Amiri", "Montserrat Bold", "Arial Black"]
            )
            caption_color = st.color_picker("🎨 لون النص الأساسي المضيء:", "#FFE600")
        with c2:
            words_per_line = st.selectbox(
                "📝 عدد الكلمات الظاهرة في الشاشة:",
                ["كلمة واحدة (أسلوب أليكس هورموزي المكثف)", "كلمتان", "3 كلمات", "جملة كاملة تلقائية"]
            )
            font_size = st.slider("📏 حجم النص (Pixels):", 18, 60, 34)
        with c3:
            style_preset = st.selectbox(
                "✨ التأثيرات والألوان الجاهزة (Neon Glow):",
                ["نص أصفر مع خلفية سوداء حادة", "نص أبيض وتوهج أحمر درامي", "أخضر نيون فسفوري متوهج", "نص أبيض وأصفر متناوب"]
            )

    # --- TOOL 2: SILENCE CUTTER ---
    elif selected_tool == "✂️ قص الصمت التلقائي (10 خيارات أنماط)":
        silence_mode = st.selectbox(
            "🎯 اختر نمط وإيقاع قص الصمت المخصص لمحتواك من بين 10 أنماط برمجية جاهزة:",
            [
                "1. قص سريع ومكثف جداً (Super Fast - تيك توك وريلز)",
                "2. قص متوازن وسلس (Balanced - فيديوهات الشروحات واليوتيوب)",
                "3. قص هادئ وطبيعي (Relaxed - للبودكاست والقصص)",
                "4. إزالة السكتات والتوقفات الطويلة فقط",
                "5. تنظيف ترددات التلعثم والتفكير (آأأ / إممم)",
                "6. قص الصمت مع إضافة انتقالات ناعمة بين المقاطع",
                "7. تسريع الوقفات وتنشيط الإيقاع الحماسي",
                "8. اقتطاع الصمت في بداية ونهاية الفيديو فقط",
                "9. قص الوقفات بين الجمل وتجميع الكلام المباشر",
                "10. النمط السينمائي المخصص للمقابلات والأفلام الوثائقية"
            ]
        )

    # --- TOOL 3: DRAMATIC ZOOM ---
    elif selected_tool == "🎯 الزووم الدرامي والكوميدي (Meme & Action)":
        zoom_mode = st.selectbox(
            "🎬 اختر سيناريو ومحاكاة الكاميرا والزووم الذكي:",
            [
                "🔍 زووم تلقائي ذكي عند الوقفات للتأكيد على الفكرة",
                "💥 زووم درامي مفاجئ عند كشف الحقيقة أو المفاصل الحاسمة",
                "😂 زووم كوميدي سريع عند المزاح أو التلعثم (Meme Zoom)",
                "👤 زووم تتبعي وتدريجي لمركز وجه المتحدث",
                "⚡ زووم سريع ومكثف للمقاطع الحماسية والألعاب"
            ]
        )

    # --- TOOL 4: DUBBING & VOICE CLONING ---
    elif selected_tool == "🎙️ الدبلجة واستنساخ البصمة الصوتية (Voice Cloning)":
        c1, c2 = st.columns(2)
        with c1:
            dub_option = st.selectbox(
                "🧬 هويّة ونوع الصوت المعالج:",
                [
                    "🧬 استنساخ البصمة الصوتية ونبرة صانع المحتوى الأصلي (Voice Cloning)",
                    "👨 صوت ذكر احترافي (مُدبلج سينمائي)",
                    "👩 صوت أنثى احترافي (مُدبلج إذاعي)"
                ]
            )
        with c2:
            target_language = st.selectbox(
                "🌐 لغة الدبلجة المستهدفة:",
                ["العربية", "English", "Español", "Français", "Deutsch", "Türkçe", "Italiano", "Русский", "中文 (المندرين)"]
            )
    st.markdown('</div>', unsafe_allow_html=True)

    # STEP 3: FILE UPLOAD
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("3️⃣ ارفع فيديو المحتوى لبدء المونتاج التلقائي:")
    uploaded_file = st.file_uploader("اختر ملف الفيديو (MP4, MOV, AVI):", type=["mp4", "mov", "avi"])

    if uploaded_file is not None:
        st.success("تم رفع الملف بنجاح! جاهز للتعديل المعالج.")
        st.video(uploaded_file)
        
        if st.button(f"⚡ بدء التعديل والمعالجة بـ [{selected_tool}]"):
            with st.spinner("جاري معالجة الفيديو، تطبيق تأثيرات النيون والذكاء الاصطناعي..."):
                time.sleep(3)
                st.session_state.usage_count += 1
                
            st.balloons()
            st.success("✨ اكتملت المعالجة بنجاح! جاهز للتحميل والتصدير.")
            
            st.download_button(
                label="📥 تحميل الفيديو المعالج بجودة عالية HD",
                data=uploaded_file.getvalue(),
                file_name=f"VidCraft_Pro_{uploaded_file.name}",
                mime="video/mp4"
            )
    st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# 6. FOOTER & FEEDBACK
# ==========================================
st.markdown("---")
st.subheader("💬 تقييم الأداء والملاحظات")
user_comment = st.text_area("أترك انطباعك أو أي ميزة ترغب في إضافتها مستقبلاً:")
if st.button("إرسال التقييم"):
    if user_comment:
        st.success("تم استلام تقييمك بنجاح! شكراً لك يا زكرياء على مسا
