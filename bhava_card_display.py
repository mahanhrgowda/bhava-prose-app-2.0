import streamlit as st
from data import PHONEME_BHAVA_MAP, SAMPLE_INTENTS
from PIL import Image, ImageDraw, ImageFont
import io

def render_bhava_card(phoneme):
    bhava_data = PHONEME_BHAVA_MAP.get(phoneme, {
        "bhava": "Unknown",
        "chakra": "N/A",
        "rasa": "N/A",
        "emoji": "⚠️"
    })

    bhava = bhava_data["bhava"]
    chakra = bhava_data["chakra"]
    rasa = bhava_data["rasa"]
    emoji = bhava_data["emoji"]
    intents = SAMPLE_INTENTS.get(bhava, ["🔍 No sample intents available."])

    # Render Card
    card_html = f"""
    <div class='bhava-card' style='background-color:#f9f9f9; padding:1rem; border-radius:1rem; box-shadow:0 4px 10px rgba(0,0,0,0.05); margin-bottom:1rem;'>
        <h3>{emoji} {bhava}</h3>
        <p><strong>🧘 Chakra:</strong> {chakra}<br>
        <strong>🎭 Rasa:</strong> {rasa}</p>
        <hr style='border-top: 1px solid #ccc;'>
        <ul>
            {''.join(f'<li>{intent}</li>' for intent in intents)}
        </ul>
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)

    # Export as Image
    if st.button(f"📸 Export {bhava} Card", key=f"export_{phoneme}"):
        # Create image
        img = Image.new('RGB', (400, 300), color='#f9f9f9')
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()
        
        draw.text((20, 20), f"{emoji} {bhava}", fill='black', font=font)
        draw.text((20, 60), f"Chakra: {chakra}", fill='black', font=font)
        draw.text((20, 90), f"Rasa: {rasa}", fill='black', font=font)
        draw.line((20, 120, 380, 120), fill='gray')
        for i, intent in enumerate(intents[:3]):
            draw.text((20, 140 + i*30), intent, fill='black', font=font)

        # Save to buffer
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        st.download_button(
            label=f"Download {bhava} Card",
            data=buf.getvalue(),
            file_name=f"{bhava}_card.png",
            mime="image/png"
        )
