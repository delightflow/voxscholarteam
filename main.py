import streamlit as st 

st.title('트렌드를 분석하는 11조입니다.💫')

from st_audiorec import st_audiorec



import column12

import sidebar

import ploty

import webinput

import audio 
if st.button("음성 녹음 시작"):
    audio.audiorec_demo_app()