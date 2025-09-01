import streamlit as st

# ---------------------
# Page Settings
# ---------------------
st.set_page_config(
    page_title="App Features｜Tasksnap",
    page_icon="🛠️",
    layout="wide"
)

# ---------------------
# Custom CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    @keyframes glow {
        0% { box-shadow: 0 0 10px rgba(0,85,165,0.2); }
        50% { box-shadow: 0 0 25px rgba(0,85,165,0.4), 0 0 35px rgba(255,153,0,0.2); }
        100% { box-shadow: 0 0 10px rgba(0,85,165,0.2); }
    }
    body {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
    }
    .center-title {
        text-align: center;
        color: #003366;
        font-size: 52px;
        font-weight: 900;
        letter-spacing: 3px;
        margin-bottom: 18px;
        margin-top: 18px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.10);
    }
    .feature-title {
        text-align: center;
        font-size: 34px;
        font-weight: 900;
        color: #0055A5;
        margin-bottom: 12px;
        margin-top: 38px;
        letter-spacing: 2px;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .center-section {
        text-align: center;
        font-size: 24px;
        color: #234;
        margin-bottom: 40px;
        margin-top: 20px;
        font-weight: 500;
        line-height: 1.9;
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08), 0 3px 10px rgba(0,85,165,0.1);
        border-left: 5px solid #FF9900;
        animation: fadeInUp 1s ease-out 0.3s both;
    }
    .center-img-caption {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 8px;
        width: 100%;
        max-width: 95vw;   /* Responsive width */
    }

    @media (max-width: 600px) {
        .center-img-caption {
            max-width: 100vw; /* Full width on small screens */
            padding: 0 4vw;
        }
        .center-img-caption img {
            max-width: 100%;
            width: 100%;
        }
    }
    .center-img-caption img {
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.15), 0 5px 15px rgba(0,85,165,0.2);
        margin-bottom: 12px;
        max-width: 100%;
        width: 100%;
        height: auto;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 3px solid transparent;
        background-clip: padding-box;
    }
    .center-img-caption img:hover {
        transform: translateY(-8px) scale(1.03);
        box-shadow: 0 25px 60px rgba(0,0,0,0.2), 0 10px 25px rgba(0,85,165,0.3), 0 0 30px rgba(255,153,0,0.2);
        border-color: #FF9900;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .img-caption-text {
        font-size: 18px;
        background: linear-gradient(45deg, #0055A5, #003366);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        margin-top: 8px;
        letter-spacing: 1.5px;
        text-align: center;
        text-shadow: 0 2px 4px rgba(0,85,165,0.2);
    }
    .divider {
        border: none;
        border-top: 2px solid #e0e7ef;
        margin: 40px 0 32px 0;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 48px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# Title
# ---------------------
st.markdown("<div class='center-title'>🛠️ App Features</div>", unsafe_allow_html=True)
st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# Feature: Dynamic Wall
# ---------------------
st.markdown("<div class='feature-title'>📢 Dynamic Wall</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
Users can publish posts, leave comments, and give likes, similar to a campus version of Dcard/Threads,<br>
instantly sharing freelancing experiences and discussing everyday life, creating an active campus community.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("動態牆- 重做UI-追蹤主題.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Following - Home UI</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("動態牆- 查看匿名貼文.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>View Post</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("動態牆- 各主題.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Browse Topics</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# Feature: Mini-Games Module
# ---------------------
st.markdown("<div class='feature-title'>🎮 Mini-Games<br>App Store</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
Built-in fun and easy mini-games allow students to relax in their spare time,<br>
and also earn tokens that can be used to redeem virtual items within the software or discounts from partner merchants,<br>
increasing user engagement and interactivity!
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("遊戲-主ui.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Game Home</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("遊戲- intro.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Game Introduction</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("代幣兌換首頁.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Token Exchange</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# Feature: Freelance / Propose
# ---------------------
st.markdown("<div class='feature-title'>🤝 Freelance / Propose</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
Inspired by the Uber model, the platform offers a two-way system for freelancing:<br>
freelancers can receive officially matched tasks, and clients can post their needs to find suitable talent.<br>
Identity verification and breach of contract clauses are in place to protect the rights of both parties.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("接案者模式 - 首頁UI.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Freelancer Mode Home</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("發案者模式已刊登 - 首頁UI.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Client Mode Home</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("發案者模式已刊登 - 首頁UI.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Browse Freelancer Profile</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# Feature: Instant Messaging
# ---------------------
st.markdown("<div class='feature-title'>💬 Instant Messaging<br>Chat Room</div>", unsafe_allow_html=True)
st.markdown("""
<div class='center-section'>
The real-time chat room function allows for quick communication between freelancers and clients or friends,<br>
and also provides an official notification channel to ensure that every transaction process is clear and transparent,<br>
reducing misunderstandings and increasing user trust.
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("訊息-主ui.png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Messages Home</div></div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("訊息聊天室(線上).png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Chat Room (Online)</div></div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='center-img-caption'>", unsafe_allow_html=True)
    st.image("訊息聊天室(未在線上).png", use_container_width=True)
    st.markdown("<div class='img-caption-text'>Chat Room (Offline)</div></div>", unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# Technical Specifications Block
# ---------------------
st.markdown("<div class='feature-title'>💻 Technical Specifications</div>", unsafe_allow_html=True)
tech1, tech2 = st.columns(2)
with tech1:
    st.markdown("""
    <div style="background:linear-gradient(135deg, #ffffff, #f0f8ff); padding:25px; border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <h4 style="color:#0055A5; margin-bottom:15px;">📱 Supported Platforms</h4>
        <ul style="color:#234; line-height:1.8;">
            <li>iOS 12.0 and above</li>
            <li>Android 8.0 and above</li>
            <li>Web Version (all major browsers)</li>
            <li>PWA Support</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with tech2:
    st.markdown("""
    <div style="background:linear-gradient(135deg, #ffffff, #fff8f0); padding:25px; border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <h4 style="color:#FF9900; margin-bottom:15px;">🔒 Security Features</h4>
        <ul style="color:#234; line-height:1.8;">
            <li>SSL Encrypted Transmission</li>
            <li>Two-Factor Authentication</li>
            <li>Third-Party Payment Protection</li>
            <li>Manual Review of Freelancers</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr class='divider'>", unsafe_allow_html=True)

# ---------------------
# Footer
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | App Features</div>",
    unsafe_allow_html=True
)
