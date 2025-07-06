import os
import io
from gtts import gTTS
import streamlit as st
import speech_recognition as sr
from googletrans import LANGUAGES, Translator

is_translate_on = False  

translator = Translator()  # Initializing the translator module

# Create a mapping between language names and language codes
language_mapping = {v: k for k, v in LANGUAGES.items()}

def get_language_code(language_name):
    """Get the correct language code from the language name"""
    return language_mapping.get(language_name, 'en')  # Default to English if not found

def translator_function(spoken_text, from_language, to_language):
    """
    Translates text using googletrans. Handles potential recognition errors.
    """
    if spoken_text is None:
        return "Speech recognition failed."
    try:
        result = translator.translate(spoken_text, src=from_language, dest=to_language)
        return result.text
    except Exception as e:
        return f"Translation error: {str(e)}"

def text_to_voice(text_data, to_language):
    myobj = gTTS(text=text_data, lang=to_language, slow=False)
    
    # Create audio bytes in memory instead of saving to file
    audio_buffer = io.BytesIO()
    myobj.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    
    # Play audio using Streamlit's built-in audio player with autoplay
    st.audio(audio_buffer, format="audio/mp3", autoplay=True)

def main_process(output_placeholder, from_language, to_language):
    global is_translate_on

    if "conversation" not in st.session_state:
        st.session_state.conversation = []

    with st.spinner('Listening...'):
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            rec.pause_threshold = 1
            audio = rec.listen(source, phrase_time_limit=300)

    try:
        with st.spinner('Processing...'):
            # Use the correct language code for speech recognition
            spoken_text = rec.recognize_google(audio, language=from_language)

        with st.spinner('Translating...'):
            translated_text = translator_function(spoken_text, from_language, to_language)

        # Update conversation history immediately after translation
        st.session_state.conversation.append(f"""
            <div style="display: flex; justify-content: space-between;">
                <div style="flex: 1;"><b>From Language:</b> {spoken_text}</div>
                <div style="flex: 1; text-align: right;"><b>Translated:</b> {translated_text}</div>
            </div>
        """)

        # Display translated text in a prominent area above the history
        st.markdown(f"<h2 style='color: #fff;'>Translated Text: {translated_text}</h2>", unsafe_allow_html=True)

        with st.spinner('Generating audio...'):
            text_to_voice(translated_text, to_language)

    except sr.UnknownValueError:
        st.markdown("<h2 style='color: #dc3545;'>Speech recognition failed. Please try again.</h2>", unsafe_allow_html=True)
    except sr.RequestError as e:
        st.markdown(f"<h2 style='color: #dc3545;'>Speech recognition error: {e}</h2>", unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f"<h2 style='color: #dc3545;'>An error occurred: {e}</h2>", unsafe_allow_html=True)

# UI layout
st.set_page_config(page_title="Language Translator", page_icon="🌍")

# Background image
background_image_url = "https://w.wallhaven.cc/full/7p/wallhaven-7pzkqv.jpg"  
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    div[data-testid="stVerticalBlock"] > div:has(div.element-container div.stMarkdown) {{
        background-color: rgba(255, 255, 255, 0);
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        max-height: 300px;
        overflow-y: auto;
        backdrop-filter: blur(10px); 
        -webkit-backdrop-filter: blur(15px);
        box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
    }}
    h2 {{
        margin-top: 0px; 
        padding-top: 0px; 
    }}
    div.element-container div.stMarkdown p {{
        margin: 10px 0;
        padding: 5px;
        border-bottom: 1px solid rgba(200, 200, 200, 0.4);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Language selection with columns for better layout
col1, col2 = st.columns(2)
from_language_name = col1.selectbox("From Language:", list(LANGUAGES.values()))
to_language_name = col2.selectbox("To Language:", list(LANGUAGES.values()))

# Convert language names to language codes
from_language = get_language_code(from_language_name)
to_language = get_language_code(to_language_name)

# Creating a container for buttons and use columns for horizontal placements
button_container = st.container()
col3, col4 = button_container.columns(2)

start_button = col3.button("Start")
stop_button = col4.button("Stop")

# Create history container
history_container = st.container()
with history_container:
    st.header("Translation History")
    if "conversation" in st.session_state:
        for line in reversed(st.session_state.conversation):
            st.markdown(f"{line}", unsafe_allow_html=True)

# Check if "Start" button is clicked
if start_button:
    if not is_translate_on:
        is_translate_on = True
        output_placeholder = st.empty()
        main_process(output_placeholder, from_language, to_language)

# Check if "Stop" button is clicked
if stop_button:
    is_translate_on = False
