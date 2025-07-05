import json

def load_data():
    with open("outfit_data.json", "r") as f:
        return json.load(f)

def recommend_outfits(height, weight, skin_tone, gender):

    outfits = load_data()
    recommended = []

    for item in outfits:
       if "gender" in item and skin_tone in item["skin_tones"] and item["gender"].lower() == gender.lower():


            recommended.append(item["name"])

    return recommended[:5]
