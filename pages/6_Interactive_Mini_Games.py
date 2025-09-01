import streamlit as st

# ---------------------
# Basic Page Configuration
# ---------------------
st.set_page_config(
    page_title="Interactive Mini Games Experience｜Tasksnap",
    page_icon="🍪",
    layout="wide"
)

# ---------------------
# Custom CSS
# ---------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #de6262 0%, #ffb88c 100%);
    background-attachment: fixed;
}

div[data-testid="stMarkdownContainer"] h1 {
    text-align: center;
    color: white;
    font-size: 3rem;
    margin: 2rem 0;
}


</style>
""", unsafe_allow_html=True)

# ---------------------
# Title
# ---------------------
st.markdown("# 🍪 Interactive Mini Games Experience")

# ---------------------
# Content
# ---------------------
st.markdown("""
<div style="
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem auto;
    max-width: 700px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    font-size: 1.2rem;
    line-height: 1.8;
">
    <strong>Thank you for visiting our website!</strong> 🎉<br><br>
    This is a <strong>cute interactive mini-game</strong> we've carefully designed, inviting you to experience this fortune cookie machine full of surprises 🎮<br><br>
    <strong>Have a nice day!</strong> ☀️
</div>
""", unsafe_allow_html=True)

# ---------------------
# Game Button
# ---------------------
st.markdown("""
<style>
.learn-more {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  font-family: inherit;
  font-size: 18px;
  font-weight: 700;
  color: white !important;
  padding: 15px 40px;
  background: linear-gradient(45deg, #FF8C00, #FF7F00);
  border: 3px solid #CC5500;
  border-radius: 12px;
  box-shadow: 0 6px 0 #CC5500, 0 8px 15px rgba(0,0,0,0.3);
  transform-style: preserve-3d;
  transition: all 150ms ease;
}

.learn-more:hover {
  background: linear-gradient(45deg, #FF7F00, #FF8C00);
  transform: translateY(-2px);
  box-shadow: 0 8px 0 #CC5500, 0 10px 20px rgba(0,0,0,0.4);
}

.learn-more:active {
  background: linear-gradient(45deg, #CC5500, #B8860B);
  transform: translateY(4px);
  box-shadow: 0 2px 0 #CC5500, 0 4px 8px rgba(0,0,0,0.2);
}
</style>

<div style="text-align: center; margin: 2rem 0;">
    <a href="https://ipikeq22.github.io/tasksnap_Sweet_Cookie_Bite_Game/" target="_blank" class="learn-more">
        🎮 Start Game
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------------
# Game Instructions
# ---------------------
st.markdown("""
<div style="text-align: center; color: white; font-size: 2.5rem; font-weight: 700; margin: 3rem 0 2rem 0;">
🎯 How to Play
</div>
""", unsafe_allow_html=True)

# Step 1
st.image("1e.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>Step 1: Click "Start Game"</strong><br>
Click the orange button above to begin your lucky journey
</div>
""", unsafe_allow_html=True)

# Step 2
st.image("2e.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>Step 2: Click "Give Me Luck" Button</strong><br>
Once in the game, click the "Give Me Luck" button on the screen
</div>
""", unsafe_allow_html=True)

# Step 3
st.image("3e.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>Step 3: Machine Starts Shaking</strong><br>
The fortune cookie machine will start shaking, preparing to drop a mysterious fortune cookie
</div>
""", unsafe_allow_html=True)

# Step 4
st.image("4e.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>Step 4: Get Your Fortune Message</strong><br>
The cookie will open and display your personalized lucky message. You can also click "Try Again" to get different themed fortunes
</div>
""", unsafe_allow_html=True)

# Step 5
st.image("5e.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>Step 5: Share with Friends</strong><br>
When you get a fortune you like, click "Share" and the content will be automatically copied. You can paste it to share with your family and friends
</div>
""", unsafe_allow_html=True)

# ---------------------
# Our Mission
# ---------------------
st.markdown("""
<div style="text-align: center; color: white; font-size: 2.5rem; font-weight: 700; margin: 3rem 0 2rem 0;">
❤️ Our Mission
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: white; font-size: 1.1rem; line-height: 1.8; text-align: left; max-width: 90%; margin: 2rem auto; font-family: serif; font-weight: bold;">
In this fast-paced, busy world, we hope to create a game that brings smiles and moments of warmth to people. Just like opening a fortune cookie with a surprise note inside, that simple yet genuine joy fills our hearts with anticipation.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: white; font-size: 1.1rem; line-height: 1.8; text-align: left; max-width: 90%; margin: 1rem auto; font-family: serif; font-weight: bold;">
Lucky Cookie Bite was born to pass on this feeling to every player. Whether children or adults, everyone can easily draw their own luck in the game, finding a bit of childlike wonder and happiness in the colorful cookie world.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: white; font-size: 1.1rem; line-height: 1.8; text-align: left; max-width: 90%; margin: 1rem auto; font-family: serif; font-weight: bold;">
If you can smile because of a little bit of luck in the game, that is our original and most sincere wish for creating this game.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: white; font-size: 1.1rem; text-align: right; max-width: 90%; margin: 2rem auto 0 auto; font-family: serif; font-weight: 600;">
With respect,<br>
Tasksnap Team
</div>
""", unsafe_allow_html=True)

# ---------------------
# Footer
# ---------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.8); margin-top: 2rem;">
© 2025 Tasksnap App | Interactive Mini Games Experience 🍪
</div>
""", unsafe_allow_html=True)