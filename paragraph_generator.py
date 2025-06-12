import random
from data import PHONEME_BHAVA_MAP, SAMPLE_INTENTS
from transliteration_utils import format_bhava_sentence, generate_sanskrit_sentence

def generate_bhava_paragraph(phonemes, scheme="English", mode="Linked"):
    sentences = []
    used_bhavas = set()

    for phoneme in phonemes:
        data = PHONEME_BHAVA_MAP.get(phoneme, PHONEME_BHAVA_MAP["unknown"])
        bhava = data["bhava"]
        if bhava in used_bhavas:
            continue
        used_bhavas.add(bhava)
        intent_list = SAMPLE_INTENTS.get(bhava, [])

        if mode == "Sanskrit":
            sentence = generate_sanskrit_sentence(bhava)
        else:
            if not intent_list:
                continue
            random_intent = random.choice(intent_list)
            sentence = format_bhava_sentence(bhava, random_intent, scheme) if mode == "Linked" else random_intent

        sentences.append(sentence)

    return " ".join(sentences) if sentences else "⚠️ No Bhāva paragraph could be generated."