from st_audiorec import st_audiorec
import streamlit as st 
import json
from google.cloud import speech

from google.oauth2 import service_account

# Load the JSON secret
service_account_info = {
    "type": st.secrets["type"],
    "project_id": st.secrets["project_id"],
    "private_key_id": st.secrets["private_key_id"],
    "private_key": st.secrets["private_key"],
    "client_email": st.secrets["client_email"],
    "client_id": st.secrets["client_id"],
    "auth_uri": st.secrets["auth_uri"],
    "token_uri": st.secrets["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["client_x509_cert_url"]
}

# Create the SpeechClient with the loaded credentials
credentials = service_account.Credentials.from_service_account_info(service_account_info)
client = speech.SpeechClient(credentials=credentials)

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



def transcribe_google(audio_bytes):
    """Google Cloud Speech-to-Text를 사용하여 오디오 바이트를 텍스트로 변환합니다."""
    audio = speech.RecognitionAudio(content=audio_bytes)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,
        audio_channel_count=2,
        language_code="ko-KR"  # 여기서 언어 설정을 조정할 수 있습니다.
    )

    # API 요청 및 응답
    response = client.recognize(config=config, audio=audio)
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript

    return transcription

def audiorec_demo_app():
    """오디오 녹음하고 텍스트로 변환합니다."""
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        col_playback, col_space = st.columns([0.58,0.42])
        with col_playback:
            st.audio(wav_audio_data, format='audio/wav')

        transcription = transcribe_google(wav_audio_data)
        st.text_area("Transcription", transcription, height=100)

if __name__ == "__main__":
    audiorec_demo_app()