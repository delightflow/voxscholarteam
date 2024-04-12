from st_audiorec import st_audiorec
import streamlit as st 

from google.cloud import speech


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

# Google Cloud 클라이언트 설정
client = speech.SpeechClient(api_key='AIzaSyBtq6JYbwosAYklb711_-n5_dx4N4QFaPk')

def transcribe_google(audio_bytes):
    """Google Cloud Speech-to-Text를 사용하여 오디오 바이트를 텍스트로 변환합니다."""
    audio = speech.RecognitionAudio(content=audio_bytes)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
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