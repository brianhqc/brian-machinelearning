import streamlit as st
import pandas as pd
st.title('The Machine Learning App')

st.info('The Telcom Churn Prediction Model')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/brianhqc/brian-machinelearning/refs/heads/master/Telco-Customer-Churn.csv')
  df
