import streamlit as st 

st.title('트렌드를 분석하는 11조입니다.💫')

# from st_audiorec import st_audiorec



import column12
import crawling
if st.button('크롤링 시작'):
    st.write('아카이브 크롤링을 시작합니다.')

import sidebar

import ploty

import webinput




# import audio 



# if 'recording_started' not in st.session_state:
#     st.session_state.recording_started = False

# if st.button("음성 녹음 시작", key='start_rec'):
#     st.session_state.recording_started = True

# if st.session_state.recording_started:
#     audio.audiorec_demo_app()