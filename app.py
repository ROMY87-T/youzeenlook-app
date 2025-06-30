# import streamlit as st

st.set_page_config(page_title="YouzeenLook - AI Fashion Assistant", layout="centered")

st.title("🧠 YouzeenLook - AI Fashion Assistant")
st.write("Welcome to YouzeenLook! Let us help you find the perfect outfits based on your height, weight, and skin tone.")

# User Inputs
height = st.number_input("📏 Your Height (cm):", min_value=100, max_value=250)
weight = st.number_input("⚖️ Your Weight (kg):", min_value=30, max_value=200)
skin_tone = st.selectbox("🎨 Skin Tone:", ["Light", "Wheatish", "Tan", "Dark"])

# Submit Button
if st.button("Show Outfit Recommendations"):
    st.success(f"Based on your height: {height} cm, weight: {weight} kg, and skin tone: {skin_tone}, here are some suggestions:")

    st.markdown("""
    - 👚 Light-colored top  
    - 👖 Dark jeans or trousers  
    - 👗 Medium-length dress for formal occasions  
    - 🧥 Try layers with soft tones for contrast
    """)
    st.caption("👓 Augmented Reality (AR) try-on coming soon!")

# Footer
st.markdown("---")
st.caption("Powered by YouzeenLook | AI for Fashion")
youzeenlook-app
