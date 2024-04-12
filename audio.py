import streamlit as st
from st_audiorec import st_audiorec
import whisper

model = whisper.load_model("base")  # You can choose another model size if needed

# CSS Customizations
st.markdown(
    '''
    <style>
    .css-1egvi7u {margin-top: -3rem;}
    .stAudio {height: 45px;}
    .css-v37k9u a, .css-nlntq9 a {color: #ff4c4b;}
    </style>
    ''', 
    unsafe_allow_html=True
)

def transcribe(audio):
    # Load the audio file and decode it into text
    result = model.transcribe(audio)
    return result["text"]

def audiorec_demo_app():
    st.title("Audio Recorder with Speech-to-Text")
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        # Display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        
        # Transcribe audio
        transcription = transcribe(wav_audio_data)
        st.text_area("Transcription", transcription, height=100)

audiorec_demo_app()
