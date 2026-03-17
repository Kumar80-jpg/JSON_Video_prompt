import json
import os

# Create prompts folder if not exists
os.makedirs("prompts", exist_ok=True)

# -------- PART 1 PROMPT --------
part1 = {
    "duration": "8 seconds",
    "resolution": "3840x2160",
    "fps": 30,
    "force_duration": True,
    "style": "cinematic tech",

    "audio": {
        "voice": {
            "language": "ta-IN",
            "gender": "male",
            "speed": 0.70,
            "volume": 1.4,
            "enable_tts": True
        }
    },

    "scenes": [
        {
            "time": "0-3",
            "voice": "அனைவரும் தெரிந்திருக்க வேண்டிய AI Tools.",
            "visual": "Futuristic AI background, cinematic lighting",
            "text": "Top AI Tools"
        },
        {
            "time": "3-5.5",
            "voice": "ChatGPT. எதையும் எழுத உதவும்.",
            "visual": "AI chat typing interface",
            "text": "ChatGPT"
        },
        {
            "time": "5.5-8",
            "voice": "Midjourney. அழகான படங்கள் உருவாக்கும்.",
            "visual": "AI generating digital art",
            "text": "Midjourney"
        }
    ],

    "captions": {
        "enabled": False
    }
}

# -------- PART 2 PROMPT --------
part2 = {
    "duration": "7 seconds",
    "resolution": "3840x2160",
    "fps": 30,
    "force_duration": True,
    "style": "cinematic tech",

    "audio": {
        "voice": {
            "language": "ta-IN",
            "gender": "male",
            "speed": 0.60,
            "volume": 1.5,
            "enable_tts": True
        }
    },

    "scenes": [
        {
            "time": "0-2.3",
            "voice": "Runway. வீடியோ எடிட்டிங் மிகவும் எளிது.",
            "visual": "Video editing timeline animation",
            "text": "Runway ML"
        },
        {
            "time": "2.3-4.6",
            "voice": "ElevenLabs. மனித குரல் போல பேசும் AI.",
            "visual": "Audio waveform animation",
            "text": "ElevenLabs"
        },
        {
            "time": "4.6-7",
            "voice": "Durable. சில நிமிடங்களில் வலைத்தளம் உருவாக்கலாம்.",
            "visual": "Website building animation",
            "text": "Durable AI"
        }
    ],

    "captions": {
        "enabled": False
    }
}

# Save JSON files
with open("prompts/part1.json", "w", encoding="utf-8") as f:
    json.dump(part1, f, ensure_ascii=False, indent=4)

with open("prompts/part2.json", "w", encoding="utf-8") as f:
    json.dump(part2, f, ensure_ascii=False, indent=4)

print("✅ Prompts saved successfully!")