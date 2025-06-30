import streamlit as st
from ai_model import recommend_outfits
import json

# Set page configuration
st.set_page_config(page_title="YouzeenLook - AI Fashion Assistant", layout="wide")

# App title and description
st.title("🧠 YouzeenLook - AI Fashion Assistant")
st.write("Find your perfect outfit based on your height, weight, and skin tone.")

# User inputs
height = st.number_input("Height (cm)", min_value=100, max_value=250)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200)
skin_tone = st.selectbox("Skin Tone", ["Light", "Wheatish", "Tan", "Dark"])

# Recommendation button
if st.button("Recommend Outfits"):
    results = recommend_outfits(height, weight, skin_tone)
    
    if results:
        st.success("Here are your recommended outfits:")
        for item in results:
            st.markdown(f"- 👕 {item}")
    else:
        st.warning("No suitable outfits found for your profile.")

# Coming feature notice
st.caption("👓 Coming soon: Try on your favorite outfits in Augmented Reality with YouzeenLook.")

