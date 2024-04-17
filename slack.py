import requests
import pandas as pd
import time
import streamlit as st

def send_slack_message(message):
  url = "https://hooks.slack.com/services/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" 
  headers = {'Content-type': 'application/json'}
  data = {
    "text": message
  }
  response = requests.post(url, headers=headers, json=data)
  if response.status_code != 200:
    raise ValueError(f"Slack request returned an error {response.status_code}, the response is:\n{response.text}")

def format_bestseller_message(index, row):

  return f"번호: {index + 1}\n제목: {row['제목']}\n저자: {row['저자']}\n초록: {row['초록']}\n게재일: {row['게재일']}\n한줄요약: {row['한 줄 요약']}\n키워드: {row['키워드']}"

if __name__ == "__main__":
  df = pd.read_csv('crawling.csv')

  # Streamlit app
  st.title("슬랙으로 보내기")
  button_clicked = st.button("전송 시작")
  if button_clicked:
    # 전체 데이터셋 순회
    st.write("전송 중...예상 시간 1초/개")
    for index, row in df.iterrows():
      message = format_bestseller_message(index, row)
      send_slack_message(message)
      progress_message = f"진행 중... ({index+1}/{len(df)})"  # 진행 상황 메시지 생성
      st.write(progress_message)
      time.sleep(1)
    st.write("전송 완료! ")
