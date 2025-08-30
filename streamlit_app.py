import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')

df = pd.read_csv('https://raw.githubusercontent.com/brianhqc/brian-machinelearning/refs/heads/master/Telco-Customer-Churn.csv')
df
