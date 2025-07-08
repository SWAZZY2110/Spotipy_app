import streamlit as st
from utils.helpers import get_top_tracks, authenticate_spotify

# make a streamlit app 
# use plotly express to put the top songs along with the energy and danceability.

import plotly.express as px

sp = authenticate_spotify()
st.title("Spotify Top Tracks")
# Load data using helper function
data = get_top_tracks(sp, limit=20)

print(data)
# Streamlit app
st.title("Top Songs Energy Visualization")

# Display data
st.write("Here are the top songs with their energy levels:")
st.subheader("Your favorite tracks")
for i, row in data.iterrows():
    st.image(row["image"], caption=row["artist"], use_container_width=True)
    st.markdown(f"**album**: {row['album']}")
    st.markdown(f"**popularity**: {row['popularity']}")