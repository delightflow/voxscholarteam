import streamlit as st 

st.title('트렌드를 분석하는 11조입니다.💫')

from st_audiorec import st_audiorec

from audio import audiorec_demo_app
if st.button('음성 녹음 시작'):
    audiorec_demo_app()  # 버튼 클릭 시 audiorec_demo_app 함수를 호출합니다.

import column12

import sidebar

import ploty

import webinput

