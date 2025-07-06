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
gender = st.selectbox("Gender", ["Male", "Female"])

outfits = recommend_outfits(height, weight, skin_tone, gender)

if outfits:
    st.success("Suggested outfits:")
    for outfit in outfits:
        st.markdown(f"- 👕 {outfit}")
    st.image("https://source.unsplash.com/400x400/?fashion,outfit", caption="Sample Outfit")
else:
    st.warning("No suitable outfit found.")

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
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from matplotlib.colors import rgb_to_hsv

def extract_skin_color(image):
    image_np = np.array(image)
    image_rgb = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return "Face not detected"

    (x, y, w, h) = faces[0]
    face_roi = image_np[y:y+h, x:x+w]
    center = face_roi[h//2-10:h//2+10, w//2-10:w//2+10]
    avg_color = np.mean(center.reshape(-1, 3), axis=0) / 255.0
    hsv = rgb_to_hsv(np.array([avg_color]))[0]

    h, s, v = hsv
    if v < 0.35:
        return "Dark"
    elif s < 0.3:
        return "Fair"
    elif h < 0.1 or h > 0.9:
        return "Pinkish"
    elif 0.1 <= h <= 0.2:
        return "Wheatish"
    else:
        return "Tan"
def classify_body_shape(gender, height, weight):
    bmi = weight / ((height / 100) ** 2)
    if gender == "Female":
        if bmi < 18.5:
            return "Rectangle"
        elif bmi < 25:
            return "Pear"
        elif bmi < 30:
            return "Apple"
        else:
            return "Full Hourglass"
    else:
        if bmi < 18.5:
            return "Slim"
        elif bmi < 25:
            return "Average Build"
        elif bmi < 30:
            return "Athletic"
        else:
            return "Plus Size"

def suggest_outfit(gender, skin_color, body_shape):
    if gender == "Female":
        if body_shape == "Pear":
            return "Wear tops with patterns or volume to balance your shape."
        elif body_shape == "Apple":
            return "Try high-waisted dresses or wrap styles to define your waist."
        elif skin_color == "Wheatish":
            return "Warm colors like orange, maroon, and olive will suit your tone."
        else:
            return "Go for short jackets and wide-leg pants."
    else:
        if body_shape == "Average Build":
            return "Slim fit shirts and straight-leg trousers suit you well."
        elif body_shape == "Athletic":
            return "Open jackets with solid color tees are a good choice."
        else:
            return "Dark colors and minimal prints help balance your look."
    return "Choose what makes you feel confident and comfortable."
st.set_page_config(page_title="AI Fashion Assistant", layout="centered")

st.title("🧠👗 AI Fashion Assistant")
st.markdown("Upload your photo and enter your details to get personalized outfit suggestions.")

uploaded_file = st.file_uploader("📸 Upload a clear photo of your face", type=["jpg", "jpeg", "png"])
gender = st.selectbox("👤 Select your gender", ["Male", "Female"])
height = st.number_input("📏 Your height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("⚖️ Your weight (kg)", min_value=30, max_value=200, value=70)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    skin_color = extract_skin_color(image)
    body_shape = classify_body_shape(gender, height, weight)
    outfit = suggest_outfit(gender, skin_color, body_shape)

    st.markdown("### 🎨 Detected Skin Tone:")
    st.success(skin_color)

    st.markdown("### 🧍 Estimated Body Shape:")
    st.info(body_shape)

    st.markdown("### 👕 Recommended Outfit:")
    st.write(outfit)
else:
    st.warning("Please upload a clear face photo to proceed.")
