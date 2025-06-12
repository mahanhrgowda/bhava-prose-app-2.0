# 📁 transliteration_utils.py
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# 🔤 Transliterate Bhāva terms

def transliterate_bhava_term(term: str, scheme: str) -> str:
    if scheme == "English":
        return term
    elif scheme == "IAST":
        return transliterate(term, sanscript.ITRANS, sanscript.IAST)
    elif scheme == "Devanagari":
        return transliterate(term, sanscript.ITRANS, sanscript.DEVANAGARI)
    return term

# 📝 Format sentence with Bhāva embedded

def format_bhava_sentence(bhava: str, sentence: str, scheme: str = "English") -> str:
    bhava_trans = transliterate_bhava_term(bhava, scheme)
    return f"{sentence} (Bhāva: {bhava_trans})"

# 🔮 Dictionary for full Sanskrit Bhāva labels

BHAVA_SANSKRIT_DICTIONARY = {
    "Śāntiḥ": "शान्तिः",
    "Ānandaḥ": "आनन्दः",
    "Bhaktiḥ": "भक्तिः",
    "Jñānam": "ज्ञानम्",
    "Vīryam": "वीर्यम्",
    "Utsāhaḥ": "उत्साहः",
    "Karunā": "करुणा",
    "Krodhaḥ": "क्रोधः",
    "Rāgaḥ": "रागः",
    "Vismayaḥ": "विस्मयः",
    "Śokaḥ": "शोकः",
    "Hāsaḥ": "हासः",
    "Jugupsā": "जुगुप्सा",
    "Bhayaṁ": "भयम्"
}

# 🕉️ Future expansion: full Sanskrit sentence builder

def generate_sanskrit_sentence(bhava: str) -> str:
    return BHAVA_SANSKRIT_DICTIONARY.get(bhava, bhava)
