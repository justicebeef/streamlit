import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from urllib2 import Request, urlopen
import json

st.title("Befolkningsvekst")
st.write("## Befolkningsvekst per kommune")
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

#data = pd.read_csv("https://data.ssb.no/api/v0/dataset/1106.csv", encoding='ISO-8859-1')
#st.write(data)

#
 

request=Request('https://data.ssb.no/api/v0/dataset/1106.json?lang=no')
response = urlopen(request)
x = response.read()
data = json.loads(x)
df = pd.json_normalize(data['results'])
st.write(df)