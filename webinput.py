import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import streamlit as st

iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
  return species_dict[x]

df['species'] = df['species'].apply(mapp_species)

#####
st.sidebar.title('Select Species🌸')

select_species = st.sidebar.selectbox(
    '확인하고 싶은 종을 선택하세요',
    ['setosa','versicolor','virginica']
)
tmp_df = df[df['species']== select_species]
st.table(tmp_df.head())