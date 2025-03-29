import streamlit as st

home = st.Page("home.py", title="Home", icon=":material/home:")
ipl_data = st.Page("ipl_data.py", title="IPL Data", icon=":material/dataset:")
cricclubs_data = st.Page("cricclubs_data.py", title="Cricclubs Data", icon=":material/dataset:")
cricheroes_data = st.Page("cricheroes_data.py", title="Cricheroes Data", icon=":material/dataset:")

pg = st.navigation([home, ipl_data, cricclubs_data, cricheroes_data])
st.set_page_config(page_title="Analytics home", page_icon=":material/monitoring:")
pg.run()


