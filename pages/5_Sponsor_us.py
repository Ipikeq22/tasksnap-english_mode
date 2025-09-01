import streamlit as st

# ---------------------
# Page Basic Settings
# ---------------------
st.set_page_config(
    page_title="Sponsor Us｜Tasksnap",
    page_icon="💖",
    layout="wide"
)

# ---------------------
# Custom CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes heartbeat {
        0% { transform: scale(1); }
        14% { transform: scale(1.1); }
        28% { transform: scale(1); }
        42% { transform: scale(1.1); }
        70% { transform: scale(1); }
    }
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    body {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
    }
    .main-title {
        text-align: center;
        font-size: 60px;
        color: #003366;
        font-weight: 900;
        letter-spacing: 4px;
        margin-bottom: 12px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .intro-text {
        text-align: center;
        font-size: 24px;
        line-height: 2;
        color: #234;
        margin-bottom: 40px;
        margin-top: 20px;
        font-weight: 500;
        background: linear-gradient(135deg, #ffffff, #fff0f5);
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08), 0 5px 15px rgba(255,105,180,0.1);
        border-left: 5px solid #FF9900;
        position: relative;
    }
    .sponsor-card {
        background: linear-gradient(135deg, #ffffff, #fff0f5, #f0f8ff);
        border-radius: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.12), 0 8px 20px rgba(255,105,180,0.15);
        padding: 45px 35px 40px 35px;
        margin: 0 auto 30px auto;
        max-width: 580px;
        text-align: center;
        border: 3px solid transparent;
        background-clip: padding-box;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInRight 1s ease-out;
    }
    .sponsor-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #FF69B4, #FF1493, #DC143C, #FF6347);
        border-radius: 25px 25px 0 0;
    }
    .sponsor-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 30px 70px rgba(0,0,0,0.18), 0 12px 30px rgba(255,105,180,0.25), 0 0 40px rgba(255,20,147,0.2);
        border-color: #FF1493;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .qr-title, .form-title {
        text-align: center;
        font-size: 26px;
        color: #0055A5;
        font-weight: 800;
        margin-bottom: 18px;
        letter-spacing: 2px;
    }
    .contact-block {
        text-align: center;
        margin-top: 48px;
        margin-bottom: 12px;
    }
    .contact-block h3 {
        color: #003366;
        font-size: 24px;
        margin-bottom: 8px;
        font-weight: 800;
    }
    .contact-block b {
        color: #0055A5;
        font-size: 18px;
        letter-spacing: 1px;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 40px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    .stForm {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1), 0 5px 15px rgba(0,85,165,0.1);
        border: 2px solid rgba(0,85,165,0.1);
    }
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e0e7ef;
        padding: 12px 16px;
        font-size: 16px;
        transition: all 0.3s ease;
        background: #ffffff;
    }
    .stTextInput > div > div > input:focus {
        border-color: #0055A5;
        box-shadow: 0 0 15px rgba(0,85,165,0.2);
        outline: none;
    }
    .stSelectbox > div > div > div {
        border-radius: 12px;
        border: 2px solid #e0e7ef;
        background: #ffffff;
        transition: all 0.3s ease;
    }
    .stSelectbox > div > div > div:hover {
        border-color: #0055A5;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid #e0e7ef;
        padding: 12px 16px;
        font-size: 16px;
        transition: all 0.3s ease;
        background: #ffffff;
        min-height: 100px;
    }
    .stTextArea > div > div > textarea:focus {
        border-color: #0055A5;
        box-shadow: 0 0 15px rgba(0,85,165,0.2);
        outline: none;
    }
    .stButton > button {
        background: linear-gradient(45deg, #0055A5, #003366);
        border: none;
        border-radius: 12px;
        color: white;
        font-weight: 700;
        font-size: 16px;
        padding: 12px 30px;
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(0,85,165,0.3);
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(0,85,165,0.4);
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# Title
# ---------------------
st.markdown("<div class='main-title'>💖 Sponsor Us</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------
# Sponsorship Introduction Text
# ---------------------
st.markdown("""
<div class='intro-text'>
We are a university student team working hard to develop a secure and trusted freelance platform.<br>
To continuously optimize features, maintain servers, and promote safer freelance opportunities for more students,<br>
we need your support and encouragement!<br><br>
Whether it's the cost of a coffee or corporate partnership, it all helps us go further 💪
</div>
""", unsafe_allow_html=True)
st.write("---")

# ---------------------
# Two Columns: Left QR Code, Right Form
# ---------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<div class='qr-title'>📱 Scan QR Code to Sponsor</div>", unsafe_allow_html=True)
    st.image("簡報.png", width=550, caption="Scan QR Code to sponsor us")

with col2:
    st.markdown("<div class='form-title'>📝 Sponsorship Information Form</div>", unsafe_allow_html=True)
    with st.form("sponsor_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Contact Email")
        amount = st.selectbox("Sponsorship Amount", ["☕ Basic Support｜A Cup of Coffee", "🍱 Core Support｜A Big Meal", "🏢 Brand Support｜Corporate Plan", "Other"])
        amount_way = st.selectbox("Sponsorship Method", ["Online Transfer", "Convenience Store Transfer", "Cash Payment"])
        message = st.text_area("Message for us (Optional)")
        submitted = st.form_submit_button("Submit Information")
        if submitted:
            st.success(f"Thank you for your support, {name}! We have received your sponsorship information ❤️")

# ---------------------
# Sponsorship Plans Section
# ---------------------
st.markdown("<div style='text-align:center; margin-top:48px; margin-bottom:36px;'><h3>💖 Sponsorship Plans</h3></div>", unsafe_allow_html=True)
st.markdown("""
<div style="overflow-x:auto; margin:20px 0;">
<table style="width:100%; border-collapse:collapse; background:linear-gradient(135deg, #ffffff, #f8fbff); border-radius:15px; box-shadow:0 15px 40px rgba(0,0,0,0.1); overflow:hidden;">
    <thead>
        <tr style="background:linear-gradient(135deg, #0055A5, #003366); color:white;">
            <th style="padding:20px; text-align:left; font-size:18px; font-weight:700;">Sponsorship Amount</th>
            <th style="padding:20px; text-align:left; font-size:18px; font-weight:700;">Target Audience</th>
            <th style="padding:20px; text-align:left; font-size:18px; font-weight:700;">Plan Contents</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom:1px solid #e0e7ef;">
            <td style="padding:25px 20px; vertical-align:top;">
                <div style="font-size:24px; margin-bottom:8px;">☕ <strong>Basic Support｜A Cup of Coffee</strong></div>
                <div style="font-size:20px; font-weight:700; color:#0055A5;">NT$ 150</div>
            </td>
            <td style="padding:25px 20px; vertical-align:top; color:#666; font-size:16px;">General users, students</td>
            <td style="padding:25px 20px; vertical-align:top;">
                <ul style="margin:0; padding-left:20px; color:#333; font-size:15px; line-height:1.8;">
                    <li>Support basic server operations</li>
                    <li>Thank you card (digital version)</li>
                    <li>Tasksnap limited sponsor badge (physical)</li>
                    <li>Join official Discord community</li>
                </ul>
            </td>
        </tr>
        <tr style="border-bottom:1px solid #e0e7ef; background:rgba(255,153,0,0.05);">
            <td style="padding:25px 20px; vertical-align:top;">
                <div style="font-size:24px; margin-bottom:8px;">🍱 <strong>Core Support｜A Big Meal</strong></div>
                <div style="font-size:20px; font-weight:700; color:#FF9900;">NT$ 800</div>
            </td>
            <td style="padding:25px 20px; vertical-align:top; color:#666; font-size:16px;">Platform enthusiasts or development supporters</td>
            <td style="padding:25px 20px; vertical-align:top;">
                <ul style="margin:0; padding-left:20px; color:#333; font-size:15px; line-height:1.8;">
                    <li>Support new feature development</li>
                    <li>Priority access to beta features</li>
                    <li>Tasksnap limited postcard + sticker set</li>
                    <li>Join official Discord VIP sponsor community</li>
                    <li>Discount on limited merchandise (T-shirts, stickers, etc.)</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="padding:25px 20px; vertical-align:top;">
                <div style="font-size:24px; margin-bottom:8px;">🏢 <strong>Brand Support｜Corporate Plan</strong></div>
                <div style="font-size:20px; font-weight:700; color:#4CAF50;">NT$ 5000+ (Negotiable)</div>
            </td>
            <td style="padding:25px 20px; vertical-align:top; color:#666; font-size:16px;">Educational institutions, partner companies, brand promotion</td>
            <td style="padding:25px 20px; vertical-align:top;">
                <ul style="margin:0; padding-left:20px; color:#333; font-size:15px; line-height:1.8;">
                    <li>Official partnership recognition</li>
                    <li>Brand logo display on official website and events</li>
                    <li>Custom collaboration services (campus events, interface integration)</li>
                    <li>VIP outsourcing discounts</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------
# Contact Information
# ---------------------
st.markdown("""
<div class='contact-block'>
    <h3>📩 Contact Us</h3>
    For receipts or corporate partnership inquiries, please email:<br>
    <b>campusfreelance@example.com</b>
</div>
""", unsafe_allow_html=True)

# ---------------------
# Footer
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | Thank you for your support and love 💖</div>",
    unsafe_allow_html=True
)