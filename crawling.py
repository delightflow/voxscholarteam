from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import streamlit as st
import streamlit as st
import streamlit as st
import pandas as pd




search_keyword = st.text_input("검색어를 입력하세요: ")
search_date = st.text_input("검색을 시작할 날짜를 입력하세요(yyyy-mm-dd): ")
search_db = st.selectbox("검색할 데이터베이스를 선택하세요(이공계: arXiv , 인문계: jstor)", ["arXiv", "jstor"])
search_button = st.button("검색 시작")


today = time.strftime('%Y/%m/%d', time.localtime(time.time()))
if search_button:
  browser = webdriver.Chrome()
  if search_db == "arXiv":
  
    url = f"https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term={search_keyword}&terms-0-field=all&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date={search_date}&date-to_date=2024-04-15&date-date_type=submitted_date&abstracts=show&size=100&order=-announced_date_first"
    find_container = 'list-title'
    find_title = 'title'
    find_author = 'authors'
    find_abstract = 'abstract'
    find_date = 'submission-history'
    
  else:
    search_keyword = search_keyword.replace(" ", "+")
    search_date = search_date.replace("-", "/")
    url = f"https://www.jstor.org/action/doAdvancedSearch?q0={search_keyword}&sd={search_date}&ed={today}&f0=all&c1=AND&f1=all&acc=on&so=rel"
    find_container = 'result__main__metadata'
    find_title = 'title'
    find_author = 'search-results-vue-pharos-link'
    find_author2 = 'contrib metadata-row'
    find_date = 'break-word'
    
  browser.get(url)
  
  
  list = []
  wait = WebDriverWait(browser, 5)
  links = WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, find_container)))
  st.write(f'{len(links)}개의 논문이 검색되었습니다.')
  i = 0
  for link in links:
    if search_db == "arXiv":
      title = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, find_title))).text
      wait.until(EC.presence_of_element_located((By.CLASS_NAME, find_author)))
      abstract = browser.find_element(By.CLASS_NAME,find_abstract).text
      author = browser.find_element(By.CLASS_NAME,find_author).text
      wait.until(EC.presence_of_element_located((By.CLASS_NAME, find_date)))
      date = browser.find_element(By.CLASS_NAME, find_date).text
    else:
    
      try:
        browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + 100;', links)
        time.sleep(1)
        title = link.find_element(By.CLASS_NAME, find_title).text
        print(f'{title}+ "제목입니다"')
        time.sleep(1)
        abstract = "JSTOR에서는 초록을 제공하지 않습니다."
        author = "JSTOR에서는 저자를 제공하지 않습니다."
        # author_link = browser.find_element(By.CLASS_NAME, find_author2).find_element(By.TAG_NAME,find_author).get_attribute('href')
        # author = author_link.split('=')[-1].replace('+', ' ')
        time.sleep(1)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, find_date)))
        date = link.find_element(By.CLASS_NAME, find_date).find_element(By.CLASS_NAME, 'metadata').text
        print(f'{date}+ "게재일입니다"')
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      except:
        title = "제목을 찾을 수 없습니다."
        date = "게재일을 찾을 수 없습니다."
    
    
    
    list.append(
      {'제목': title,
       '저자': author,
       '초록': abstract,
       '게재일': date}
    )
    # browser.back()
    # WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, find_container)))
    i += 1
    print(i,'개 추출 성공')
    # 테스트로 3개만 해봄
    # if i == 3:
    #     break

  browser.quit()

  df = pd.DataFrame(list)
  df.to_csv("crawling.csv",encoding='utf-8-sig')


  # Download the CSV file
  st.download_button(
    label="Download CSV",
    data=df.to_csv().encode('utf-8-sig'),
    file_name="crawling.csv",
    mime="text/csv"
  )

  df = pd.read_csv('crawling.csv')
  st.dataframe(df)
  