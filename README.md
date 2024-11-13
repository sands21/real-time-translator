# 🌍 Language Translator Web App

![Demo Video](https://drive.google.com/uc?export=download&id=1JHs56RI5nN4PrLU3GDzfWEREVOWCw4IF)

This project is a real-time speech-to-speech language translator web app built with Streamlit, Google Text-to-Speech, and Google Translate APIs. The app allows users to select input and output languages, translate spoken words into the desired language, and play back the translated speech.

## 📋 Features

- **Real-Time Speech Recognition**: Captures spoken input using the `speech_recognition` library.
- **Language Translation**: Translates spoken text into a selected language using `googletrans`.
- **Text-to-Speech Output**: Converts the translated text back into speech for playback using `gTTS` and `pygame`.
- **Translation History**: Keeps a session-based record of translations for easy reference.
- **User-Friendly Interface**: Developed with Streamlit, offering a clean and intuitive UI.
- **Background Styling**: Custom background and blur effect for a more engaging visual experience.

## 🎬 Demonstration

Check out the video above to see the app in action!

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- Install dependencies with the following command:

```bash
pip install streamlit pygame gTTS googletrans==3.1.0a0 SpeechRecognition
```

### Running the Application

1. **Clone the repository** and navigate to the project directory.

   ```bash
   git clone https://github.com/sands21/real-time-translator.git
   cd real-time-translator
   ```

2. **Start the Streamlit App**:

   ```bash
   streamlit run app.py
   ```

3. **Access the app** at `http://localhost:8501` on your browser.

## 🚀 Usage

1. Select the languages for translation (`From Language` and `To Language`).
2. Click **Start** to begin listening to your speech input.
3. Your speech will be translated and the text will be displayed along with audio playback in the chosen language.
4. **Stop** the process anytime by clicking the **Stop** button.

## 📁 File Structure

- `app.py` - Main application script.
- `README.md` - Documentation for the project.

## 📝 Notes

- Ensure you have a working microphone for speech input.
- The app requires an active internet connection for both Google Translate and Google Text-to-Speech.

## ⚖️ License

This project is licensed under the MIT License.

## 🌐 Acknowledgments

Special thanks to the creators of Streamlit, Google Translate, and the Python community for their fantastic resources.

---

**Note**: If you encounter any issues or have questions, please reach out via [GitHub Issues](https://github.com/sands21/real-time-translator/issues).
