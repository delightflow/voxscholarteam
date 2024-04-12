import streamlit as st 
from PIL import Image
img1 = Image.open('puppy1.jpeg')
img2 = Image.open('puppy2.jpg')

col1,col2 = st.columns([1,1])

with col1 :
  st.title('column1')
  st.subheader('column1의 subheader')
  st.image(img1,width=200)

with col2 :
  st.title('column2')
  st.checkbox('checkbox1 in col2 ')
  st.checkbox('checkbox2 in col2 ')
  st.image(img2,width=200)