🪷 Bhāva Name Explorer
A refined Streamlit app that maps phonemes to Sanskrit Bhāvas, Chakras, and Rasas, generating:

🎨 Mantra-style Bhāva Cards with image export
📝 Dynamic Intention Paragraphs
🔤 Transliteration (English/IAST/Devanāgarī)
📊 Bhāva Sequence Analysis
📄 PDF Export

🚀 Features

🔠 Input phonemes (e.g., ma, na, ha) with validation
🎨 Render animated Bhāva Cards with PNG export
📝 Generate spiritual intent paragraphs in Plain, Linked, or Sanskrit modes
🌐 Transliterate Bhāvas into English, IAST, or Devanāgarī
📋 Copy-ready output and shareable links
🎲 Random phoneme generator for inspiration
📜 Persistent input history
📊 Summary of invoked chakras and rasas
📄 Export results as PDF

📦 Setup
pip install -r requirements.txt
streamlit run bhava_app.py

📁 Project Structure
.
├── bhava_app.py                # Main Streamlit UI
├── bhava_card_display.py       # Bhāva card rendering and export
├── data.py                     # Phoneme → Bhāva–Chakra–Rasa map
├── paragraph_generator.py      # Paragraph generation logic
├── transliteration_utils.py    # Transliteration utilities
├── templates/                  # LaTeX templates for PDF
│   └── bhava_report.tex
├── requirements.txt
└── README.md

🙏 Credits
Inspired by Nāṭyaśāstra, Bhāgavata Purāṇa, and Sanskrit rasa theory.
Crafted with ❤️ by Mahan Ravindra
🔮 Future Work

ML-based Bhāva similarity analysis using vector embeddings
Interactive Bhāva trend dashboard
Mobile-optimized UI

