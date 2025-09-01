import streamlit as st

# ---------------------
# 頁面基本設定
# ---------------------
# 修改頁面標題設定
st.set_page_config(
    page_title="Tasksnap App Official Website",
    page_icon="🏠",
    layout="wide"
)

# ---------------------
# 自訂 CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    @keyframes glow {
        0% { box-shadow: 0 0 20px rgba(255,153,0,0.3), 0 15px 50px rgba(0,0,0,0.2); }
        50% { box-shadow: 0 0 40px rgba(255,153,0,0.6), 0 20px 60px rgba(0,0,0,0.3); }
        100% { box-shadow: 0 0 20px rgba(255,153,0,0.3), 0 15px 50px rgba(0,0,0,0.2); }
    }
    @keyframes slideUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .hero {
        background: 
            linear-gradient(135deg, rgba(0,51,102,0.95), rgba(0,85,165,0.9), rgba(255,153,0,0.1)),
            url('https://images.unsplash.com/photo-1499914485622-a88fac536970?w=1200&auto=format&fit=crop&q=60') center/cover no-repeat;
        padding: 100px 40px;
        border-radius: 25px;
        color: #ffffff;
        text-align: center;
        margin-bottom: 50px;
        box-shadow: 0 25px 80px rgba(0,0,0,0.25), 0 0 50px rgba(255,153,0,0.2);
        position: relative;
        overflow: hidden;
        animation: glow 3s ease-in-out infinite;
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shine 4s ease-in-out infinite;
        transform: rotate(45deg);
    }
    @keyframes shine {
        0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
        50% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        100% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
    }
    .h1 {
        font-size: 68px;
        letter-spacing: 6px;
        font-weight: 900;
        margin-bottom: 0px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        background: linear-gradient(45deg, #FF9900, #FFD700, #FF6600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 0 30px rgba(255,153,0,0.5);
        animation: pulse 2s ease-in-out infinite;
    }
    .hero h2 {
        margin-top: 0px;
        margin-bottom: 20px;
        font-size: 36px;
        font-weight: 800;
        letter-spacing: 3px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 0 0 20px rgba(255,255,255,0.8), 2px 4px 15px rgba(0,0,0,0.3);
        animation: slideUp 1s ease-out 0.5s both;
    }
    .hero p {
        font-size: 24px;
        line-height: 1.9;
        max-width: 900px;
        margin: 0 auto;
        font-weight: 500;
        letter-spacing: 1.5px;
        text-shadow: 0 0 15px rgba(255,255,255,0.6), 2px 4px 12px rgba(0,0,0,0.2);
        animation: slideUp 1s ease-out 1s both;
    }
    .slogan {
        text-align: center;
        font-size: 36px;
        line-height: 1.8;
        margin: 48px 0 18px 0;
        color: #003366;
        letter-spacing: 2px;
        font-weight: bold;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .slogan-img {
        display: block;
        margin: 0 auto 32px auto;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        max-width: 220px;
    }
    .caption {
        text-align: center;
        font-size: 16px;
        color: #888;
        margin-top: 48px;
        letter-spacing: 1.5px;
    }
    .stats-card {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.15), 0 5px 15px rgba(0,85,165,0.1);
        padding: 40px 18px 30px 18px;
        text-align: center;
        margin: 12px 0;
        font-size: 26px;
        color: #003366;
        font-weight: 700;
        letter-spacing: 1.5px;
        border: 2px solid transparent;
        background-clip: padding-box;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }
    .stats-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0,85,165,0.15), rgba(255,153,0,0.15), transparent);
        transition: left 0.6s;
    }
    .stats-card:hover {
        transform: translateY(-10px) scale(1.05);
        box-shadow: 0 25px 60px rgba(0,51,102,0.2), 0 10px 25px rgba(0,85,165,0.4), 0 0 30px rgba(255,153,0,0.2);
        border-color: #0055A5;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .stats-card:hover::before {
        left: 100%;
    }
    .trust-card {
        background: linear-gradient(135deg, #f7faff, #ffffff);
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.12), 0 3px 10px rgba(0,85,165,0.1);
        padding: 28px 22px 22px 22px;
        margin: 15px 0;
        font-size: 18px;
        color: #222;
        font-weight: 500;
        border-left: 6px solid #0055A5;
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    .trust-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 0;
        height: 100%;
        background: linear-gradient(135deg, rgba(0,85,165,0.08), rgba(255,153,0,0.08), rgba(0,51,102,0.05));
        transition: width 0.4s ease;
    }
    .trust-card:hover {
        transform: translateX(8px) scale(1.02);
        box-shadow: 0 15px 45px rgba(0,51,102,0.15), 0 5px 15px rgba(0,85,165,0.3), 0 0 20px rgba(255,153,0,0.1);
        border-left-width: 8px;
        border-left-color: #003366;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .trust-card:hover::after {
        width: 100%;
    }
    .trust-card .author {
        font-size: 15px;
        color: #0055A5;
        margin-top: 8px;
        font-weight: 700;
    }
    .faq-card {
        background: linear-gradient(135deg, #ffffff, #fffbf5);
        border-radius: 18px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.1), 0 4px 12px rgba(255,153,0,0.1);
        padding: 28px 22px 22px 22px;
        margin: 18px 0;
        font-size: 18px;
        color: #003366;
        font-weight: 600;
        border-left: 6px solid #FF9900;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }
    .faq-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #FF9900, #FFD700, #FF6600);
        border-radius: 18px 18px 0 0;
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    .faq-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 50px rgba(0,51,102,0.12), 0 8px 20px rgba(255,153,0,0.25), 0 0 25px rgba(0,85,165,0.1);
        border-left-width: 8px;
    }
    .faq-card:hover::before {
        transform: scaleX(1);
    }
    .faq-q {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 8px;
        background: linear-gradient(45deg, #FF9900, #FF6600);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 2px 4px rgba(255,153,0,0.3);
    }
    .faq-a {
        font-size: 17px;
        color: #222;
        font-weight: 400;
    }
    .email-form {
        text-align: center;
        margin-top: 48px;
        margin-bottom: 12px;
    }
    body {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
    }
    h3 {
        font-weight: 800;
    }
    .stForm {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 2px solid rgba(255,153,0,0.2);
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    .stTextInput > div > div > input:focus {
        border-color: #FF9900;
        box-shadow: 0 0 15px rgba(255,153,0,0.3);
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF9900, #FF6600);
        border: none;
        border-radius: 10px;
        color: white;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(255,153,0,0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255,153,0,0.4);
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .step-card {
        transition: all 0.3s ease;
    }
    .step-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(0,0,0,0.15) !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# HERO BANNER
# ---------------------
# Hero Banner 區塊
st.markdown(
    '<h1 style="text-align:center; font-size:68px; letter-spacing:6px; font-weight:900; font-family:\'Arial\',\'Helvetica\',sans-serif; margin-bottom:12px; color:#003366;">Tasksnap</h1>',
    unsafe_allow_html=True
)

st.markdown("""
    <div class="hero">
        <h2>Next Generation Freelance Platform</h2>
        <p>A Secure Platform Built for Students<br>
        Combining Social Feed, Mini Games, Identity Verification & Legal Protection<br>
        Make Freelancing More Secure, Rewarding, and Fun!</p>
    </div>
""", unsafe_allow_html=True)

# ---------------------
# 合作或成果數字
# ---------------------
# 服務成果區塊
st.markdown('<div style="text-align:center; margin-top:48px; margin-bottom:36px;"><h3>Our Achievements</h3></div>', unsafe_allow_html=True)
stats1, stats2, stats3 = st.columns(3)
with stats1:
    st.markdown('<div class="stats-card"><span style="color:#FF9900;">120+</span><br>Successful Matches</div>', unsafe_allow_html=True)
with stats2:
    st.markdown('<div class="stats-card">Over <span style="color:#FF9900;">3000+</span><br>Student Users</div>', unsafe_allow_html=True)
with stats3:
    st.markdown('<div class="stats-card"><span style="color:#FF9900;">5000+</span><br>Tokens Distributed</div>', unsafe_allow_html=True)

# ---------------------
# 產品特色區塊
# ---------------------
st.markdown('<div style="text-align:center; margin-top:56px; margin-bottom:36px;"><h3>🌟 Why Choose Tasksnap?</h3></div>', unsafe_allow_html=True)
feature1, feature2, feature3, feature4 = st.columns(4)
with feature1:
    st.markdown('''
        <div style="text-align:center; padding:20px; background:linear-gradient(135deg, #ffffff, #f0f8ff); border-radius:15px; box-shadow:0 8px 25px rgba(0,0,0,0.08); margin:10px 0;">
            <div style="font-size:40px; margin-bottom:10px;">🛡️</div>
            <div style="font-size:18px; font-weight:700; color:#003366; margin-bottom:8px;">Security</div>
            <div style="font-size:14px; color:#666;">ID Verification<br>Contract Protection</div>
        </div>
    ''', unsafe_allow_html=True)
with feature2:
    st.markdown('''
        <div style="text-align:center; padding:20px; background:linear-gradient(135deg, #ffffff, #fff8f0); border-radius:15px; box-shadow:0 8px 25px rgba(0,0,0,0.08); margin:10px 0;">
            <div style="font-size:40px; margin-bottom:10px;">⚡</div>
            <div style="font-size:18px; font-weight:700; color:#003366; margin-bottom:8px;">Quick Matching</div>
            <div style="font-size:14px; color:#666;">AI Smart Matching<br>Instant Notifications</div>
        </div>
    ''', unsafe_allow_html=True)
with feature3:
    st.markdown('''
        <div style="text-align:center; padding:20px; background:linear-gradient(135deg, #ffffff, #f0fff0); border-radius:15px; box-shadow:0 8px 25px rgba(0,0,0,0.08); margin:10px 0;">
            <div style="font-size:40px; margin-bottom:10px;">🎮</div>
            <div style="font-size:18px; font-weight:700; color:#003366; margin-bottom:8px;">Fun Interaction</div>
            <div style="font-size:14px; color:#666;">Mini Games for Tokens<br>Social Feed</div>
        </div>
    ''', unsafe_allow_html=True)
with feature4:
    st.markdown('''
        <div style="text-align:center; padding:20px; background:linear-gradient(135deg, #ffffff, #fff0f5); border-radius:15px; box-shadow:0 8px 25px rgba(0,0,0,0.08); margin:10px 0;">
            <div style="font-size:40px; margin-bottom:10px;">💰</div>
            <div style="font-size:18px; font-weight:700; color:#003366; margin-bottom:8px;">Transparent Fees</div>
            <div style="font-size:14px; color:#666;">No Hidden Fees<br>Clear and Transparent</div>
        </div>
    ''', unsafe_allow_html=True)

# ---------------------
# 使用流程區塊
# ---------------------
st.markdown('<div style="text-align:center; margin-top:56px; margin-bottom:36px;"><h3>📋 How It Works</h3></div>', unsafe_allow_html=True)
step1, step2, step3, step4 = st.columns(4)
with step1:
    st.markdown('''
        <div class="step-card" style="text-align:center; padding:25px 15px; background:linear-gradient(135deg, #e3f2fd, #ffffff); border-radius:20px; box-shadow:0 10px 30px rgba(0,85,165,0.1); margin:10px 0; position:relative;">
            <div style="position:absolute; top:-15px; left:50%; transform:translateX(-50%); background:#0055A5; color:white; width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700;">1</div>
            <div style="font-size:35px; margin:15px 0 10px 0;">📝</div>
            <div style="font-size:16px; font-weight:700; color:#003366; margin-bottom:8px;">Sign Up & Verify</div>
            <div style="font-size:13px; color:#666;">Complete ID Verification<br>Create Your Profile</div>
        </div>
    ''', unsafe_allow_html=True)
with step2:
    st.markdown('''
        <div class="step-card" style="text-align:center; padding:25px 15px; background:linear-gradient(135deg, #fff3e0, #ffffff); border-radius:20px; box-shadow:0 10px 30px rgba(255,153,0,0.1); margin:10px 0; position:relative;">
            <div style="position:absolute; top:-15px; left:50%; transform:translateX(-50%); background:#FF9900; color:white; width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700;">2</div>
            <div style="font-size:35px; margin:15px 0 10px 0;">🔍</div>
            <div style="font-size:16px; font-weight:700; color:#003366; margin-bottom:8px;">Find Tasks</div>
            <div style="font-size:13px; color:#666;">Browse Available Projects<br>or Post Your Requirements</div>
        </div>
    ''', unsafe_allow_html=True)
with step3:
    st.markdown('''
        <div class="step-card" style="text-align:center; padding:25px 15px; background:linear-gradient(135deg, #e8f5e8, #ffffff); border-radius:20px; box-shadow:0 10px 30px rgba(76,175,80,0.1); margin:10px 0; position:relative;">
            <div style="position:absolute; top:-15px; left:50%; transform:translateX(-50%); background:#4CAF50; color:white; width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700;">3</div>
            <div style="font-size:35px; margin:15px 0 10px 0;">🤝</div>
            <div style="font-size:16px; font-weight:700; color:#003366; margin-bottom:8px;">Start Collaborating</div>
            <div style="font-size:13px; color:#666;">Agree on Terms<br>Sign Digital Contract</div>
        </div>
    ''', unsafe_allow_html=True)
with step4:
    st.markdown('''
        <div class="step-card" style="text-align:center; padding:25px 15px; background:linear-gradient(135deg, #fce4ec, #ffffff); border-radius:20px; box-shadow:0 10px 30px rgba(233,30,99,0.1); margin:10px 0; position:relative;">
            <div style="position:absolute; top:-15px; left:50%; transform:translateX(-50%); background:#E91E63; color:white; width:30px; height:30px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700;">4</div>
            <div style="font-size:35px; margin:15px 0 10px 0;">💎</div>
            <div style="font-size:16px; font-weight:700; color:#003366; margin-bottom:8px;">Get Paid</div>
            <div style="font-size:13px; color:#666;">Secure Payment Processing<br>Earn Token Rewards</div>
        </div>
    ''', unsafe_allow_html=True)

# ---------------------
# 信任區塊（合作單位/用戶好評）
# ---------------------
# 用戶評價
st.markdown('<div style="text-align:center; margin-top:56px; margin-bottom:36px;"><h3>User Reviews</h3></div>', unsafe_allow_html=True)
trust1, trust2, trust3 = st.columns(3)
with trust1:
    st.markdown('<div class="trust-card">"Super secure platform for my first freelance job!"<div class="author">— John, Computer Science Junior</div></div>', unsafe_allow_html=True)
with trust2:
    st.markdown('<div class="trust-card">"Smooth verification process and great collaboration!"<div class="author">— Emma, Design Sophomore</div></div>', unsafe_allow_html=True)
with trust3:
    st.markdown('<div class="trust-card">"Love earning tokens through mini games!"<div class="author">— Mike, Business Senior</div></div>', unsafe_allow_html=True)

# ---------------------
# FAQ 常見問題區塊
# ---------------------
# FAQ 區塊
st.markdown('<div style="text-align:center; margin-top:56px; margin-bottom:36px;"><h3>FAQ</h3></div>', unsafe_allow_html=True)
faq_data = [
    {
        "q": "Why verify identity?",
        "a": "To ensure safety and trust, we verify all users are real students or clients."
    },
    {
        "q": "What if I don't get paid?",
        "a": "Our escrow system and contracts protect all transactions. Support team handles disputes."
    },
    {
        "q": "How to use tokens?",
        "a": "Earn tokens from tasks and activities, redeem for merchant discounts or gifts."
    },
    {
        "q": "Can beginners join?",
        "a": "Absolutely! We offer tutorials and starter tasks to help you succeed."
    }
]
for faq in faq_data:
    st.markdown(f'''
        <div class="faq-card" style="text-align:center;">
            <div class="faq-q">{faq["q"]}</div>
            <div class="faq-a">{faq["a"]}</div>
        </div>
    ''', unsafe_allow_html=True)

# ---------------------
# 訂閱/聯絡表單
# ---------------------
# 訂閱表單
st.markdown('<div class="email-form" style="text-align:center;"><b>Get Latest Updates! 📧</b></div>', unsafe_allow_html=True)
with st.form("email_form", clear_on_submit=True):
    email = st.text_input("Email", label_visibility="collapsed", placeholder="Enter your email")
    submitted = st.form_submit_button("Subscribe")
    if submitted and email:
        st.success("Thanks for subscribing! We'll keep you updated.")

st.write("---")

# ---------------------
# 合作夥伴區塊
# ---------------------
st.markdown('<div style="text-align:center; margin-top:56px; margin-bottom:36px;"><h3>🤝 Our Partners</h3></div>', unsafe_allow_html=True)
st.markdown('''
    <div style="text-align:center; padding:30px; background:linear-gradient(135deg, #ffffff, #f8fbff); border-radius:20px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:20px 0;">
        <div style="display:flex; justify-content:center; align-items:center; flex-wrap:wrap; gap:40px;">
            <div style="padding:15px 25px; background:#f0f8ff; border-radius:10px; font-weight:600; color:#0055A5;">🏫 台X大學</div>
            <div style="padding:15px 25px; background:#fff8f0; border-radius:10px; font-weight:600; color:#FF9900;">🏫 政X大學</div>
            <div style="padding:15px 25px; background:#f0fff0; border-radius:10px; font-weight:600; color:#4CAF50;">🏫 清X大學</div>
            <div style="padding:15px 25px; background:#fff0f5; border-radius:10px; font-weight:600; color:#E91E63;">🏫 交X大學</div>
        </div>
        <div style="margin-top:20px; font-size:14px; color:#666;">Cooperate with many well-known universities in Taiwan to provide students with a safe environment for receiving cases</div>
    </div>
''', unsafe_allow_html=True)

# ---------------------
# 頁尾
# ---------------------
st.markdown('<div class="caption" style="text-align:center;">© 2025 Tasksnap App | All Rights Reserved</div>', unsafe_allow_html=True)
