import streamlit as st
import random
from paragraph_generator import generate_bhava_paragraph
from bhava_card_display import render_bhava_card
from data import PHONEME_BHAVA_MAP
from PIL import Image
import io
import latex

# Page Config
st.set_page_config(page_title="🪷 Bhāva Name Explorer", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for Chakra-inspired theme
st.markdown("""
    <style>
        .stApp { background-color: #f5f6f5; }
        .bhava-card { transition: transform 0.3s ease; }
        .bhava-card:hover { transform: scale(1.05); }
        .stButton > button { border-radius: 1rem; }
        .stTextInput > div > input { border: 2px solid #d4a373; }
    </style>
""", unsafe_allow_html=True)

# Sidebar Controls
with st.sidebar:
    st.header("🪷 Bhāva Explorer Controls")
    phoneme_input = st.text_input(
        "Enter phonemes (comma-separated, e.g., ma,ha,na):",
        value="ma,ha,na",
        help="Enter phonemes from Sanskrit syllables (e.g., ma, na, ka). Invalid phonemes will show a warning."
    )
    phonemes = [p.strip().lower() for p in phoneme_input.split(",") if p.strip()]
    
    # Validate phonemes
    invalid_phonemes = [p for p in phonemes if p not in PHONEME_BHAVA_MAP]
    if invalid_phonemes:
        st.warning(f"Invalid phonemes: {', '.join(invalid_phonemes)}. Please use valid phonemes from the dataset.")

    col1, col2 = st.columns(2)
    with col1:
        mode = st.radio("Sentence Mode:", ["Plain", "Linked", "Sanskrit"], help="Choose how sentences are formatted.")
    with col2:
        scheme = st.selectbox("Transliteration Scheme:", ["English", "IAST", "Devanagari"], help="Select Bhāva display format.")

    # Random Phoneme Generator
    if st.button("🎲 Generate Random Phonemes"):
        random_phonemes = random.sample(list(PHONEME_BHAVA_MAP.keys()), k=min(3, len(PHONEME_BHAVA_MAP)))
        phoneme_input = ",".join(random_phonemes)
        st.session_state.phoneme_input = phoneme_input
        phonemes = random_phonemes

    # Recent Inputs History
    if "history" not in st.session_state:
        st.session_state.history = []
    if phonemes and phoneme_input not in st.session_state.history:
        st.session_state.history = [phoneme_input] + st.session_state.history[:4]
    if st.session_state.history:
        st.subheader("Recent Inputs")
        for hist in st.session_state.history:
            if st.button(hist, key=f"hist_{hist}"):
                st.session_state.phoneme_input = hist
                phonemes = [p.strip().lower() for p in hist.split(",") if p.strip()]

# Main Content
st.title("🪷 Bhāva Name Explorer")
st.markdown("""
Enter a name or sound pattern broken into phonemes to explore their spiritual essence through Bhāva, Chakra, and Rasa.
Generate intention-filled paragraphs and export Bhāva cards for your practice.
""")

if phonemes:
    # Bhāva Cards Section
    st.subheader("🎨 Bhāva Mantra Cards")
    cols = st.columns(min(len(phonemes), 3))
    for idx, phoneme in enumerate(phonemes):
        with cols[idx % 3]:
            render_bhava_card(phoneme)
    
    # Bhāva Sequence Analysis
    st.subheader("🔮 Bhāva Sequence Summary")
    chakras = [PHONEME_BHAVA_MAP[p]["chakra"] for p in phonemes if p in PHONEME_BHAVA_MAP]
    rasas = [PHONEME_BHAVA_MAP[p]["rasa"] for p in phonemes if p in PHONEME_BHAVA_MAP]
    st.write(f"**Chakras Invoked**: {', '.join(set(chakras))}")
    st.write(f"**Rasas Expressed**: {', '.join(set(rasas))}")

    # Generated Paragraph
    st.subheader("📝 Generated Bhāva Paragraph")
    paragraph = generate_bhava_paragraph(phonemes, scheme=scheme, mode=mode)
    st.write(paragraph)

    # Copy-friendly Output
    st.text_area("📋 Copy-friendly Output:", paragraph, height=150)

    # Share Paragraph
    share_text = f"Explore my Bhāva journey: {paragraph}"
    st.button("📤 Share Paragraph", on_click=lambda: st.write(f"Copy this: {share_text}"))

    # PDF Export
    if st.button("📄 Export as PDF"):
        latex.generate_pdf(paragraph, phonemes)
        with open("bhava_report.pdf", "rb") as f:
            st.download_button("Download PDF", f, file_name="bhava_report.pdf")