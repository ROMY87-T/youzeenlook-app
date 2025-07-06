import streamlit as st
import numpy as np
import cv2
import json
import requests
from PIL import Image
from matplotlib.colors import rgb_to_hsv

def extract_skin_tone(image):
    image_np = np.array(image)
    image_rgb = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return "Unknown"

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

def estimate_body_shape(gender, height, weight):
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
            return "Athletic"
        elif bmi < 30:
            return "Muscular"
        else:
            return "Plus Size"

def load_outfits():
    with open("outfits_with_images.json", "r") as f:
        return json.load(f)

def find_best_match(user_data, outfits):
    def similarity(o):
        score = 0
        if o["gender"] == user_data["gender"]:
            score += 1
        if abs(o["height"] - user_data["height"]) <= 5:
            score += 1
        if abs(o["weight"] - user_data["weight"]) <= 5:
            score += 1
        if o["skin_tone"] == user_data["skin_tone"]:
            score += 1
        if o["body_shape"] == user_data["body_shape"]:
            score += 1
        return score

    outfits_sorted = sorted(outfits, key=similarity, reverse=True)
    return outfits_sorted[0] if outfits_sorted else None

st.set_page_config(page_title="AI Fashion Assistant", layout="centered")
st.title("🧠👗 AI Fashion Assistant with Visual Recommendations")

uploaded_file = st.file_uploader("📸 Upload a clear photo of your face", type=["jpg", "jpeg", "png"])
gender = st.selectbox("👤 Select your gender", ["Male", "Female"])
height = st.number_input("📏 Your height (cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("⚖️ Your weight (kg)", min_value=30, max_value=200, value=70)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    skin_tone = extract_skin_tone(image)
    body_shape = estimate_body_shape(gender, height, weight)

    st.markdown("### 🎨 Detected Skin Tone:")
    st.success(skin_tone)

    st.markdown("### 🧍 Estimated Body Shape:")
    st.info(body_shape)

    outfit_data = load_outfits()
    user_data = {
        "gender": gender,
        "height": height,
        "weight": weight,
        "skin_tone": skin_tone,
        "body_shape": body_shape
    }

    match = find_best_match(user_data, outfit_data)

    if match:
        st.markdown("### 👕 Recommended Outfit:")
        st.write(match["recommendation"])
        st.image(match["image_url"], caption="Example Outfit", use_container_width=True)
    else:
        st.warning("No suitable outfit found in the database.")
else:
    st.info("Please upload a face image to get started.")