import streamlit as st

# ---------------------
# Page Basic Settings
# ---------------------
st.set_page_config(
    page_title="FAQ｜Tasksnap",
    page_icon="❓",
    layout="wide"
)

# ---------------------
# Custom CSS
# ---------------------
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
    }
    .main-title {
        text-align: center;
        font-size: 54px;
        color: #003366;
        font-weight: 900;
        letter-spacing: 4px;
        margin-bottom: 8px;
        font-family: "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #234;
        margin-bottom: 36px;
        margin-top: 8px;
        font-weight: 500;
        letter-spacing: 1.5px;
    }
    .category-title {
        text-align: center;
        color: #0055A5;
        font-size: 28px;
        font-weight: 800;
        margin-top: 48px;
        margin-bottom: 18px;
        letter-spacing: 2px;
    }
    .faq-item {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        padding: 25px;
        margin: 15px 0;
        border-left: 4px solid #FF9900;
        transition: all 0.3s ease;
    }
    .faq-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.12);
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .faq-question {
        font-size: 18px;
        font-weight: 700;
        color: #003366;
        margin-bottom: 10px;
    }
    .faq-answer {
        font-size: 16px;
        color: #234;
        line-height: 1.7;
    }
    .contact-box {
        background: linear-gradient(135deg, #ffffff, #fff8f0);
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        padding: 30px;
        text-align: center;
        margin: 30px 0;
        border: 2px solid #FF9900;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 40px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# Title
# ---------------------
st.markdown("<div class='main-title'>❓ Frequently Asked Questions</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Can't find the answer? Feel free to contact our customer service team</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------
# Account Related Questions
# ---------------------
st.markdown("<div class='category-title'>👤 Account Related</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: How do I register for a Tasksnap account?</div>
    <div class='faq-answer'>A: You can register using your school email. We'll send a verification email to your inbox. After verification, you need to upload your student ID for identity verification to ensure all platform users are genuine students.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: What should I do if I forget my password?</div>
    <div class='faq-answer'>A: Click "Forgot Password" on the login page, enter your registered email, and the system will send a password reset link to your email.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: Can I modify my personal information?</div>
    <div class='faq-answer'>A: Yes! After logging in, go to the "Personal Settings" page where you can modify your nickname, self-introduction, skill tags, and other information. However, school and department information requires re-verification to change.</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# Freelance Related Questions
# ---------------------
st.markdown("<div class='category-title'>💼 Freelance Related</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: How do I start taking on projects?</div>
    <div class='faq-answer'>A: After completing identity verification, you can browse available projects in "Freelance Mode" or showcase your skills and previous work in your "Personal Profile" to let project posters contact you directly.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: How do I receive payment after completing a project?</div>
    <div class='faq-answer'>A: We use a third-party payment system to ensure transaction security. After project completion and confirmation by the project poster, payment will be transferred to your designated bank account within 3-5 business days.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: What should I do if I encounter a dispute?</div>
    <div class='faq-answer'>A: The platform provides dispute resolution services. You can submit a complaint in the "Customer Service Center," and we'll respond within 24 hours to help both parties reach a consensus.</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# Project Posting Related Questions
# ---------------------
st.markdown("<div class='category-title'>📋 Project Posting Related</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: How do I post a project?</div>
    <div class='faq-answer'>A: Switch to "Project Posting Mode," click "Post New Project," and fill in project details, budget, timeline, and other information. After posting, the project will undergo platform review and can start receiving applications once approved.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: Is there a fee for posting projects?</div>
    <div class='faq-answer'>A: Posting projects is free, but a small platform service fee (approximately 5% of the project amount) will be charged after successful matching, used for platform maintenance and customer support.</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# Project/Freelance Function Flow Diagram
# ---------------------
st.markdown("<div class='category-title'>📊 Project/Freelance Function Flow Diagram</div>", unsafe_allow_html=True)
st.image("接案發案功能介紹圖.png", caption="Project/Freelance Function Flow Diagram", use_container_width=True)

# ---------------------
# Token Related Questions
# ---------------------
st.markdown("<div class='category-title'>🪙 Token Related</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: How do I earn tokens?</div>
    <div class='faq-answer'>A: You can earn tokens by completing projects, playing mini-games, participating in community activities, inviting friends to register, and more. Daily login also provides check-in rewards.</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: What can tokens be exchanged for?</div>
    <div class='faq-answer'>A: Tokens can be exchanged for virtual items on the platform, discount coupons from partner merchants, or to boost your personal profile visibility. We also regularly launch limited-time exchange events.</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# Contact Us
# ---------------------
st.markdown("""
<div class='contact-box'>
    <h3 style="color:#FF9900; margin-bottom:15px;">🤝 Have Other Questions?</h3>
    <p style="color:#234; margin-bottom:20px;">Our customer service team is here to help you anytime</p>
    <div style="display:flex; justify-content:center; gap:30px; flex-wrap:wrap;">
        <div style="text-align:center;">
            <div style="font-size:24px; margin-bottom:5px;">📧</div>
            <div style="font-weight:600; color:#0055A5;">Coming Soon</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:24px; margin-bottom:5px;">💬</div>
            <div style="font-weight:600; color:#0055A5;">Online Support (9:00-18:00)</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:24px; margin-bottom:5px;">📱</div>
            <div style="font-weight:600; color:#0055A5;">Official LINE: Coming Soon</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------
# Footer
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | Frequently Asked Questions</div>",
    unsafe_allow_html=True
)