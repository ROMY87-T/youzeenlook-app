from ai_model import recommend_outfits
import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="YouzeenLook - AI Fashion Assistant", layout="centered")

# ----- Header -----
st.markdown("<h1 style='text-align: center;'>🧠 YouzeenLook</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>AI Fashion Assistant - Find your perfect outfit</h4>", unsafe_allow_html=True)

st.divider()

# ----- Hero Section with Video -----
st.markdown("## 🎥 What is YouzeenLook?")
st.markdown("Discover the power of AI to recommend outfits based on your height, weight, and skin tone. And try them on virtually!")

video_url = "https://www.youtube.com/embed/YOUR_VIDEO_ID"  # ضع هنا ID الفيديو الخاص بك
html(f'<iframe width="100%" height="350" src="{video_url}" frameborder="0" allowfullscreen></iframe>', height=370)

st.divider()

# ----- AI Features Section -----
st.markdown("## 🧬 AI-Powered Features")
st.markdown("- 👤 Personalized outfit suggestions based on your body")
st.markdown("- 🎨 Skin tone detection to match color palettes")
st.markdown("- 📏 Fit recommendations using your height & weight")

st.divider()

# ----- AI Form Section -----
st.markdown("## 👗 Try AI Outfit Recommendation")

height = st.slider("Height (cm)", min_value=100, max_value=220, value=170)
weight = st.slider("Weight (kg)", min_value=30, max_value=150, value=65)
skin_tone = st.selectbox("Skin Tone", ["Light", "Medium", "Dark"])

if st.button("Get Outfit Suggestion"):
    name, image = get_recommendation(height, weight, skin_tone)
    st.success(f"Suggested: {name}")
    st.image(image, caption=name)

st.divider()

# ----- AR Try-On Section -----
st.markdown("## 🪄 Virtual Try-On (AR)")
st.markdown("Experience your recommended outfit on your body using Augmented Reality. Try before you buy!")

st.markdown("🚧 *AR Feature Coming Soon — stay tuned!*")

st.divider()

# ----- Footer -----
st.markdown("""
<hr style='border: 1px solid #ccc;'/>
<center>
    <small>© 2025 YouzeenLook. All rights reserved.</small><br/>
    <a href="mailto:contact@youzeenlook.com">contact@youzeenlook.com</a>
</center>
""", unsafe_allow_html=True)
