import streamlit as st
from ai_model import recommend_outfits
import json

# Set wide layout and page title
st.set_page_config(page_title="YouzeenLook - AI Fashion Assistant", layout="wide")

# Custom CSS styles
st.markdown("""
    <style>
    body {
        background-color: #f9f4ff;
    }
    .main {
        padding: 20px;
    }
    h1 {
        color: #6a1b9a;
        font-size: 3em;
        text-align: center;
    }
    .stButton>button {
        background-color: #6a1b9a;
        color: white;
        border-radius: 10px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #8e24aa;
        color: #fff;
    }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<h1>🧠 YouzeenLook - AI Fashion Assistant</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:1px solid #ddd;'>", unsafe_allow_html=True)
st.write("Find your perfect outfit based on your height, weight, and skin tone.")

# Inputs
col1, col2, col3 = st.columns(3)
with col1:
    height = st.number_input("Height (cm)", min_value=100, max_value=250)
with col2:
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200)
with col3:
    skin_tone = st.selectbox("Skin Tone", ["Light", "Wheatish", "Tan", "Dark"])

# Recommend button
if st.button("Recommend Outfits"):
    results = recommend_outfits(height, weight, skin_tone)
    if results:
        st.success("Here are your recommended outfits:")
        for item in results:
            st.markdown(f"- 👕 {item}")
    else:
        st.warning("No suitable outfits found for your profile.")

st.markdown("<br><br>", unsafe_allow_html=True)
st.caption("👓 Coming soon: Try on your favorite outfits in Augmented Reality with YouzeenLook.")


