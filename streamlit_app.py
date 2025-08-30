import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('The Machine Learning App')

st.info('This Model Predicts Churn of Telcom Users')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/brianhqc/brian-machinelearning/refs/heads/master/Telco-Customer-Churn.csv')
  df

  st.write('**X**')
  X = df.drop('Churn', axis = 1)
  X

  st.write('**y**')
  y = df['Churn']
  y

with st.expander('Data Visualization'):
  fig, ax= plt.subplots()
  ax = sns.kdeplot(data=df, x='MonthlyCharges', hue='Churn', color='Red', shade=True, palette = {'No':'red','Yes':'green'}, common_norm=False)
  st.pyplot(fig)

# Data Preparateions
with st.sidebar:
  st.header('Input Features')
  gender = st.selectbox('gender', df['gender'].unique())
  tenure = st.slider('tenure', df['tenure'].min(), df['tenure'].max())
  MonthlyCharges = st.slider('MonthlyCharges', df['MonthlyCharges'].min(), df['MonthlyCharges'].max())

