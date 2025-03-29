import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.write("## :material/trending_up: Indian Premier League Analysis")
st.write("Indian premier league is the most popular T20 league played in the world, its operated by BCCI and has been running since 2008. With this analysis we will look into the stats from 2008-2016 and will get some answers to the questions.\n\n")



# TODO: Load data from a CSV file
deliveries = pd.read_csv('data/ipl_data/deliveries.csv')
matches = pd.read_csv('data/ipl_data/matches.csv')

st.write("### :material/database: Matches (2008-2016)")
st.dataframe(matches)
st.write("### :material/database: Deliveries in each match (2008-2016)")
st.dataframe(deliveries)