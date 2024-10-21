import streamlit as st
import pandas as pd

st.write("hello word")
movie_input = st.text_input("Favourite movie")

st.write(f"You're favorite movie is: {movie_input}")
st.write("# is this an h1?")
st.write("## is this an h2?")

data = pd.read_csv("imdb_top_1000.csv")
st.write(data)