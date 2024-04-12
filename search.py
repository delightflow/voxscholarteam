import openai
import streamlit as st

def query_gpt(text, model="text-davinci-002"):
    """OpenAI GPT를 사용하여 주어진 텍스트에 대한 쿼리를 실행하고 결과를 반환합니다."""
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    
    response = openai.Completion.create(
        engine=model,
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def display_gpt_response():
    """사용자 입력을 받아 GPT 모델로 쿼리하고 결과를 출력합니다."""
    user_input = st.text_area("Enter text to query GPT:", height=150)
    if st.button("Submit to GPT"):
        response_text = query_gpt(user_input)
        st.write(response_text)
