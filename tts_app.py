
import streamlit as st
from gtts import gTTS
import io


st.set_page_config(
    page_title="Professional Text-to-Speech",
    page_icon="🎙️",
    layout="wide"
)
st.sidebar.title("🎙️ About the App")
st.sidebar.info(
    """
    This web application is designed to convert written text into high-quality, 
    natural-sounding audio with a distinct **Indian English accent**.

    **Technology Used:**
    - **gTTS (Google Text-to-Speech):** A powerful Python library that interfaces with Google's Text-to-Speech API to generate the audio.
    - **Streamlit:** An open-source framework used to build and deploy the interactive web interface.
    """
)
st.sidebar.success("Built by Gemini")


st.title("Professional Text-to-Speech Converter")
st.markdown("Transform your text into engaging, human-like audio. Ideal for presentations, content creation, and accessibility.")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("1. Enter Your Text")
    text_input = st.text_area(
        "Paste or type your content here. The conversion process is fast, but longer texts may take a few moments.",
        height=250,
        value="Hello, and welcome! This is a demonstration of the text-to-speech converter. You can type or paste any paragraph here to begin."
    )

with col2:
    st.header("Instructions")
    st.markdown(
        """
        - **Enter Text:** Type or paste your desired text into the text box on the left.
        - **Generate:** Click the 'Convert to Speech' button.
        - **Listen & Download:** Once processed, you can play the audio directly or download it as an MP3 file.
        """
    )
    # 
    st.info("The generated audio will have a clear, natural-sounding Indian English accent.")



st.header("2. Generate and Download Audio")

if st.button("Convert to Speech", type="primary", use_container_width=True):
    if text_input.strip():
        with st.spinner("Generating your audio file... Please wait."):
            try:
                
                tts = gTTS(text=text_input, lang='en', tld='co.in', slow=False)
                
                
                audio_fp = io.BytesIO()
                tts.write_to_fp(audio_fp)
                audio_fp.seek(0)
                
                
                st.success("Your audio has been generated successfully!")
                
                st.audio(audio_fp, format='audio/mp3', start_time=0)
                
                st.download_button(
                    label="⬇️ Download MP3 File",
                    data=audio_fp,
                    file_name="generated_speech_indian_english.mp3",
                    mime="audio/mp3",
                    use_container_width=True
                )

            except Exception as e:
                st.error(f"An error occurred during conversion: {e}")
                st.error("This may be due to a network issue. Please check your internet connection and try again.")
    else:
        st.warning("The text box is empty. Please enter some text to convert.")



st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Powered by Google's Text-to-Speech API</p>", unsafe_allow_html=True)

