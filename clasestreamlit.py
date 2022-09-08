import streamlit as st
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split

df = pd.read_csv('./income.csv')
df

st.image('./pig.jpg')

siteHeader = st.container()
with siteHeader:
    st.title('Modelo de evaluación de ingresos')
    st.markdown('El objetivo de este proyecto es proveer una herramienta que nos permita predecir sí una persona ganará más o menos de $50K anuales.')


daViz = st.container()
with daViz:
    st.subheader('Exploración de la data:')
    st.dataframe(df.head())    
    st.caption('¿Habrá diferencia entre hombres y mujeres?')