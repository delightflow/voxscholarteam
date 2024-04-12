from st_audiorec import st_audiorec
import streamlit as st 
import whisper

import numpy as np
import soundfile as sf
import io


# DESIGN implement changes to the standard streamlit UI/UX
# --> optional, not relevant for the functionality of the component!

# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # lightmode

model = whisper.load_model("small") 



def transcribe(audio_bytes):
    # Convert bytes to a NumPy array
    with io.BytesIO(audio_bytes) as audio_buffer:
        audio, samplerate = sf.read(audio_buffer, dtype='float32')
    
    # Transcribe audio
    result = model.transcribe(audio, sample_rate=samplerate)
    return result["text"]



def audiorec_demo_app():


    wav_audio_data = st_audiorec()

    # add some spacing and informative messages

    if wav_audio_data is not None:
        # display audio data as received on the Python side
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')
        
        transcription = transcribe(wav_audio_data)
        st.text_area("Transcription", transcription, height=100)




if __name__ == "__main__":
    audiorec_demo_app()