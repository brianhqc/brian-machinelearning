import streamlit as st
import pandas as pd

st.title('The Telcom Churn Prediction App')

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/brianhqc/brian-machinelearning/refs/heads/master/Telco-Customer-Churn.csv')
  df
