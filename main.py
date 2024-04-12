import streamlit as st 

st.title('트렌드를 분석하는 11조입니다.💫')

from st_audiorec import st_audiorec



import column12

import sidebar

import ploty

import webinput

import audio 

import search

if st.button("음성 녹음 시작"):
    audio.audiorec_demo_app()

if 'transcribed_text' in st.session_state:
    st.text_area("Transcribed Text", st.session_state.transcribed_text, height=150)
    if st.button("Analyze with GPT"):
        search.display_gpt_response()