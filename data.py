import pandas as pd

# Load dataset
df = pd.read_csv("phoneme_bhava_full.csv")

# Generate PHONEME_BHAVA_MAP with fallback
PHONEME_BHAVA_MAP = {
    row["phoneme"]: {
        "bhava": row["bhava"],
        "chakra": row["chakra"],
        "rasa": row["rasa"],
        "emoji": row.get("bhava_emoji", "🌀"),
        "bhava_vector": eval(row["bhava_vector"]),
        "rasa_vector": eval(row["rasa_vector"]),
        "chakra_vector": eval(row["chakra_vector"])
    }
    for _, row in df.iterrows()
}

# Fallback for unknown phonemes
PHONEME_BHAVA_MAP["unknown"] = {
    "bhava": "Śāntiḥ",
    "chakra": "Sahasrāra",
    "rasa": "Śānta",
    "emoji": "🕉️",
    "bhava_vector": [0.5] * 12,
    "rasa_vector": [0.5] * 12,
    "chakra_vector": [0.5] * 12
}

# Sample Intents
SAMPLE_INTENTS = {
    "Śāntiḥ": ["🕊️ I seek peace and rest", "😌 Calmness is my goal", "🌌 Let the world be tranquil"],
    "Ānandaḥ": ["🌟 Joy arises from within", "🤍 Let bliss guide every action", "😍 I am one with divine joy"],
    "Bhaktiḥ": ["🙏 I surrender to the divine", "🕊️ All I do is for my beloved deity", "🙏 Let my devotion guide me"],
    "Jñānam": ["🔮 I seek the truth in all things", "🕶️ Knowledge is the path to liberation", "🔦 Let wisdom light the way"],
    "Vīryam": ["⚔️ I will fight with courage", "🌟 Strength arises within me", "💪 Let us act with power and resolve"],
    "Utsāhaḥ": ["🎉 I feel energized and motivated", "🌟 Let's take this challenge with enthusiasm", "🚀 There's so much to do and I'm ready"],
    "Karunā": ["🩵 I feel deep compassion for others", "😭 May all beings be happy and free", "🩸 This suffering touches my heart"],
    "Krodhaḥ": ["🔥 This injustice must be destroyed", "😡 My anger is righteous and focused", "⚔️ Let the flames of truth burn deceit"],
    "Rāgaḥ": ["❤️ Love flows through me like a river", "🌈 Attraction draws me closer to truth", "🌟 Let the beauty of the world move me"],
    "Vismayaḥ": ["🤔 I marvel at the mysteries around me", "🌟 Wonder fills my heart with curiosity", "💡 Let awe reveal the unseen truths"],
    "Śokaḥ": ["😞 My heart feels the weight of sorrow", "🩵 Let me sit with this grief", "😥 Tears cleanse what words cannot"],
    "Hāsaḥ": ["😂 Laughter heals and unites", "😃 Let joy erupt like a child’s giggle", "😆 I laugh in the face of despair"],
    "Jugupsā": ["😖 I reject what is impure and harmful", "🕳️ This disgust is a guide to cleanse", "🧬 Let clarity arise through aversion"],
    "Bhayaṁ": ["😱 Fear reveals the edges of safety", "😬 Let me move through fear with awareness", "😯 Even in terror, I find growth"],
    "Ratiḥ": ["❤️ Love flows through me like a river", "🌈 Attraction draws me closer to truth", "🌟 Let the beauty of the world move me"],
    "Śamaḥ": ["🕉️ I rest in serene balance", "🌿 Let tranquility guide my actions", "🙏 Peace is my true nature"]
}