import streamlit as st

# ---------------------
# Page Basic Settings
# ---------------------
st.set_page_config(
    page_title="Talent Recruitment｜Tasksnap",
    page_icon="🚀",
    layout="wide"
)

# ---------------------
# Custom CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
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
        line-height: 1.8;
    }
    .section-title {
        text-align: center;
        color: #0055A5;
        font-size: 28px;
        font-weight: 800;
        margin-top: 48px;
        margin-bottom: 18px;
        letter-spacing: 2px;
    }
    .card-list {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0 auto 40px auto;
        background: linear-gradient(135deg, #ffffff, #f8fbff, #fff8f0);
        border-radius: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.12), 0 8px 20px rgba(0,85,165,0.15);
        padding: 45px 40px 30px 40px;
        max-width: 580px;
        border: 2px solid transparent;
        background-clip: padding-box;
        transition: all 0.4s ease;
        animation: slideInLeft 1s ease-out;
    }
    .card-list:hover {
        transform: translateY(-5px);
        box-shadow: 0 30px 70px rgba(0,0,0,0.18), 0 12px 30px rgba(0,85,165,0.2), 0 0 40px rgba(255,153,0,0.1);
    }
    .card-item {
        width: 100%;
        margin-bottom: 28px;
        background: linear-gradient(135deg, #f7faff, #ffffff);
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,85,165,0.1), 0 3px 10px rgba(0,0,0,0.05);
        padding: 25px 28px 18px 28px;
        text-align: left;
        border-left: 4px solid #FF9900;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    .card-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #FF9900, #0055A5);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    .card-item:hover {
        transform: translateX(8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0,85,165,0.15), 0 5px 15px rgba(255,153,0,0.2);
        border-left-width: 6px;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .card-item:hover::before {
        transform: scaleX(1);
    }
    .card-title {
        font-size: 20px;
        color: #FF9900;
        font-weight: bold;
        margin-bottom: 6px;
        letter-spacing: 1px;
    }
    .card-desc {
        font-size: 16px;
        color: #234;
        margin-left: 8px;
        margin-bottom: 2px;
        line-height: 1.7;
    }
    .offer-list {
        margin-top: 0;
        margin-bottom: 32px;
        padding: 28px 36px 18px 36px;
    }
    .offer-item {
        font-size: 17px;
        color: #003366;
        margin-bottom: 10px;
        text-align: left;
        width: 100%;
        padding-left: 8px;
        position: relative;
    }
    .offer-item:before {
        content: "•";
        color: #FF9900;
        font-size: 22px;
        position: absolute;
        left: -14px;
        top: -2px;
    }
    .join-block {
        text-align: center;
        font-size: 18px;
        line-height: 2;
        margin-bottom: 32px;
        margin-top: 12px;
    }
    .cta-block {
        text-align: center;
        font-size: 20px;
        margin-top: 40px;
        margin-bottom: 24px;
        font-weight: 600;
        letter-spacing: 1.5px;
    }
    .cta-block:hover {
        transform: perspective(1000px) rotateX(5deg) scale(1.05) !important;
        box-shadow: 0 25px 60px rgba(102,126,234,0.7), 0 10px 30px rgba(0,0,0,0.2), 0 0 50px rgba(240,147,251,0.6) !important;
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
st.markdown("<div class='main-title'>🚀 Talent Recruitment</div>", unsafe_allow_html=True)
st.markdown("""
<div class='subtitle'>
We believe that <b>every great idea needs a passionate team to bring it to life.</b><br><br>
Tasksnap is developed by a group of university students,<br>
and we're looking for more like-minded partners to join us,<br>
starting from campus to create the safest and most secure freelance environment!
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------
# Job Openings (Beautiful Card Style)
# ---------------------
st.markdown("<div class='section-title'>🔍 Roles We're Looking For</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card-list'>
    <div class='card-item'>
        <div class='card-title'>✅ UI/UX Designer</div>
        <div class='card-desc'>- Help optimize platform interface and user experience</div>
        <div class='card-desc'>- Familiarity with Figma preferred</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ Frontend Engineer</div>
        <div class='card-desc'>- Proficient in HTML / CSS / JavaScript</div>
        <div class='card-desc'>- Development experience is a plus</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ Backend Developer</div>
        <div class='card-desc'>- Proficient in Python / Firebase / Google Sheets API</div>
        <div class='card-desc'>- Able to help integrate payment and membership systems</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ Marketing Planner / Campus Ambassador</div>
        <div class='card-desc'>- Skilled in social media management and copywriting</div>
        <div class='card-desc'>- Help promote the platform and attract more users</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ Game Developer</div>
        <div class='card-desc'>- Proficient in Unity</div>
        <div class='card-desc'>- Create cross-platform games</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# Benefits (Beautiful Card Style)
# ---------------------
st.markdown("<div class='section-title'>🌱 What We Offer</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card-list offer-list'>
    <div class='offer-item'>Flexible, free remote working environment</div>
    <div class='offer-item'>Real product development experience to strengthen your resume</div>
    <div class='offer-item'>Participate in cross-campus, cross-department collaboration to expand your network</div>
    <div class='offer-item'>Witness the birth of a new campus freelance model together</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# How to Join
# ---------------------
st.markdown("<div class='section-title'>📩 How to Join Us?</div>", unsafe_allow_html=True)
st.markdown("""
<div class='join-block'>
If you love creating and enjoy challenges,<br>
please send your <b>resume or portfolio</b> to:<br>
<b>campusfreelance@example.com</b><br>
We'll contact you as soon as possible to arrange further discussion!
</div>
""", unsafe_allow_html=True)

# ---------------------
# Call to Action
# ---------------------
st.markdown("""
<div class='cta-block' style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    border-radius: 25px;
    box-shadow: 0 15px 35px rgba(102,126,234,0.4), 0 5px 15px rgba(0,0,0,0.1);
    padding: 40px 20px 35px 20px;
    margin: 0 auto 32px auto;
    max-width: 600px;
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #ffffff;
    position: relative;
    overflow: hidden;
    animation: pulse-glow 3s ease-in-out infinite;
    transform: perspective(1000px) rotateX(5deg);
    transition: all 0.3s ease;
">
    Let's work together to transform campus freelance ecosystem,<br>
    <span style="color:#ffffff; font-size:24px; text-shadow: 0 0 10px rgba(255,255,255,0.5);"><b>ensuring every student's effort is recognized and properly protected.</b></span><br>
    <span style="font-size:28px; color:#ffffff; text-shadow: 0 0 15px rgba(255,255,255,0.7);">🚀 Join us, starting now!</span>
</div>
<style>
@keyframes pulse-glow {
    0%, 100% { 
        box-shadow: 0 15px 35px rgba(102,126,234,0.4), 0 5px 15px rgba(0,0,0,0.1), 0 0 20px rgba(102,126,234,0.3);
        transform: perspective(1000px) rotateX(5deg) scale(1);
    }
    50% { 
        box-shadow: 0 20px 50px rgba(102,126,234,0.6), 0 8px 25px rgba(0,0,0,0.15), 0 0 40px rgba(240,147,251,0.5);
        transform: perspective(1000px) rotateX(5deg) scale(1.02);
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------
# Team Culture Section
# ---------------------
st.markdown("<div class='section-title'>🌈 Team Culture</div>", unsafe_allow_html=True)
culture1, culture2, culture3 = st.columns(3)
with culture1:
    st.markdown("""
    <div style="text-align:center; padding:25px 20px; background:linear-gradient(135deg, #ffffff, #f0f8ff); border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <div style="font-size:50px; margin-bottom:15px;">🚀</div>
        <h4 style="color:#0055A5; margin-bottom:10px;">Innovation First</h4>
        <p style="color:#666; font-size:14px; line-height:1.6;">Encourage innovative thinking, every idea deserves to be discussed and realized</p>
    </div>
    """, unsafe_allow_html=True)
with culture2:
    st.markdown("""
    <div style="text-align:center; padding:25px 20px; background:linear-gradient(135deg, #ffffff, #fff8f0); border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <div style="font-size:50px; margin-bottom:15px;">🤝</div>
        <h4 style="color:#FF9900; margin-bottom:10px;">Collaboration & Unity</h4>
        <p style="color:#666; font-size:14px; line-height:1.6;">Cross-disciplinary collaboration, learning from each other, growing together</p>
    </div>
    """, unsafe_allow_html=True)
with culture3:
    st.markdown("""
    <div style="text-align:center; padding:25px 20px; background:linear-gradient(135deg, #ffffff, #f0fff0); border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <div style="font-size:50px; margin-bottom:15px;">⚖️</div>
        <h4 style="color:#4CAF50; margin-bottom:10px;">Work-Life Balance</h4>
        <p style="color:#666; font-size:14px; line-height:1.6;">Flexible hours, focus on efficiency rather than long hours</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------
# Footer
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | Talent Recruitment</div>",
    unsafe_allow_html=True)