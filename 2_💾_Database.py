import streamlit as st 
import pickle 
import yaml 
import pandas as pd 
cfg = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)
PKL_PATH = cfg['PATH']["PKL_PATH"]
st.set_page_config(layout="wide")

#Load databse 
try:
    with open(PKL_PATH, 'rb') as file:
        database = pickle.load(file)
except (FileNotFoundError, EOFError):
    st.warning("Database is empty or not found.")
    database = {}

Index, Id, Name, Image  = st.columns([0.5,0.5,3,3])

for idx, person in database.items():
    with Index:
        st.write(idx)
    with Id: 
        st.write(person['id'])
    with Name:     
        st.write(person['name'])
    with Image:     
        st.image(person['image'],width=200)

if database:
    df = pd.DataFrame([
        {"Index": idx, "ID": person['id'], "Name": person['name']}
        for idx, person in database.items()
    ])
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download CSV", csv, "database.csv", "text/csv")

